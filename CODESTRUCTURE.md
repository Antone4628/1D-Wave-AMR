# Project Code Structure

Auto-generated on: Thu May 29 10:30:06 MDT 2025
Project: 1D-Wave-AMR

```
1D-Wave-AMR/
├── experiments
│   ├── configs
│   │   ├── archive
│   │   │   ├── gamma_c_10.0.yaml
│   │   │   ├── gamma_c_100.0.yaml
│   │   │   ├── gamma_c_100.0_fixed_level_2.yaml
│   │   │   ├── gamma_c_100.0_random.yaml
│   │   │   ├── gamma_c_2.5.yaml
│   │   │   ├── gamma_c_25.0.yaml
│   │   │   ├── gamma_c_25.0_fixed_level_1.yaml
│   │   │   ├── gamma_c_25.0_fixed_level_2.yaml
│   │   │   ├── gamma_c_25.0_fixed_level_3.yaml
│   │   │   ├── gamma_c_25.0_random.yaml
│   │   │   ├── gamma_c_5.0.yaml
│   │   │   ├── gamma_c_50.0.yaml
│   │   │   ├── gamma_c_50.0_fixed_level_2.yaml
│   │   │   ├── gamma_c_50.0_random.yaml
│   │   │   └── test_config.yaml
│   │   ├── production
│   │   │   ├── element_budget_sweep
│   │   │   ├── gamma_c_sweep
│   │   │   ├── refinement_strategy_sweep
│   │   │   ├── gamma_c_100.0_full_run.yaml
│   │   │   └── gamma_c_100.0_random_step_domain_sweep.yaml
│   │   ├── tests
│   │   │   ├── quick_gpu_test.yaml
│   │   │   └── test_quick.yaml
│   │   ├── gamma_c_10.0.yaml
│   │   ├── gamma_c_100.0.yaml
│   │   ├── gamma_c_100.0_fixed_level_2.yaml
│   │   ├── gamma_c_100.0_random.yaml
│   │   ├── gamma_c_2.5.yaml
│   │   ├── gamma_c_25.0.yaml
│   │   ├── gamma_c_25.0_fixed_level_1.yaml
│   │   ├── gamma_c_25.0_fixed_level_2.yaml
│   │   ├── gamma_c_25.0_fixed_level_3.yaml
│   │   ├── gamma_c_25.0_random.yaml
│   │   ├── gamma_c_5.0.yaml
│   │   ├── gamma_c_50.0.yaml
│   │   ├── gamma_c_50.0_fixed_level_2.yaml
│   │   ├── gamma_c_50.0_random.yaml
│   │   ├── test_base_template.yaml
│   │   └── test_config.yaml
│   ├── manifests
│   │   ├── latest_test_manifest.yaml
│   │   └── test_manifest_2025-05-29_094907.yaml
│   ├── results
│   │   ├── gamma_c_100.0
│   │   │   ├── run_20250523_094718
│   │   │   └── run_20250523_201454
│   │   ├── gamma_c_25.0
│   │   │   ├── run_20250523_093432
│   │   │   ├── run_20250524_085638
│   │   │   └── run_20250526_095808
│   │   └── gamma_c_25.0_gpu
│   │       └── run_20250524_090233
│   ├── run_experiments_mixed.py
│   ├── run_experiments_mixed_gpu.py
│   └── test_mixed_approach.py
├── logs
│   ├── parameter_sweeps
│   │   └── step_domain_fraction
│   │       ├── run_2025-05-26_105842
│   │       ├── run_2025-05-26_105929
│   │       ├── run_2025-05-26_155744
│   │       ├── run_2025-05-26_155752
│   │       ├── run_2025-05-26_160141
│   │       ├── run_2025-05-26_184551
│   │       ├── run_2025-05-27_085636
│   │       ├── job_array_1884275_0.err
│   │       ├── job_array_1884275_0.out
│   │       ├── job_array_1884275_1.err
│   │       ├── job_array_1884275_1.out
│   │       ├── job_array_1884275_2.err
│   │       ├── job_array_1884275_2.out
│   │       ├── job_array_1884275_3.err
│   │       ├── job_array_1884275_3.out
│   │       ├── job_array_1884280_0.err
│   │       ├── job_array_1884280_0.out
│   │       ├── job_array_1884280_1.err
│   │       ├── job_array_1884280_1.out
│   │       ├── job_array_1884280_2.err
│   │       ├── job_array_1884280_2.out
│   │       ├── job_array_1884280_3.err
│   │       ├── job_array_1884280_3.out
│   │       ├── job_array_20k_1885722_0.err
│   │       ├── job_array_20k_1885722_0.out
│   │       ├── job_array_20k_1885722_1.err
│   │       ├── job_array_20k_1885722_1.out
│   │       ├── job_array_20k_1885722_2.err
│   │       └── job_array_20k_1885722_2.out
│   ├── amr_100k_1879743.err
│   ├── amr_100k_1879743.out
│   ├── amr_restart_1880495.err
│   ├── amr_restart_1880495.out
│   ├── amr_test_1879739.err
│   ├── amr_test_1879739.out
│   ├── step_domain_sweep_1887294_0.err
│   ├── step_domain_sweep_1887294_0.out
│   ├── step_domain_sweep_1887294_1.err
│   ├── step_domain_sweep_1887294_1.out
│   ├── step_domain_sweep_1887294_2.err
│   ├── step_domain_sweep_1887294_2.out
│   ├── step_domain_sweep_1887302_0.err
│   ├── step_domain_sweep_1887302_0.out
│   ├── step_domain_sweep_1887302_1.err
│   ├── step_domain_sweep_1887302_1.out
│   ├── step_domain_sweep_1887302_2.err
│   ├── step_domain_sweep_1887302_2.out
│   ├── test_param_sweep_1888906_0.err
│   ├── test_param_sweep_1888906_0.out
│   ├── test_param_sweep_1888906_1.err
│   ├── test_param_sweep_1888906_1.out
│   ├── test_param_sweep_1888910_0.err
│   ├── test_param_sweep_1888910_0.out
│   ├── test_param_sweep_1888910_1.err
│   ├── test_param_sweep_1888910_1.out
│   ├── test_param_sweep_1888912_0.err
│   ├── test_param_sweep_1888912_0.out
│   ├── test_param_sweep_1888912_1.err
│   ├── test_param_sweep_1888912_1.out
│   ├── test_param_sweep_1888914_0.err
│   ├── test_param_sweep_1888914_0.out
│   ├── test_param_sweep_1888914_1.err
│   └── test_param_sweep_1888914_1.out
├── notebooks
│   └── interactive_amr_testing.ipynb
├── numerical
│   ├── amr
│   │   ├── __init__.py
│   │   ├── adapt.py
│   │   ├── adapt_documented.py
│   │   ├── forest.py
│   │   ├── forest_documented.py
│   │   ├── model_adapt_sequential.py
│   │   ├── model_marker.py
│   │   └── projection.py
│   ├── callbacks
│   │   ├── __init__.py
│   │   ├── enhanced_callback.py
│   │   ├── enhanced_callback_mixed.py
│   │   ├── enhanced_callback_options.py
│   │   ├── enhanced_callback_v2.py
│   │   └── simple_monitor_callback.py
│   ├── dg
│   │   ├── __init__.py
│   │   ├── basis.py
│   │   └── matrices.py
│   ├── grid
│   │   ├── __init__.py
│   │   └── mesh.py
│   ├── solvers
│   │   ├── __init__.py
│   │   ├── dg_steady_solver.py
│   │   ├── dg_wave_solver.py
│   │   ├── dg_wave_solver_backup.py
│   │   ├── dg_wave_solver_clean.py
│   │   ├── dg_wave_solver_documented.py
│   │   ├── dg_wave_solver_free.py
│   │   ├── dg_wave_solver_mixed.py
│   │   ├── dg_wave_solver_mixed_clean.py
│   │   ├── dg_wave_solver_mixed_model.py
│   │   ├── dg_wave_solver_model.py
│   │   ├── dg_wave_solver_model_free.py
│   │   ├── dg_wave_solver_model_sequential.py
│   │   ├── dg_wave_solver_options.py
│   │   ├── utils.py
│   │   └── wave.py
│   └── __init__.py
├── results
│   ├── parameter_sweeps
│   │   └── step_domain_fraction
│   │       ├── run_2025-05-26_155744
│   │       ├── run_2025-05-26_155752
│   │       ├── run_2025-05-26_160141
│   │       ├── run_2025-05-26_184551
│   │       └── run_2025-05-27_085636
│   ├── step_domain_sweep_2025-05-28_090828
│   │   ├── step_domain_0.05
│   │   │   ├── gamma_c_100.0_gpu
│   │   │   └── run_info.yaml
│   │   ├── step_domain_0.10
│   │   │   ├── gamma_c_100.0_gpu
│   │   │   └── run_info.yaml
│   │   └── step_domain_0.15
│   │       ├── gamma_c_100.0_gpu
│   │       └── run_info.yaml
│   ├── step_domain_sweep_2025-05-28_092701
│   │   ├── step_domain_0.05
│   │   │   ├── gamma_c_100.0_gpu
│   │   │   └── run_info.yaml
│   │   ├── step_domain_0.10
│   │   │   ├── gamma_c_100.0_gpu
│   │   │   └── run_info.yaml
│   │   └── step_domain_0.15
│   │       ├── gamma_c_100.0_gpu
│   │       └── run_info.yaml
│   └── test_param_sweep_2025-05-29_094907
│       ├── gamma_25.0_step_0.05_rl_10_budget_25
│       │   ├── models
│       │   ├── tensorboard
│       │   ├── config.yaml
│       │   ├── device_info.txt
│       │   ├── final_model.zip
│       │   ├── monitor.csv
│       │   └── performance.txt
│       └── gamma_50.0_step_0.1_rl_25_budget_30
│           ├── models
│           ├── tensorboard
│           ├── config.yaml
│           ├── device_info.txt
│           ├── final_model.zip
│           ├── monitor.csv
│           └── performance.txt
├── scripts
│   ├── 1D_wave_amr.py
│   └── forest_example.py
├── slurm_scripts
│   ├── full_training_job.slurm
│   ├── restart_100k.slurm
│   ├── step_domain_sweep.slurm
│   ├── step_domain_sweep_20k.slurm
│   ├── step_domain_sweep_streamlined.slurm
│   ├── test_amr_job.slurm
│   └── test_param_sweep.slurm
├── src
│   └── dg_package
│       ├── __init__.py
│       ├── amr.py
│       ├── numerics.py
│       └── numerics_amr.py
├── tests
│   ├── outputs
│   │   ├── barrier_function 2.png
│   │   ├── barrier_function.png
│   │   ├── reward_vs_resource 2.png
│   │   └── reward_vs_resource.png
│   ├── test_amr
│   │   ├── __init__.py
│   │   ├── balance_test.py
│   │   ├── class_test.py
│   │   ├── delta_u_test.py
│   │   ├── flux_test.py
│   │   ├── mixed_model_class_test.py
│   │   ├── model_class_test.py
│   │   ├── projection_test.py
│   │   ├── python_matrices_comparison.pdf
│   │   ├── sequential_model_test.py
│   │   ├── steady_class_test.py
│   │   ├── steady_solve_analyze.py
│   │   ├── steady_test.py
│   │   ├── step_method_test.py
│   │   ├── test_gaussian_advection.py
│   │   ├── test_refinement_parameters.py
│   │   └── value_test.py
│   ├── test_animation
│   │   ├── __init__.py
│   │   └── manim_test.py
│   ├── test_RL
│   │   ├── __init__.py
│   │   ├── test_barrier_function.py
│   │   ├── test_reward.py
│   │   └── train_test.py
│   ├── __init__.py
│   ├── mixed_class_test.py
│   └── mixed_class_test_loop.py
├── tools
│   ├── __init__.py
│   ├── analyze_rl_performance.py
│   ├── analyze_tensorboard.py
│   ├── analyze_tensorboard_pdf.py
│   ├── CODESTRUCTURE.md
│   └── generate_codestructure.py
├── CODESTRUCTURE.md
├── create_base_config.py
├── create_manifest_system.py
├── create_slurm_scripts.py
├── create_test_sweep.py
├── monitor_param_sweep.py
├── project_structure.md
├── README.md
├── requirements.txt
├── setup.py
├── submit_test_sweep.sh
└── temp_config_3.yaml
```

## Key Directories

- **experiments/**: Training configurations and results
- **numerical/**: Core AMR and RL implementation
- **slurm_scripts/**: HPC job submission scripts
- **logs/**: SLURM job output and error logs
- **tools/**: Utility scripts and analysis tools

*Generated automatically using tools/generate_codestructure.py*