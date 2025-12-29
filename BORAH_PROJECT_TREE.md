# Project Tree

Generated: 2025-12-29 13:49:45
Project: 1D-Wave-AMR
Included: .py
Data dirs: collapsed

```
1D-Wave-AMR/
├── analysis/
│   ├── automated_reports/
│   │   └── quick_overview.py
│   ├── data/ [3 dirs, 0 files]
│   ├── data_management/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── debug_script_commands.py
│   │   ├── simple_transfer_for_anova.py
│   │   ├── transfer_analysis_files.py
│   │   ├── transfer_json_data.py
│   │   └── transfer_model_files.py
│   ├── model_performance/
│   │   ├── baseline_evaluator.py
│   │   ├── baseline_simulation_runner.py
│   │   ├── batch_model_evaluator.py
│   │   ├── batch_results_analyzer.py
│   │   ├── comprehensive_analyzer.py
│   │   ├── comprehensive_analyzer_backup.py
│   │   ├── dg_wave_solver_evaluation.py
│   │   ├── evaluate_single_model_by_index.py
│   │   ├── key_models_analyzer.py
│   │   ├── model_marker_evaluation.py
│   │   ├── pareto_front_analyzer.py
│   │   ├── pareto_key_models_analyzer.py
│   │   ├── pareto_key_models_analyzer_backup.py
│   │   ├── run_single_animation.py
│   │   ├── single_model_runner.py
│   │   ├── single_model_runner_batch.py
│   │   └── test_cost_ratio.py
│   ├── statistical_analysis/
│   │   ├── __init__.py
│   │   ├── anova_analysis.py
│   │   ├── anova_analysis_pingouin.py
│   │   └── test_imports.py
│   ├── transferability/
│   │   ├── animations/ [4 dirs, 0 files]
│   │   ├── results/ [0 dirs, 29 files]
│   │   ├── collect_results.py
│   │   ├── generate_job_list.py
│   │   ├── transferability_config.py
│   │   └── transferability_runner.py
│   ├── utilities/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── verification/
│   │   ├── verify_new_icases.py
│   │   └── verify_new_icases_updated.py
│   └── data_sample.py
├── animations/ [19 dirs, 0 files]
├── anova_results_session3_100k_uniform_20250715_153315/
├── anova_results_session3_100k_uniform_20250715_153845/
├── anova_results_session3_100k_uniform_20250715_154633/
├── collected_reports/
├── experiments/
│   ├── configs/
│   │   ├── archive/
│   │   ├── param_sweep/
│   │   ├── production/
│   │   │   ├── element_budget_sweep/
│   │   │   ├── gamma_c_sweep/
│   │   │   └── refinement_strategy_sweep/
│   │   └── tests/
│   ├── manifests/
│   ├── results/ [3 dirs, 0 files]
│   ├── run_experiments_mixed.py
│   ├── run_experiments_mixed_gpu.py
│   └── test_mixed_approach.py
├── logs/ [3 dirs, 0 files]
├── notebooks/
├── numerical/
│   ├── amr/
│   │   ├── __init__.py
│   │   ├── adapt.py
│   │   ├── adapt_documented.py
│   │   ├── forest.py
│   │   ├── forest_documented.py
│   │   ├── model_adapt_sequential.py
│   │   ├── model_marker.py
│   │   └── projection.py
│   ├── callbacks/
│   │   ├── __init__.py
│   │   ├── enhanced_callback.py
│   │   ├── enhanced_callback_data.py
│   │   ├── enhanced_callback_mixed.py
│   │   ├── enhanced_callback_mixed_backup.py
│   │   ├── enhanced_callback_options.py
│   │   ├── enhanced_callback_v2.py
│   │   └── simple_monitor_callback.py
│   ├── dg/
│   │   ├── __init__.py
│   │   ├── basis.py
│   │   └── matrices.py
│   ├── environments/
│   │   ├── __init__.py
│   │   ├── dg_amr_env.py
│   │   ├── dg_amr_env_backup.py
│   │   ├── dg_amr_env_clean.py
│   │   ├── dg_amr_env_documented.py
│   │   ├── dg_amr_env_mixed.py
│   │   └── dg_amr_env_mixed_backup.py
│   ├── grid/
│   │   ├── __init__.py
│   │   └── mesh.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   ├── dg_steady_solver.py
│   │   ├── dg_wave_solver.py
│   │   ├── dg_wave_solver_backup.py
│   │   ├── dg_wave_solver_baseline.py
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
├── results/ [11 dirs, 0 files]
├── scripts/
│   ├── 1D_wave_amr.py
│   └── forest_example.py
├── slurm_scripts/
│   ├── logs/ [0 dirs, 0 files]
│   ├── param_sweep/
│   └── param_sweep_data/
├── src/
│   └── dg_package/
│       ├── __init__.py
│       ├── amr.py
│       ├── numerics.py
│       └── numerics_amr.py
├── tests/
│   ├── outputs/
│   ├── test_amr/
│   │   ├── __init__.py
│   │   ├── balance_test.py
│   │   ├── class_test.py
│   │   ├── delta_u_test.py
│   │   ├── flux_test.py
│   │   ├── mixed_model_class_test.py
│   │   ├── model_class_test.py
│   │   ├── projection_test.py
│   │   ├── sequential_model_test.py
│   │   ├── steady_class_test.py
│   │   ├── steady_solve_analyze.py
│   │   ├── steady_test.py
│   │   ├── step_method_test.py
│   │   ├── test_gaussian_advection.py
│   │   ├── test_refinement_parameters.py
│   │   └── value_test.py
│   ├── test_animation/
│   │   ├── __init__.py
│   │   └── manim_test.py
│   ├── test_RL/
│   │   ├── __init__.py
│   │   ├── check_env.py
│   │   ├── test_barrier_function.py
│   │   ├── test_env.py
│   │   ├── test_reward.py
│   │   └── train_test.py
│   ├── __init__.py
│   ├── mixed_class_test.py
│   ├── mixed_class_test_loop.py
│   └── test_enhanced_callback.py
├── tools/
│   ├── __init__.py
│   ├── analyze_rl_performance.py
│   ├── analyze_tensorboard.py
│   ├── analyze_tensorboard_pdf.py
│   ├── generate_codestructure.py
│   ├── generate_model_transfer_commands.py
│   ├── generate_robust_model_transfer.py
│   ├── hpc_data_survey.py
│   └── tree_gen.py
├── anova_analysis_pingouin.py
├── batch_analysis_runner.py
├── batch_animation_runner.py
├── collect_training_reports.py
├── create_base_config.py
├── create_batch_baseline_jobs.py
├── create_batch_evaluation_jobs.py
├── create_data_export_scripts.py
├── create_data_export_scripts_original.py
├── create_manifest_system.py
├── create_slurm_scripts.py
├── create_test_sweep.py
├── debug_paths.py
├── inspect_csv_structure.py
├── monitor_param_sweep.py
├── setup.py
├── setup_local_analysis.py
├── test_batch_animations.py
└── test_minimal_training.py
```

---
*Generated by tools/tree_gen.py*