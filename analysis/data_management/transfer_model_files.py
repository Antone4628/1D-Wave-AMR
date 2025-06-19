#!/usr/bin/env python3
"""
Transfer Model Files - SSH Multiplexed Version

This tool transfers final_model.zip files using SSH multiplexing to avoid rate limiting,
while preserving directory structure for Workflow 4 model evaluation.

Creates structure for model performance analysis:
    analysis/data/models/session3_100k_uniform/
    ├── gamma_25.0_step_0.025_rl_10_budget_25/
    │   └── final_model.zip
    └── ... (all 81 parameter combinations)

Usage:
    python analysis/data_management/transfer_model_files.py session3_100k_uniform \
        --hpc-path antonechacartegu@borah-login:/path/to/results/session3_100k_uniform
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime
import argparse

class ModelFilesTransfer:
    """Transfer model files using SSH multiplexing for Workflow 4 model evaluation."""
    
    def __init__(self, sweep_name: str, verbose: bool = False):
        self.sweep_name = sweep_name
        self.verbose = verbose
        self.local_models_path = Path("analysis/data/models") / sweep_name
        self.expected_combinations = self._generate_parameter_combinations()
        
        # SSH multiplexing configuration
        self.ssh_host = None
        self.ssh_path = None
        self.control_path = None
        self.master_connection_active = False
    
    def _generate_parameter_combinations(self):
        """Generate the 81 expected parameter combination names."""
        gamma_values = [25.0, 50.0, 100.0]
        step_values = [0.025, 0.05, 0.1]
        rl_values = [10, 25, 40] 
        budget_values = [25, 30, 40]
        
        combinations = []
        for gamma in gamma_values:
            for step in step_values:
                for rl in rl_values:
                    for budget in budget_values:
                        combo = f"gamma_{gamma}_step_{step}_rl_{rl}_budget_{budget}"
                        combinations.append(combo)
        return combinations
    
    def setup_ssh_multiplexing(self, hpc_path: str) -> dict:
        """Setup SSH connection multiplexing for efficient file operations."""
        # Parse HPC path
        if ':' not in hpc_path:
            return {'success': False, 'error': 'Invalid HPC path format (expected user@host:/path)'}
        
        self.ssh_host, self.ssh_path = hpc_path.split(':', 1)
        
        # Create control path for multiplexing
        import tempfile
        temp_dir = tempfile.gettempdir()
        control_name = f"ssh_mux_{self.ssh_host.replace('@', '_').replace('.', '_')}"
        self.control_path = os.path.join(temp_dir, control_name)
        
        if self.verbose:
            print(f"🔗 Setting up SSH multiplexing...")
            print(f"   Host: {self.ssh_host}")
            print(f"   Control path: {self.control_path}")
        
        # Setup master connection with multiplexing
        master_cmd = [
            'ssh', '-M', '-S', self.control_path,
            '-o', 'ControlPersist=300',  # Keep connection for 5 minutes
            '-o', 'ConnectTimeout=30',
            '-o', 'ServerAliveInterval=60',
            '-o', 'ServerAliveCountMax=3',
            '-f',  # Background the connection
            self.ssh_host,
            'sleep 10'  # Keep connection alive briefly
        ]
        
        try:
            result = subprocess.run(master_cmd, capture_output=True, text=True, timeout=45)
            
            if result.returncode == 0:
                self.master_connection_active = True
                if self.verbose:
                    print("✅ SSH master connection established")
                return {'success': True}
            else:
                return {'success': False, 'error': f'Master connection failed: {result.stderr}'}
                
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Master connection timeout'}
        except Exception as e:
            return {'success': False, 'error': f'Master connection error: {str(e)}'}
    
    def cleanup_ssh_multiplexing(self):
        """Clean up SSH multiplexing connection."""
        if self.master_connection_active and self.control_path:
            try:
                # Close master connection
                cleanup_cmd = ['ssh', '-S', self.control_path, '-O', 'exit', self.ssh_host]
                subprocess.run(cleanup_cmd, capture_output=True, timeout=10)
                
                # Remove control file if it exists
                if os.path.exists(self.control_path):
                    os.remove(self.control_path)
                
                if self.verbose:
                    print("🔌 SSH multiplexing cleaned up")
                    
            except Exception as e:
                if self.verbose:
                    print(f"⚠️ Cleanup warning: {e}")
            finally:
                self.master_connection_active = False
    
    def run_multiplexed_ssh(self, command: str, timeout: int = 30) -> subprocess.CompletedProcess:
        """Run SSH command using the multiplexed connection."""
        if not self.master_connection_active:
            raise RuntimeError("SSH master connection not active")
        
        ssh_cmd = [
            'ssh', '-S', self.control_path,
            '-o', 'ConnectTimeout=10',
            self.ssh_host,
            command
        ]
        
        return subprocess.run(ssh_cmd, capture_output=True, text=True, timeout=timeout)
    
    def validate_hpc_path(self, hpc_path: str) -> dict:
        """Validate HPC path using multiplexed connection."""
        print(f"🔍 Validating HPC path: {hpc_path}")
        
        # Setup multiplexing first
        mux_result = self.setup_ssh_multiplexing(hpc_path)
        if not mux_result['success']:
            return {'valid': False, 'error': mux_result['error']}
        
        # Test path existence using multiplexed connection
        try:
            result = self.run_multiplexed_ssh(f'test -d {self.ssh_path} && echo EXISTS || echo MISSING', timeout=20)
            
            if result.returncode == 0:
                if "EXISTS" in result.stdout:
                    print("✅ HPC path exists and is accessible")
                    return {'valid': True, 'error': None}
                else:
                    print("❌ HPC path does not exist")
                    return {'valid': False, 'error': 'Path does not exist'}
            else:
                print(f"❌ Path validation failed: {result.stderr}")
                return {'valid': False, 'error': f'Path validation failed: {result.stderr}'}
                
        except Exception as e:
            print(f"❌ Validation error: {e}")
            return {'valid': False, 'error': str(e)}
    
    def survey_hpc_models(self, hpc_path: str) -> dict:
        """Survey what model files actually exist on HPC using multiplexed connection."""
        print(f"🔍 Surveying model files on HPC...")
        
        try:
            # List all directories in the sweep path
            result = self.run_multiplexed_ssh(f'ls -la {self.ssh_path}/ 2>/dev/null || echo NO_DIRS', timeout=45)
            
            if "NO_DIRS" in result.stdout:
                return {'directories': [], 'error': 'No directories found'}
            
            # Parse directory listing
            directories = []
            for line in result.stdout.split('\n'):
                if 'gamma_' in line and 'step_' in line:
                    # Extract directory name
                    parts = line.split()
                    if len(parts) >= 9:
                        dirname = parts[-1]
                        directories.append(dirname)
            
            print(f"📂 Found {len(directories)} parameter directories on HPC")
            
            # Check for final_model.zip in first few directories for diagnosis
            model_check_results = {}
            check_dirs = directories[:5] if len(directories) > 5 else directories
            
            for dirname in check_dirs:
                model_result = self.run_multiplexed_ssh(f'ls {self.ssh_path}/{dirname}/final_model.zip 2>/dev/null && echo MODEL_EXISTS || echo MODEL_MISSING', timeout=20)
                
                has_model = "MODEL_EXISTS" in model_result.stdout
                model_check_results[dirname] = {
                    'has_final_model': has_model
                }
                
                if self.verbose:
                    print(f"   {dirname}: final_model.zip {'✅' if has_model else '❌'}")
            
            return {
                'directories': directories,
                'model_check_results': model_check_results,
                'total_dirs_found': len(directories),
                'error': None
            }
            
        except Exception as e:
            return {'directories': [], 'error': str(e)}
    
    def check_model_existence(self, hpc_path: str, combo_name: str) -> dict:
        """Check if final_model.zip exists for a parameter combination using multiplexed connection."""
        
        try:
            # Check directory and final_model.zip in a single SSH call for efficiency
            check_cmd = f'''
                cd {self.ssh_path} &&
                if [ -d "{combo_name}" ]; then
                    echo "DIR_EXISTS"
                    cd "{combo_name}"
                    [ -f "final_model.zip" ] && echo "MODEL_EXISTS" || echo "MODEL_MISSING"
                else
                    echo "DIR_MISSING"
                fi
            '''
            
            result = self.run_multiplexed_ssh(check_cmd, timeout=15)
            
            if result.returncode != 0:
                return {
                    'directory_exists': False,
                    'model_exists': False,
                    'error': f'Check command failed: {result.stderr}'
                }
            
            output = result.stdout.strip()
            
            # Parse results
            dir_exists = "DIR_EXISTS" in output
            model_exists = "MODEL_EXISTS" in output
            
            return {
                'directory_exists': dir_exists,
                'model_exists': model_exists,
                'error': None if dir_exists else 'Directory does not exist'
            }
            
        except Exception as e:
            return {
                'directory_exists': False,
                'model_exists': False,
                'error': str(e)
            }
    
    def clean_existing_structure(self):
        """Remove any existing transferred models to start clean."""
        if self.local_models_path.exists():
            print(f"🗑️  Removing existing models: {self.local_models_path}")
            import shutil
            shutil.rmtree(self.local_models_path)
        
        self.local_models_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created clean models directory: {self.local_models_path}")
    
    def transfer_model_files(self, hpc_path: str, dry_run: bool = False):
        """Enhanced transfer of model files with SSH multiplexing and detailed error categorization."""
        print(f"🚀 Starting model file transfer with SSH multiplexing...")
        print(f"   Source: {hpc_path}")
        print(f"   Destination: {self.local_models_path}")
        
        if dry_run:
            print("   [DRY RUN MODE - No files will be transferred]")
        
        try:
            # First, validate HPC path (this sets up SSH multiplexing)
            validation = self.validate_hpc_path(hpc_path)
            if not validation['valid']:
                return {
                    'error': validation['error'], 
                    'transferred_count': 0,
                    'failure_categories': {
                        'directory_missing': [],
                        'model_missing': [],
                        'transfer_error': []
                    },
                    'survey_results': {'directories': [], 'error': 'HPC path validation failed'},
                    'dry_run': dry_run
                }
            
            # Survey HPC models using multiplexed connection
            survey = self.survey_hpc_models(hpc_path)
            if survey['error']:
                print(f"⚠️ Survey warning: {survey['error']}")
            
            transferred_combinations = []
            failure_categories = {
                'directory_missing': [],
                'model_missing': [],
                'transfer_error': []
            }

            print(f"\n🔄 Processing {len(self.expected_combinations)} parameter combinations...")
            
            for i, combo_name in enumerate(self.expected_combinations):
                if i % 10 == 0:
                    print(f"   Progress: {i}/81")
                
                # Check model existence using multiplexed connection
                existence = self.check_model_existence(hpc_path, combo_name)
                
                if not existence['directory_exists']:
                    failure_categories['directory_missing'].append(combo_name)
                    if self.verbose:
                        print(f"❌ {combo_name}: Directory missing")
                    continue
                
                if not existence['model_exists']:
                    failure_categories['model_missing'].append(combo_name)
                    if self.verbose:
                        print(f"❌ {combo_name}: final_model.zip missing")
                    continue
                
                # Model exists, proceed with transfer
                if dry_run:
                    transferred_combinations.append(combo_name)
                    if self.verbose:
                        print(f"✅ {combo_name}: Would transfer")
                    continue
                
                # Create local directory
                local_combo_dir = self.local_models_path / combo_name
                local_combo_dir.mkdir(exist_ok=True)
                
                # Transfer final_model.zip using rsync with SSH multiplexing
                model_source = f"{self.ssh_host}:{self.ssh_path}/{combo_name}/final_model.zip"
                model_dest = str(local_combo_dir / "final_model.zip")
                
                model_cmd = ['rsync', '-avz', '-e', f'ssh -S {self.control_path}', model_source, model_dest]

                try:
                    result = subprocess.run(model_cmd, capture_output=True, text=True, timeout=120)
                    
                    if result.returncode == 0:
                        transferred_combinations.append(combo_name)
                        if self.verbose:
                            print(f"✅ {combo_name}")
                    else:
                        failure_categories['transfer_error'].append({
                            'combo': combo_name,
                            'error': result.stderr
                        })
                        if self.verbose:
                            print(f"❌ {combo_name}: Transfer failed")
                            
                except Exception as e:
                    failure_categories['transfer_error'].append({
                        'combo': combo_name,
                        'error': str(e)
                    })
                    if self.verbose:
                        print(f"💥 {combo_name}: {e}")
            
            return {
                'transferred_count': len(transferred_combinations),
                'transferred_combinations': transferred_combinations,
                'failure_categories': failure_categories,
                'survey_results': survey,
                'dry_run': dry_run
            }
            
        except Exception as e:
            print(f"💥 Critical error during transfer: {e}")
            return {
                'error': str(e),
                'transferred_count': 0,
                'failure_categories': {
                    'directory_missing': [],
                    'model_missing': [],
                    'transfer_error': []
                },
                'survey_results': {'directories': [], 'error': f'Critical error: {str(e)}'},
                'dry_run': dry_run
            }
        finally:
            # Always cleanup SSH multiplexing
            self.cleanup_ssh_multiplexing()
    
    def print_detailed_results(self, results: dict):
        """Print comprehensive transfer results."""
        print(f"\n📊 DETAILED MODEL TRANSFER RESULTS:")
        print(f"=" * 60)
        
        transferred = results['transferred_count']
        total_failed = 81 - transferred
        
        print(f"✅ Successfully transferred: {transferred}/81 ({transferred/81*100:.1f}%)")
        print(f"❌ Failed transfers: {total_failed}/81 ({total_failed/81*100:.1f}%)")
        
        if total_failed > 0:
            print(f"\n📋 FAILURE BREAKDOWN:")
            
            categories = results['failure_categories']
            
            if categories['directory_missing']:
                print(f"   📂 Missing directories: {len(categories['directory_missing'])}")
                if len(categories['directory_missing']) <= 5:
                    for combo in categories['directory_missing']:
                        print(f"      - {combo}")
                else:
                    print(f"      - {categories['directory_missing'][0]} ... (and {len(categories['directory_missing'])-1} more)")
            
            if categories['model_missing']:
                print(f"   📄 Missing final_model.zip: {len(categories['model_missing'])}")
                if len(categories['model_missing']) <= 5:
                    for combo in categories['model_missing']:
                        print(f"      - {combo}")
                else:
                    print(f"      - {categories['model_missing'][0]} ... (and {len(categories['model_missing'])-1} more)")
                
            if categories['transfer_error']:
                print(f"   🔄 Transfer errors: {len(categories['transfer_error'])}")
        
        # Survey results
        if 'survey_results' in results and results['survey_results'].get('directories'):
            survey = results['survey_results']
            print(f"\n🔍 HPC SURVEY RESULTS:")
            print(f"   Directories found on HPC: {survey['total_dirs_found']}")
            
            if survey.get('model_check_results'):
                print(f"   Sample model analysis:")
                for dirname, info in list(survey['model_check_results'].items())[:3]:
                    print(f"      {dirname}: final_model.zip {'✅' if info['has_final_model'] else '❌'}")
    
    def validate_transfer(self):
        """Validate transferred structure is ready for Workflow 4 model evaluation."""
        print("🔍 Validating transfer for Workflow 4 model evaluation...")
        
        found_combinations = []
        missing_combinations = []
        
        for combo_name in self.expected_combinations:
            combo_dir = self.local_models_path / combo_name
            model_file = combo_dir / "final_model.zip"
            
            if combo_dir.exists() and model_file.exists():
                found_combinations.append(combo_name)
            else:
                missing_combinations.append(combo_name)
        
        validation_result = {
            'total_expected': 81,
            'found_complete': len(found_combinations),
            'missing_combinations': len(missing_combinations),
            'workflow4_ready': len(found_combinations) >= 70  # 86% threshold
        }
        
        print(f"📊 Validation Results:")
        print(f"   Complete model combinations: {validation_result['found_complete']}/81")
        print(f"   Missing combinations: {validation_result['missing_combinations']}")
        
        if validation_result['workflow4_ready']:
            print("✅ Structure ready for Workflow 4 model evaluation")
            print(f"🎯 Ready for: python analysis/model_performance/evaluate_model_performance.py {self.sweep_name}")
        else:
            print("❌ Insufficient models for comprehensive analysis")
        
        return validation_result
    
    def create_transfer_metadata(self):
        """Create metadata for the model transfer."""
        metadata = {
            'sweep_name': self.sweep_name,
            'transfer_timestamp': datetime.now().isoformat(),
            'transfer_type': 'model_files_ssh_multiplexed',
            'structure_compatible_with': ['workflow4_model_evaluation'],
            'files_per_combination': ['final_model.zip'],
            'total_expected_combinations': 81,
            'ssh_multiplexing_used': True,
            'parameter_space': {
                'gamma_c': [25.0, 50.0, 100.0],
                'step_domain_fraction': [0.025, 0.05, 0.1],
                'rl_iterations_per_timestep': [10, 25, 40],
                'element_budget': [25, 30, 40]
            },
            'model_details': {
                'model_type': 'final_trained_models',
                'training_timesteps': '100k',
                'algorithm': 'A2C',
                'framework': 'stable_baselines3'
            }
        }
        
        metadata_path = self.local_models_path / "transfer_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"📋 Model transfer metadata: {metadata_path}")
        return metadata_path


def main():
    parser = argparse.ArgumentParser(description='Transfer model files using SSH multiplexing')
    parser.add_argument('sweep_name', help='Name of the parameter sweep')
    parser.add_argument('--hpc-path', required=True, help='HPC path to sweep results')
    parser.add_argument('--dry-run', action='store_true', help='Preview transfer without executing')
    parser.add_argument('--keep-existing', action='store_true', help='Keep existing models (do not clean)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    print("="*70)
    print(f"TRANSFER MODEL FILES: {args.sweep_name}")
    print("="*70)
    
    # Initialize model transfer
    transfer = ModelFilesTransfer(args.sweep_name, verbose=args.verbose)
    
    # Clean existing structure unless requested otherwise
    if not args.keep_existing:
        transfer.clean_existing_structure()
    
    # Execute model transfer
    results = transfer.transfer_model_files(args.hpc_path, dry_run=args.dry_run)
    
    # Print comprehensive results
    transfer.print_detailed_results(results)
    
    # If not dry run, validate and create metadata
    if not args.dry_run and results.get('transferred_count', 0) > 0:
        validation = transfer.validate_transfer()
        transfer.create_transfer_metadata()
        
        if validation.get('workflow4_ready', False):
            print(f"\n🎉 SUCCESS! Ready for Workflow 4 model evaluation:")
            print(f"   python analysis/model_performance/evaluate_model_performance.py {args.sweep_name}")
    
    return 0


if __name__ == "__main__":
    exit(main())