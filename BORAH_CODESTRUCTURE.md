# Project Code Structure

Auto-generated on: Thu Jul 31 15:43:46 MDT 2025
Project: 1D-Wave-AMR

```
1D-Wave-AMR/
├── analysis
│   ├── automated_reports
│   │   └── quick_overview.py
│   ├── data
│   │   ├── model_performance
│   │   │   └── session3_100k_uniform
│   │   ├── models
│   │   │   └── session3_100k_uniform
│   │   └── processed
│   │       ├── full_param_sweep_data_20250601_105453
│   │       └── session3_100k_uniform
│   ├── data_management
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── debug_script_commands.py
│   │   ├── simple_transfer_for_anova.py
│   │   ├── transfer_analysis_files.py
│   │   ├── transfer_json_data.py
│   │   └── transfer_model_files.py
│   ├── model_performance
│   │   ├── baseline_evaluator.py
│   │   ├── baseline_simulation_runner.py
│   │   ├── batch_model_evaluator.py
│   │   ├── batch_results_analyzer.py
│   │   ├── comprehensive_analyzer.py
│   │   ├── comprehensive_analyzer.py.backup
│   │   ├── comprehensive_analyzer_backup.py
│   │   ├── dg_wave_solver_evaluation.py
│   │   ├── dg_wave_solver_evaluation.py.backup
│   │   ├── evaluate_single_model_by_index.py
│   │   ├── evaluate_single_model_by_index.py.backup
│   │   ├── key_models_analyzer.py
│   │   ├── model_marker_evaluation.py
│   │   ├── model_marker_evaluation.py.backup
│   │   ├── pareto_front_analyzer.py
│   │   ├── pareto_key_models_analyzer.py
│   │   ├── pareto_key_models_analyzer_backup.py
│   │   ├── run_single_animation.py
│   │   ├── single_model_runner.py
│   │   ├── single_model_runner_batch.py
│   │   └── test_cost_ratio.py
│   ├── statistical_analysis
│   │   ├── __init__.py
│   │   ├── anova_analysis.py
│   │   ├── anova_analysis_pingouin.py
│   │   └── test_imports.py
│   ├── utilities
│   │   ├── __init__.py
│   │   └── config.py
│   └── data_sample.py
├── animations
│   ├── baselines
│   │   ├── conventional-amr_ref4_budget80_t0.0001
│   │   │   └── baseline_conventional-amr_ref4_budget80_t0.0001_snapshot.png
│   │   ├── no-amr_ref4_budget80
│   │   │   └── baseline_no-amr_ref4_budget80_snapshot.png
│   │   └── no-amr_ref5_budget150
│   │       └── baseline_no-amr_ref5_budget150_final.png
│   ├── gamma_100.0_step_0.1_rl_10_budget_25
│   │   ├── final_model_g100.0_s0.1_r10_b25_final.pdf
│   │   └── final_model_g100.0_s0.1_r10_b25_final.png
│   ├── gamma_100.0_step_0.1_rl_40_budget_40
│   │   ├── final_model_g100.0_s0.1_r40_b40_snapshot.pdf
│   │   └── final_model_g100.0_s0.1_r40_b40_snapshot.png
│   ├── gamma_25.0_step_0.025_rl_10_budget_25
│   │   ├── final_model_g25.0_s0.025_r10_b25_final.pdf
│   │   ├── final_model_g25.0_s0.025_r10_b25_final.png
│   │   ├── final_model_g25.0_s0.025_r10_b25_snapshot.pdf
│   │   └── final_model_g25.0_s0.025_r10_b25_snapshot.png
│   ├── gamma_25.0_step_0.1_rl_40_budget_30
│   │   ├── final_model_g25.0_s0.1_r40_b30_final.pdf
│   │   ├── final_model_g25.0_s0.1_r40_b30_final.png
│   │   ├── final_model_g25.0_s0.1_r40_b30_snapshot.pdf
│   │   └── final_model_g25.0_s0.1_r40_b30_snapshot.png
│   ├── gamma_50.0_step_0.05_rl_10_budget_25
│   │   ├── final_model_g50.0_s0.05_r10_b25_final.pdf
│   │   ├── final_model_g50.0_s0.05_r10_b25_final.png
│   │   ├── final_model_g50.0_s0.05_r10_b25_snapshot.pdf
│   │   └── final_model_g50.0_s0.05_r10_b25_snapshot.png
│   ├── gamma_50.0_step_0.10_rl_25_budget_30
│   └── gamma_50.0_step_0.1_rl_25_budget_30
│       ├── final_model_g50.0_s0.1_r25_b30_animate.mp4
│       ├── final_model_g50.0_s0.1_r25_b30_final.pdf
│       ├── final_model_g50.0_s0.1_r25_b30_final.png
│       ├── final_model_g50.0_s0.1_r25_b30_snapshot.pdf
│       └── final_model_g50.0_s0.1_r25_b30_snapshot.png
├── anova_results_session3_100k_uniform_20250715_153315
│   ├── anova_detailed_session3_100k_uniform.json
│   └── pingouin_anova_results_session3_100k_uniform.pdf
├── anova_results_session3_100k_uniform_20250715_153845
│   ├── anova_detailed_session3_100k_uniform.json
│   └── pingouin_anova_results_session3_100k_uniform.pdf
├── anova_results_session3_100k_uniform_20250715_154633
│   ├── anova_detailed_session3_100k_uniform.json
│   ├── anova_summary_session3_100k_uniform.csv
│   ├── cleaned_data_session3_100k_uniform.csv
│   └── pingouin_anova_results_session3_100k_uniform.pdf
├── collected_reports
│   ├── gamma_100.0_step_0.025_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.025_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.05_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_100.0_step_0.1_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.025_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.05_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_25.0_step_0.1_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.025_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_40_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.05_rl_40_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_10_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_10_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_10_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_25_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_25_budget_30_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_25_budget_40_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_40_budget_25_50k_training_report.pdf
│   ├── gamma_50.0_step_0.1_rl_40_budget_30_50k_training_report.pdf
│   └── gamma_50.0_step_0.1_rl_40_budget_40_50k_training_report.pdf
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
│   │   ├── param_sweep
│   │   │   ├── base_template.yaml
│   │   │   ├── base_template.yaml.backup
│   │   │   └── substitution_guide.yaml
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
│   │   ├── full_param_sweep_2025-05-29_105232.yaml
│   │   ├── latest_manifest.yaml
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
│   ├── param_sweep
│   │   ├── group_01_1888923_0.err
│   │   ├── group_01_1888923_0.out
│   │   ├── group_01_1888923_1.err
│   │   ├── group_01_1888923_1.out
│   │   ├── group_01_1888923_2.err
│   │   ├── group_01_1888923_2.out
│   │   ├── group_01_1888923_3.err
│   │   ├── group_01_1888923_3.out
│   │   ├── group_01_1888923_4.err
│   │   ├── group_01_1888923_4.out
│   │   ├── group_01_1888923_5.err
│   │   ├── group_01_1888923_5.out
│   │   ├── group_01_1888923_6.err
│   │   ├── group_01_1888923_6.out
│   │   ├── group_01_1888923_7.err
│   │   ├── group_01_1888923_7.out
│   │   ├── group_01_1888923_8.err
│   │   ├── group_01_1888923_8.out
│   │   ├── group_01_1889005_0.err
│   │   ├── group_01_1889005_0.out
│   │   ├── group_01_1889005_1.err
│   │   ├── group_01_1889005_1.out
│   │   ├── group_01_1889005_2.err
│   │   ├── group_01_1889005_2.out
│   │   ├── group_01_1889005_3.err
│   │   ├── group_01_1889005_3.out
│   │   ├── group_01_1889005_4.err
│   │   ├── group_01_1889005_4.out
│   │   ├── group_01_1889005_5.err
│   │   ├── group_01_1889005_5.out
│   │   ├── group_01_1889005_6.err
│   │   ├── group_01_1889005_6.out
│   │   ├── group_01_1889005_7.err
│   │   ├── group_01_1889005_7.out
│   │   ├── group_01_1889005_8.err
│   │   ├── group_01_1889005_8.out
│   │   ├── group_01_1889088_0.err
│   │   ├── group_01_1889088_0.out
│   │   ├── group_01_1889088_1.err
│   │   ├── group_01_1889088_1.out
│   │   ├── group_01_1889088_2.err
│   │   ├── group_01_1889088_2.out
│   │   ├── group_01_1889088_3.err
│   │   ├── group_01_1889088_3.out
│   │   ├── group_01_1889088_4.err
│   │   ├── group_01_1889088_4.out
│   │   ├── group_01_1889088_5.err
│   │   ├── group_01_1889088_5.out
│   │   ├── group_01_1889088_6.err
│   │   ├── group_01_1889088_6.out
│   │   ├── group_01_1889088_7.err
│   │   ├── group_01_1889088_7.out
│   │   ├── group_01_1889088_8.err
│   │   ├── group_01_1889088_8.out
│   │   ├── group_02_1888930_0.err
│   │   ├── group_02_1888930_0.out
│   │   ├── group_02_1888930_1.err
│   │   ├── group_02_1888930_1.out
│   │   ├── group_02_1888930_2.err
│   │   ├── group_02_1888930_2.out
│   │   ├── group_02_1888930_3.err
│   │   ├── group_02_1888930_3.out
│   │   ├── group_02_1888930_4.err
│   │   ├── group_02_1888930_4.out
│   │   ├── group_02_1888930_5.err
│   │   ├── group_02_1888930_5.out
│   │   ├── group_02_1888930_6.err
│   │   ├── group_02_1888930_6.out
│   │   ├── group_02_1888930_7.err
│   │   ├── group_02_1888930_7.out
│   │   ├── group_02_1888930_8.err
│   │   ├── group_02_1888930_8.out
│   │   ├── group_02_1889010_0.err
│   │   ├── group_02_1889010_0.out
│   │   ├── group_02_1889010_1.err
│   │   ├── group_02_1889010_1.out
│   │   ├── group_02_1889010_2.err
│   │   ├── group_02_1889010_2.out
│   │   ├── group_02_1889010_3.err
│   │   ├── group_02_1889010_3.out
│   │   ├── group_02_1889010_4.err
│   │   ├── group_02_1889010_4.out
│   │   ├── group_02_1889010_5.err
│   │   ├── group_02_1889010_5.out
│   │   ├── group_02_1889010_6.err
│   │   ├── group_02_1889010_6.out
│   │   ├── group_02_1889010_7.err
│   │   ├── group_02_1889010_7.out
│   │   ├── group_02_1889010_8.err
│   │   ├── group_02_1889010_8.out
│   │   ├── group_02_1889093_0.err
│   │   ├── group_02_1889093_0.out
│   │   ├── group_02_1889093_1.err
│   │   ├── group_02_1889093_1.out
│   │   ├── group_02_1889093_2.err
│   │   ├── group_02_1889093_2.out
│   │   ├── group_02_1889093_3.err
│   │   ├── group_02_1889093_3.out
│   │   ├── group_02_1889093_4.err
│   │   ├── group_02_1889093_4.out
│   │   ├── group_02_1889093_5.err
│   │   ├── group_02_1889093_5.out
│   │   ├── group_02_1889093_6.err
│   │   ├── group_02_1889093_6.out
│   │   ├── group_02_1889093_7.err
│   │   ├── group_02_1889093_7.out
│   │   ├── group_02_1889093_8.err
│   │   ├── group_02_1889093_8.out
│   │   ├── group_03_1888933_0.err
│   │   ├── group_03_1888933_0.out
│   │   ├── group_03_1888933_1.err
│   │   ├── group_03_1888933_1.out
│   │   ├── group_03_1888933_2.err
│   │   ├── group_03_1888933_2.out
│   │   ├── group_03_1888933_3.err
│   │   ├── group_03_1888933_3.out
│   │   ├── group_03_1888933_4.err
│   │   ├── group_03_1888933_4.out
│   │   ├── group_03_1888933_5.err
│   │   ├── group_03_1888933_5.out
│   │   ├── group_03_1888933_6.err
│   │   ├── group_03_1888933_6.out
│   │   ├── group_03_1888933_7.err
│   │   ├── group_03_1888933_7.out
│   │   ├── group_03_1888933_8.err
│   │   ├── group_03_1888933_8.out
│   │   ├── group_03_1889011_0.err
│   │   ├── group_03_1889011_0.out
│   │   ├── group_03_1889011_1.err
│   │   ├── group_03_1889011_1.out
│   │   ├── group_03_1889011_2.err
│   │   ├── group_03_1889011_2.out
│   │   ├── group_03_1889011_3.err
│   │   ├── group_03_1889011_3.out
│   │   ├── group_03_1889011_4.err
│   │   ├── group_03_1889011_4.out
│   │   ├── group_03_1889011_5.err
│   │   ├── group_03_1889011_5.out
│   │   ├── group_03_1889011_6.err
│   │   ├── group_03_1889011_6.out
│   │   ├── group_03_1889011_7.err
│   │   ├── group_03_1889011_7.out
│   │   ├── group_03_1889011_8.err
│   │   ├── group_03_1889011_8.out
│   │   ├── group_03_1889094_0.err
│   │   ├── group_03_1889094_0.out
│   │   ├── group_03_1889094_1.err
│   │   ├── group_03_1889094_1.out
│   │   ├── group_03_1889094_2.err
│   │   ├── group_03_1889094_2.out
│   │   ├── group_03_1889094_3.err
│   │   ├── group_03_1889094_3.out
│   │   ├── group_03_1889094_4.err
│   │   ├── group_03_1889094_4.out
│   │   ├── group_03_1889094_5.err
│   │   ├── group_03_1889094_5.out
│   │   ├── group_03_1889094_6.err
│   │   ├── group_03_1889094_6.out
│   │   ├── group_03_1889094_7.err
│   │   ├── group_03_1889094_7.out
│   │   ├── group_03_1889094_8.err
│   │   ├── group_03_1889094_8.out
│   │   ├── group_04_1888935_0.err
│   │   ├── group_04_1888935_0.out
│   │   ├── group_04_1888935_1.err
│   │   ├── group_04_1888935_1.out
│   │   ├── group_04_1888935_2.err
│   │   ├── group_04_1888935_2.out
│   │   ├── group_04_1888935_3.err
│   │   ├── group_04_1888935_3.out
│   │   ├── group_04_1888935_4.err
│   │   ├── group_04_1888935_4.out
│   │   ├── group_04_1888935_5.err
│   │   ├── group_04_1888935_5.out
│   │   ├── group_04_1888935_6.err
│   │   ├── group_04_1888935_6.out
│   │   ├── group_04_1888935_7.err
│   │   ├── group_04_1888935_7.out
│   │   ├── group_04_1888935_8.err
│   │   ├── group_04_1888935_8.out
│   │   ├── group_04_1889012_0.err
│   │   ├── group_04_1889012_0.out
│   │   ├── group_04_1889012_1.err
│   │   ├── group_04_1889012_1.out
│   │   ├── group_04_1889012_2.err
│   │   ├── group_04_1889012_2.out
│   │   ├── group_04_1889012_3.err
│   │   ├── group_04_1889012_3.out
│   │   ├── group_04_1889012_4.err
│   │   ├── group_04_1889012_4.out
│   │   ├── group_04_1889012_5.err
│   │   ├── group_04_1889012_5.out
│   │   ├── group_04_1889012_6.err
│   │   ├── group_04_1889012_6.out
│   │   ├── group_04_1889012_7.err
│   │   ├── group_04_1889012_7.out
│   │   ├── group_04_1889012_8.err
│   │   ├── group_04_1889012_8.out
│   │   ├── group_04_1889095_0.err
│   │   ├── group_04_1889095_0.out
│   │   ├── group_04_1889095_1.err
│   │   ├── group_04_1889095_1.out
│   │   ├── group_04_1889095_2.err
│   │   ├── group_04_1889095_2.out
│   │   ├── group_04_1889095_3.err
│   │   ├── group_04_1889095_3.out
│   │   ├── group_04_1889095_4.err
│   │   ├── group_04_1889095_4.out
│   │   ├── group_04_1889095_5.err
│   │   ├── group_04_1889095_5.out
│   │   ├── group_04_1889095_6.err
│   │   ├── group_04_1889095_6.out
│   │   ├── group_04_1889095_7.err
│   │   ├── group_04_1889095_7.out
│   │   ├── group_04_1889095_8.err
│   │   ├── group_04_1889095_8.out
│   │   ├── group_05_1888940_0.err
│   │   ├── group_05_1888940_0.out
│   │   ├── group_05_1888940_1.err
│   │   ├── group_05_1888940_1.out
│   │   ├── group_05_1888940_2.err
│   │   ├── group_05_1888940_2.out
│   │   ├── group_05_1888940_3.err
│   │   ├── group_05_1888940_3.out
│   │   ├── group_05_1888940_4.err
│   │   ├── group_05_1888940_4.out
│   │   ├── group_05_1888940_5.err
│   │   ├── group_05_1888940_5.out
│   │   ├── group_05_1888940_6.err
│   │   ├── group_05_1888940_6.out
│   │   ├── group_05_1888940_7.err
│   │   ├── group_05_1888940_7.out
│   │   ├── group_05_1888940_8.err
│   │   ├── group_05_1888940_8.out
│   │   ├── group_05_1889017_0.err
│   │   ├── group_05_1889017_0.out
│   │   ├── group_05_1889017_1.err
│   │   ├── group_05_1889017_1.out
│   │   ├── group_05_1889017_2.err
│   │   ├── group_05_1889017_2.out
│   │   ├── group_05_1889017_3.err
│   │   ├── group_05_1889017_3.out
│   │   ├── group_05_1889017_4.err
│   │   ├── group_05_1889017_4.out
│   │   ├── group_05_1889017_5.err
│   │   ├── group_05_1889017_5.out
│   │   ├── group_05_1889017_6.err
│   │   ├── group_05_1889017_6.out
│   │   ├── group_05_1889017_7.err
│   │   ├── group_05_1889017_7.out
│   │   ├── group_05_1889017_8.err
│   │   ├── group_05_1889017_8.out
│   │   ├── group_05_1889096_0.err
│   │   ├── group_05_1889096_0.out
│   │   ├── group_05_1889096_1.err
│   │   ├── group_05_1889096_1.out
│   │   ├── group_05_1889096_2.err
│   │   ├── group_05_1889096_2.out
│   │   ├── group_05_1889096_3.err
│   │   ├── group_05_1889096_3.out
│   │   ├── group_05_1889096_4.err
│   │   ├── group_05_1889096_4.out
│   │   ├── group_05_1889096_5.err
│   │   ├── group_05_1889096_5.out
│   │   ├── group_05_1889096_6.err
│   │   ├── group_05_1889096_6.out
│   │   ├── group_05_1889096_7.err
│   │   ├── group_05_1889096_7.out
│   │   ├── group_05_1889096_8.err
│   │   ├── group_05_1889096_8.out
│   │   ├── group_06_1888945_0.err
│   │   ├── group_06_1888945_0.out
│   │   ├── group_06_1888945_1.err
│   │   ├── group_06_1888945_1.out
│   │   ├── group_06_1888945_2.err
│   │   ├── group_06_1888945_2.out
│   │   ├── group_06_1888945_3.err
│   │   ├── group_06_1888945_3.out
│   │   ├── group_06_1888945_4.err
│   │   ├── group_06_1888945_4.out
│   │   ├── group_06_1888945_5.err
│   │   ├── group_06_1888945_5.out
│   │   ├── group_06_1888945_6.err
│   │   ├── group_06_1888945_6.out
│   │   ├── group_06_1888945_7.err
│   │   ├── group_06_1888945_7.out
│   │   ├── group_06_1888945_8.err
│   │   ├── group_06_1888945_8.out
│   │   ├── group_06_1889018_0.err
│   │   ├── group_06_1889018_0.out
│   │   ├── group_06_1889018_1.err
│   │   ├── group_06_1889018_1.out
│   │   ├── group_06_1889018_2.err
│   │   ├── group_06_1889018_2.out
│   │   ├── group_06_1889018_3.err
│   │   ├── group_06_1889018_3.out
│   │   ├── group_06_1889018_4.err
│   │   ├── group_06_1889018_4.out
│   │   ├── group_06_1889018_5.err
│   │   ├── group_06_1889018_5.out
│   │   ├── group_06_1889018_6.err
│   │   ├── group_06_1889018_6.out
│   │   ├── group_06_1889018_7.err
│   │   ├── group_06_1889018_7.out
│   │   ├── group_06_1889018_8.err
│   │   ├── group_06_1889018_8.out
│   │   ├── group_06_1889097_0.err
│   │   ├── group_06_1889097_0.out
│   │   ├── group_06_1889097_1.err
│   │   ├── group_06_1889097_1.out
│   │   ├── group_06_1889097_2.err
│   │   ├── group_06_1889097_2.out
│   │   ├── group_06_1889097_3.err
│   │   ├── group_06_1889097_3.out
│   │   ├── group_06_1889097_4.err
│   │   ├── group_06_1889097_4.out
│   │   ├── group_06_1889097_5.err
│   │   ├── group_06_1889097_5.out
│   │   ├── group_06_1889097_6.err
│   │   ├── group_06_1889097_6.out
│   │   ├── group_06_1889097_7.err
│   │   ├── group_06_1889097_7.out
│   │   ├── group_06_1889097_8.err
│   │   ├── group_06_1889097_8.out
│   │   ├── group_07_1888952_0.err
│   │   ├── group_07_1888952_0.out
│   │   ├── group_07_1888952_1.err
│   │   ├── group_07_1888952_1.out
│   │   ├── group_07_1888952_2.err
│   │   ├── group_07_1888952_2.out
│   │   ├── group_07_1888952_3.err
│   │   ├── group_07_1888952_3.out
│   │   ├── group_07_1888952_4.err
│   │   ├── group_07_1888952_4.out
│   │   ├── group_07_1888952_5.err
│   │   ├── group_07_1888952_5.out
│   │   ├── group_07_1888952_6.err
│   │   ├── group_07_1888952_6.out
│   │   ├── group_07_1888952_7.err
│   │   ├── group_07_1888952_7.out
│   │   ├── group_07_1888952_8.err
│   │   ├── group_07_1888952_8.out
│   │   ├── group_07_1889019_0.err
│   │   ├── group_07_1889019_0.out
│   │   ├── group_07_1889019_1.err
│   │   ├── group_07_1889019_1.out
│   │   ├── group_07_1889019_2.err
│   │   ├── group_07_1889019_2.out
│   │   ├── group_07_1889019_3.err
│   │   ├── group_07_1889019_3.out
│   │   ├── group_07_1889019_4.err
│   │   ├── group_07_1889019_4.out
│   │   ├── group_07_1889019_5.err
│   │   ├── group_07_1889019_5.out
│   │   ├── group_07_1889019_6.err
│   │   ├── group_07_1889019_6.out
│   │   ├── group_07_1889019_7.err
│   │   ├── group_07_1889019_7.out
│   │   ├── group_07_1889019_8.err
│   │   ├── group_07_1889019_8.out
│   │   ├── group_07_1889098_0.err
│   │   ├── group_07_1889098_0.out
│   │   ├── group_07_1889098_1.err
│   │   ├── group_07_1889098_1.out
│   │   ├── group_07_1889098_2.err
│   │   ├── group_07_1889098_2.out
│   │   ├── group_07_1889098_3.err
│   │   ├── group_07_1889098_3.out
│   │   ├── group_07_1889098_4.err
│   │   ├── group_07_1889098_4.out
│   │   ├── group_07_1889098_5.err
│   │   ├── group_07_1889098_5.out
│   │   ├── group_07_1889098_6.err
│   │   ├── group_07_1889098_6.out
│   │   ├── group_07_1889098_7.err
│   │   ├── group_07_1889098_7.out
│   │   ├── group_07_1889098_8.err
│   │   ├── group_07_1889098_8.out
│   │   ├── group_08_1888958_0.err
│   │   ├── group_08_1888958_0.out
│   │   ├── group_08_1888958_1.err
│   │   ├── group_08_1888958_1.out
│   │   ├── group_08_1888958_2.err
│   │   ├── group_08_1888958_2.out
│   │   ├── group_08_1888958_3.err
│   │   ├── group_08_1888958_3.out
│   │   ├── group_08_1888958_4.err
│   │   ├── group_08_1888958_4.out
│   │   ├── group_08_1888958_5.err
│   │   ├── group_08_1888958_5.out
│   │   ├── group_08_1888958_6.err
│   │   ├── group_08_1888958_6.out
│   │   ├── group_08_1888958_7.err
│   │   ├── group_08_1888958_7.out
│   │   ├── group_08_1888958_8.err
│   │   ├── group_08_1888958_8.out
│   │   ├── group_08_1889020_0.err
│   │   ├── group_08_1889020_0.out
│   │   ├── group_08_1889020_1.err
│   │   ├── group_08_1889020_1.out
│   │   ├── group_08_1889020_2.err
│   │   ├── group_08_1889020_2.out
│   │   ├── group_08_1889020_3.err
│   │   ├── group_08_1889020_3.out
│   │   ├── group_08_1889020_4.err
│   │   ├── group_08_1889020_4.out
│   │   ├── group_08_1889020_5.err
│   │   ├── group_08_1889020_5.out
│   │   ├── group_08_1889020_6.err
│   │   ├── group_08_1889020_6.out
│   │   ├── group_08_1889020_7.err
│   │   ├── group_08_1889020_7.out
│   │   ├── group_08_1889020_8.err
│   │   ├── group_08_1889020_8.out
│   │   ├── group_08_1889099_0.err
│   │   ├── group_08_1889099_0.out
│   │   ├── group_08_1889099_1.err
│   │   ├── group_08_1889099_1.out
│   │   ├── group_08_1889099_2.err
│   │   ├── group_08_1889099_2.out
│   │   ├── group_08_1889099_3.err
│   │   ├── group_08_1889099_3.out
│   │   ├── group_08_1889099_4.err
│   │   ├── group_08_1889099_4.out
│   │   ├── group_08_1889099_5.err
│   │   ├── group_08_1889099_5.out
│   │   ├── group_08_1889099_6.err
│   │   ├── group_08_1889099_6.out
│   │   ├── group_08_1889099_7.err
│   │   ├── group_08_1889099_7.out
│   │   ├── group_08_1889099_8.err
│   │   ├── group_08_1889099_8.out
│   │   ├── group_09_1888964_0.err
│   │   ├── group_09_1888964_0.out
│   │   ├── group_09_1888964_1.err
│   │   ├── group_09_1888964_1.out
│   │   ├── group_09_1888964_2.err
│   │   ├── group_09_1888964_2.out
│   │   ├── group_09_1888964_3.err
│   │   ├── group_09_1888964_3.out
│   │   ├── group_09_1888964_4.err
│   │   ├── group_09_1888964_4.out
│   │   ├── group_09_1888964_5.err
│   │   ├── group_09_1888964_5.out
│   │   ├── group_09_1888964_6.err
│   │   ├── group_09_1888964_6.out
│   │   ├── group_09_1888964_7.err
│   │   ├── group_09_1888964_7.out
│   │   ├── group_09_1888964_8.err
│   │   ├── group_09_1888964_8.out
│   │   ├── group_09_1889021_0.err
│   │   ├── group_09_1889021_0.out
│   │   ├── group_09_1889021_1.err
│   │   ├── group_09_1889021_1.out
│   │   ├── group_09_1889021_2.err
│   │   ├── group_09_1889021_2.out
│   │   ├── group_09_1889021_3.err
│   │   ├── group_09_1889021_3.out
│   │   ├── group_09_1889021_4.err
│   │   ├── group_09_1889021_4.out
│   │   ├── group_09_1889021_5.err
│   │   ├── group_09_1889021_5.out
│   │   ├── group_09_1889021_6.err
│   │   ├── group_09_1889021_6.out
│   │   ├── group_09_1889021_7.err
│   │   ├── group_09_1889021_7.out
│   │   ├── group_09_1889021_8.err
│   │   ├── group_09_1889021_8.out
│   │   ├── group_09_1889100_0.err
│   │   ├── group_09_1889100_0.out
│   │   ├── group_09_1889100_1.err
│   │   ├── group_09_1889100_1.out
│   │   ├── group_09_1889100_2.err
│   │   ├── group_09_1889100_2.out
│   │   ├── group_09_1889100_3.err
│   │   ├── group_09_1889100_3.out
│   │   ├── group_09_1889100_4.err
│   │   ├── group_09_1889100_4.out
│   │   ├── group_09_1889100_5.err
│   │   ├── group_09_1889100_5.out
│   │   ├── group_09_1889100_6.err
│   │   ├── group_09_1889100_6.out
│   │   ├── group_09_1889100_7.err
│   │   ├── group_09_1889100_7.out
│   │   ├── group_09_1889100_8.err
│   │   └── group_09_1889100_8.out
│   ├── param_sweep_data
│   │   ├── group_01_1912820_0.err
│   │   ├── group_01_1912820_0.out
│   │   ├── group_01_1912820_1.err
│   │   ├── group_01_1912820_1.out
│   │   ├── group_01_1912820_2.err
│   │   ├── group_01_1912820_2.out
│   │   ├── group_01_1912820_3.err
│   │   ├── group_01_1912820_3.out
│   │   ├── group_01_1912820_4.err
│   │   ├── group_01_1912820_4.out
│   │   ├── group_01_1912820_5.err
│   │   ├── group_01_1912820_5.out
│   │   ├── group_01_1912820_6.err
│   │   ├── group_01_1912820_6.out
│   │   ├── group_01_1912820_7.err
│   │   ├── group_01_1912820_7.out
│   │   ├── group_01_1912820_8.err
│   │   ├── group_01_1912820_8.out
│   │   ├── group_01_1969928_0.err
│   │   ├── group_01_1969928_0.out
│   │   ├── group_01_1969928_1.err
│   │   ├── group_01_1969928_1.out
│   │   ├── group_01_1969928_2.err
│   │   ├── group_01_1969928_2.out
│   │   ├── group_01_1969928_3.err
│   │   ├── group_01_1969928_3.out
│   │   ├── group_01_1969957_0.err
│   │   ├── group_01_1969957_0.out
│   │   ├── group_01_1969957_1.err
│   │   ├── group_01_1969957_1.out
│   │   ├── group_01_1969957_2.err
│   │   ├── group_01_1969957_2.out
│   │   ├── group_01_1969957_3.err
│   │   ├── group_01_1969957_3.out
│   │   ├── group_01_1969957_4.err
│   │   ├── group_01_1969957_4.out
│   │   ├── group_01_1969957_5.err
│   │   ├── group_01_1969957_5.out
│   │   ├── group_01_1969957_6.err
│   │   ├── group_01_1969957_6.out
│   │   ├── group_01_1969957_7.err
│   │   ├── group_01_1969957_7.out
│   │   ├── group_01_1969957_8.err
│   │   ├── group_01_1969957_8.out
│   │   ├── group_02_1912821_0.err
│   │   ├── group_02_1912821_0.out
│   │   ├── group_02_1912821_1.err
│   │   ├── group_02_1912821_1.out
│   │   ├── group_02_1912821_2.err
│   │   ├── group_02_1912821_2.out
│   │   ├── group_02_1912821_3.err
│   │   ├── group_02_1912821_3.out
│   │   ├── group_02_1912821_4.err
│   │   ├── group_02_1912821_4.out
│   │   ├── group_02_1912821_5.err
│   │   ├── group_02_1912821_5.out
│   │   ├── group_02_1912821_6.err
│   │   ├── group_02_1912821_6.out
│   │   ├── group_02_1912821_7.err
│   │   ├── group_02_1912821_7.out
│   │   ├── group_02_1912821_8.err
│   │   ├── group_02_1912821_8.out
│   │   ├── group_02_1969963_0.err
│   │   ├── group_02_1969963_0.out
│   │   ├── group_02_1969963_1.err
│   │   ├── group_02_1969963_1.out
│   │   ├── group_02_1969963_2.err
│   │   ├── group_02_1969963_2.out
│   │   ├── group_02_1969963_3.err
│   │   ├── group_02_1969963_3.out
│   │   ├── group_02_1969963_4.err
│   │   ├── group_02_1969963_4.out
│   │   ├── group_02_1969963_5.err
│   │   ├── group_02_1969963_5.out
│   │   ├── group_02_1969963_6.err
│   │   ├── group_02_1969963_6.out
│   │   ├── group_02_1969963_7.err
│   │   ├── group_02_1969963_7.out
│   │   ├── group_02_1969963_8.err
│   │   ├── group_02_1969963_8.out
│   │   ├── group_03_1912826_0.err
│   │   ├── group_03_1912826_0.out
│   │   ├── group_03_1912826_1.err
│   │   ├── group_03_1912826_1.out
│   │   ├── group_03_1912826_2.err
│   │   ├── group_03_1912826_2.out
│   │   ├── group_03_1912826_3.err
│   │   ├── group_03_1912826_3.out
│   │   ├── group_03_1912826_4.err
│   │   ├── group_03_1912826_4.out
│   │   ├── group_03_1912826_5.err
│   │   ├── group_03_1912826_5.out
│   │   ├── group_03_1912826_6.err
│   │   ├── group_03_1912826_6.out
│   │   ├── group_03_1912826_7.err
│   │   ├── group_03_1912826_7.out
│   │   ├── group_03_1912826_8.err
│   │   ├── group_03_1912826_8.out
│   │   ├── group_03_1969965_0.err
│   │   ├── group_03_1969965_0.out
│   │   ├── group_03_1969965_1.err
│   │   ├── group_03_1969965_1.out
│   │   ├── group_03_1969965_2.err
│   │   ├── group_03_1969965_2.out
│   │   ├── group_03_1969965_3.err
│   │   ├── group_03_1969965_3.out
│   │   ├── group_03_1969965_4.err
│   │   ├── group_03_1969965_4.out
│   │   ├── group_03_1969965_5.err
│   │   ├── group_03_1969965_5.out
│   │   ├── group_03_1969965_6.err
│   │   ├── group_03_1969965_6.out
│   │   ├── group_03_1969965_7.err
│   │   ├── group_03_1969965_7.out
│   │   ├── group_03_1969965_8.err
│   │   ├── group_03_1969965_8.out
│   │   ├── group_04_1912827_0.err
│   │   ├── group_04_1912827_0.out
│   │   ├── group_04_1912827_1.err
│   │   ├── group_04_1912827_1.out
│   │   ├── group_04_1912827_2.err
│   │   ├── group_04_1912827_2.out
│   │   ├── group_04_1912827_3.err
│   │   ├── group_04_1912827_3.out
│   │   ├── group_04_1912827_4.err
│   │   ├── group_04_1912827_4.out
│   │   ├── group_04_1912827_5.err
│   │   ├── group_04_1912827_5.out
│   │   ├── group_04_1912827_6.err
│   │   ├── group_04_1912827_6.out
│   │   ├── group_04_1912827_7.err
│   │   ├── group_04_1912827_7.out
│   │   ├── group_04_1912827_8.err
│   │   ├── group_04_1912827_8.out
│   │   ├── group_04_1969966_0.err
│   │   ├── group_04_1969966_0.out
│   │   ├── group_04_1969966_1.err
│   │   ├── group_04_1969966_1.out
│   │   ├── group_04_1969966_2.err
│   │   ├── group_04_1969966_2.out
│   │   ├── group_04_1969966_3.err
│   │   ├── group_04_1969966_3.out
│   │   ├── group_04_1969966_4.err
│   │   ├── group_04_1969966_4.out
│   │   ├── group_04_1969966_5.err
│   │   ├── group_04_1969966_5.out
│   │   ├── group_04_1969966_6.err
│   │   ├── group_04_1969966_6.out
│   │   ├── group_04_1969966_7.err
│   │   ├── group_04_1969966_7.out
│   │   ├── group_04_1969966_8.err
│   │   ├── group_04_1969966_8.out
│   │   ├── group_05_1912828_0.err
│   │   ├── group_05_1912828_0.out
│   │   ├── group_05_1912828_1.err
│   │   ├── group_05_1912828_1.out
│   │   ├── group_05_1912828_2.err
│   │   ├── group_05_1912828_2.out
│   │   ├── group_05_1912828_3.err
│   │   ├── group_05_1912828_3.out
│   │   ├── group_05_1912828_4.err
│   │   ├── group_05_1912828_4.out
│   │   ├── group_05_1912828_5.err
│   │   ├── group_05_1912828_5.out
│   │   ├── group_05_1912828_6.err
│   │   ├── group_05_1912828_6.out
│   │   ├── group_05_1912828_7.err
│   │   ├── group_05_1912828_7.out
│   │   ├── group_05_1912828_8.err
│   │   ├── group_05_1912828_8.out
│   │   ├── group_05_1969967_0.err
│   │   ├── group_05_1969967_0.out
│   │   ├── group_05_1969967_1.err
│   │   ├── group_05_1969967_1.out
│   │   ├── group_05_1969967_2.err
│   │   ├── group_05_1969967_2.out
│   │   ├── group_05_1969967_3.err
│   │   ├── group_05_1969967_3.out
│   │   ├── group_05_1969967_4.err
│   │   ├── group_05_1969967_4.out
│   │   ├── group_05_1969967_5.err
│   │   ├── group_05_1969967_5.out
│   │   ├── group_05_1969967_6.err
│   │   ├── group_05_1969967_6.out
│   │   ├── group_05_1969967_7.err
│   │   ├── group_05_1969967_7.out
│   │   ├── group_05_1969967_8.err
│   │   ├── group_05_1969967_8.out
│   │   ├── group_06_1912829_0.err
│   │   ├── group_06_1912829_0.out
│   │   ├── group_06_1912829_1.err
│   │   ├── group_06_1912829_1.out
│   │   ├── group_06_1912829_2.err
│   │   ├── group_06_1912829_2.out
│   │   ├── group_06_1912829_3.err
│   │   ├── group_06_1912829_3.out
│   │   ├── group_06_1912829_4.err
│   │   ├── group_06_1912829_4.out
│   │   ├── group_06_1912829_5.err
│   │   ├── group_06_1912829_5.out
│   │   ├── group_06_1912829_6.err
│   │   ├── group_06_1912829_6.out
│   │   ├── group_06_1912829_7.err
│   │   ├── group_06_1912829_7.out
│   │   ├── group_06_1912829_8.err
│   │   ├── group_06_1912829_8.out
│   │   ├── group_06_1969969_0.err
│   │   ├── group_06_1969969_0.out
│   │   ├── group_06_1969969_1.err
│   │   ├── group_06_1969969_1.out
│   │   ├── group_06_1969969_2.err
│   │   ├── group_06_1969969_2.out
│   │   ├── group_06_1969969_3.err
│   │   ├── group_06_1969969_3.out
│   │   ├── group_06_1969969_4.err
│   │   ├── group_06_1969969_4.out
│   │   ├── group_06_1969969_5.err
│   │   ├── group_06_1969969_5.out
│   │   ├── group_06_1969969_6.err
│   │   ├── group_06_1969969_6.out
│   │   ├── group_06_1969969_7.err
│   │   ├── group_06_1969969_7.out
│   │   ├── group_06_1969969_8.err
│   │   ├── group_06_1969969_8.out
│   │   ├── group_07_1912830_0.err
│   │   ├── group_07_1912830_0.out
│   │   ├── group_07_1912830_1.err
│   │   ├── group_07_1912830_1.out
│   │   ├── group_07_1912830_2.err
│   │   ├── group_07_1912830_2.out
│   │   ├── group_07_1912830_3.err
│   │   ├── group_07_1912830_3.out
│   │   ├── group_07_1912830_4.err
│   │   ├── group_07_1912830_4.out
│   │   ├── group_07_1912830_5.err
│   │   ├── group_07_1912830_5.out
│   │   ├── group_07_1912830_6.err
│   │   ├── group_07_1912830_6.out
│   │   ├── group_07_1912830_7.err
│   │   ├── group_07_1912830_7.out
│   │   ├── group_07_1912830_8.err
│   │   ├── group_07_1912830_8.out
│   │   ├── group_07_1969970_0.err
│   │   ├── group_07_1969970_0.out
│   │   ├── group_07_1969970_1.err
│   │   ├── group_07_1969970_1.out
│   │   ├── group_07_1969970_2.err
│   │   ├── group_07_1969970_2.out
│   │   ├── group_07_1969970_3.err
│   │   ├── group_07_1969970_3.out
│   │   ├── group_07_1969970_4.err
│   │   ├── group_07_1969970_4.out
│   │   ├── group_07_1969970_5.err
│   │   ├── group_07_1969970_5.out
│   │   ├── group_07_1969970_6.err
│   │   ├── group_07_1969970_6.out
│   │   ├── group_07_1969970_7.err
│   │   ├── group_07_1969970_7.out
│   │   ├── group_07_1969970_8.err
│   │   ├── group_07_1969970_8.out
│   │   ├── group_08_1912831_0.err
│   │   ├── group_08_1912831_0.out
│   │   ├── group_08_1912831_1.err
│   │   ├── group_08_1912831_1.out
│   │   ├── group_08_1912831_2.err
│   │   ├── group_08_1912831_2.out
│   │   ├── group_08_1912831_3.err
│   │   ├── group_08_1912831_3.out
│   │   ├── group_08_1912831_4.err
│   │   ├── group_08_1912831_4.out
│   │   ├── group_08_1912831_5.err
│   │   ├── group_08_1912831_5.out
│   │   ├── group_08_1912831_6.err
│   │   ├── group_08_1912831_6.out
│   │   ├── group_08_1912831_7.err
│   │   ├── group_08_1912831_7.out
│   │   ├── group_08_1912831_8.err
│   │   ├── group_08_1912831_8.out
│   │   ├── group_08_1969971_0.err
│   │   ├── group_08_1969971_0.out
│   │   ├── group_08_1969971_1.err
│   │   ├── group_08_1969971_1.out
│   │   ├── group_08_1969971_2.err
│   │   ├── group_08_1969971_2.out
│   │   ├── group_08_1969971_3.err
│   │   ├── group_08_1969971_3.out
│   │   ├── group_08_1969971_4.err
│   │   ├── group_08_1969971_4.out
│   │   ├── group_08_1969971_5.err
│   │   ├── group_08_1969971_5.out
│   │   ├── group_08_1969971_6.err
│   │   ├── group_08_1969971_6.out
│   │   ├── group_08_1969971_7.err
│   │   ├── group_08_1969971_7.out
│   │   ├── group_08_1969971_8.err
│   │   ├── group_08_1969971_8.out
│   │   ├── group_09_1912832_0.err
│   │   ├── group_09_1912832_0.out
│   │   ├── group_09_1912832_1.err
│   │   ├── group_09_1912832_1.out
│   │   ├── group_09_1912832_2.err
│   │   ├── group_09_1912832_2.out
│   │   ├── group_09_1912832_3.err
│   │   ├── group_09_1912832_3.out
│   │   ├── group_09_1912832_4.err
│   │   ├── group_09_1912832_4.out
│   │   ├── group_09_1912832_5.err
│   │   ├── group_09_1912832_5.out
│   │   ├── group_09_1912832_6.err
│   │   ├── group_09_1912832_6.out
│   │   ├── group_09_1912832_7.err
│   │   ├── group_09_1912832_7.out
│   │   ├── group_09_1912832_8.err
│   │   ├── group_09_1912832_8.out
│   │   ├── group_09_1969972_0.err
│   │   ├── group_09_1969972_0.out
│   │   ├── group_09_1969972_1.err
│   │   ├── group_09_1969972_1.out
│   │   ├── group_09_1969972_2.err
│   │   ├── group_09_1969972_2.out
│   │   ├── group_09_1969972_3.err
│   │   ├── group_09_1969972_3.out
│   │   ├── group_09_1969972_4.err
│   │   ├── group_09_1969972_4.out
│   │   ├── group_09_1969972_5.err
│   │   ├── group_09_1969972_5.out
│   │   ├── group_09_1969972_6.err
│   │   ├── group_09_1969972_6.out
│   │   ├── group_09_1969972_7.err
│   │   ├── group_09_1969972_7.out
│   │   ├── group_09_1969972_8.err
│   │   └── group_09_1969972_8.out
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
│   ├── batch_ref_0_budget_50_1994114_1.err
│   ├── batch_ref_0_budget_50_1994114_1.out
│   ├── batch_ref_0_budget_50_1994114_2.err
│   ├── batch_ref_0_budget_50_1994114_2.out
│   ├── batch_ref_0_budget_50_1994114_3.err
│   ├── batch_ref_0_budget_50_1994114_3.out
│   ├── batch_ref_0_budget_50_1995674_1.err
│   ├── batch_ref_0_budget_50_1995674_1.out
│   ├── batch_ref_0_budget_50_1995674_10.err
│   ├── batch_ref_0_budget_50_1995674_10.out
│   ├── batch_ref_0_budget_50_1995674_11.err
│   ├── batch_ref_0_budget_50_1995674_11.out
│   ├── batch_ref_0_budget_50_1995674_12.err
│   ├── batch_ref_0_budget_50_1995674_12.out
│   ├── batch_ref_0_budget_50_1995674_13.err
│   ├── batch_ref_0_budget_50_1995674_13.out
│   ├── batch_ref_0_budget_50_1995674_14.err
│   ├── batch_ref_0_budget_50_1995674_14.out
│   ├── batch_ref_0_budget_50_1995674_15.err
│   ├── batch_ref_0_budget_50_1995674_15.out
│   ├── batch_ref_0_budget_50_1995674_16.err
│   ├── batch_ref_0_budget_50_1995674_16.out
│   ├── batch_ref_0_budget_50_1995674_17.err
│   ├── batch_ref_0_budget_50_1995674_17.out
│   ├── batch_ref_0_budget_50_1995674_18.err
│   ├── batch_ref_0_budget_50_1995674_18.out
│   ├── batch_ref_0_budget_50_1995674_19.err
│   ├── batch_ref_0_budget_50_1995674_19.out
│   ├── batch_ref_0_budget_50_1995674_2.err
│   ├── batch_ref_0_budget_50_1995674_2.out
│   ├── batch_ref_0_budget_50_1995674_20.err
│   ├── batch_ref_0_budget_50_1995674_20.out
│   ├── batch_ref_0_budget_50_1995674_21.err
│   ├── batch_ref_0_budget_50_1995674_21.out
│   ├── batch_ref_0_budget_50_1995674_22.err
│   ├── batch_ref_0_budget_50_1995674_22.out
│   ├── batch_ref_0_budget_50_1995674_23.err
│   ├── batch_ref_0_budget_50_1995674_23.out
│   ├── batch_ref_0_budget_50_1995674_24.err
│   ├── batch_ref_0_budget_50_1995674_24.out
│   ├── batch_ref_0_budget_50_1995674_25.err
│   ├── batch_ref_0_budget_50_1995674_25.out
│   ├── batch_ref_0_budget_50_1995674_26.err
│   ├── batch_ref_0_budget_50_1995674_26.out
│   ├── batch_ref_0_budget_50_1995674_27.err
│   ├── batch_ref_0_budget_50_1995674_27.out
│   ├── batch_ref_0_budget_50_1995674_28.err
│   ├── batch_ref_0_budget_50_1995674_28.out
│   ├── batch_ref_0_budget_50_1995674_29.err
│   ├── batch_ref_0_budget_50_1995674_29.out
│   ├── batch_ref_0_budget_50_1995674_3.err
│   ├── batch_ref_0_budget_50_1995674_3.out
│   ├── batch_ref_0_budget_50_1995674_30.err
│   ├── batch_ref_0_budget_50_1995674_30.out
│   ├── batch_ref_0_budget_50_1995674_31.err
│   ├── batch_ref_0_budget_50_1995674_31.out
│   ├── batch_ref_0_budget_50_1995674_32.err
│   ├── batch_ref_0_budget_50_1995674_32.out
│   ├── batch_ref_0_budget_50_1995674_33.err
│   ├── batch_ref_0_budget_50_1995674_33.out
│   ├── batch_ref_0_budget_50_1995674_34.err
│   ├── batch_ref_0_budget_50_1995674_34.out
│   ├── batch_ref_0_budget_50_1995674_35.err
│   ├── batch_ref_0_budget_50_1995674_35.out
│   ├── batch_ref_0_budget_50_1995674_36.err
│   ├── batch_ref_0_budget_50_1995674_36.out
│   ├── batch_ref_0_budget_50_1995674_37.err
│   ├── batch_ref_0_budget_50_1995674_37.out
│   ├── batch_ref_0_budget_50_1995674_38.err
│   ├── batch_ref_0_budget_50_1995674_38.out
│   ├── batch_ref_0_budget_50_1995674_39.err
│   ├── batch_ref_0_budget_50_1995674_39.out
│   ├── batch_ref_0_budget_50_1995674_4.err
│   ├── batch_ref_0_budget_50_1995674_4.out
│   ├── batch_ref_0_budget_50_1995674_40.err
│   ├── batch_ref_0_budget_50_1995674_40.out
│   ├── batch_ref_0_budget_50_1995674_41.err
│   ├── batch_ref_0_budget_50_1995674_41.out
│   ├── batch_ref_0_budget_50_1995674_42.err
│   ├── batch_ref_0_budget_50_1995674_42.out
│   ├── batch_ref_0_budget_50_1995674_43.err
│   ├── batch_ref_0_budget_50_1995674_43.out
│   ├── batch_ref_0_budget_50_1995674_44.err
│   ├── batch_ref_0_budget_50_1995674_44.out
│   ├── batch_ref_0_budget_50_1995674_45.err
│   ├── batch_ref_0_budget_50_1995674_45.out
│   ├── batch_ref_0_budget_50_1995674_46.err
│   ├── batch_ref_0_budget_50_1995674_46.out
│   ├── batch_ref_0_budget_50_1995674_47.err
│   ├── batch_ref_0_budget_50_1995674_47.out
│   ├── batch_ref_0_budget_50_1995674_48.err
│   ├── batch_ref_0_budget_50_1995674_48.out
│   ├── batch_ref_0_budget_50_1995674_49.err
│   ├── batch_ref_0_budget_50_1995674_49.out
│   ├── batch_ref_0_budget_50_1995674_5.err
│   ├── batch_ref_0_budget_50_1995674_5.out
│   ├── batch_ref_0_budget_50_1995674_50.err
│   ├── batch_ref_0_budget_50_1995674_50.out
│   ├── batch_ref_0_budget_50_1995674_51.err
│   ├── batch_ref_0_budget_50_1995674_51.out
│   ├── batch_ref_0_budget_50_1995674_52.err
│   ├── batch_ref_0_budget_50_1995674_52.out
│   ├── batch_ref_0_budget_50_1995674_53.err
│   ├── batch_ref_0_budget_50_1995674_53.out
│   ├── batch_ref_0_budget_50_1995674_54.err
│   ├── batch_ref_0_budget_50_1995674_54.out
│   ├── batch_ref_0_budget_50_1995674_55.err
│   ├── batch_ref_0_budget_50_1995674_55.out
│   ├── batch_ref_0_budget_50_1995674_56.err
│   ├── batch_ref_0_budget_50_1995674_56.out
│   ├── batch_ref_0_budget_50_1995674_57.err
│   ├── batch_ref_0_budget_50_1995674_57.out
│   ├── batch_ref_0_budget_50_1995674_58.err
│   ├── batch_ref_0_budget_50_1995674_58.out
│   ├── batch_ref_0_budget_50_1995674_59.err
│   ├── batch_ref_0_budget_50_1995674_59.out
│   ├── batch_ref_0_budget_50_1995674_6.err
│   ├── batch_ref_0_budget_50_1995674_6.out
│   ├── batch_ref_0_budget_50_1995674_60.err
│   ├── batch_ref_0_budget_50_1995674_60.out
│   ├── batch_ref_0_budget_50_1995674_61.err
│   ├── batch_ref_0_budget_50_1995674_61.out
│   ├── batch_ref_0_budget_50_1995674_62.err
│   ├── batch_ref_0_budget_50_1995674_62.out
│   ├── batch_ref_0_budget_50_1995674_63.err
│   ├── batch_ref_0_budget_50_1995674_63.out
│   ├── batch_ref_0_budget_50_1995674_64.err
│   ├── batch_ref_0_budget_50_1995674_64.out
│   ├── batch_ref_0_budget_50_1995674_65.err
│   ├── batch_ref_0_budget_50_1995674_65.out
│   ├── batch_ref_0_budget_50_1995674_66.err
│   ├── batch_ref_0_budget_50_1995674_66.out
│   ├── batch_ref_0_budget_50_1995674_67.err
│   ├── batch_ref_0_budget_50_1995674_67.out
│   ├── batch_ref_0_budget_50_1995674_68.err
│   ├── batch_ref_0_budget_50_1995674_68.out
│   ├── batch_ref_0_budget_50_1995674_69.err
│   ├── batch_ref_0_budget_50_1995674_69.out
│   ├── batch_ref_0_budget_50_1995674_7.err
│   ├── batch_ref_0_budget_50_1995674_7.out
│   ├── batch_ref_0_budget_50_1995674_70.err
│   ├── batch_ref_0_budget_50_1995674_70.out
│   ├── batch_ref_0_budget_50_1995674_71.err
│   ├── batch_ref_0_budget_50_1995674_71.out
│   ├── batch_ref_0_budget_50_1995674_72.err
│   ├── batch_ref_0_budget_50_1995674_72.out
│   ├── batch_ref_0_budget_50_1995674_73.err
│   ├── batch_ref_0_budget_50_1995674_73.out
│   ├── batch_ref_0_budget_50_1995674_74.err
│   ├── batch_ref_0_budget_50_1995674_74.out
│   ├── batch_ref_0_budget_50_1995674_75.err
│   ├── batch_ref_0_budget_50_1995674_75.out
│   ├── batch_ref_0_budget_50_1995674_76.err
│   ├── batch_ref_0_budget_50_1995674_76.out
│   ├── batch_ref_0_budget_50_1995674_77.err
│   ├── batch_ref_0_budget_50_1995674_77.out
│   ├── batch_ref_0_budget_50_1995674_78.err
│   ├── batch_ref_0_budget_50_1995674_78.out
│   ├── batch_ref_0_budget_50_1995674_79.err
│   ├── batch_ref_0_budget_50_1995674_79.out
│   ├── batch_ref_0_budget_50_1995674_8.err
│   ├── batch_ref_0_budget_50_1995674_8.out
│   ├── batch_ref_0_budget_50_1995674_80.err
│   ├── batch_ref_0_budget_50_1995674_80.out
│   ├── batch_ref_0_budget_50_1995674_81.err
│   ├── batch_ref_0_budget_50_1995674_81.out
│   ├── batch_ref_0_budget_50_1995674_9.err
│   ├── batch_ref_0_budget_50_1995674_9.out
│   ├── batch_ref_0_budget_50_2039809_1.err
│   ├── batch_ref_0_budget_50_2039809_1.out
│   ├── batch_ref_0_budget_50_2039809_10.err
│   ├── batch_ref_0_budget_50_2039809_10.out
│   ├── batch_ref_0_budget_50_2039809_11.err
│   ├── batch_ref_0_budget_50_2039809_11.out
│   ├── batch_ref_0_budget_50_2039809_12.err
│   ├── batch_ref_0_budget_50_2039809_12.out
│   ├── batch_ref_0_budget_50_2039809_13.err
│   ├── batch_ref_0_budget_50_2039809_13.out
│   ├── batch_ref_0_budget_50_2039809_14.err
│   ├── batch_ref_0_budget_50_2039809_14.out
│   ├── batch_ref_0_budget_50_2039809_15.err
│   ├── batch_ref_0_budget_50_2039809_15.out
│   ├── batch_ref_0_budget_50_2039809_16.err
│   ├── batch_ref_0_budget_50_2039809_16.out
│   ├── batch_ref_0_budget_50_2039809_17.err
│   ├── batch_ref_0_budget_50_2039809_17.out
│   ├── batch_ref_0_budget_50_2039809_18.err
│   ├── batch_ref_0_budget_50_2039809_18.out
│   ├── batch_ref_0_budget_50_2039809_19.err
│   ├── batch_ref_0_budget_50_2039809_19.out
│   ├── batch_ref_0_budget_50_2039809_2.err
│   ├── batch_ref_0_budget_50_2039809_2.out
│   ├── batch_ref_0_budget_50_2039809_20.err
│   ├── batch_ref_0_budget_50_2039809_20.out
│   ├── batch_ref_0_budget_50_2039809_21.err
│   ├── batch_ref_0_budget_50_2039809_21.out
│   ├── batch_ref_0_budget_50_2039809_22.err
│   ├── batch_ref_0_budget_50_2039809_22.out
│   ├── batch_ref_0_budget_50_2039809_23.err
│   ├── batch_ref_0_budget_50_2039809_23.out
│   ├── batch_ref_0_budget_50_2039809_24.err
│   ├── batch_ref_0_budget_50_2039809_24.out
│   ├── batch_ref_0_budget_50_2039809_25.err
│   ├── batch_ref_0_budget_50_2039809_25.out
│   ├── batch_ref_0_budget_50_2039809_26.err
│   ├── batch_ref_0_budget_50_2039809_26.out
│   ├── batch_ref_0_budget_50_2039809_27.err
│   ├── batch_ref_0_budget_50_2039809_27.out
│   ├── batch_ref_0_budget_50_2039809_28.err
│   ├── batch_ref_0_budget_50_2039809_28.out
│   ├── batch_ref_0_budget_50_2039809_29.err
│   ├── batch_ref_0_budget_50_2039809_29.out
│   ├── batch_ref_0_budget_50_2039809_3.err
│   ├── batch_ref_0_budget_50_2039809_3.out
│   ├── batch_ref_0_budget_50_2039809_30.err
│   ├── batch_ref_0_budget_50_2039809_30.out
│   ├── batch_ref_0_budget_50_2039809_31.err
│   ├── batch_ref_0_budget_50_2039809_31.out
│   ├── batch_ref_0_budget_50_2039809_32.err
│   ├── batch_ref_0_budget_50_2039809_32.out
│   ├── batch_ref_0_budget_50_2039809_33.err
│   ├── batch_ref_0_budget_50_2039809_33.out
│   ├── batch_ref_0_budget_50_2039809_34.err
│   ├── batch_ref_0_budget_50_2039809_34.out
│   ├── batch_ref_0_budget_50_2039809_35.err
│   ├── batch_ref_0_budget_50_2039809_35.out
│   ├── batch_ref_0_budget_50_2039809_36.err
│   ├── batch_ref_0_budget_50_2039809_36.out
│   ├── batch_ref_0_budget_50_2039809_37.err
│   ├── batch_ref_0_budget_50_2039809_37.out
│   ├── batch_ref_0_budget_50_2039809_38.err
│   ├── batch_ref_0_budget_50_2039809_38.out
│   ├── batch_ref_0_budget_50_2039809_39.err
│   ├── batch_ref_0_budget_50_2039809_39.out
│   ├── batch_ref_0_budget_50_2039809_4.err
│   ├── batch_ref_0_budget_50_2039809_4.out
│   ├── batch_ref_0_budget_50_2039809_40.err
│   ├── batch_ref_0_budget_50_2039809_40.out
│   ├── batch_ref_0_budget_50_2039809_41.err
│   ├── batch_ref_0_budget_50_2039809_41.out
│   ├── batch_ref_0_budget_50_2039809_42.err
│   ├── batch_ref_0_budget_50_2039809_42.out
│   ├── batch_ref_0_budget_50_2039809_43.err
│   ├── batch_ref_0_budget_50_2039809_43.out
│   ├── batch_ref_0_budget_50_2039809_44.err
│   ├── batch_ref_0_budget_50_2039809_44.out
│   ├── batch_ref_0_budget_50_2039809_45.err
│   ├── batch_ref_0_budget_50_2039809_45.out
│   ├── batch_ref_0_budget_50_2039809_46.err
│   ├── batch_ref_0_budget_50_2039809_46.out
│   ├── batch_ref_0_budget_50_2039809_47.err
│   ├── batch_ref_0_budget_50_2039809_47.out
│   ├── batch_ref_0_budget_50_2039809_48.err
│   ├── batch_ref_0_budget_50_2039809_48.out
│   ├── batch_ref_0_budget_50_2039809_49.err
│   ├── batch_ref_0_budget_50_2039809_49.out
│   ├── batch_ref_0_budget_50_2039809_5.err
│   ├── batch_ref_0_budget_50_2039809_5.out
│   ├── batch_ref_0_budget_50_2039809_50.err
│   ├── batch_ref_0_budget_50_2039809_50.out
│   ├── batch_ref_0_budget_50_2039809_51.err
│   ├── batch_ref_0_budget_50_2039809_51.out
│   ├── batch_ref_0_budget_50_2039809_52.err
│   ├── batch_ref_0_budget_50_2039809_52.out
│   ├── batch_ref_0_budget_50_2039809_53.err
│   ├── batch_ref_0_budget_50_2039809_53.out
│   ├── batch_ref_0_budget_50_2039809_54.err
│   ├── batch_ref_0_budget_50_2039809_54.out
│   ├── batch_ref_0_budget_50_2039809_55.err
│   ├── batch_ref_0_budget_50_2039809_55.out
│   ├── batch_ref_0_budget_50_2039809_56.err
│   ├── batch_ref_0_budget_50_2039809_56.out
│   ├── batch_ref_0_budget_50_2039809_57.err
│   ├── batch_ref_0_budget_50_2039809_57.out
│   ├── batch_ref_0_budget_50_2039809_58.err
│   ├── batch_ref_0_budget_50_2039809_58.out
│   ├── batch_ref_0_budget_50_2039809_59.err
│   ├── batch_ref_0_budget_50_2039809_59.out
│   ├── batch_ref_0_budget_50_2039809_6.err
│   ├── batch_ref_0_budget_50_2039809_6.out
│   ├── batch_ref_0_budget_50_2039809_60.err
│   ├── batch_ref_0_budget_50_2039809_60.out
│   ├── batch_ref_0_budget_50_2039809_61.err
│   ├── batch_ref_0_budget_50_2039809_61.out
│   ├── batch_ref_0_budget_50_2039809_62.err
│   ├── batch_ref_0_budget_50_2039809_62.out
│   ├── batch_ref_0_budget_50_2039809_63.err
│   ├── batch_ref_0_budget_50_2039809_63.out
│   ├── batch_ref_0_budget_50_2039809_64.err
│   ├── batch_ref_0_budget_50_2039809_64.out
│   ├── batch_ref_0_budget_50_2039809_65.err
│   ├── batch_ref_0_budget_50_2039809_65.out
│   ├── batch_ref_0_budget_50_2039809_66.err
│   ├── batch_ref_0_budget_50_2039809_66.out
│   ├── batch_ref_0_budget_50_2039809_67.err
│   ├── batch_ref_0_budget_50_2039809_67.out
│   ├── batch_ref_0_budget_50_2039809_68.err
│   ├── batch_ref_0_budget_50_2039809_68.out
│   ├── batch_ref_0_budget_50_2039809_69.err
│   ├── batch_ref_0_budget_50_2039809_69.out
│   ├── batch_ref_0_budget_50_2039809_7.err
│   ├── batch_ref_0_budget_50_2039809_7.out
│   ├── batch_ref_0_budget_50_2039809_70.err
│   ├── batch_ref_0_budget_50_2039809_70.out
│   ├── batch_ref_0_budget_50_2039809_71.err
│   ├── batch_ref_0_budget_50_2039809_71.out
│   ├── batch_ref_0_budget_50_2039809_72.err
│   ├── batch_ref_0_budget_50_2039809_72.out
│   ├── batch_ref_0_budget_50_2039809_73.err
│   ├── batch_ref_0_budget_50_2039809_73.out
│   ├── batch_ref_0_budget_50_2039809_74.err
│   ├── batch_ref_0_budget_50_2039809_74.out
│   ├── batch_ref_0_budget_50_2039809_75.err
│   ├── batch_ref_0_budget_50_2039809_75.out
│   ├── batch_ref_0_budget_50_2039809_76.err
│   ├── batch_ref_0_budget_50_2039809_76.out
│   ├── batch_ref_0_budget_50_2039809_77.err
│   ├── batch_ref_0_budget_50_2039809_77.out
│   ├── batch_ref_0_budget_50_2039809_78.err
│   ├── batch_ref_0_budget_50_2039809_78.out
│   ├── batch_ref_0_budget_50_2039809_79.err
│   ├── batch_ref_0_budget_50_2039809_79.out
│   ├── batch_ref_0_budget_50_2039809_8.err
│   ├── batch_ref_0_budget_50_2039809_8.out
│   ├── batch_ref_0_budget_50_2039809_80.err
│   ├── batch_ref_0_budget_50_2039809_80.out
│   ├── batch_ref_0_budget_50_2039809_81.err
│   ├── batch_ref_0_budget_50_2039809_81.out
│   ├── batch_ref_0_budget_50_2039809_9.err
│   ├── batch_ref_0_budget_50_2039809_9.out
│   ├── batch_ref_2_budget_50_2004762_1.err
│   ├── batch_ref_2_budget_50_2004762_1.out
│   ├── batch_ref_2_budget_50_2004762_10.err
│   ├── batch_ref_2_budget_50_2004762_10.out
│   ├── batch_ref_2_budget_50_2004762_11.err
│   ├── batch_ref_2_budget_50_2004762_11.out
│   ├── batch_ref_2_budget_50_2004762_12.err
│   ├── batch_ref_2_budget_50_2004762_12.out
│   ├── batch_ref_2_budget_50_2004762_13.err
│   ├── batch_ref_2_budget_50_2004762_13.out
│   ├── batch_ref_2_budget_50_2004762_14.err
│   ├── batch_ref_2_budget_50_2004762_14.out
│   ├── batch_ref_2_budget_50_2004762_15.err
│   ├── batch_ref_2_budget_50_2004762_15.out
│   ├── batch_ref_2_budget_50_2004762_16.err
│   ├── batch_ref_2_budget_50_2004762_16.out
│   ├── batch_ref_2_budget_50_2004762_17.err
│   ├── batch_ref_2_budget_50_2004762_17.out
│   ├── batch_ref_2_budget_50_2004762_18.err
│   ├── batch_ref_2_budget_50_2004762_18.out
│   ├── batch_ref_2_budget_50_2004762_19.err
│   ├── batch_ref_2_budget_50_2004762_19.out
│   ├── batch_ref_2_budget_50_2004762_2.err
│   ├── batch_ref_2_budget_50_2004762_2.out
│   ├── batch_ref_2_budget_50_2004762_20.err
│   ├── batch_ref_2_budget_50_2004762_20.out
│   ├── batch_ref_2_budget_50_2004762_21.err
│   ├── batch_ref_2_budget_50_2004762_21.out
│   ├── batch_ref_2_budget_50_2004762_22.err
│   ├── batch_ref_2_budget_50_2004762_22.out
│   ├── batch_ref_2_budget_50_2004762_23.err
│   ├── batch_ref_2_budget_50_2004762_23.out
│   ├── batch_ref_2_budget_50_2004762_24.err
│   ├── batch_ref_2_budget_50_2004762_24.out
│   ├── batch_ref_2_budget_50_2004762_25.err
│   ├── batch_ref_2_budget_50_2004762_25.out
│   ├── batch_ref_2_budget_50_2004762_26.err
│   ├── batch_ref_2_budget_50_2004762_26.out
│   ├── batch_ref_2_budget_50_2004762_27.err
│   ├── batch_ref_2_budget_50_2004762_27.out
│   ├── batch_ref_2_budget_50_2004762_28.err
│   ├── batch_ref_2_budget_50_2004762_28.out
│   ├── batch_ref_2_budget_50_2004762_29.err
│   ├── batch_ref_2_budget_50_2004762_29.out
│   ├── batch_ref_2_budget_50_2004762_3.err
│   ├── batch_ref_2_budget_50_2004762_3.out
│   ├── batch_ref_2_budget_50_2004762_30.err
│   ├── batch_ref_2_budget_50_2004762_30.out
│   ├── batch_ref_2_budget_50_2004762_31.err
│   ├── batch_ref_2_budget_50_2004762_31.out
│   ├── batch_ref_2_budget_50_2004762_32.err
│   ├── batch_ref_2_budget_50_2004762_32.out
│   ├── batch_ref_2_budget_50_2004762_33.err
│   ├── batch_ref_2_budget_50_2004762_33.out
│   ├── batch_ref_2_budget_50_2004762_34.err
│   ├── batch_ref_2_budget_50_2004762_34.out
│   ├── batch_ref_2_budget_50_2004762_35.err
│   ├── batch_ref_2_budget_50_2004762_35.out
│   ├── batch_ref_2_budget_50_2004762_36.err
│   ├── batch_ref_2_budget_50_2004762_36.out
│   ├── batch_ref_2_budget_50_2004762_37.err
│   ├── batch_ref_2_budget_50_2004762_37.out
│   ├── batch_ref_2_budget_50_2004762_38.err
│   ├── batch_ref_2_budget_50_2004762_38.out
│   ├── batch_ref_2_budget_50_2004762_39.err
│   ├── batch_ref_2_budget_50_2004762_39.out
│   ├── batch_ref_2_budget_50_2004762_4.err
│   ├── batch_ref_2_budget_50_2004762_4.out
│   ├── batch_ref_2_budget_50_2004762_40.err
│   ├── batch_ref_2_budget_50_2004762_40.out
│   ├── batch_ref_2_budget_50_2004762_41.err
│   ├── batch_ref_2_budget_50_2004762_41.out
│   ├── batch_ref_2_budget_50_2004762_42.err
│   ├── batch_ref_2_budget_50_2004762_42.out
│   ├── batch_ref_2_budget_50_2004762_43.err
│   ├── batch_ref_2_budget_50_2004762_43.out
│   ├── batch_ref_2_budget_50_2004762_44.err
│   ├── batch_ref_2_budget_50_2004762_44.out
│   ├── batch_ref_2_budget_50_2004762_45.err
│   ├── batch_ref_2_budget_50_2004762_45.out
│   ├── batch_ref_2_budget_50_2004762_46.err
│   ├── batch_ref_2_budget_50_2004762_46.out
│   ├── batch_ref_2_budget_50_2004762_47.err
│   ├── batch_ref_2_budget_50_2004762_47.out
│   ├── batch_ref_2_budget_50_2004762_48.err
│   ├── batch_ref_2_budget_50_2004762_48.out
│   ├── batch_ref_2_budget_50_2004762_49.err
│   ├── batch_ref_2_budget_50_2004762_49.out
│   ├── batch_ref_2_budget_50_2004762_5.err
│   ├── batch_ref_2_budget_50_2004762_5.out
│   ├── batch_ref_2_budget_50_2004762_50.err
│   ├── batch_ref_2_budget_50_2004762_50.out
│   ├── batch_ref_2_budget_50_2004762_51.err
│   ├── batch_ref_2_budget_50_2004762_51.out
│   ├── batch_ref_2_budget_50_2004762_52.err
│   ├── batch_ref_2_budget_50_2004762_52.out
│   ├── batch_ref_2_budget_50_2004762_53.err
│   ├── batch_ref_2_budget_50_2004762_53.out
│   ├── batch_ref_2_budget_50_2004762_54.err
│   ├── batch_ref_2_budget_50_2004762_54.out
│   ├── batch_ref_2_budget_50_2004762_55.err
│   ├── batch_ref_2_budget_50_2004762_55.out
│   ├── batch_ref_2_budget_50_2004762_56.err
│   ├── batch_ref_2_budget_50_2004762_56.out
│   ├── batch_ref_2_budget_50_2004762_57.err
│   ├── batch_ref_2_budget_50_2004762_57.out
│   ├── batch_ref_2_budget_50_2004762_58.err
│   ├── batch_ref_2_budget_50_2004762_58.out
│   ├── batch_ref_2_budget_50_2004762_59.err
│   ├── batch_ref_2_budget_50_2004762_59.out
│   ├── batch_ref_2_budget_50_2004762_6.err
│   ├── batch_ref_2_budget_50_2004762_6.out
│   ├── batch_ref_2_budget_50_2004762_60.err
│   ├── batch_ref_2_budget_50_2004762_60.out
│   ├── batch_ref_2_budget_50_2004762_61.err
│   ├── batch_ref_2_budget_50_2004762_61.out
│   ├── batch_ref_2_budget_50_2004762_62.err
│   ├── batch_ref_2_budget_50_2004762_62.out
│   ├── batch_ref_2_budget_50_2004762_63.err
│   ├── batch_ref_2_budget_50_2004762_63.out
│   ├── batch_ref_2_budget_50_2004762_64.err
│   ├── batch_ref_2_budget_50_2004762_64.out
│   ├── batch_ref_2_budget_50_2004762_65.err
│   ├── batch_ref_2_budget_50_2004762_65.out
│   ├── batch_ref_2_budget_50_2004762_66.err
│   ├── batch_ref_2_budget_50_2004762_66.out
│   ├── batch_ref_2_budget_50_2004762_67.err
│   ├── batch_ref_2_budget_50_2004762_67.out
│   ├── batch_ref_2_budget_50_2004762_68.err
│   ├── batch_ref_2_budget_50_2004762_68.out
│   ├── batch_ref_2_budget_50_2004762_69.err
│   ├── batch_ref_2_budget_50_2004762_69.out
│   ├── batch_ref_2_budget_50_2004762_7.err
│   ├── batch_ref_2_budget_50_2004762_7.out
│   ├── batch_ref_2_budget_50_2004762_70.err
│   ├── batch_ref_2_budget_50_2004762_70.out
│   ├── batch_ref_2_budget_50_2004762_71.err
│   ├── batch_ref_2_budget_50_2004762_71.out
│   ├── batch_ref_2_budget_50_2004762_72.err
│   ├── batch_ref_2_budget_50_2004762_72.out
│   ├── batch_ref_2_budget_50_2004762_73.err
│   ├── batch_ref_2_budget_50_2004762_73.out
│   ├── batch_ref_2_budget_50_2004762_74.err
│   ├── batch_ref_2_budget_50_2004762_74.out
│   ├── batch_ref_2_budget_50_2004762_75.err
│   ├── batch_ref_2_budget_50_2004762_75.out
│   ├── batch_ref_2_budget_50_2004762_76.err
│   ├── batch_ref_2_budget_50_2004762_76.out
│   ├── batch_ref_2_budget_50_2004762_77.err
│   ├── batch_ref_2_budget_50_2004762_77.out
│   ├── batch_ref_2_budget_50_2004762_78.err
│   ├── batch_ref_2_budget_50_2004762_78.out
│   ├── batch_ref_2_budget_50_2004762_79.err
│   ├── batch_ref_2_budget_50_2004762_79.out
│   ├── batch_ref_2_budget_50_2004762_8.err
│   ├── batch_ref_2_budget_50_2004762_8.out
│   ├── batch_ref_2_budget_50_2004762_80.err
│   ├── batch_ref_2_budget_50_2004762_80.out
│   ├── batch_ref_2_budget_50_2004762_81.err
│   ├── batch_ref_2_budget_50_2004762_81.out
│   ├── batch_ref_2_budget_50_2004762_9.err
│   ├── batch_ref_2_budget_50_2004762_9.out
│   ├── batch_ref_2_budget_50_2005710_1.err
│   ├── batch_ref_2_budget_50_2005710_1.out
│   ├── batch_ref_2_budget_50_2005710_10.err
│   ├── batch_ref_2_budget_50_2005710_10.out
│   ├── batch_ref_2_budget_50_2005710_11.err
│   ├── batch_ref_2_budget_50_2005710_11.out
│   ├── batch_ref_2_budget_50_2005710_12.err
│   ├── batch_ref_2_budget_50_2005710_12.out
│   ├── batch_ref_2_budget_50_2005710_13.err
│   ├── batch_ref_2_budget_50_2005710_13.out
│   ├── batch_ref_2_budget_50_2005710_14.err
│   ├── batch_ref_2_budget_50_2005710_14.out
│   ├── batch_ref_2_budget_50_2005710_15.err
│   ├── batch_ref_2_budget_50_2005710_15.out
│   ├── batch_ref_2_budget_50_2005710_16.err
│   ├── batch_ref_2_budget_50_2005710_16.out
│   ├── batch_ref_2_budget_50_2005710_17.err
│   ├── batch_ref_2_budget_50_2005710_17.out
│   ├── batch_ref_2_budget_50_2005710_18.err
│   ├── batch_ref_2_budget_50_2005710_18.out
│   ├── batch_ref_2_budget_50_2005710_19.err
│   ├── batch_ref_2_budget_50_2005710_19.out
│   ├── batch_ref_2_budget_50_2005710_2.err
│   ├── batch_ref_2_budget_50_2005710_2.out
│   ├── batch_ref_2_budget_50_2005710_20.err
│   ├── batch_ref_2_budget_50_2005710_20.out
│   ├── batch_ref_2_budget_50_2005710_21.err
│   ├── batch_ref_2_budget_50_2005710_21.out
│   ├── batch_ref_2_budget_50_2005710_22.err
│   ├── batch_ref_2_budget_50_2005710_22.out
│   ├── batch_ref_2_budget_50_2005710_23.err
│   ├── batch_ref_2_budget_50_2005710_23.out
│   ├── batch_ref_2_budget_50_2005710_24.err
│   ├── batch_ref_2_budget_50_2005710_24.out
│   ├── batch_ref_2_budget_50_2005710_25.err
│   ├── batch_ref_2_budget_50_2005710_25.out
│   ├── batch_ref_2_budget_50_2005710_26.err
│   ├── batch_ref_2_budget_50_2005710_26.out
│   ├── batch_ref_2_budget_50_2005710_27.err
│   ├── batch_ref_2_budget_50_2005710_27.out
│   ├── batch_ref_2_budget_50_2005710_28.err
│   ├── batch_ref_2_budget_50_2005710_28.out
│   ├── batch_ref_2_budget_50_2005710_29.err
│   ├── batch_ref_2_budget_50_2005710_29.out
│   ├── batch_ref_2_budget_50_2005710_3.err
│   ├── batch_ref_2_budget_50_2005710_3.out
│   ├── batch_ref_2_budget_50_2005710_30.err
│   ├── batch_ref_2_budget_50_2005710_30.out
│   ├── batch_ref_2_budget_50_2005710_31.err
│   ├── batch_ref_2_budget_50_2005710_31.out
│   ├── batch_ref_2_budget_50_2005710_32.err
│   ├── batch_ref_2_budget_50_2005710_32.out
│   ├── batch_ref_2_budget_50_2005710_33.err
│   ├── batch_ref_2_budget_50_2005710_33.out
│   ├── batch_ref_2_budget_50_2005710_34.err
│   ├── batch_ref_2_budget_50_2005710_34.out
│   ├── batch_ref_2_budget_50_2005710_35.err
│   ├── batch_ref_2_budget_50_2005710_35.out
│   ├── batch_ref_2_budget_50_2005710_36.err
│   ├── batch_ref_2_budget_50_2005710_36.out
│   ├── batch_ref_2_budget_50_2005710_37.err
│   ├── batch_ref_2_budget_50_2005710_37.out
│   ├── batch_ref_2_budget_50_2005710_38.err
│   ├── batch_ref_2_budget_50_2005710_38.out
│   ├── batch_ref_2_budget_50_2005710_39.err
│   ├── batch_ref_2_budget_50_2005710_39.out
│   ├── batch_ref_2_budget_50_2005710_4.err
│   ├── batch_ref_2_budget_50_2005710_4.out
│   ├── batch_ref_2_budget_50_2005710_40.err
│   ├── batch_ref_2_budget_50_2005710_40.out
│   ├── batch_ref_2_budget_50_2005710_41.err
│   ├── batch_ref_2_budget_50_2005710_41.out
│   ├── batch_ref_2_budget_50_2005710_42.err
│   ├── batch_ref_2_budget_50_2005710_42.out
│   ├── batch_ref_2_budget_50_2005710_43.err
│   ├── batch_ref_2_budget_50_2005710_43.out
│   ├── batch_ref_2_budget_50_2005710_44.err
│   ├── batch_ref_2_budget_50_2005710_44.out
│   ├── batch_ref_2_budget_50_2005710_45.err
│   ├── batch_ref_2_budget_50_2005710_45.out
│   ├── batch_ref_2_budget_50_2005710_46.err
│   ├── batch_ref_2_budget_50_2005710_46.out
│   ├── batch_ref_2_budget_50_2005710_47.err
│   ├── batch_ref_2_budget_50_2005710_47.out
│   ├── batch_ref_2_budget_50_2005710_48.err
│   ├── batch_ref_2_budget_50_2005710_48.out
│   ├── batch_ref_2_budget_50_2005710_49.err
│   ├── batch_ref_2_budget_50_2005710_49.out
│   ├── batch_ref_2_budget_50_2005710_5.err
│   ├── batch_ref_2_budget_50_2005710_5.out
│   ├── batch_ref_2_budget_50_2005710_50.err
│   ├── batch_ref_2_budget_50_2005710_50.out
│   ├── batch_ref_2_budget_50_2005710_51.err
│   ├── batch_ref_2_budget_50_2005710_51.out
│   ├── batch_ref_2_budget_50_2005710_52.err
│   ├── batch_ref_2_budget_50_2005710_52.out
│   ├── batch_ref_2_budget_50_2005710_53.err
│   ├── batch_ref_2_budget_50_2005710_53.out
│   ├── batch_ref_2_budget_50_2005710_54.err
│   ├── batch_ref_2_budget_50_2005710_54.out
│   ├── batch_ref_2_budget_50_2005710_55.err
│   ├── batch_ref_2_budget_50_2005710_55.out
│   ├── batch_ref_2_budget_50_2005710_56.err
│   ├── batch_ref_2_budget_50_2005710_56.out
│   ├── batch_ref_2_budget_50_2005710_57.err
│   ├── batch_ref_2_budget_50_2005710_57.out
│   ├── batch_ref_2_budget_50_2005710_58.err
│   ├── batch_ref_2_budget_50_2005710_58.out
│   ├── batch_ref_2_budget_50_2005710_59.err
│   ├── batch_ref_2_budget_50_2005710_59.out
│   ├── batch_ref_2_budget_50_2005710_6.err
│   ├── batch_ref_2_budget_50_2005710_6.out
│   ├── batch_ref_2_budget_50_2005710_60.err
│   ├── batch_ref_2_budget_50_2005710_60.out
│   ├── batch_ref_2_budget_50_2005710_61.err
│   ├── batch_ref_2_budget_50_2005710_61.out
│   ├── batch_ref_2_budget_50_2005710_62.err
│   ├── batch_ref_2_budget_50_2005710_62.out
│   ├── batch_ref_2_budget_50_2005710_63.err
│   ├── batch_ref_2_budget_50_2005710_63.out
│   ├── batch_ref_2_budget_50_2005710_64.err
│   ├── batch_ref_2_budget_50_2005710_64.out
│   ├── batch_ref_2_budget_50_2005710_65.err
│   ├── batch_ref_2_budget_50_2005710_65.out
│   ├── batch_ref_2_budget_50_2005710_66.err
│   ├── batch_ref_2_budget_50_2005710_66.out
│   ├── batch_ref_2_budget_50_2005710_67.err
│   ├── batch_ref_2_budget_50_2005710_67.out
│   ├── batch_ref_2_budget_50_2005710_68.err
│   ├── batch_ref_2_budget_50_2005710_68.out
│   ├── batch_ref_2_budget_50_2005710_69.err
│   ├── batch_ref_2_budget_50_2005710_69.out
│   ├── batch_ref_2_budget_50_2005710_7.err
│   ├── batch_ref_2_budget_50_2005710_7.out
│   ├── batch_ref_2_budget_50_2005710_70.err
│   ├── batch_ref_2_budget_50_2005710_70.out
│   ├── batch_ref_2_budget_50_2005710_71.err
│   ├── batch_ref_2_budget_50_2005710_71.out
│   ├── batch_ref_2_budget_50_2005710_72.err
│   ├── batch_ref_2_budget_50_2005710_72.out
│   ├── batch_ref_2_budget_50_2005710_73.err
│   ├── batch_ref_2_budget_50_2005710_73.out
│   ├── batch_ref_2_budget_50_2005710_74.err
│   ├── batch_ref_2_budget_50_2005710_74.out
│   ├── batch_ref_2_budget_50_2005710_75.err
│   ├── batch_ref_2_budget_50_2005710_75.out
│   ├── batch_ref_2_budget_50_2005710_76.err
│   ├── batch_ref_2_budget_50_2005710_76.out
│   ├── batch_ref_2_budget_50_2005710_77.err
│   ├── batch_ref_2_budget_50_2005710_77.out
│   ├── batch_ref_2_budget_50_2005710_78.err
│   ├── batch_ref_2_budget_50_2005710_78.out
│   ├── batch_ref_2_budget_50_2005710_79.err
│   ├── batch_ref_2_budget_50_2005710_79.out
│   ├── batch_ref_2_budget_50_2005710_8.err
│   ├── batch_ref_2_budget_50_2005710_8.out
│   ├── batch_ref_2_budget_50_2005710_80.err
│   ├── batch_ref_2_budget_50_2005710_80.out
│   ├── batch_ref_2_budget_50_2005710_81.err
│   ├── batch_ref_2_budget_50_2005710_81.out
│   ├── batch_ref_2_budget_50_2005710_9.err
│   ├── batch_ref_2_budget_50_2005710_9.out
│   ├── batch_ref_2_budget_50_2006197_1.err
│   ├── batch_ref_2_budget_50_2006197_1.out
│   ├── batch_ref_2_budget_50_2006197_10.err
│   ├── batch_ref_2_budget_50_2006197_10.out
│   ├── batch_ref_2_budget_50_2006197_11.err
│   ├── batch_ref_2_budget_50_2006197_11.out
│   ├── batch_ref_2_budget_50_2006197_12.err
│   ├── batch_ref_2_budget_50_2006197_12.out
│   ├── batch_ref_2_budget_50_2006197_13.err
│   ├── batch_ref_2_budget_50_2006197_13.out
│   ├── batch_ref_2_budget_50_2006197_14.err
│   ├── batch_ref_2_budget_50_2006197_14.out
│   ├── batch_ref_2_budget_50_2006197_15.err
│   ├── batch_ref_2_budget_50_2006197_15.out
│   ├── batch_ref_2_budget_50_2006197_16.err
│   ├── batch_ref_2_budget_50_2006197_16.out
│   ├── batch_ref_2_budget_50_2006197_17.err
│   ├── batch_ref_2_budget_50_2006197_17.out
│   ├── batch_ref_2_budget_50_2006197_18.err
│   ├── batch_ref_2_budget_50_2006197_18.out
│   ├── batch_ref_2_budget_50_2006197_19.err
│   ├── batch_ref_2_budget_50_2006197_19.out
│   ├── batch_ref_2_budget_50_2006197_2.err
│   ├── batch_ref_2_budget_50_2006197_2.out
│   ├── batch_ref_2_budget_50_2006197_20.err
│   ├── batch_ref_2_budget_50_2006197_20.out
│   ├── batch_ref_2_budget_50_2006197_21.err
│   ├── batch_ref_2_budget_50_2006197_21.out
│   ├── batch_ref_2_budget_50_2006197_22.err
│   ├── batch_ref_2_budget_50_2006197_22.out
│   ├── batch_ref_2_budget_50_2006197_23.err
│   ├── batch_ref_2_budget_50_2006197_23.out
│   ├── batch_ref_2_budget_50_2006197_24.err
│   ├── batch_ref_2_budget_50_2006197_24.out
│   ├── batch_ref_2_budget_50_2006197_25.err
│   ├── batch_ref_2_budget_50_2006197_25.out
│   ├── batch_ref_2_budget_50_2006197_26.err
│   ├── batch_ref_2_budget_50_2006197_26.out
│   ├── batch_ref_2_budget_50_2006197_27.err
│   ├── batch_ref_2_budget_50_2006197_27.out
│   ├── batch_ref_2_budget_50_2006197_28.err
│   ├── batch_ref_2_budget_50_2006197_28.out
│   ├── batch_ref_2_budget_50_2006197_29.err
│   ├── batch_ref_2_budget_50_2006197_29.out
│   ├── batch_ref_2_budget_50_2006197_3.err
│   ├── batch_ref_2_budget_50_2006197_3.out
│   ├── batch_ref_2_budget_50_2006197_30.err
│   ├── batch_ref_2_budget_50_2006197_30.out
│   ├── batch_ref_2_budget_50_2006197_31.err
│   ├── batch_ref_2_budget_50_2006197_31.out
│   ├── batch_ref_2_budget_50_2006197_32.err
│   ├── batch_ref_2_budget_50_2006197_32.out
│   ├── batch_ref_2_budget_50_2006197_33.err
│   ├── batch_ref_2_budget_50_2006197_33.out
│   ├── batch_ref_2_budget_50_2006197_34.err
│   ├── batch_ref_2_budget_50_2006197_34.out
│   ├── batch_ref_2_budget_50_2006197_35.err
│   ├── batch_ref_2_budget_50_2006197_35.out
│   ├── batch_ref_2_budget_50_2006197_36.err
│   ├── batch_ref_2_budget_50_2006197_36.out
│   ├── batch_ref_2_budget_50_2006197_37.err
│   ├── batch_ref_2_budget_50_2006197_37.out
│   ├── batch_ref_2_budget_50_2006197_38.err
│   ├── batch_ref_2_budget_50_2006197_38.out
│   ├── batch_ref_2_budget_50_2006197_39.err
│   ├── batch_ref_2_budget_50_2006197_39.out
│   ├── batch_ref_2_budget_50_2006197_4.err
│   ├── batch_ref_2_budget_50_2006197_4.out
│   ├── batch_ref_2_budget_50_2006197_40.err
│   ├── batch_ref_2_budget_50_2006197_40.out
│   ├── batch_ref_2_budget_50_2006197_41.err
│   ├── batch_ref_2_budget_50_2006197_41.out
│   ├── batch_ref_2_budget_50_2006197_42.err
│   ├── batch_ref_2_budget_50_2006197_42.out
│   ├── batch_ref_2_budget_50_2006197_43.err
│   ├── batch_ref_2_budget_50_2006197_43.out
│   ├── batch_ref_2_budget_50_2006197_44.err
│   ├── batch_ref_2_budget_50_2006197_44.out
│   ├── batch_ref_2_budget_50_2006197_45.err
│   ├── batch_ref_2_budget_50_2006197_45.out
│   ├── batch_ref_2_budget_50_2006197_46.err
│   ├── batch_ref_2_budget_50_2006197_46.out
│   ├── batch_ref_2_budget_50_2006197_47.err
│   ├── batch_ref_2_budget_50_2006197_47.out
│   ├── batch_ref_2_budget_50_2006197_48.err
│   ├── batch_ref_2_budget_50_2006197_48.out
│   ├── batch_ref_2_budget_50_2006197_49.err
│   ├── batch_ref_2_budget_50_2006197_49.out
│   ├── batch_ref_2_budget_50_2006197_5.err
│   ├── batch_ref_2_budget_50_2006197_5.out
│   ├── batch_ref_2_budget_50_2006197_50.err
│   ├── batch_ref_2_budget_50_2006197_50.out
│   ├── batch_ref_2_budget_50_2006197_51.err
│   ├── batch_ref_2_budget_50_2006197_51.out
│   ├── batch_ref_2_budget_50_2006197_52.err
│   ├── batch_ref_2_budget_50_2006197_52.out
│   ├── batch_ref_2_budget_50_2006197_53.err
│   ├── batch_ref_2_budget_50_2006197_53.out
│   ├── batch_ref_2_budget_50_2006197_54.err
│   ├── batch_ref_2_budget_50_2006197_54.out
│   ├── batch_ref_2_budget_50_2006197_55.err
│   ├── batch_ref_2_budget_50_2006197_55.out
│   ├── batch_ref_2_budget_50_2006197_56.err
│   ├── batch_ref_2_budget_50_2006197_56.out
│   ├── batch_ref_2_budget_50_2006197_57.err
│   ├── batch_ref_2_budget_50_2006197_57.out
│   ├── batch_ref_2_budget_50_2006197_58.err
│   ├── batch_ref_2_budget_50_2006197_58.out
│   ├── batch_ref_2_budget_50_2006197_59.err
│   ├── batch_ref_2_budget_50_2006197_59.out
│   ├── batch_ref_2_budget_50_2006197_6.err
│   ├── batch_ref_2_budget_50_2006197_6.out
│   ├── batch_ref_2_budget_50_2006197_60.err
│   ├── batch_ref_2_budget_50_2006197_60.out
│   ├── batch_ref_2_budget_50_2006197_61.err
│   ├── batch_ref_2_budget_50_2006197_61.out
│   ├── batch_ref_2_budget_50_2006197_62.err
│   ├── batch_ref_2_budget_50_2006197_62.out
│   ├── batch_ref_2_budget_50_2006197_63.err
│   ├── batch_ref_2_budget_50_2006197_63.out
│   ├── batch_ref_2_budget_50_2006197_64.err
│   ├── batch_ref_2_budget_50_2006197_64.out
│   ├── batch_ref_2_budget_50_2006197_65.err
│   ├── batch_ref_2_budget_50_2006197_65.out
│   ├── batch_ref_2_budget_50_2006197_66.err
│   ├── batch_ref_2_budget_50_2006197_66.out
│   ├── batch_ref_2_budget_50_2006197_67.err
│   ├── batch_ref_2_budget_50_2006197_67.out
│   ├── batch_ref_2_budget_50_2006197_68.err
│   ├── batch_ref_2_budget_50_2006197_68.out
│   ├── batch_ref_2_budget_50_2006197_69.err
│   ├── batch_ref_2_budget_50_2006197_69.out
│   ├── batch_ref_2_budget_50_2006197_7.err
│   ├── batch_ref_2_budget_50_2006197_7.out
│   ├── batch_ref_2_budget_50_2006197_70.err
│   ├── batch_ref_2_budget_50_2006197_70.out
│   ├── batch_ref_2_budget_50_2006197_71.err
│   ├── batch_ref_2_budget_50_2006197_71.out
│   ├── batch_ref_2_budget_50_2006197_72.err
│   ├── batch_ref_2_budget_50_2006197_72.out
│   ├── batch_ref_2_budget_50_2006197_73.err
│   ├── batch_ref_2_budget_50_2006197_73.out
│   ├── batch_ref_2_budget_50_2006197_74.err
│   ├── batch_ref_2_budget_50_2006197_74.out
│   ├── batch_ref_2_budget_50_2006197_75.err
│   ├── batch_ref_2_budget_50_2006197_75.out
│   ├── batch_ref_2_budget_50_2006197_76.err
│   ├── batch_ref_2_budget_50_2006197_76.out
│   ├── batch_ref_2_budget_50_2006197_77.err
│   ├── batch_ref_2_budget_50_2006197_77.out
│   ├── batch_ref_2_budget_50_2006197_78.err
│   ├── batch_ref_2_budget_50_2006197_78.out
│   ├── batch_ref_2_budget_50_2006197_79.err
│   ├── batch_ref_2_budget_50_2006197_79.out
│   ├── batch_ref_2_budget_50_2006197_8.err
│   ├── batch_ref_2_budget_50_2006197_8.out
│   ├── batch_ref_2_budget_50_2006197_80.err
│   ├── batch_ref_2_budget_50_2006197_80.out
│   ├── batch_ref_2_budget_50_2006197_81.err
│   ├── batch_ref_2_budget_50_2006197_81.out
│   ├── batch_ref_2_budget_50_2006197_9.err
│   ├── batch_ref_2_budget_50_2006197_9.out
│   ├── batch_ref_2_budget_50_2007827_1.err
│   ├── batch_ref_2_budget_50_2007827_1.out
│   ├── batch_ref_2_budget_50_2007827_10.err
│   ├── batch_ref_2_budget_50_2007827_10.out
│   ├── batch_ref_2_budget_50_2007827_11.err
│   ├── batch_ref_2_budget_50_2007827_11.out
│   ├── batch_ref_2_budget_50_2007827_12.err
│   ├── batch_ref_2_budget_50_2007827_12.out
│   ├── batch_ref_2_budget_50_2007827_13.err
│   ├── batch_ref_2_budget_50_2007827_13.out
│   ├── batch_ref_2_budget_50_2007827_14.err
│   ├── batch_ref_2_budget_50_2007827_14.out
│   ├── batch_ref_2_budget_50_2007827_15.err
│   ├── batch_ref_2_budget_50_2007827_15.out
│   ├── batch_ref_2_budget_50_2007827_16.err
│   ├── batch_ref_2_budget_50_2007827_16.out
│   ├── batch_ref_2_budget_50_2007827_17.err
│   ├── batch_ref_2_budget_50_2007827_17.out
│   ├── batch_ref_2_budget_50_2007827_18.err
│   ├── batch_ref_2_budget_50_2007827_18.out
│   ├── batch_ref_2_budget_50_2007827_19.err
│   ├── batch_ref_2_budget_50_2007827_19.out
│   ├── batch_ref_2_budget_50_2007827_2.err
│   ├── batch_ref_2_budget_50_2007827_2.out
│   ├── batch_ref_2_budget_50_2007827_20.err
│   ├── batch_ref_2_budget_50_2007827_20.out
│   ├── batch_ref_2_budget_50_2007827_21.err
│   ├── batch_ref_2_budget_50_2007827_21.out
│   ├── batch_ref_2_budget_50_2007827_22.err
│   ├── batch_ref_2_budget_50_2007827_22.out
│   ├── batch_ref_2_budget_50_2007827_23.err
│   ├── batch_ref_2_budget_50_2007827_23.out
│   ├── batch_ref_2_budget_50_2007827_24.err
│   ├── batch_ref_2_budget_50_2007827_24.out
│   ├── batch_ref_2_budget_50_2007827_25.err
│   ├── batch_ref_2_budget_50_2007827_25.out
│   ├── batch_ref_2_budget_50_2007827_26.err
│   ├── batch_ref_2_budget_50_2007827_26.out
│   ├── batch_ref_2_budget_50_2007827_27.err
│   ├── batch_ref_2_budget_50_2007827_27.out
│   ├── batch_ref_2_budget_50_2007827_28.err
│   ├── batch_ref_2_budget_50_2007827_28.out
│   ├── batch_ref_2_budget_50_2007827_29.err
│   ├── batch_ref_2_budget_50_2007827_29.out
│   ├── batch_ref_2_budget_50_2007827_3.err
│   ├── batch_ref_2_budget_50_2007827_3.out
│   ├── batch_ref_2_budget_50_2007827_30.err
│   ├── batch_ref_2_budget_50_2007827_30.out
│   ├── batch_ref_2_budget_50_2007827_31.err
│   ├── batch_ref_2_budget_50_2007827_31.out
│   ├── batch_ref_2_budget_50_2007827_32.err
│   ├── batch_ref_2_budget_50_2007827_32.out
│   ├── batch_ref_2_budget_50_2007827_33.err
│   ├── batch_ref_2_budget_50_2007827_33.out
│   ├── batch_ref_2_budget_50_2007827_34.err
│   ├── batch_ref_2_budget_50_2007827_34.out
│   ├── batch_ref_2_budget_50_2007827_35.err
│   ├── batch_ref_2_budget_50_2007827_35.out
│   ├── batch_ref_2_budget_50_2007827_36.err
│   ├── batch_ref_2_budget_50_2007827_36.out
│   ├── batch_ref_2_budget_50_2007827_37.err
│   ├── batch_ref_2_budget_50_2007827_37.out
│   ├── batch_ref_2_budget_50_2007827_38.err
│   ├── batch_ref_2_budget_50_2007827_38.out
│   ├── batch_ref_2_budget_50_2007827_39.err
│   ├── batch_ref_2_budget_50_2007827_39.out
│   ├── batch_ref_2_budget_50_2007827_4.err
│   ├── batch_ref_2_budget_50_2007827_4.out
│   ├── batch_ref_2_budget_50_2007827_40.err
│   ├── batch_ref_2_budget_50_2007827_40.out
│   ├── batch_ref_2_budget_50_2007827_41.err
│   ├── batch_ref_2_budget_50_2007827_41.out
│   ├── batch_ref_2_budget_50_2007827_42.err
│   ├── batch_ref_2_budget_50_2007827_42.out
│   ├── batch_ref_2_budget_50_2007827_43.err
│   ├── batch_ref_2_budget_50_2007827_43.out
│   ├── batch_ref_2_budget_50_2007827_44.err
│   ├── batch_ref_2_budget_50_2007827_44.out
│   ├── batch_ref_2_budget_50_2007827_45.err
│   ├── batch_ref_2_budget_50_2007827_45.out
│   ├── batch_ref_2_budget_50_2007827_46.err
│   ├── batch_ref_2_budget_50_2007827_46.out
│   ├── batch_ref_2_budget_50_2007827_47.err
│   ├── batch_ref_2_budget_50_2007827_47.out
│   ├── batch_ref_2_budget_50_2007827_48.err
│   ├── batch_ref_2_budget_50_2007827_48.out
│   ├── batch_ref_2_budget_50_2007827_49.err
│   ├── batch_ref_2_budget_50_2007827_49.out
│   ├── batch_ref_2_budget_50_2007827_5.err
│   ├── batch_ref_2_budget_50_2007827_5.out
│   ├── batch_ref_2_budget_50_2007827_50.err
│   ├── batch_ref_2_budget_50_2007827_50.out
│   ├── batch_ref_2_budget_50_2007827_51.err
│   ├── batch_ref_2_budget_50_2007827_51.out
│   ├── batch_ref_2_budget_50_2007827_52.err
│   ├── batch_ref_2_budget_50_2007827_52.out
│   ├── batch_ref_2_budget_50_2007827_53.err
│   ├── batch_ref_2_budget_50_2007827_53.out
│   ├── batch_ref_2_budget_50_2007827_54.err
│   ├── batch_ref_2_budget_50_2007827_54.out
│   ├── batch_ref_2_budget_50_2007827_55.err
│   ├── batch_ref_2_budget_50_2007827_55.out
│   ├── batch_ref_2_budget_50_2007827_56.err
│   ├── batch_ref_2_budget_50_2007827_56.out
│   ├── batch_ref_2_budget_50_2007827_57.err
│   ├── batch_ref_2_budget_50_2007827_57.out
│   ├── batch_ref_2_budget_50_2007827_58.err
│   ├── batch_ref_2_budget_50_2007827_58.out
│   ├── batch_ref_2_budget_50_2007827_59.err
│   ├── batch_ref_2_budget_50_2007827_59.out
│   ├── batch_ref_2_budget_50_2007827_6.err
│   ├── batch_ref_2_budget_50_2007827_6.out
│   ├── batch_ref_2_budget_50_2007827_60.err
│   ├── batch_ref_2_budget_50_2007827_60.out
│   ├── batch_ref_2_budget_50_2007827_61.err
│   ├── batch_ref_2_budget_50_2007827_61.out
│   ├── batch_ref_2_budget_50_2007827_62.err
│   ├── batch_ref_2_budget_50_2007827_62.out
│   ├── batch_ref_2_budget_50_2007827_63.err
│   ├── batch_ref_2_budget_50_2007827_63.out
│   ├── batch_ref_2_budget_50_2007827_64.err
│   ├── batch_ref_2_budget_50_2007827_64.out
│   ├── batch_ref_2_budget_50_2007827_65.err
│   ├── batch_ref_2_budget_50_2007827_65.out
│   ├── batch_ref_2_budget_50_2007827_66.err
│   ├── batch_ref_2_budget_50_2007827_66.out
│   ├── batch_ref_2_budget_50_2007827_67.err
│   ├── batch_ref_2_budget_50_2007827_67.out
│   ├── batch_ref_2_budget_50_2007827_68.err
│   ├── batch_ref_2_budget_50_2007827_68.out
│   ├── batch_ref_2_budget_50_2007827_69.err
│   ├── batch_ref_2_budget_50_2007827_69.out
│   ├── batch_ref_2_budget_50_2007827_7.err
│   ├── batch_ref_2_budget_50_2007827_7.out
│   ├── batch_ref_2_budget_50_2007827_70.err
│   ├── batch_ref_2_budget_50_2007827_70.out
│   ├── batch_ref_2_budget_50_2007827_71.err
│   ├── batch_ref_2_budget_50_2007827_71.out
│   ├── batch_ref_2_budget_50_2007827_72.err
│   ├── batch_ref_2_budget_50_2007827_72.out
│   ├── batch_ref_2_budget_50_2007827_73.err
│   ├── batch_ref_2_budget_50_2007827_73.out
│   ├── batch_ref_2_budget_50_2007827_74.err
│   ├── batch_ref_2_budget_50_2007827_74.out
│   ├── batch_ref_2_budget_50_2007827_75.err
│   ├── batch_ref_2_budget_50_2007827_75.out
│   ├── batch_ref_2_budget_50_2007827_76.err
│   ├── batch_ref_2_budget_50_2007827_76.out
│   ├── batch_ref_2_budget_50_2007827_77.err
│   ├── batch_ref_2_budget_50_2007827_77.out
│   ├── batch_ref_2_budget_50_2007827_78.err
│   ├── batch_ref_2_budget_50_2007827_78.out
│   ├── batch_ref_2_budget_50_2007827_79.err
│   ├── batch_ref_2_budget_50_2007827_79.out
│   ├── batch_ref_2_budget_50_2007827_8.err
│   ├── batch_ref_2_budget_50_2007827_8.out
│   ├── batch_ref_2_budget_50_2007827_80.err
│   ├── batch_ref_2_budget_50_2007827_80.out
│   ├── batch_ref_2_budget_50_2007827_81.err
│   ├── batch_ref_2_budget_50_2007827_81.out
│   ├── batch_ref_2_budget_50_2007827_9.err
│   ├── batch_ref_2_budget_50_2007827_9.out
│   ├── batch_ref_2_budget_50_2007914_1.err
│   ├── batch_ref_2_budget_50_2007914_1.out
│   ├── batch_ref_2_budget_50_2007914_10.err
│   ├── batch_ref_2_budget_50_2007914_10.out
│   ├── batch_ref_2_budget_50_2007914_11.err
│   ├── batch_ref_2_budget_50_2007914_11.out
│   ├── batch_ref_2_budget_50_2007914_12.err
│   ├── batch_ref_2_budget_50_2007914_12.out
│   ├── batch_ref_2_budget_50_2007914_13.err
│   ├── batch_ref_2_budget_50_2007914_13.out
│   ├── batch_ref_2_budget_50_2007914_14.err
│   ├── batch_ref_2_budget_50_2007914_14.out
│   ├── batch_ref_2_budget_50_2007914_15.err
│   ├── batch_ref_2_budget_50_2007914_15.out
│   ├── batch_ref_2_budget_50_2007914_16.err
│   ├── batch_ref_2_budget_50_2007914_16.out
│   ├── batch_ref_2_budget_50_2007914_17.err
│   ├── batch_ref_2_budget_50_2007914_17.out
│   ├── batch_ref_2_budget_50_2007914_18.err
│   ├── batch_ref_2_budget_50_2007914_18.out
│   ├── batch_ref_2_budget_50_2007914_19.err
│   ├── batch_ref_2_budget_50_2007914_19.out
│   ├── batch_ref_2_budget_50_2007914_2.err
│   ├── batch_ref_2_budget_50_2007914_2.out
│   ├── batch_ref_2_budget_50_2007914_20.err
│   ├── batch_ref_2_budget_50_2007914_20.out
│   ├── batch_ref_2_budget_50_2007914_21.err
│   ├── batch_ref_2_budget_50_2007914_21.out
│   ├── batch_ref_2_budget_50_2007914_22.err
│   ├── batch_ref_2_budget_50_2007914_22.out
│   ├── batch_ref_2_budget_50_2007914_23.err
│   ├── batch_ref_2_budget_50_2007914_23.out
│   ├── batch_ref_2_budget_50_2007914_24.err
│   ├── batch_ref_2_budget_50_2007914_24.out
│   ├── batch_ref_2_budget_50_2007914_25.err
│   ├── batch_ref_2_budget_50_2007914_25.out
│   ├── batch_ref_2_budget_50_2007914_26.err
│   ├── batch_ref_2_budget_50_2007914_26.out
│   ├── batch_ref_2_budget_50_2007914_27.err
│   ├── batch_ref_2_budget_50_2007914_27.out
│   ├── batch_ref_2_budget_50_2007914_28.err
│   ├── batch_ref_2_budget_50_2007914_28.out
│   ├── batch_ref_2_budget_50_2007914_29.err
│   ├── batch_ref_2_budget_50_2007914_29.out
│   ├── batch_ref_2_budget_50_2007914_3.err
│   ├── batch_ref_2_budget_50_2007914_3.out
│   ├── batch_ref_2_budget_50_2007914_30.err
│   ├── batch_ref_2_budget_50_2007914_30.out
│   ├── batch_ref_2_budget_50_2007914_31.err
│   ├── batch_ref_2_budget_50_2007914_31.out
│   ├── batch_ref_2_budget_50_2007914_32.err
│   ├── batch_ref_2_budget_50_2007914_32.out
│   ├── batch_ref_2_budget_50_2007914_33.err
│   ├── batch_ref_2_budget_50_2007914_33.out
│   ├── batch_ref_2_budget_50_2007914_34.err
│   ├── batch_ref_2_budget_50_2007914_34.out
│   ├── batch_ref_2_budget_50_2007914_35.err
│   ├── batch_ref_2_budget_50_2007914_35.out
│   ├── batch_ref_2_budget_50_2007914_36.err
│   ├── batch_ref_2_budget_50_2007914_36.out
│   ├── batch_ref_2_budget_50_2007914_37.err
│   ├── batch_ref_2_budget_50_2007914_37.out
│   ├── batch_ref_2_budget_50_2007914_38.err
│   ├── batch_ref_2_budget_50_2007914_38.out
│   ├── batch_ref_2_budget_50_2007914_39.err
│   ├── batch_ref_2_budget_50_2007914_39.out
│   ├── batch_ref_2_budget_50_2007914_4.err
│   ├── batch_ref_2_budget_50_2007914_4.out
│   ├── batch_ref_2_budget_50_2007914_40.err
│   ├── batch_ref_2_budget_50_2007914_40.out
│   ├── batch_ref_2_budget_50_2007914_41.err
│   ├── batch_ref_2_budget_50_2007914_41.out
│   ├── batch_ref_2_budget_50_2007914_42.err
│   ├── batch_ref_2_budget_50_2007914_42.out
│   ├── batch_ref_2_budget_50_2007914_43.err
│   ├── batch_ref_2_budget_50_2007914_43.out
│   ├── batch_ref_2_budget_50_2007914_44.err
│   ├── batch_ref_2_budget_50_2007914_44.out
│   ├── batch_ref_2_budget_50_2007914_45.err
│   ├── batch_ref_2_budget_50_2007914_45.out
│   ├── batch_ref_2_budget_50_2007914_46.err
│   ├── batch_ref_2_budget_50_2007914_46.out
│   ├── batch_ref_2_budget_50_2007914_47.err
│   ├── batch_ref_2_budget_50_2007914_47.out
│   ├── batch_ref_2_budget_50_2007914_48.err
│   ├── batch_ref_2_budget_50_2007914_48.out
│   ├── batch_ref_2_budget_50_2007914_49.err
│   ├── batch_ref_2_budget_50_2007914_49.out
│   ├── batch_ref_2_budget_50_2007914_5.err
│   ├── batch_ref_2_budget_50_2007914_5.out
│   ├── batch_ref_2_budget_50_2007914_50.err
│   ├── batch_ref_2_budget_50_2007914_50.out
│   ├── batch_ref_2_budget_50_2007914_51.err
│   ├── batch_ref_2_budget_50_2007914_51.out
│   ├── batch_ref_2_budget_50_2007914_52.err
│   ├── batch_ref_2_budget_50_2007914_52.out
│   ├── batch_ref_2_budget_50_2007914_53.err
│   ├── batch_ref_2_budget_50_2007914_53.out
│   ├── batch_ref_2_budget_50_2007914_54.err
│   ├── batch_ref_2_budget_50_2007914_54.out
│   ├── batch_ref_2_budget_50_2007914_55.err
│   ├── batch_ref_2_budget_50_2007914_55.out
│   ├── batch_ref_2_budget_50_2007914_56.err
│   ├── batch_ref_2_budget_50_2007914_56.out
│   ├── batch_ref_2_budget_50_2007914_57.err
│   ├── batch_ref_2_budget_50_2007914_57.out
│   ├── batch_ref_2_budget_50_2007914_58.err
│   ├── batch_ref_2_budget_50_2007914_58.out
│   ├── batch_ref_2_budget_50_2007914_59.err
│   ├── batch_ref_2_budget_50_2007914_59.out
│   ├── batch_ref_2_budget_50_2007914_6.err
│   ├── batch_ref_2_budget_50_2007914_6.out
│   ├── batch_ref_2_budget_50_2007914_60.err
│   ├── batch_ref_2_budget_50_2007914_60.out
│   ├── batch_ref_2_budget_50_2007914_61.err
│   ├── batch_ref_2_budget_50_2007914_61.out
│   ├── batch_ref_2_budget_50_2007914_62.err
│   ├── batch_ref_2_budget_50_2007914_62.out
│   ├── batch_ref_2_budget_50_2007914_63.err
│   ├── batch_ref_2_budget_50_2007914_63.out
│   ├── batch_ref_2_budget_50_2007914_64.err
│   ├── batch_ref_2_budget_50_2007914_64.out
│   ├── batch_ref_2_budget_50_2007914_65.err
│   ├── batch_ref_2_budget_50_2007914_65.out
│   ├── batch_ref_2_budget_50_2007914_66.err
│   ├── batch_ref_2_budget_50_2007914_66.out
│   ├── batch_ref_2_budget_50_2007914_67.err
│   ├── batch_ref_2_budget_50_2007914_67.out
│   ├── batch_ref_2_budget_50_2007914_68.err
│   ├── batch_ref_2_budget_50_2007914_68.out
│   ├── batch_ref_2_budget_50_2007914_69.err
│   ├── batch_ref_2_budget_50_2007914_69.out
│   ├── batch_ref_2_budget_50_2007914_7.err
│   ├── batch_ref_2_budget_50_2007914_7.out
│   ├── batch_ref_2_budget_50_2007914_70.err
│   ├── batch_ref_2_budget_50_2007914_70.out
│   ├── batch_ref_2_budget_50_2007914_71.err
│   ├── batch_ref_2_budget_50_2007914_71.out
│   ├── batch_ref_2_budget_50_2007914_72.err
│   ├── batch_ref_2_budget_50_2007914_72.out
│   ├── batch_ref_2_budget_50_2007914_73.err
│   ├── batch_ref_2_budget_50_2007914_73.out
│   ├── batch_ref_2_budget_50_2007914_74.err
│   ├── batch_ref_2_budget_50_2007914_74.out
│   ├── batch_ref_2_budget_50_2007914_75.err
│   ├── batch_ref_2_budget_50_2007914_75.out
│   ├── batch_ref_2_budget_50_2007914_76.err
│   ├── batch_ref_2_budget_50_2007914_76.out
│   ├── batch_ref_2_budget_50_2007914_77.err
│   ├── batch_ref_2_budget_50_2007914_77.out
│   ├── batch_ref_2_budget_50_2007914_78.err
│   ├── batch_ref_2_budget_50_2007914_78.out
│   ├── batch_ref_2_budget_50_2007914_79.err
│   ├── batch_ref_2_budget_50_2007914_79.out
│   ├── batch_ref_2_budget_50_2007914_8.err
│   ├── batch_ref_2_budget_50_2007914_8.out
│   ├── batch_ref_2_budget_50_2007914_80.err
│   ├── batch_ref_2_budget_50_2007914_80.out
│   ├── batch_ref_2_budget_50_2007914_81.err
│   ├── batch_ref_2_budget_50_2007914_81.out
│   ├── batch_ref_2_budget_50_2007914_9.err
│   ├── batch_ref_2_budget_50_2007914_9.out
│   ├── batch_ref_2_budget_50_2039810_1.err
│   ├── batch_ref_2_budget_50_2039810_1.out
│   ├── batch_ref_2_budget_50_2039810_10.err
│   ├── batch_ref_2_budget_50_2039810_10.out
│   ├── batch_ref_2_budget_50_2039810_11.err
│   ├── batch_ref_2_budget_50_2039810_11.out
│   ├── batch_ref_2_budget_50_2039810_12.err
│   ├── batch_ref_2_budget_50_2039810_12.out
│   ├── batch_ref_2_budget_50_2039810_13.err
│   ├── batch_ref_2_budget_50_2039810_13.out
│   ├── batch_ref_2_budget_50_2039810_14.err
│   ├── batch_ref_2_budget_50_2039810_14.out
│   ├── batch_ref_2_budget_50_2039810_15.err
│   ├── batch_ref_2_budget_50_2039810_15.out
│   ├── batch_ref_2_budget_50_2039810_16.err
│   ├── batch_ref_2_budget_50_2039810_16.out
│   ├── batch_ref_2_budget_50_2039810_17.err
│   ├── batch_ref_2_budget_50_2039810_17.out
│   ├── batch_ref_2_budget_50_2039810_18.err
│   ├── batch_ref_2_budget_50_2039810_18.out
│   ├── batch_ref_2_budget_50_2039810_19.err
│   ├── batch_ref_2_budget_50_2039810_19.out
│   ├── batch_ref_2_budget_50_2039810_2.err
│   ├── batch_ref_2_budget_50_2039810_2.out
│   ├── batch_ref_2_budget_50_2039810_20.err
│   ├── batch_ref_2_budget_50_2039810_20.out
│   ├── batch_ref_2_budget_50_2039810_21.err
│   ├── batch_ref_2_budget_50_2039810_21.out
│   ├── batch_ref_2_budget_50_2039810_22.err
│   ├── batch_ref_2_budget_50_2039810_22.out
│   ├── batch_ref_2_budget_50_2039810_23.err
│   ├── batch_ref_2_budget_50_2039810_23.out
│   ├── batch_ref_2_budget_50_2039810_24.err
│   ├── batch_ref_2_budget_50_2039810_24.out
│   ├── batch_ref_2_budget_50_2039810_25.err
│   ├── batch_ref_2_budget_50_2039810_25.out
│   ├── batch_ref_2_budget_50_2039810_26.err
│   ├── batch_ref_2_budget_50_2039810_26.out
│   ├── batch_ref_2_budget_50_2039810_27.err
│   ├── batch_ref_2_budget_50_2039810_27.out
│   ├── batch_ref_2_budget_50_2039810_28.err
│   ├── batch_ref_2_budget_50_2039810_28.out
│   ├── batch_ref_2_budget_50_2039810_29.err
│   ├── batch_ref_2_budget_50_2039810_29.out
│   ├── batch_ref_2_budget_50_2039810_3.err
│   ├── batch_ref_2_budget_50_2039810_3.out
│   ├── batch_ref_2_budget_50_2039810_30.err
│   ├── batch_ref_2_budget_50_2039810_30.out
│   ├── batch_ref_2_budget_50_2039810_31.err
│   ├── batch_ref_2_budget_50_2039810_31.out
│   ├── batch_ref_2_budget_50_2039810_32.err
│   ├── batch_ref_2_budget_50_2039810_32.out
│   ├── batch_ref_2_budget_50_2039810_33.err
│   ├── batch_ref_2_budget_50_2039810_33.out
│   ├── batch_ref_2_budget_50_2039810_34.err
│   ├── batch_ref_2_budget_50_2039810_34.out
│   ├── batch_ref_2_budget_50_2039810_35.err
│   ├── batch_ref_2_budget_50_2039810_35.out
│   ├── batch_ref_2_budget_50_2039810_36.err
│   ├── batch_ref_2_budget_50_2039810_36.out
│   ├── batch_ref_2_budget_50_2039810_37.err
│   ├── batch_ref_2_budget_50_2039810_37.out
│   ├── batch_ref_2_budget_50_2039810_38.err
│   ├── batch_ref_2_budget_50_2039810_38.out
│   ├── batch_ref_2_budget_50_2039810_39.err
│   ├── batch_ref_2_budget_50_2039810_39.out
│   ├── batch_ref_2_budget_50_2039810_4.err
│   ├── batch_ref_2_budget_50_2039810_4.out
│   ├── batch_ref_2_budget_50_2039810_40.err
│   ├── batch_ref_2_budget_50_2039810_40.out
│   ├── batch_ref_2_budget_50_2039810_41.err
│   ├── batch_ref_2_budget_50_2039810_41.out
│   ├── batch_ref_2_budget_50_2039810_42.err
│   ├── batch_ref_2_budget_50_2039810_42.out
│   ├── batch_ref_2_budget_50_2039810_43.err
│   ├── batch_ref_2_budget_50_2039810_43.out
│   ├── batch_ref_2_budget_50_2039810_44.err
│   ├── batch_ref_2_budget_50_2039810_44.out
│   ├── batch_ref_2_budget_50_2039810_45.err
│   ├── batch_ref_2_budget_50_2039810_45.out
│   ├── batch_ref_2_budget_50_2039810_46.err
│   ├── batch_ref_2_budget_50_2039810_46.out
│   ├── batch_ref_2_budget_50_2039810_47.err
│   ├── batch_ref_2_budget_50_2039810_47.out
│   ├── batch_ref_2_budget_50_2039810_48.err
│   ├── batch_ref_2_budget_50_2039810_48.out
│   ├── batch_ref_2_budget_50_2039810_49.err
│   ├── batch_ref_2_budget_50_2039810_49.out
│   ├── batch_ref_2_budget_50_2039810_5.err
│   ├── batch_ref_2_budget_50_2039810_5.out
│   ├── batch_ref_2_budget_50_2039810_50.err
│   ├── batch_ref_2_budget_50_2039810_50.out
│   ├── batch_ref_2_budget_50_2039810_51.err
│   ├── batch_ref_2_budget_50_2039810_51.out
│   ├── batch_ref_2_budget_50_2039810_52.err
│   ├── batch_ref_2_budget_50_2039810_52.out
│   ├── batch_ref_2_budget_50_2039810_53.err
│   ├── batch_ref_2_budget_50_2039810_53.out
│   ├── batch_ref_2_budget_50_2039810_54.err
│   ├── batch_ref_2_budget_50_2039810_54.out
│   ├── batch_ref_2_budget_50_2039810_55.err
│   ├── batch_ref_2_budget_50_2039810_55.out
│   ├── batch_ref_2_budget_50_2039810_56.err
│   ├── batch_ref_2_budget_50_2039810_56.out
│   ├── batch_ref_2_budget_50_2039810_57.err
│   ├── batch_ref_2_budget_50_2039810_57.out
│   ├── batch_ref_2_budget_50_2039810_58.err
│   ├── batch_ref_2_budget_50_2039810_58.out
│   ├── batch_ref_2_budget_50_2039810_59.err
│   ├── batch_ref_2_budget_50_2039810_59.out
│   ├── batch_ref_2_budget_50_2039810_6.err
│   ├── batch_ref_2_budget_50_2039810_6.out
│   ├── batch_ref_2_budget_50_2039810_60.err
│   ├── batch_ref_2_budget_50_2039810_60.out
│   ├── batch_ref_2_budget_50_2039810_61.err
│   ├── batch_ref_2_budget_50_2039810_61.out
│   ├── batch_ref_2_budget_50_2039810_62.err
│   ├── batch_ref_2_budget_50_2039810_62.out
│   ├── batch_ref_2_budget_50_2039810_63.err
│   ├── batch_ref_2_budget_50_2039810_63.out
│   ├── batch_ref_2_budget_50_2039810_64.err
│   ├── batch_ref_2_budget_50_2039810_64.out
│   ├── batch_ref_2_budget_50_2039810_65.err
│   ├── batch_ref_2_budget_50_2039810_65.out
│   ├── batch_ref_2_budget_50_2039810_66.err
│   ├── batch_ref_2_budget_50_2039810_66.out
│   ├── batch_ref_2_budget_50_2039810_67.err
│   ├── batch_ref_2_budget_50_2039810_67.out
│   ├── batch_ref_2_budget_50_2039810_68.err
│   ├── batch_ref_2_budget_50_2039810_68.out
│   ├── batch_ref_2_budget_50_2039810_69.err
│   ├── batch_ref_2_budget_50_2039810_69.out
│   ├── batch_ref_2_budget_50_2039810_7.err
│   ├── batch_ref_2_budget_50_2039810_7.out
│   ├── batch_ref_2_budget_50_2039810_70.err
│   ├── batch_ref_2_budget_50_2039810_70.out
│   ├── batch_ref_2_budget_50_2039810_71.err
│   ├── batch_ref_2_budget_50_2039810_71.out
│   ├── batch_ref_2_budget_50_2039810_72.err
│   ├── batch_ref_2_budget_50_2039810_72.out
│   ├── batch_ref_2_budget_50_2039810_73.err
│   ├── batch_ref_2_budget_50_2039810_73.out
│   ├── batch_ref_2_budget_50_2039810_74.err
│   ├── batch_ref_2_budget_50_2039810_74.out
│   ├── batch_ref_2_budget_50_2039810_75.err
│   ├── batch_ref_2_budget_50_2039810_75.out
│   ├── batch_ref_2_budget_50_2039810_76.err
│   ├── batch_ref_2_budget_50_2039810_76.out
│   ├── batch_ref_2_budget_50_2039810_77.err
│   ├── batch_ref_2_budget_50_2039810_77.out
│   ├── batch_ref_2_budget_50_2039810_78.err
│   ├── batch_ref_2_budget_50_2039810_78.out
│   ├── batch_ref_2_budget_50_2039810_79.err
│   ├── batch_ref_2_budget_50_2039810_79.out
│   ├── batch_ref_2_budget_50_2039810_8.err
│   ├── batch_ref_2_budget_50_2039810_8.out
│   ├── batch_ref_2_budget_50_2039810_80.err
│   ├── batch_ref_2_budget_50_2039810_80.out
│   ├── batch_ref_2_budget_50_2039810_81.err
│   ├── batch_ref_2_budget_50_2039810_81.out
│   ├── batch_ref_2_budget_50_2039810_9.err
│   ├── batch_ref_2_budget_50_2039810_9.out
│   ├── batch_ref_3_budget_100_2038466_1.err
│   ├── batch_ref_3_budget_100_2038466_1.out
│   ├── batch_ref_3_budget_100_2038466_10.err
│   ├── batch_ref_3_budget_100_2038466_10.out
│   ├── batch_ref_3_budget_100_2038466_11.err
│   ├── batch_ref_3_budget_100_2038466_11.out
│   ├── batch_ref_3_budget_100_2038466_12.err
│   ├── batch_ref_3_budget_100_2038466_12.out
│   ├── batch_ref_3_budget_100_2038466_13.err
│   ├── batch_ref_3_budget_100_2038466_13.out
│   ├── batch_ref_3_budget_100_2038466_14.err
│   ├── batch_ref_3_budget_100_2038466_14.out
│   ├── batch_ref_3_budget_100_2038466_15.err
│   ├── batch_ref_3_budget_100_2038466_15.out
│   ├── batch_ref_3_budget_100_2038466_16.err
│   ├── batch_ref_3_budget_100_2038466_16.out
│   ├── batch_ref_3_budget_100_2038466_17.err
│   ├── batch_ref_3_budget_100_2038466_17.out
│   ├── batch_ref_3_budget_100_2038466_18.err
│   ├── batch_ref_3_budget_100_2038466_18.out
│   ├── batch_ref_3_budget_100_2038466_19.err
│   ├── batch_ref_3_budget_100_2038466_19.out
│   ├── batch_ref_3_budget_100_2038466_2.err
│   ├── batch_ref_3_budget_100_2038466_2.out
│   ├── batch_ref_3_budget_100_2038466_20.err
│   ├── batch_ref_3_budget_100_2038466_20.out
│   ├── batch_ref_3_budget_100_2038466_21.err
│   ├── batch_ref_3_budget_100_2038466_21.out
│   ├── batch_ref_3_budget_100_2038466_22.err
│   ├── batch_ref_3_budget_100_2038466_22.out
│   ├── batch_ref_3_budget_100_2038466_23.err
│   ├── batch_ref_3_budget_100_2038466_23.out
│   ├── batch_ref_3_budget_100_2038466_24.err
│   ├── batch_ref_3_budget_100_2038466_24.out
│   ├── batch_ref_3_budget_100_2038466_25.err
│   ├── batch_ref_3_budget_100_2038466_25.out
│   ├── batch_ref_3_budget_100_2038466_26.err
│   ├── batch_ref_3_budget_100_2038466_26.out
│   ├── batch_ref_3_budget_100_2038466_27.err
│   ├── batch_ref_3_budget_100_2038466_27.out
│   ├── batch_ref_3_budget_100_2038466_28.err
│   ├── batch_ref_3_budget_100_2038466_28.out
│   ├── batch_ref_3_budget_100_2038466_29.err
│   ├── batch_ref_3_budget_100_2038466_29.out
│   ├── batch_ref_3_budget_100_2038466_3.err
│   ├── batch_ref_3_budget_100_2038466_3.out
│   ├── batch_ref_3_budget_100_2038466_30.err
│   ├── batch_ref_3_budget_100_2038466_30.out
│   ├── batch_ref_3_budget_100_2038466_31.err
│   ├── batch_ref_3_budget_100_2038466_31.out
│   ├── batch_ref_3_budget_100_2038466_32.err
│   ├── batch_ref_3_budget_100_2038466_32.out
│   ├── batch_ref_3_budget_100_2038466_33.err
│   ├── batch_ref_3_budget_100_2038466_33.out
│   ├── batch_ref_3_budget_100_2038466_34.err
│   ├── batch_ref_3_budget_100_2038466_34.out
│   ├── batch_ref_3_budget_100_2038466_35.err
│   ├── batch_ref_3_budget_100_2038466_35.out
│   ├── batch_ref_3_budget_100_2038466_36.err
│   ├── batch_ref_3_budget_100_2038466_36.out
│   ├── batch_ref_3_budget_100_2038466_37.err
│   ├── batch_ref_3_budget_100_2038466_37.out
│   ├── batch_ref_3_budget_100_2038466_38.err
│   ├── batch_ref_3_budget_100_2038466_38.out
│   ├── batch_ref_3_budget_100_2038466_39.err
│   ├── batch_ref_3_budget_100_2038466_39.out
│   ├── batch_ref_3_budget_100_2038466_4.err
│   ├── batch_ref_3_budget_100_2038466_4.out
│   ├── batch_ref_3_budget_100_2038466_40.err
│   ├── batch_ref_3_budget_100_2038466_40.out
│   ├── batch_ref_3_budget_100_2038466_41.err
│   ├── batch_ref_3_budget_100_2038466_41.out
│   ├── batch_ref_3_budget_100_2038466_42.err
│   ├── batch_ref_3_budget_100_2038466_42.out
│   ├── batch_ref_3_budget_100_2038466_43.err
│   ├── batch_ref_3_budget_100_2038466_43.out
│   ├── batch_ref_3_budget_100_2038466_44.err
│   ├── batch_ref_3_budget_100_2038466_44.out
│   ├── batch_ref_3_budget_100_2038466_45.err
│   ├── batch_ref_3_budget_100_2038466_45.out
│   ├── batch_ref_3_budget_100_2038466_46.err
│   ├── batch_ref_3_budget_100_2038466_46.out
│   ├── batch_ref_3_budget_100_2038466_47.err
│   ├── batch_ref_3_budget_100_2038466_47.out
│   ├── batch_ref_3_budget_100_2038466_48.err
│   ├── batch_ref_3_budget_100_2038466_48.out
│   ├── batch_ref_3_budget_100_2038466_49.err
│   ├── batch_ref_3_budget_100_2038466_49.out
│   ├── batch_ref_3_budget_100_2038466_5.err
│   ├── batch_ref_3_budget_100_2038466_5.out
│   ├── batch_ref_3_budget_100_2038466_50.err
│   ├── batch_ref_3_budget_100_2038466_50.out
│   ├── batch_ref_3_budget_100_2038466_51.err
│   ├── batch_ref_3_budget_100_2038466_51.out
│   ├── batch_ref_3_budget_100_2038466_52.err
│   ├── batch_ref_3_budget_100_2038466_52.out
│   ├── batch_ref_3_budget_100_2038466_53.err
│   ├── batch_ref_3_budget_100_2038466_53.out
│   ├── batch_ref_3_budget_100_2038466_54.err
│   ├── batch_ref_3_budget_100_2038466_54.out
│   ├── batch_ref_3_budget_100_2038466_55.err
│   ├── batch_ref_3_budget_100_2038466_55.out
│   ├── batch_ref_3_budget_100_2038466_56.err
│   ├── batch_ref_3_budget_100_2038466_56.out
│   ├── batch_ref_3_budget_100_2038466_57.err
│   ├── batch_ref_3_budget_100_2038466_57.out
│   ├── batch_ref_3_budget_100_2038466_58.err
│   ├── batch_ref_3_budget_100_2038466_58.out
│   ├── batch_ref_3_budget_100_2038466_59.err
│   ├── batch_ref_3_budget_100_2038466_59.out
│   ├── batch_ref_3_budget_100_2038466_6.err
│   ├── batch_ref_3_budget_100_2038466_6.out
│   ├── batch_ref_3_budget_100_2038466_60.err
│   ├── batch_ref_3_budget_100_2038466_60.out
│   ├── batch_ref_3_budget_100_2038466_61.err
│   ├── batch_ref_3_budget_100_2038466_61.out
│   ├── batch_ref_3_budget_100_2038466_62.err
│   ├── batch_ref_3_budget_100_2038466_62.out
│   ├── batch_ref_3_budget_100_2038466_63.err
│   ├── batch_ref_3_budget_100_2038466_63.out
│   ├── batch_ref_3_budget_100_2038466_64.err
│   ├── batch_ref_3_budget_100_2038466_64.out
│   ├── batch_ref_3_budget_100_2038466_65.err
│   ├── batch_ref_3_budget_100_2038466_65.out
│   ├── batch_ref_3_budget_100_2038466_66.err
│   ├── batch_ref_3_budget_100_2038466_66.out
│   ├── batch_ref_3_budget_100_2038466_67.err
│   ├── batch_ref_3_budget_100_2038466_67.out
│   ├── batch_ref_3_budget_100_2038466_68.err
│   ├── batch_ref_3_budget_100_2038466_68.out
│   ├── batch_ref_3_budget_100_2038466_69.err
│   ├── batch_ref_3_budget_100_2038466_69.out
│   ├── batch_ref_3_budget_100_2038466_7.err
│   ├── batch_ref_3_budget_100_2038466_7.out
│   ├── batch_ref_3_budget_100_2038466_70.err
│   ├── batch_ref_3_budget_100_2038466_70.out
│   ├── batch_ref_3_budget_100_2038466_71.err
│   ├── batch_ref_3_budget_100_2038466_71.out
│   ├── batch_ref_3_budget_100_2038466_72.err
│   ├── batch_ref_3_budget_100_2038466_72.out
│   ├── batch_ref_3_budget_100_2038466_73.err
│   ├── batch_ref_3_budget_100_2038466_73.out
│   ├── batch_ref_3_budget_100_2038466_74.err
│   ├── batch_ref_3_budget_100_2038466_74.out
│   ├── batch_ref_3_budget_100_2038466_75.err
│   ├── batch_ref_3_budget_100_2038466_75.out
│   ├── batch_ref_3_budget_100_2038466_76.err
│   ├── batch_ref_3_budget_100_2038466_76.out
│   ├── batch_ref_3_budget_100_2038466_77.err
│   ├── batch_ref_3_budget_100_2038466_77.out
│   ├── batch_ref_3_budget_100_2038466_78.err
│   ├── batch_ref_3_budget_100_2038466_78.out
│   ├── batch_ref_3_budget_100_2038466_79.err
│   ├── batch_ref_3_budget_100_2038466_79.out
│   ├── batch_ref_3_budget_100_2038466_8.err
│   ├── batch_ref_3_budget_100_2038466_8.out
│   ├── batch_ref_3_budget_100_2038466_80.err
│   ├── batch_ref_3_budget_100_2038466_80.out
│   ├── batch_ref_3_budget_100_2038466_81.err
│   ├── batch_ref_3_budget_100_2038466_81.out
│   ├── batch_ref_3_budget_100_2038466_9.err
│   ├── batch_ref_3_budget_100_2038466_9.out
│   ├── batch_ref_3_budget_100_2039811_1.err
│   ├── batch_ref_3_budget_100_2039811_1.out
│   ├── batch_ref_3_budget_100_2039811_10.err
│   ├── batch_ref_3_budget_100_2039811_10.out
│   ├── batch_ref_3_budget_100_2039811_11.err
│   ├── batch_ref_3_budget_100_2039811_11.out
│   ├── batch_ref_3_budget_100_2039811_12.err
│   ├── batch_ref_3_budget_100_2039811_12.out
│   ├── batch_ref_3_budget_100_2039811_13.err
│   ├── batch_ref_3_budget_100_2039811_13.out
│   ├── batch_ref_3_budget_100_2039811_14.err
│   ├── batch_ref_3_budget_100_2039811_14.out
│   ├── batch_ref_3_budget_100_2039811_15.err
│   ├── batch_ref_3_budget_100_2039811_15.out
│   ├── batch_ref_3_budget_100_2039811_16.err
│   ├── batch_ref_3_budget_100_2039811_16.out
│   ├── batch_ref_3_budget_100_2039811_17.err
│   ├── batch_ref_3_budget_100_2039811_17.out
│   ├── batch_ref_3_budget_100_2039811_18.err
│   ├── batch_ref_3_budget_100_2039811_18.out
│   ├── batch_ref_3_budget_100_2039811_19.err
│   ├── batch_ref_3_budget_100_2039811_19.out
│   ├── batch_ref_3_budget_100_2039811_2.err
│   ├── batch_ref_3_budget_100_2039811_2.out
│   ├── batch_ref_3_budget_100_2039811_20.err
│   ├── batch_ref_3_budget_100_2039811_20.out
│   ├── batch_ref_3_budget_100_2039811_21.err
│   ├── batch_ref_3_budget_100_2039811_21.out
│   ├── batch_ref_3_budget_100_2039811_22.err
│   ├── batch_ref_3_budget_100_2039811_22.out
│   ├── batch_ref_3_budget_100_2039811_23.err
│   ├── batch_ref_3_budget_100_2039811_23.out
│   ├── batch_ref_3_budget_100_2039811_24.err
│   ├── batch_ref_3_budget_100_2039811_24.out
│   ├── batch_ref_3_budget_100_2039811_25.err
│   ├── batch_ref_3_budget_100_2039811_25.out
│   ├── batch_ref_3_budget_100_2039811_26.err
│   ├── batch_ref_3_budget_100_2039811_26.out
│   ├── batch_ref_3_budget_100_2039811_27.err
│   ├── batch_ref_3_budget_100_2039811_27.out
│   ├── batch_ref_3_budget_100_2039811_28.err
│   ├── batch_ref_3_budget_100_2039811_28.out
│   ├── batch_ref_3_budget_100_2039811_29.err
│   ├── batch_ref_3_budget_100_2039811_29.out
│   ├── batch_ref_3_budget_100_2039811_3.err
│   ├── batch_ref_3_budget_100_2039811_3.out
│   ├── batch_ref_3_budget_100_2039811_30.err
│   ├── batch_ref_3_budget_100_2039811_30.out
│   ├── batch_ref_3_budget_100_2039811_31.err
│   ├── batch_ref_3_budget_100_2039811_31.out
│   ├── batch_ref_3_budget_100_2039811_32.err
│   ├── batch_ref_3_budget_100_2039811_32.out
│   ├── batch_ref_3_budget_100_2039811_33.err
│   ├── batch_ref_3_budget_100_2039811_33.out
│   ├── batch_ref_3_budget_100_2039811_34.err
│   ├── batch_ref_3_budget_100_2039811_34.out
│   ├── batch_ref_3_budget_100_2039811_35.err
│   ├── batch_ref_3_budget_100_2039811_35.out
│   ├── batch_ref_3_budget_100_2039811_36.err
│   ├── batch_ref_3_budget_100_2039811_36.out
│   ├── batch_ref_3_budget_100_2039811_37.err
│   ├── batch_ref_3_budget_100_2039811_37.out
│   ├── batch_ref_3_budget_100_2039811_38.err
│   ├── batch_ref_3_budget_100_2039811_38.out
│   ├── batch_ref_3_budget_100_2039811_39.err
│   ├── batch_ref_3_budget_100_2039811_39.out
│   ├── batch_ref_3_budget_100_2039811_4.err
│   ├── batch_ref_3_budget_100_2039811_4.out
│   ├── batch_ref_3_budget_100_2039811_40.err
│   ├── batch_ref_3_budget_100_2039811_40.out
│   ├── batch_ref_3_budget_100_2039811_41.err
│   ├── batch_ref_3_budget_100_2039811_41.out
│   ├── batch_ref_3_budget_100_2039811_42.err
│   ├── batch_ref_3_budget_100_2039811_42.out
│   ├── batch_ref_3_budget_100_2039811_43.err
│   ├── batch_ref_3_budget_100_2039811_43.out
│   ├── batch_ref_3_budget_100_2039811_44.err
│   ├── batch_ref_3_budget_100_2039811_44.out
│   ├── batch_ref_3_budget_100_2039811_45.err
│   ├── batch_ref_3_budget_100_2039811_45.out
│   ├── batch_ref_3_budget_100_2039811_46.err
│   ├── batch_ref_3_budget_100_2039811_46.out
│   ├── batch_ref_3_budget_100_2039811_47.err
│   ├── batch_ref_3_budget_100_2039811_47.out
│   ├── batch_ref_3_budget_100_2039811_48.err
│   ├── batch_ref_3_budget_100_2039811_48.out
│   ├── batch_ref_3_budget_100_2039811_49.err
│   ├── batch_ref_3_budget_100_2039811_49.out
│   ├── batch_ref_3_budget_100_2039811_5.err
│   ├── batch_ref_3_budget_100_2039811_5.out
│   ├── batch_ref_3_budget_100_2039811_50.err
│   ├── batch_ref_3_budget_100_2039811_50.out
│   ├── batch_ref_3_budget_100_2039811_51.err
│   ├── batch_ref_3_budget_100_2039811_51.out
│   ├── batch_ref_3_budget_100_2039811_52.err
│   ├── batch_ref_3_budget_100_2039811_52.out
│   ├── batch_ref_3_budget_100_2039811_53.err
│   ├── batch_ref_3_budget_100_2039811_53.out
│   ├── batch_ref_3_budget_100_2039811_54.err
│   ├── batch_ref_3_budget_100_2039811_54.out
│   ├── batch_ref_3_budget_100_2039811_55.err
│   ├── batch_ref_3_budget_100_2039811_55.out
│   ├── batch_ref_3_budget_100_2039811_56.err
│   ├── batch_ref_3_budget_100_2039811_56.out
│   ├── batch_ref_3_budget_100_2039811_57.err
│   ├── batch_ref_3_budget_100_2039811_57.out
│   ├── batch_ref_3_budget_100_2039811_58.err
│   ├── batch_ref_3_budget_100_2039811_58.out
│   ├── batch_ref_3_budget_100_2039811_59.err
│   ├── batch_ref_3_budget_100_2039811_59.out
│   ├── batch_ref_3_budget_100_2039811_6.err
│   ├── batch_ref_3_budget_100_2039811_6.out
│   ├── batch_ref_3_budget_100_2039811_60.err
│   ├── batch_ref_3_budget_100_2039811_60.out
│   ├── batch_ref_3_budget_100_2039811_61.err
│   ├── batch_ref_3_budget_100_2039811_61.out
│   ├── batch_ref_3_budget_100_2039811_62.err
│   ├── batch_ref_3_budget_100_2039811_62.out
│   ├── batch_ref_3_budget_100_2039811_63.err
│   ├── batch_ref_3_budget_100_2039811_63.out
│   ├── batch_ref_3_budget_100_2039811_64.err
│   ├── batch_ref_3_budget_100_2039811_64.out
│   ├── batch_ref_3_budget_100_2039811_65.err
│   ├── batch_ref_3_budget_100_2039811_65.out
│   ├── batch_ref_3_budget_100_2039811_66.err
│   ├── batch_ref_3_budget_100_2039811_66.out
│   ├── batch_ref_3_budget_100_2039811_67.err
│   ├── batch_ref_3_budget_100_2039811_67.out
│   ├── batch_ref_3_budget_100_2039811_68.err
│   ├── batch_ref_3_budget_100_2039811_68.out
│   ├── batch_ref_3_budget_100_2039811_69.err
│   ├── batch_ref_3_budget_100_2039811_69.out
│   ├── batch_ref_3_budget_100_2039811_7.err
│   ├── batch_ref_3_budget_100_2039811_7.out
│   ├── batch_ref_3_budget_100_2039811_70.err
│   ├── batch_ref_3_budget_100_2039811_70.out
│   ├── batch_ref_3_budget_100_2039811_71.err
│   ├── batch_ref_3_budget_100_2039811_71.out
│   ├── batch_ref_3_budget_100_2039811_72.err
│   ├── batch_ref_3_budget_100_2039811_72.out
│   ├── batch_ref_3_budget_100_2039811_73.err
│   ├── batch_ref_3_budget_100_2039811_73.out
│   ├── batch_ref_3_budget_100_2039811_74.err
│   ├── batch_ref_3_budget_100_2039811_74.out
│   ├── batch_ref_3_budget_100_2039811_75.err
│   ├── batch_ref_3_budget_100_2039811_75.out
│   ├── batch_ref_3_budget_100_2039811_76.err
│   ├── batch_ref_3_budget_100_2039811_76.out
│   ├── batch_ref_3_budget_100_2039811_77.err
│   ├── batch_ref_3_budget_100_2039811_77.out
│   ├── batch_ref_3_budget_100_2039811_78.err
│   ├── batch_ref_3_budget_100_2039811_78.out
│   ├── batch_ref_3_budget_100_2039811_79.err
│   ├── batch_ref_3_budget_100_2039811_79.out
│   ├── batch_ref_3_budget_100_2039811_8.err
│   ├── batch_ref_3_budget_100_2039811_8.out
│   ├── batch_ref_3_budget_100_2039811_80.err
│   ├── batch_ref_3_budget_100_2039811_80.out
│   ├── batch_ref_3_budget_100_2039811_81.err
│   ├── batch_ref_3_budget_100_2039811_81.out
│   ├── batch_ref_3_budget_100_2039811_9.err
│   ├── batch_ref_3_budget_100_2039811_9.out
│   ├── batch_ref_3_budget_150_2038467_1.err
│   ├── batch_ref_3_budget_150_2038467_1.out
│   ├── batch_ref_3_budget_150_2038467_10.err
│   ├── batch_ref_3_budget_150_2038467_10.out
│   ├── batch_ref_3_budget_150_2038467_11.err
│   ├── batch_ref_3_budget_150_2038467_11.out
│   ├── batch_ref_3_budget_150_2038467_12.err
│   ├── batch_ref_3_budget_150_2038467_12.out
│   ├── batch_ref_3_budget_150_2038467_13.err
│   ├── batch_ref_3_budget_150_2038467_13.out
│   ├── batch_ref_3_budget_150_2038467_14.err
│   ├── batch_ref_3_budget_150_2038467_14.out
│   ├── batch_ref_3_budget_150_2038467_15.err
│   ├── batch_ref_3_budget_150_2038467_15.out
│   ├── batch_ref_3_budget_150_2038467_16.err
│   ├── batch_ref_3_budget_150_2038467_16.out
│   ├── batch_ref_3_budget_150_2038467_17.err
│   ├── batch_ref_3_budget_150_2038467_17.out
│   ├── batch_ref_3_budget_150_2038467_18.err
│   ├── batch_ref_3_budget_150_2038467_18.out
│   ├── batch_ref_3_budget_150_2038467_19.err
│   ├── batch_ref_3_budget_150_2038467_19.out
│   ├── batch_ref_3_budget_150_2038467_2.err
│   ├── batch_ref_3_budget_150_2038467_2.out
│   ├── batch_ref_3_budget_150_2038467_20.err
│   ├── batch_ref_3_budget_150_2038467_20.out
│   ├── batch_ref_3_budget_150_2038467_21.err
│   ├── batch_ref_3_budget_150_2038467_21.out
│   ├── batch_ref_3_budget_150_2038467_22.err
│   ├── batch_ref_3_budget_150_2038467_22.out
│   ├── batch_ref_3_budget_150_2038467_23.err
│   ├── batch_ref_3_budget_150_2038467_23.out
│   ├── batch_ref_3_budget_150_2038467_24.err
│   ├── batch_ref_3_budget_150_2038467_24.out
│   ├── batch_ref_3_budget_150_2038467_25.err
│   ├── batch_ref_3_budget_150_2038467_25.out
│   ├── batch_ref_3_budget_150_2038467_26.err
│   ├── batch_ref_3_budget_150_2038467_26.out
│   ├── batch_ref_3_budget_150_2038467_27.err
│   ├── batch_ref_3_budget_150_2038467_27.out
│   ├── batch_ref_3_budget_150_2038467_28.err
│   ├── batch_ref_3_budget_150_2038467_28.out
│   ├── batch_ref_3_budget_150_2038467_29.err
│   ├── batch_ref_3_budget_150_2038467_29.out
│   ├── batch_ref_3_budget_150_2038467_3.err
│   ├── batch_ref_3_budget_150_2038467_3.out
│   ├── batch_ref_3_budget_150_2038467_30.err
│   ├── batch_ref_3_budget_150_2038467_30.out
│   ├── batch_ref_3_budget_150_2038467_31.err
│   ├── batch_ref_3_budget_150_2038467_31.out
│   ├── batch_ref_3_budget_150_2038467_32.err
│   ├── batch_ref_3_budget_150_2038467_32.out
│   ├── batch_ref_3_budget_150_2038467_33.err
│   ├── batch_ref_3_budget_150_2038467_33.out
│   ├── batch_ref_3_budget_150_2038467_34.err
│   ├── batch_ref_3_budget_150_2038467_34.out
│   ├── batch_ref_3_budget_150_2038467_35.err
│   ├── batch_ref_3_budget_150_2038467_35.out
│   ├── batch_ref_3_budget_150_2038467_36.err
│   ├── batch_ref_3_budget_150_2038467_36.out
│   ├── batch_ref_3_budget_150_2038467_37.err
│   ├── batch_ref_3_budget_150_2038467_37.out
│   ├── batch_ref_3_budget_150_2038467_38.err
│   ├── batch_ref_3_budget_150_2038467_38.out
│   ├── batch_ref_3_budget_150_2038467_39.err
│   ├── batch_ref_3_budget_150_2038467_39.out
│   ├── batch_ref_3_budget_150_2038467_4.err
│   ├── batch_ref_3_budget_150_2038467_4.out
│   ├── batch_ref_3_budget_150_2038467_40.err
│   ├── batch_ref_3_budget_150_2038467_40.out
│   ├── batch_ref_3_budget_150_2038467_41.err
│   ├── batch_ref_3_budget_150_2038467_41.out
│   ├── batch_ref_3_budget_150_2038467_42.err
│   ├── batch_ref_3_budget_150_2038467_42.out
│   ├── batch_ref_3_budget_150_2038467_43.err
│   ├── batch_ref_3_budget_150_2038467_43.out
│   ├── batch_ref_3_budget_150_2038467_44.err
│   ├── batch_ref_3_budget_150_2038467_44.out
│   ├── batch_ref_3_budget_150_2038467_45.err
│   ├── batch_ref_3_budget_150_2038467_45.out
│   ├── batch_ref_3_budget_150_2038467_46.err
│   ├── batch_ref_3_budget_150_2038467_46.out
│   ├── batch_ref_3_budget_150_2038467_47.err
│   ├── batch_ref_3_budget_150_2038467_47.out
│   ├── batch_ref_3_budget_150_2038467_48.err
│   ├── batch_ref_3_budget_150_2038467_48.out
│   ├── batch_ref_3_budget_150_2038467_49.err
│   ├── batch_ref_3_budget_150_2038467_49.out
│   ├── batch_ref_3_budget_150_2038467_5.err
│   ├── batch_ref_3_budget_150_2038467_5.out
│   ├── batch_ref_3_budget_150_2038467_50.err
│   ├── batch_ref_3_budget_150_2038467_50.out
│   ├── batch_ref_3_budget_150_2038467_51.err
│   ├── batch_ref_3_budget_150_2038467_51.out
│   ├── batch_ref_3_budget_150_2038467_52.err
│   ├── batch_ref_3_budget_150_2038467_52.out
│   ├── batch_ref_3_budget_150_2038467_53.err
│   ├── batch_ref_3_budget_150_2038467_53.out
│   ├── batch_ref_3_budget_150_2038467_54.err
│   ├── batch_ref_3_budget_150_2038467_54.out
│   ├── batch_ref_3_budget_150_2038467_55.err
│   ├── batch_ref_3_budget_150_2038467_55.out
│   ├── batch_ref_3_budget_150_2038467_56.err
│   ├── batch_ref_3_budget_150_2038467_56.out
│   ├── batch_ref_3_budget_150_2038467_57.err
│   ├── batch_ref_3_budget_150_2038467_57.out
│   ├── batch_ref_3_budget_150_2038467_58.err
│   ├── batch_ref_3_budget_150_2038467_58.out
│   ├── batch_ref_3_budget_150_2038467_59.err
│   ├── batch_ref_3_budget_150_2038467_59.out
│   ├── batch_ref_3_budget_150_2038467_6.err
│   ├── batch_ref_3_budget_150_2038467_6.out
│   ├── batch_ref_3_budget_150_2038467_60.err
│   ├── batch_ref_3_budget_150_2038467_60.out
│   ├── batch_ref_3_budget_150_2038467_61.err
│   ├── batch_ref_3_budget_150_2038467_61.out
│   ├── batch_ref_3_budget_150_2038467_62.err
│   ├── batch_ref_3_budget_150_2038467_62.out
│   ├── batch_ref_3_budget_150_2038467_63.err
│   ├── batch_ref_3_budget_150_2038467_63.out
│   ├── batch_ref_3_budget_150_2038467_64.err
│   ├── batch_ref_3_budget_150_2038467_64.out
│   ├── batch_ref_3_budget_150_2038467_65.err
│   ├── batch_ref_3_budget_150_2038467_65.out
│   ├── batch_ref_3_budget_150_2038467_66.err
│   ├── batch_ref_3_budget_150_2038467_66.out
│   ├── batch_ref_3_budget_150_2038467_67.err
│   ├── batch_ref_3_budget_150_2038467_67.out
│   ├── batch_ref_3_budget_150_2038467_68.err
│   ├── batch_ref_3_budget_150_2038467_68.out
│   ├── batch_ref_3_budget_150_2038467_69.err
│   ├── batch_ref_3_budget_150_2038467_69.out
│   ├── batch_ref_3_budget_150_2038467_7.err
│   ├── batch_ref_3_budget_150_2038467_7.out
│   ├── batch_ref_3_budget_150_2038467_70.err
│   ├── batch_ref_3_budget_150_2038467_70.out
│   ├── batch_ref_3_budget_150_2038467_71.err
│   ├── batch_ref_3_budget_150_2038467_71.out
│   ├── batch_ref_3_budget_150_2038467_72.err
│   ├── batch_ref_3_budget_150_2038467_72.out
│   ├── batch_ref_3_budget_150_2038467_73.err
│   ├── batch_ref_3_budget_150_2038467_73.out
│   ├── batch_ref_3_budget_150_2038467_74.err
│   ├── batch_ref_3_budget_150_2038467_74.out
│   ├── batch_ref_3_budget_150_2038467_75.err
│   ├── batch_ref_3_budget_150_2038467_75.out
│   ├── batch_ref_3_budget_150_2038467_76.err
│   ├── batch_ref_3_budget_150_2038467_76.out
│   ├── batch_ref_3_budget_150_2038467_77.err
│   ├── batch_ref_3_budget_150_2038467_77.out
│   ├── batch_ref_3_budget_150_2038467_78.err
│   ├── batch_ref_3_budget_150_2038467_78.out
│   ├── batch_ref_3_budget_150_2038467_79.err
│   ├── batch_ref_3_budget_150_2038467_79.out
│   ├── batch_ref_3_budget_150_2038467_8.err
│   ├── batch_ref_3_budget_150_2038467_8.out
│   ├── batch_ref_3_budget_150_2038467_80.err
│   ├── batch_ref_3_budget_150_2038467_80.out
│   ├── batch_ref_3_budget_150_2038467_81.err
│   ├── batch_ref_3_budget_150_2038467_81.out
│   ├── batch_ref_3_budget_150_2038467_9.err
│   ├── batch_ref_3_budget_150_2038467_9.out
│   ├── batch_ref_3_budget_150_2040017_1.err
│   ├── batch_ref_3_budget_150_2040017_1.out
│   ├── batch_ref_3_budget_150_2040017_10.err
│   ├── batch_ref_3_budget_150_2040017_10.out
│   ├── batch_ref_3_budget_150_2040017_11.err
│   ├── batch_ref_3_budget_150_2040017_11.out
│   ├── batch_ref_3_budget_150_2040017_12.err
│   ├── batch_ref_3_budget_150_2040017_12.out
│   ├── batch_ref_3_budget_150_2040017_13.err
│   ├── batch_ref_3_budget_150_2040017_13.out
│   ├── batch_ref_3_budget_150_2040017_14.err
│   ├── batch_ref_3_budget_150_2040017_14.out
│   ├── batch_ref_3_budget_150_2040017_15.err
│   ├── batch_ref_3_budget_150_2040017_15.out
│   ├── batch_ref_3_budget_150_2040017_16.err
│   ├── batch_ref_3_budget_150_2040017_16.out
│   ├── batch_ref_3_budget_150_2040017_17.err
│   ├── batch_ref_3_budget_150_2040017_17.out
│   ├── batch_ref_3_budget_150_2040017_18.err
│   ├── batch_ref_3_budget_150_2040017_18.out
│   ├── batch_ref_3_budget_150_2040017_19.err
│   ├── batch_ref_3_budget_150_2040017_19.out
│   ├── batch_ref_3_budget_150_2040017_2.err
│   ├── batch_ref_3_budget_150_2040017_2.out
│   ├── batch_ref_3_budget_150_2040017_20.err
│   ├── batch_ref_3_budget_150_2040017_20.out
│   ├── batch_ref_3_budget_150_2040017_21.err
│   ├── batch_ref_3_budget_150_2040017_21.out
│   ├── batch_ref_3_budget_150_2040017_22.err
│   ├── batch_ref_3_budget_150_2040017_22.out
│   ├── batch_ref_3_budget_150_2040017_23.err
│   ├── batch_ref_3_budget_150_2040017_23.out
│   ├── batch_ref_3_budget_150_2040017_24.err
│   ├── batch_ref_3_budget_150_2040017_24.out
│   ├── batch_ref_3_budget_150_2040017_25.err
│   ├── batch_ref_3_budget_150_2040017_25.out
│   ├── batch_ref_3_budget_150_2040017_26.err
│   ├── batch_ref_3_budget_150_2040017_26.out
│   ├── batch_ref_3_budget_150_2040017_27.err
│   ├── batch_ref_3_budget_150_2040017_27.out
│   ├── batch_ref_3_budget_150_2040017_28.err
│   ├── batch_ref_3_budget_150_2040017_28.out
│   ├── batch_ref_3_budget_150_2040017_29.err
│   ├── batch_ref_3_budget_150_2040017_29.out
│   ├── batch_ref_3_budget_150_2040017_3.err
│   ├── batch_ref_3_budget_150_2040017_3.out
│   ├── batch_ref_3_budget_150_2040017_30.err
│   ├── batch_ref_3_budget_150_2040017_30.out
│   ├── batch_ref_3_budget_150_2040017_31.err
│   ├── batch_ref_3_budget_150_2040017_31.out
│   ├── batch_ref_3_budget_150_2040017_32.err
│   ├── batch_ref_3_budget_150_2040017_32.out
│   ├── batch_ref_3_budget_150_2040017_33.err
│   ├── batch_ref_3_budget_150_2040017_33.out
│   ├── batch_ref_3_budget_150_2040017_34.err
│   ├── batch_ref_3_budget_150_2040017_34.out
│   ├── batch_ref_3_budget_150_2040017_35.err
│   ├── batch_ref_3_budget_150_2040017_35.out
│   ├── batch_ref_3_budget_150_2040017_36.err
│   ├── batch_ref_3_budget_150_2040017_36.out
│   ├── batch_ref_3_budget_150_2040017_37.err
│   ├── batch_ref_3_budget_150_2040017_37.out
│   ├── batch_ref_3_budget_150_2040017_38.err
│   ├── batch_ref_3_budget_150_2040017_38.out
│   ├── batch_ref_3_budget_150_2040017_39.err
│   ├── batch_ref_3_budget_150_2040017_39.out
│   ├── batch_ref_3_budget_150_2040017_4.err
│   ├── batch_ref_3_budget_150_2040017_4.out
│   ├── batch_ref_3_budget_150_2040017_40.err
│   ├── batch_ref_3_budget_150_2040017_40.out
│   ├── batch_ref_3_budget_150_2040017_41.err
│   ├── batch_ref_3_budget_150_2040017_41.out
│   ├── batch_ref_3_budget_150_2040017_42.err
│   ├── batch_ref_3_budget_150_2040017_42.out
│   ├── batch_ref_3_budget_150_2040017_43.err
│   ├── batch_ref_3_budget_150_2040017_43.out
│   ├── batch_ref_3_budget_150_2040017_44.err
│   ├── batch_ref_3_budget_150_2040017_44.out
│   ├── batch_ref_3_budget_150_2040017_45.err
│   ├── batch_ref_3_budget_150_2040017_45.out
│   ├── batch_ref_3_budget_150_2040017_46.err
│   ├── batch_ref_3_budget_150_2040017_46.out
│   ├── batch_ref_3_budget_150_2040017_47.err
│   ├── batch_ref_3_budget_150_2040017_47.out
│   ├── batch_ref_3_budget_150_2040017_48.err
│   ├── batch_ref_3_budget_150_2040017_48.out
│   ├── batch_ref_3_budget_150_2040017_49.err
│   ├── batch_ref_3_budget_150_2040017_49.out
│   ├── batch_ref_3_budget_150_2040017_5.err
│   ├── batch_ref_3_budget_150_2040017_5.out
│   ├── batch_ref_3_budget_150_2040017_50.err
│   ├── batch_ref_3_budget_150_2040017_50.out
│   ├── batch_ref_3_budget_150_2040017_51.err
│   ├── batch_ref_3_budget_150_2040017_51.out
│   ├── batch_ref_3_budget_150_2040017_52.err
│   ├── batch_ref_3_budget_150_2040017_52.out
│   ├── batch_ref_3_budget_150_2040017_53.err
│   ├── batch_ref_3_budget_150_2040017_53.out
│   ├── batch_ref_3_budget_150_2040017_54.err
│   ├── batch_ref_3_budget_150_2040017_54.out
│   ├── batch_ref_3_budget_150_2040017_55.err
│   ├── batch_ref_3_budget_150_2040017_55.out
│   ├── batch_ref_3_budget_150_2040017_56.err
│   ├── batch_ref_3_budget_150_2040017_56.out
│   ├── batch_ref_3_budget_150_2040017_57.err
│   ├── batch_ref_3_budget_150_2040017_57.out
│   ├── batch_ref_3_budget_150_2040017_58.err
│   ├── batch_ref_3_budget_150_2040017_58.out
│   ├── batch_ref_3_budget_150_2040017_59.err
│   ├── batch_ref_3_budget_150_2040017_59.out
│   ├── batch_ref_3_budget_150_2040017_6.err
│   ├── batch_ref_3_budget_150_2040017_6.out
│   ├── batch_ref_3_budget_150_2040017_60.err
│   ├── batch_ref_3_budget_150_2040017_60.out
│   ├── batch_ref_3_budget_150_2040017_61.err
│   ├── batch_ref_3_budget_150_2040017_61.out
│   ├── batch_ref_3_budget_150_2040017_62.err
│   ├── batch_ref_3_budget_150_2040017_62.out
│   ├── batch_ref_3_budget_150_2040017_63.err
│   ├── batch_ref_3_budget_150_2040017_63.out
│   ├── batch_ref_3_budget_150_2040017_64.err
│   ├── batch_ref_3_budget_150_2040017_64.out
│   ├── batch_ref_3_budget_150_2040017_65.err
│   ├── batch_ref_3_budget_150_2040017_65.out
│   ├── batch_ref_3_budget_150_2040017_66.err
│   ├── batch_ref_3_budget_150_2040017_66.out
│   ├── batch_ref_3_budget_150_2040017_67.err
│   ├── batch_ref_3_budget_150_2040017_67.out
│   ├── batch_ref_3_budget_150_2040017_68.err
│   ├── batch_ref_3_budget_150_2040017_68.out
│   ├── batch_ref_3_budget_150_2040017_69.err
│   ├── batch_ref_3_budget_150_2040017_69.out
│   ├── batch_ref_3_budget_150_2040017_7.err
│   ├── batch_ref_3_budget_150_2040017_7.out
│   ├── batch_ref_3_budget_150_2040017_70.err
│   ├── batch_ref_3_budget_150_2040017_70.out
│   ├── batch_ref_3_budget_150_2040017_71.err
│   ├── batch_ref_3_budget_150_2040017_71.out
│   ├── batch_ref_3_budget_150_2040017_72.err
│   ├── batch_ref_3_budget_150_2040017_72.out
│   ├── batch_ref_3_budget_150_2040017_73.err
│   ├── batch_ref_3_budget_150_2040017_73.out
│   ├── batch_ref_3_budget_150_2040017_74.err
│   ├── batch_ref_3_budget_150_2040017_74.out
│   ├── batch_ref_3_budget_150_2040017_75.err
│   ├── batch_ref_3_budget_150_2040017_75.out
│   ├── batch_ref_3_budget_150_2040017_76.err
│   ├── batch_ref_3_budget_150_2040017_76.out
│   ├── batch_ref_3_budget_150_2040017_77.err
│   ├── batch_ref_3_budget_150_2040017_77.out
│   ├── batch_ref_3_budget_150_2040017_78.err
│   ├── batch_ref_3_budget_150_2040017_78.out
│   ├── batch_ref_3_budget_150_2040017_79.err
│   ├── batch_ref_3_budget_150_2040017_79.out
│   ├── batch_ref_3_budget_150_2040017_8.err
│   ├── batch_ref_3_budget_150_2040017_8.out
│   ├── batch_ref_3_budget_150_2040017_80.err
│   ├── batch_ref_3_budget_150_2040017_80.out
│   ├── batch_ref_3_budget_150_2040017_81.err
│   ├── batch_ref_3_budget_150_2040017_81.out
│   ├── batch_ref_3_budget_150_2040017_9.err
│   ├── batch_ref_3_budget_150_2040017_9.out
│   ├── batch_ref_3_budget_200_2040018_1.err
│   ├── batch_ref_3_budget_200_2040018_1.out
│   ├── batch_ref_3_budget_200_2040018_10.err
│   ├── batch_ref_3_budget_200_2040018_10.out
│   ├── batch_ref_3_budget_200_2040018_11.err
│   ├── batch_ref_3_budget_200_2040018_11.out
│   ├── batch_ref_3_budget_200_2040018_12.err
│   ├── batch_ref_3_budget_200_2040018_12.out
│   ├── batch_ref_3_budget_200_2040018_13.err
│   ├── batch_ref_3_budget_200_2040018_13.out
│   ├── batch_ref_3_budget_200_2040018_14.err
│   ├── batch_ref_3_budget_200_2040018_14.out
│   ├── batch_ref_3_budget_200_2040018_15.err
│   ├── batch_ref_3_budget_200_2040018_15.out
│   ├── batch_ref_3_budget_200_2040018_16.err
│   ├── batch_ref_3_budget_200_2040018_16.out
│   ├── batch_ref_3_budget_200_2040018_17.err
│   ├── batch_ref_3_budget_200_2040018_17.out
│   ├── batch_ref_3_budget_200_2040018_18.err
│   ├── batch_ref_3_budget_200_2040018_18.out
│   ├── batch_ref_3_budget_200_2040018_19.err
│   ├── batch_ref_3_budget_200_2040018_19.out
│   ├── batch_ref_3_budget_200_2040018_2.err
│   ├── batch_ref_3_budget_200_2040018_2.out
│   ├── batch_ref_3_budget_200_2040018_20.err
│   ├── batch_ref_3_budget_200_2040018_20.out
│   ├── batch_ref_3_budget_200_2040018_21.err
│   ├── batch_ref_3_budget_200_2040018_21.out
│   ├── batch_ref_3_budget_200_2040018_22.err
│   ├── batch_ref_3_budget_200_2040018_22.out
│   ├── batch_ref_3_budget_200_2040018_23.err
│   ├── batch_ref_3_budget_200_2040018_23.out
│   ├── batch_ref_3_budget_200_2040018_24.err
│   ├── batch_ref_3_budget_200_2040018_24.out
│   ├── batch_ref_3_budget_200_2040018_25.err
│   ├── batch_ref_3_budget_200_2040018_25.out
│   ├── batch_ref_3_budget_200_2040018_26.err
│   ├── batch_ref_3_budget_200_2040018_26.out
│   ├── batch_ref_3_budget_200_2040018_27.err
│   ├── batch_ref_3_budget_200_2040018_27.out
│   ├── batch_ref_3_budget_200_2040018_28.err
│   ├── batch_ref_3_budget_200_2040018_28.out
│   ├── batch_ref_3_budget_200_2040018_29.err
│   ├── batch_ref_3_budget_200_2040018_29.out
│   ├── batch_ref_3_budget_200_2040018_3.err
│   ├── batch_ref_3_budget_200_2040018_3.out
│   ├── batch_ref_3_budget_200_2040018_30.err
│   ├── batch_ref_3_budget_200_2040018_30.out
│   ├── batch_ref_3_budget_200_2040018_31.err
│   ├── batch_ref_3_budget_200_2040018_31.out
│   ├── batch_ref_3_budget_200_2040018_32.err
│   ├── batch_ref_3_budget_200_2040018_32.out
│   ├── batch_ref_3_budget_200_2040018_33.err
│   ├── batch_ref_3_budget_200_2040018_33.out
│   ├── batch_ref_3_budget_200_2040018_34.err
│   ├── batch_ref_3_budget_200_2040018_34.out
│   ├── batch_ref_3_budget_200_2040018_35.err
│   ├── batch_ref_3_budget_200_2040018_35.out
│   ├── batch_ref_3_budget_200_2040018_36.err
│   ├── batch_ref_3_budget_200_2040018_36.out
│   ├── batch_ref_3_budget_200_2040018_37.err
│   ├── batch_ref_3_budget_200_2040018_37.out
│   ├── batch_ref_3_budget_200_2040018_38.err
│   ├── batch_ref_3_budget_200_2040018_38.out
│   ├── batch_ref_3_budget_200_2040018_39.err
│   ├── batch_ref_3_budget_200_2040018_39.out
│   ├── batch_ref_3_budget_200_2040018_4.err
│   ├── batch_ref_3_budget_200_2040018_4.out
│   ├── batch_ref_3_budget_200_2040018_40.err
│   ├── batch_ref_3_budget_200_2040018_40.out
│   ├── batch_ref_3_budget_200_2040018_41.err
│   ├── batch_ref_3_budget_200_2040018_41.out
│   ├── batch_ref_3_budget_200_2040018_42.err
│   ├── batch_ref_3_budget_200_2040018_42.out
│   ├── batch_ref_3_budget_200_2040018_43.err
│   ├── batch_ref_3_budget_200_2040018_43.out
│   ├── batch_ref_3_budget_200_2040018_44.err
│   ├── batch_ref_3_budget_200_2040018_44.out
│   ├── batch_ref_3_budget_200_2040018_45.err
│   ├── batch_ref_3_budget_200_2040018_45.out
│   ├── batch_ref_3_budget_200_2040018_46.err
│   ├── batch_ref_3_budget_200_2040018_46.out
│   ├── batch_ref_3_budget_200_2040018_47.err
│   ├── batch_ref_3_budget_200_2040018_47.out
│   ├── batch_ref_3_budget_200_2040018_48.err
│   ├── batch_ref_3_budget_200_2040018_48.out
│   ├── batch_ref_3_budget_200_2040018_49.err
│   ├── batch_ref_3_budget_200_2040018_49.out
│   ├── batch_ref_3_budget_200_2040018_5.err
│   ├── batch_ref_3_budget_200_2040018_5.out
│   ├── batch_ref_3_budget_200_2040018_50.err
│   ├── batch_ref_3_budget_200_2040018_50.out
│   ├── batch_ref_3_budget_200_2040018_51.err
│   ├── batch_ref_3_budget_200_2040018_51.out
│   ├── batch_ref_3_budget_200_2040018_52.err
│   ├── batch_ref_3_budget_200_2040018_52.out
│   ├── batch_ref_3_budget_200_2040018_53.err
│   ├── batch_ref_3_budget_200_2040018_53.out
│   ├── batch_ref_3_budget_200_2040018_54.err
│   ├── batch_ref_3_budget_200_2040018_54.out
│   ├── batch_ref_3_budget_200_2040018_55.err
│   ├── batch_ref_3_budget_200_2040018_55.out
│   ├── batch_ref_3_budget_200_2040018_56.err
│   ├── batch_ref_3_budget_200_2040018_56.out
│   ├── batch_ref_3_budget_200_2040018_57.err
│   ├── batch_ref_3_budget_200_2040018_57.out
│   ├── batch_ref_3_budget_200_2040018_58.err
│   ├── batch_ref_3_budget_200_2040018_58.out
│   ├── batch_ref_3_budget_200_2040018_59.err
│   ├── batch_ref_3_budget_200_2040018_59.out
│   ├── batch_ref_3_budget_200_2040018_6.err
│   ├── batch_ref_3_budget_200_2040018_6.out
│   ├── batch_ref_3_budget_200_2040018_60.err
│   ├── batch_ref_3_budget_200_2040018_60.out
│   ├── batch_ref_3_budget_200_2040018_61.err
│   ├── batch_ref_3_budget_200_2040018_61.out
│   ├── batch_ref_3_budget_200_2040018_62.err
│   ├── batch_ref_3_budget_200_2040018_62.out
│   ├── batch_ref_3_budget_200_2040018_63.err
│   ├── batch_ref_3_budget_200_2040018_63.out
│   ├── batch_ref_3_budget_200_2040018_64.err
│   ├── batch_ref_3_budget_200_2040018_64.out
│   ├── batch_ref_3_budget_200_2040018_65.err
│   ├── batch_ref_3_budget_200_2040018_65.out
│   ├── batch_ref_3_budget_200_2040018_66.err
│   ├── batch_ref_3_budget_200_2040018_66.out
│   ├── batch_ref_3_budget_200_2040018_67.err
│   ├── batch_ref_3_budget_200_2040018_67.out
│   ├── batch_ref_3_budget_200_2040018_68.err
│   ├── batch_ref_3_budget_200_2040018_68.out
│   ├── batch_ref_3_budget_200_2040018_69.err
│   ├── batch_ref_3_budget_200_2040018_69.out
│   ├── batch_ref_3_budget_200_2040018_7.err
│   ├── batch_ref_3_budget_200_2040018_7.out
│   ├── batch_ref_3_budget_200_2040018_70.err
│   ├── batch_ref_3_budget_200_2040018_70.out
│   ├── batch_ref_3_budget_200_2040018_71.err
│   ├── batch_ref_3_budget_200_2040018_71.out
│   ├── batch_ref_3_budget_200_2040018_72.err
│   ├── batch_ref_3_budget_200_2040018_72.out
│   ├── batch_ref_3_budget_200_2040018_73.err
│   ├── batch_ref_3_budget_200_2040018_73.out
│   ├── batch_ref_3_budget_200_2040018_74.err
│   ├── batch_ref_3_budget_200_2040018_74.out
│   ├── batch_ref_3_budget_200_2040018_75.err
│   ├── batch_ref_3_budget_200_2040018_75.out
│   ├── batch_ref_3_budget_200_2040018_76.err
│   ├── batch_ref_3_budget_200_2040018_76.out
│   ├── batch_ref_3_budget_200_2040018_77.err
│   ├── batch_ref_3_budget_200_2040018_77.out
│   ├── batch_ref_3_budget_200_2040018_78.err
│   ├── batch_ref_3_budget_200_2040018_78.out
│   ├── batch_ref_3_budget_200_2040018_79.err
│   ├── batch_ref_3_budget_200_2040018_79.out
│   ├── batch_ref_3_budget_200_2040018_8.err
│   ├── batch_ref_3_budget_200_2040018_8.out
│   ├── batch_ref_3_budget_200_2040018_80.err
│   ├── batch_ref_3_budget_200_2040018_80.out
│   ├── batch_ref_3_budget_200_2040018_81.err
│   ├── batch_ref_3_budget_200_2040018_81.out
│   ├── batch_ref_3_budget_200_2040018_9.err
│   ├── batch_ref_3_budget_200_2040018_9.out
│   ├── batch_ref_3_budget_50_2004681_1.err
│   ├── batch_ref_3_budget_50_2004681_1.out
│   ├── batch_ref_3_budget_50_2004681_10.err
│   ├── batch_ref_3_budget_50_2004681_10.out
│   ├── batch_ref_3_budget_50_2004681_11.err
│   ├── batch_ref_3_budget_50_2004681_11.out
│   ├── batch_ref_3_budget_50_2004681_12.err
│   ├── batch_ref_3_budget_50_2004681_12.out
│   ├── batch_ref_3_budget_50_2004681_13.err
│   ├── batch_ref_3_budget_50_2004681_13.out
│   ├── batch_ref_3_budget_50_2004681_14.err
│   ├── batch_ref_3_budget_50_2004681_14.out
│   ├── batch_ref_3_budget_50_2004681_15.err
│   ├── batch_ref_3_budget_50_2004681_15.out
│   ├── batch_ref_3_budget_50_2004681_16.err
│   ├── batch_ref_3_budget_50_2004681_16.out
│   ├── batch_ref_3_budget_50_2004681_17.err
│   ├── batch_ref_3_budget_50_2004681_17.out
│   ├── batch_ref_3_budget_50_2004681_18.err
│   ├── batch_ref_3_budget_50_2004681_18.out
│   ├── batch_ref_3_budget_50_2004681_19.err
│   ├── batch_ref_3_budget_50_2004681_19.out
│   ├── batch_ref_3_budget_50_2004681_2.err
│   ├── batch_ref_3_budget_50_2004681_2.out
│   ├── batch_ref_3_budget_50_2004681_20.err
│   ├── batch_ref_3_budget_50_2004681_20.out
│   ├── batch_ref_3_budget_50_2004681_21.err
│   ├── batch_ref_3_budget_50_2004681_21.out
│   ├── batch_ref_3_budget_50_2004681_22.err
│   ├── batch_ref_3_budget_50_2004681_22.out
│   ├── batch_ref_3_budget_50_2004681_23.err
│   ├── batch_ref_3_budget_50_2004681_23.out
│   ├── batch_ref_3_budget_50_2004681_24.err
│   ├── batch_ref_3_budget_50_2004681_24.out
│   ├── batch_ref_3_budget_50_2004681_25.err
│   ├── batch_ref_3_budget_50_2004681_25.out
│   ├── batch_ref_3_budget_50_2004681_26.err
│   ├── batch_ref_3_budget_50_2004681_26.out
│   ├── batch_ref_3_budget_50_2004681_27.err
│   ├── batch_ref_3_budget_50_2004681_27.out
│   ├── batch_ref_3_budget_50_2004681_28.err
│   ├── batch_ref_3_budget_50_2004681_28.out
│   ├── batch_ref_3_budget_50_2004681_29.err
│   ├── batch_ref_3_budget_50_2004681_29.out
│   ├── batch_ref_3_budget_50_2004681_3.err
│   ├── batch_ref_3_budget_50_2004681_3.out
│   ├── batch_ref_3_budget_50_2004681_30.err
│   ├── batch_ref_3_budget_50_2004681_30.out
│   ├── batch_ref_3_budget_50_2004681_31.err
│   ├── batch_ref_3_budget_50_2004681_31.out
│   ├── batch_ref_3_budget_50_2004681_32.err
│   ├── batch_ref_3_budget_50_2004681_32.out
│   ├── batch_ref_3_budget_50_2004681_33.err
│   ├── batch_ref_3_budget_50_2004681_33.out
│   ├── batch_ref_3_budget_50_2004681_34.err
│   ├── batch_ref_3_budget_50_2004681_34.out
│   ├── batch_ref_3_budget_50_2004681_35.err
│   ├── batch_ref_3_budget_50_2004681_35.out
│   ├── batch_ref_3_budget_50_2004681_36.err
│   ├── batch_ref_3_budget_50_2004681_36.out
│   ├── batch_ref_3_budget_50_2004681_37.err
│   ├── batch_ref_3_budget_50_2004681_37.out
│   ├── batch_ref_3_budget_50_2004681_38.err
│   ├── batch_ref_3_budget_50_2004681_38.out
│   ├── batch_ref_3_budget_50_2004681_39.err
│   ├── batch_ref_3_budget_50_2004681_39.out
│   ├── batch_ref_3_budget_50_2004681_4.err
│   ├── batch_ref_3_budget_50_2004681_4.out
│   ├── batch_ref_3_budget_50_2004681_40.err
│   ├── batch_ref_3_budget_50_2004681_40.out
│   ├── batch_ref_3_budget_50_2004681_41.err
│   ├── batch_ref_3_budget_50_2004681_41.out
│   ├── batch_ref_3_budget_50_2004681_42.err
│   ├── batch_ref_3_budget_50_2004681_42.out
│   ├── batch_ref_3_budget_50_2004681_43.err
│   ├── batch_ref_3_budget_50_2004681_43.out
│   ├── batch_ref_3_budget_50_2004681_44.err
│   ├── batch_ref_3_budget_50_2004681_44.out
│   ├── batch_ref_3_budget_50_2004681_45.err
│   ├── batch_ref_3_budget_50_2004681_45.out
│   ├── batch_ref_3_budget_50_2004681_46.err
│   ├── batch_ref_3_budget_50_2004681_46.out
│   ├── batch_ref_3_budget_50_2004681_47.err
│   ├── batch_ref_3_budget_50_2004681_47.out
│   ├── batch_ref_3_budget_50_2004681_48.err
│   ├── batch_ref_3_budget_50_2004681_48.out
│   ├── batch_ref_3_budget_50_2004681_49.err
│   ├── batch_ref_3_budget_50_2004681_49.out
│   ├── batch_ref_3_budget_50_2004681_5.err
│   ├── batch_ref_3_budget_50_2004681_5.out
│   ├── batch_ref_3_budget_50_2004681_50.err
│   ├── batch_ref_3_budget_50_2004681_50.out
│   ├── batch_ref_3_budget_50_2004681_51.err
│   ├── batch_ref_3_budget_50_2004681_51.out
│   ├── batch_ref_3_budget_50_2004681_52.err
│   ├── batch_ref_3_budget_50_2004681_52.out
│   ├── batch_ref_3_budget_50_2004681_53.err
│   ├── batch_ref_3_budget_50_2004681_53.out
│   ├── batch_ref_3_budget_50_2004681_54.err
│   ├── batch_ref_3_budget_50_2004681_54.out
│   ├── batch_ref_3_budget_50_2004681_55.err
│   ├── batch_ref_3_budget_50_2004681_55.out
│   ├── batch_ref_3_budget_50_2004681_56.err
│   ├── batch_ref_3_budget_50_2004681_56.out
│   ├── batch_ref_3_budget_50_2004681_57.err
│   ├── batch_ref_3_budget_50_2004681_57.out
│   ├── batch_ref_3_budget_50_2004681_58.err
│   ├── batch_ref_3_budget_50_2004681_58.out
│   ├── batch_ref_3_budget_50_2004681_59.err
│   ├── batch_ref_3_budget_50_2004681_59.out
│   ├── batch_ref_3_budget_50_2004681_6.err
│   ├── batch_ref_3_budget_50_2004681_6.out
│   ├── batch_ref_3_budget_50_2004681_60.err
│   ├── batch_ref_3_budget_50_2004681_60.out
│   ├── batch_ref_3_budget_50_2004681_61.err
│   ├── batch_ref_3_budget_50_2004681_61.out
│   ├── batch_ref_3_budget_50_2004681_62.err
│   ├── batch_ref_3_budget_50_2004681_62.out
│   ├── batch_ref_3_budget_50_2004681_63.err
│   ├── batch_ref_3_budget_50_2004681_63.out
│   ├── batch_ref_3_budget_50_2004681_64.err
│   ├── batch_ref_3_budget_50_2004681_64.out
│   ├── batch_ref_3_budget_50_2004681_65.err
│   ├── batch_ref_3_budget_50_2004681_65.out
│   ├── batch_ref_3_budget_50_2004681_66.err
│   ├── batch_ref_3_budget_50_2004681_66.out
│   ├── batch_ref_3_budget_50_2004681_67.err
│   ├── batch_ref_3_budget_50_2004681_67.out
│   ├── batch_ref_3_budget_50_2004681_68.err
│   ├── batch_ref_3_budget_50_2004681_68.out
│   ├── batch_ref_3_budget_50_2004681_69.err
│   ├── batch_ref_3_budget_50_2004681_69.out
│   ├── batch_ref_3_budget_50_2004681_7.err
│   ├── batch_ref_3_budget_50_2004681_7.out
│   ├── batch_ref_3_budget_50_2004681_70.err
│   ├── batch_ref_3_budget_50_2004681_70.out
│   ├── batch_ref_3_budget_50_2004681_71.err
│   ├── batch_ref_3_budget_50_2004681_71.out
│   ├── batch_ref_3_budget_50_2004681_72.err
│   ├── batch_ref_3_budget_50_2004681_72.out
│   ├── batch_ref_3_budget_50_2004681_73.err
│   ├── batch_ref_3_budget_50_2004681_73.out
│   ├── batch_ref_3_budget_50_2004681_74.err
│   ├── batch_ref_3_budget_50_2004681_74.out
│   ├── batch_ref_3_budget_50_2004681_75.err
│   ├── batch_ref_3_budget_50_2004681_75.out
│   ├── batch_ref_3_budget_50_2004681_76.err
│   ├── batch_ref_3_budget_50_2004681_76.out
│   ├── batch_ref_3_budget_50_2004681_77.err
│   ├── batch_ref_3_budget_50_2004681_77.out
│   ├── batch_ref_3_budget_50_2004681_78.err
│   ├── batch_ref_3_budget_50_2004681_78.out
│   ├── batch_ref_3_budget_50_2004681_79.err
│   ├── batch_ref_3_budget_50_2004681_79.out
│   ├── batch_ref_3_budget_50_2004681_8.err
│   ├── batch_ref_3_budget_50_2004681_8.out
│   ├── batch_ref_3_budget_50_2004681_80.err
│   ├── batch_ref_3_budget_50_2004681_80.out
│   ├── batch_ref_3_budget_50_2004681_81.err
│   ├── batch_ref_3_budget_50_2004681_81.out
│   ├── batch_ref_3_budget_50_2004681_9.err
│   ├── batch_ref_3_budget_50_2004681_9.out
│   ├── batch_ref_3_budget_50_2005609_1.err
│   ├── batch_ref_3_budget_50_2005609_1.out
│   ├── batch_ref_3_budget_50_2005609_10.err
│   ├── batch_ref_3_budget_50_2005609_10.out
│   ├── batch_ref_3_budget_50_2005609_11.err
│   ├── batch_ref_3_budget_50_2005609_11.out
│   ├── batch_ref_3_budget_50_2005609_12.err
│   ├── batch_ref_3_budget_50_2005609_12.out
│   ├── batch_ref_3_budget_50_2005609_13.err
│   ├── batch_ref_3_budget_50_2005609_13.out
│   ├── batch_ref_3_budget_50_2005609_14.err
│   ├── batch_ref_3_budget_50_2005609_14.out
│   ├── batch_ref_3_budget_50_2005609_15.err
│   ├── batch_ref_3_budget_50_2005609_15.out
│   ├── batch_ref_3_budget_50_2005609_16.err
│   ├── batch_ref_3_budget_50_2005609_16.out
│   ├── batch_ref_3_budget_50_2005609_17.err
│   ├── batch_ref_3_budget_50_2005609_17.out
│   ├── batch_ref_3_budget_50_2005609_18.err
│   ├── batch_ref_3_budget_50_2005609_18.out
│   ├── batch_ref_3_budget_50_2005609_19.err
│   ├── batch_ref_3_budget_50_2005609_19.out
│   ├── batch_ref_3_budget_50_2005609_2.err
│   ├── batch_ref_3_budget_50_2005609_2.out
│   ├── batch_ref_3_budget_50_2005609_20.err
│   ├── batch_ref_3_budget_50_2005609_20.out
│   ├── batch_ref_3_budget_50_2005609_21.err
│   ├── batch_ref_3_budget_50_2005609_21.out
│   ├── batch_ref_3_budget_50_2005609_22.err
│   ├── batch_ref_3_budget_50_2005609_22.out
│   ├── batch_ref_3_budget_50_2005609_23.err
│   ├── batch_ref_3_budget_50_2005609_23.out
│   ├── batch_ref_3_budget_50_2005609_24.err
│   ├── batch_ref_3_budget_50_2005609_24.out
│   ├── batch_ref_3_budget_50_2005609_25.err
│   ├── batch_ref_3_budget_50_2005609_25.out
│   ├── batch_ref_3_budget_50_2005609_26.err
│   ├── batch_ref_3_budget_50_2005609_26.out
│   ├── batch_ref_3_budget_50_2005609_27.err
│   ├── batch_ref_3_budget_50_2005609_27.out
│   ├── batch_ref_3_budget_50_2005609_28.err
│   ├── batch_ref_3_budget_50_2005609_28.out
│   ├── batch_ref_3_budget_50_2005609_29.err
│   ├── batch_ref_3_budget_50_2005609_29.out
│   ├── batch_ref_3_budget_50_2005609_3.err
│   ├── batch_ref_3_budget_50_2005609_3.out
│   ├── batch_ref_3_budget_50_2005609_30.err
│   ├── batch_ref_3_budget_50_2005609_30.out
│   ├── batch_ref_3_budget_50_2005609_31.err
│   ├── batch_ref_3_budget_50_2005609_31.out
│   ├── batch_ref_3_budget_50_2005609_32.err
│   ├── batch_ref_3_budget_50_2005609_32.out
│   ├── batch_ref_3_budget_50_2005609_33.err
│   ├── batch_ref_3_budget_50_2005609_33.out
│   ├── batch_ref_3_budget_50_2005609_34.err
│   ├── batch_ref_3_budget_50_2005609_34.out
│   ├── batch_ref_3_budget_50_2005609_35.err
│   ├── batch_ref_3_budget_50_2005609_35.out
│   ├── batch_ref_3_budget_50_2005609_36.err
│   ├── batch_ref_3_budget_50_2005609_36.out
│   ├── batch_ref_3_budget_50_2005609_37.err
│   ├── batch_ref_3_budget_50_2005609_37.out
│   ├── batch_ref_3_budget_50_2005609_38.err
│   ├── batch_ref_3_budget_50_2005609_38.out
│   ├── batch_ref_3_budget_50_2005609_39.err
│   ├── batch_ref_3_budget_50_2005609_39.out
│   ├── batch_ref_3_budget_50_2005609_4.err
│   ├── batch_ref_3_budget_50_2005609_4.out
│   ├── batch_ref_3_budget_50_2005609_40.err
│   ├── batch_ref_3_budget_50_2005609_40.out
│   ├── batch_ref_3_budget_50_2005609_41.err
│   ├── batch_ref_3_budget_50_2005609_41.out
│   ├── batch_ref_3_budget_50_2005609_42.err
│   ├── batch_ref_3_budget_50_2005609_42.out
│   ├── batch_ref_3_budget_50_2005609_43.err
│   ├── batch_ref_3_budget_50_2005609_43.out
│   ├── batch_ref_3_budget_50_2005609_44.err
│   ├── batch_ref_3_budget_50_2005609_44.out
│   ├── batch_ref_3_budget_50_2005609_45.err
│   ├── batch_ref_3_budget_50_2005609_45.out
│   ├── batch_ref_3_budget_50_2005609_46.err
│   ├── batch_ref_3_budget_50_2005609_46.out
│   ├── batch_ref_3_budget_50_2005609_47.err
│   ├── batch_ref_3_budget_50_2005609_47.out
│   ├── batch_ref_3_budget_50_2005609_48.err
│   ├── batch_ref_3_budget_50_2005609_48.out
│   ├── batch_ref_3_budget_50_2005609_49.err
│   ├── batch_ref_3_budget_50_2005609_49.out
│   ├── batch_ref_3_budget_50_2005609_5.err
│   ├── batch_ref_3_budget_50_2005609_5.out
│   ├── batch_ref_3_budget_50_2005609_50.err
│   ├── batch_ref_3_budget_50_2005609_50.out
│   ├── batch_ref_3_budget_50_2005609_51.err
│   ├── batch_ref_3_budget_50_2005609_51.out
│   ├── batch_ref_3_budget_50_2005609_52.err
│   ├── batch_ref_3_budget_50_2005609_52.out
│   ├── batch_ref_3_budget_50_2005609_53.err
│   ├── batch_ref_3_budget_50_2005609_53.out
│   ├── batch_ref_3_budget_50_2005609_54.err
│   ├── batch_ref_3_budget_50_2005609_54.out
│   ├── batch_ref_3_budget_50_2005609_55.err
│   ├── batch_ref_3_budget_50_2005609_55.out
│   ├── batch_ref_3_budget_50_2005609_56.err
│   ├── batch_ref_3_budget_50_2005609_56.out
│   ├── batch_ref_3_budget_50_2005609_57.err
│   ├── batch_ref_3_budget_50_2005609_57.out
│   ├── batch_ref_3_budget_50_2005609_58.err
│   ├── batch_ref_3_budget_50_2005609_58.out
│   ├── batch_ref_3_budget_50_2005609_59.err
│   ├── batch_ref_3_budget_50_2005609_59.out
│   ├── batch_ref_3_budget_50_2005609_6.err
│   ├── batch_ref_3_budget_50_2005609_6.out
│   ├── batch_ref_3_budget_50_2005609_60.err
│   ├── batch_ref_3_budget_50_2005609_60.out
│   ├── batch_ref_3_budget_50_2005609_61.err
│   ├── batch_ref_3_budget_50_2005609_61.out
│   ├── batch_ref_3_budget_50_2005609_62.err
│   ├── batch_ref_3_budget_50_2005609_62.out
│   ├── batch_ref_3_budget_50_2005609_63.err
│   ├── batch_ref_3_budget_50_2005609_63.out
│   ├── batch_ref_3_budget_50_2005609_64.err
│   ├── batch_ref_3_budget_50_2005609_64.out
│   ├── batch_ref_3_budget_50_2005609_65.err
│   ├── batch_ref_3_budget_50_2005609_65.out
│   ├── batch_ref_3_budget_50_2005609_66.err
│   ├── batch_ref_3_budget_50_2005609_66.out
│   ├── batch_ref_3_budget_50_2005609_67.err
│   ├── batch_ref_3_budget_50_2005609_67.out
│   ├── batch_ref_3_budget_50_2005609_68.err
│   ├── batch_ref_3_budget_50_2005609_68.out
│   ├── batch_ref_3_budget_50_2005609_69.err
│   ├── batch_ref_3_budget_50_2005609_69.out
│   ├── batch_ref_3_budget_50_2005609_7.err
│   ├── batch_ref_3_budget_50_2005609_7.out
│   ├── batch_ref_3_budget_50_2005609_70.err
│   ├── batch_ref_3_budget_50_2005609_70.out
│   ├── batch_ref_3_budget_50_2005609_71.err
│   ├── batch_ref_3_budget_50_2005609_71.out
│   ├── batch_ref_3_budget_50_2005609_72.err
│   ├── batch_ref_3_budget_50_2005609_72.out
│   ├── batch_ref_3_budget_50_2005609_73.err
│   ├── batch_ref_3_budget_50_2005609_73.out
│   ├── batch_ref_3_budget_50_2005609_74.err
│   ├── batch_ref_3_budget_50_2005609_74.out
│   ├── batch_ref_3_budget_50_2005609_75.err
│   ├── batch_ref_3_budget_50_2005609_75.out
│   ├── batch_ref_3_budget_50_2005609_76.err
│   ├── batch_ref_3_budget_50_2005609_76.out
│   ├── batch_ref_3_budget_50_2005609_77.err
│   ├── batch_ref_3_budget_50_2005609_77.out
│   ├── batch_ref_3_budget_50_2005609_78.err
│   ├── batch_ref_3_budget_50_2005609_78.out
│   ├── batch_ref_3_budget_50_2005609_79.err
│   ├── batch_ref_3_budget_50_2005609_79.out
│   ├── batch_ref_3_budget_50_2005609_8.err
│   ├── batch_ref_3_budget_50_2005609_8.out
│   ├── batch_ref_3_budget_50_2005609_80.err
│   ├── batch_ref_3_budget_50_2005609_80.out
│   ├── batch_ref_3_budget_50_2005609_81.err
│   ├── batch_ref_3_budget_50_2005609_81.out
│   ├── batch_ref_3_budget_50_2005609_9.err
│   ├── batch_ref_3_budget_50_2005609_9.out
│   ├── batch_ref_3_budget_50_2006096_1.err
│   ├── batch_ref_3_budget_50_2006096_1.out
│   ├── batch_ref_3_budget_50_2006096_10.err
│   ├── batch_ref_3_budget_50_2006096_10.out
│   ├── batch_ref_3_budget_50_2006096_11.err
│   ├── batch_ref_3_budget_50_2006096_11.out
│   ├── batch_ref_3_budget_50_2006096_12.err
│   ├── batch_ref_3_budget_50_2006096_12.out
│   ├── batch_ref_3_budget_50_2006096_13.err
│   ├── batch_ref_3_budget_50_2006096_13.out
│   ├── batch_ref_3_budget_50_2006096_14.err
│   ├── batch_ref_3_budget_50_2006096_14.out
│   ├── batch_ref_3_budget_50_2006096_15.err
│   ├── batch_ref_3_budget_50_2006096_15.out
│   ├── batch_ref_3_budget_50_2006096_16.err
│   ├── batch_ref_3_budget_50_2006096_16.out
│   ├── batch_ref_3_budget_50_2006096_17.err
│   ├── batch_ref_3_budget_50_2006096_17.out
│   ├── batch_ref_3_budget_50_2006096_18.err
│   ├── batch_ref_3_budget_50_2006096_18.out
│   ├── batch_ref_3_budget_50_2006096_19.err
│   ├── batch_ref_3_budget_50_2006096_19.out
│   ├── batch_ref_3_budget_50_2006096_2.err
│   ├── batch_ref_3_budget_50_2006096_2.out
│   ├── batch_ref_3_budget_50_2006096_20.err
│   ├── batch_ref_3_budget_50_2006096_20.out
│   ├── batch_ref_3_budget_50_2006096_21.err
│   ├── batch_ref_3_budget_50_2006096_21.out
│   ├── batch_ref_3_budget_50_2006096_22.err
│   ├── batch_ref_3_budget_50_2006096_22.out
│   ├── batch_ref_3_budget_50_2006096_23.err
│   ├── batch_ref_3_budget_50_2006096_23.out
│   ├── batch_ref_3_budget_50_2006096_24.err
│   ├── batch_ref_3_budget_50_2006096_24.out
│   ├── batch_ref_3_budget_50_2006096_25.err
│   ├── batch_ref_3_budget_50_2006096_25.out
│   ├── batch_ref_3_budget_50_2006096_26.err
│   ├── batch_ref_3_budget_50_2006096_26.out
│   ├── batch_ref_3_budget_50_2006096_27.err
│   ├── batch_ref_3_budget_50_2006096_27.out
│   ├── batch_ref_3_budget_50_2006096_28.err
│   ├── batch_ref_3_budget_50_2006096_28.out
│   ├── batch_ref_3_budget_50_2006096_29.err
│   ├── batch_ref_3_budget_50_2006096_29.out
│   ├── batch_ref_3_budget_50_2006096_3.err
│   ├── batch_ref_3_budget_50_2006096_3.out
│   ├── batch_ref_3_budget_50_2006096_30.err
│   ├── batch_ref_3_budget_50_2006096_30.out
│   ├── batch_ref_3_budget_50_2006096_31.err
│   ├── batch_ref_3_budget_50_2006096_31.out
│   ├── batch_ref_3_budget_50_2006096_32.err
│   ├── batch_ref_3_budget_50_2006096_32.out
│   ├── batch_ref_3_budget_50_2006096_33.err
│   ├── batch_ref_3_budget_50_2006096_33.out
│   ├── batch_ref_3_budget_50_2006096_34.err
│   ├── batch_ref_3_budget_50_2006096_34.out
│   ├── batch_ref_3_budget_50_2006096_35.err
│   ├── batch_ref_3_budget_50_2006096_35.out
│   ├── batch_ref_3_budget_50_2006096_36.err
│   ├── batch_ref_3_budget_50_2006096_36.out
│   ├── batch_ref_3_budget_50_2006096_37.err
│   ├── batch_ref_3_budget_50_2006096_37.out
│   ├── batch_ref_3_budget_50_2006096_38.err
│   ├── batch_ref_3_budget_50_2006096_38.out
│   ├── batch_ref_3_budget_50_2006096_39.err
│   ├── batch_ref_3_budget_50_2006096_39.out
│   ├── batch_ref_3_budget_50_2006096_4.err
│   ├── batch_ref_3_budget_50_2006096_4.out
│   ├── batch_ref_3_budget_50_2006096_40.err
│   ├── batch_ref_3_budget_50_2006096_40.out
│   ├── batch_ref_3_budget_50_2006096_41.err
│   ├── batch_ref_3_budget_50_2006096_41.out
│   ├── batch_ref_3_budget_50_2006096_42.err
│   ├── batch_ref_3_budget_50_2006096_42.out
│   ├── batch_ref_3_budget_50_2006096_43.err
│   ├── batch_ref_3_budget_50_2006096_43.out
│   ├── batch_ref_3_budget_50_2006096_44.err
│   ├── batch_ref_3_budget_50_2006096_44.out
│   ├── batch_ref_3_budget_50_2006096_45.err
│   ├── batch_ref_3_budget_50_2006096_45.out
│   ├── batch_ref_3_budget_50_2006096_46.err
│   ├── batch_ref_3_budget_50_2006096_46.out
│   ├── batch_ref_3_budget_50_2006096_47.err
│   ├── batch_ref_3_budget_50_2006096_47.out
│   ├── batch_ref_3_budget_50_2006096_48.err
│   ├── batch_ref_3_budget_50_2006096_48.out
│   ├── batch_ref_3_budget_50_2006096_49.err
│   ├── batch_ref_3_budget_50_2006096_49.out
│   ├── batch_ref_3_budget_50_2006096_5.err
│   ├── batch_ref_3_budget_50_2006096_5.out
│   ├── batch_ref_3_budget_50_2006096_50.err
│   ├── batch_ref_3_budget_50_2006096_50.out
│   ├── batch_ref_3_budget_50_2006096_51.err
│   ├── batch_ref_3_budget_50_2006096_51.out
│   ├── batch_ref_3_budget_50_2006096_52.err
│   ├── batch_ref_3_budget_50_2006096_52.out
│   ├── batch_ref_3_budget_50_2006096_53.err
│   ├── batch_ref_3_budget_50_2006096_53.out
│   ├── batch_ref_3_budget_50_2006096_54.err
│   ├── batch_ref_3_budget_50_2006096_54.out
│   ├── batch_ref_3_budget_50_2006096_55.err
│   ├── batch_ref_3_budget_50_2006096_55.out
│   ├── batch_ref_3_budget_50_2006096_56.err
│   ├── batch_ref_3_budget_50_2006096_56.out
│   ├── batch_ref_3_budget_50_2006096_57.err
│   ├── batch_ref_3_budget_50_2006096_57.out
│   ├── batch_ref_3_budget_50_2006096_58.err
│   ├── batch_ref_3_budget_50_2006096_58.out
│   ├── batch_ref_3_budget_50_2006096_59.err
│   ├── batch_ref_3_budget_50_2006096_59.out
│   ├── batch_ref_3_budget_50_2006096_6.err
│   ├── batch_ref_3_budget_50_2006096_6.out
│   ├── batch_ref_3_budget_50_2006096_60.err
│   ├── batch_ref_3_budget_50_2006096_60.out
│   ├── batch_ref_3_budget_50_2006096_61.err
│   ├── batch_ref_3_budget_50_2006096_61.out
│   ├── batch_ref_3_budget_50_2006096_62.err
│   ├── batch_ref_3_budget_50_2006096_62.out
│   ├── batch_ref_3_budget_50_2006096_63.err
│   ├── batch_ref_3_budget_50_2006096_63.out
│   ├── batch_ref_3_budget_50_2006096_64.err
│   ├── batch_ref_3_budget_50_2006096_64.out
│   ├── batch_ref_3_budget_50_2006096_65.err
│   ├── batch_ref_3_budget_50_2006096_65.out
│   ├── batch_ref_3_budget_50_2006096_66.err
│   ├── batch_ref_3_budget_50_2006096_66.out
│   ├── batch_ref_3_budget_50_2006096_67.err
│   ├── batch_ref_3_budget_50_2006096_67.out
│   ├── batch_ref_3_budget_50_2006096_68.err
│   ├── batch_ref_3_budget_50_2006096_68.out
│   ├── batch_ref_3_budget_50_2006096_69.err
│   ├── batch_ref_3_budget_50_2006096_69.out
│   ├── batch_ref_3_budget_50_2006096_7.err
│   ├── batch_ref_3_budget_50_2006096_7.out
│   ├── batch_ref_3_budget_50_2006096_70.err
│   ├── batch_ref_3_budget_50_2006096_70.out
│   ├── batch_ref_3_budget_50_2006096_71.err
│   ├── batch_ref_3_budget_50_2006096_71.out
│   ├── batch_ref_3_budget_50_2006096_72.err
│   ├── batch_ref_3_budget_50_2006096_72.out
│   ├── batch_ref_3_budget_50_2006096_73.err
│   ├── batch_ref_3_budget_50_2006096_73.out
│   ├── batch_ref_3_budget_50_2006096_74.err
│   ├── batch_ref_3_budget_50_2006096_74.out
│   ├── batch_ref_3_budget_50_2006096_75.err
│   ├── batch_ref_3_budget_50_2006096_75.out
│   ├── batch_ref_3_budget_50_2006096_76.err
│   ├── batch_ref_3_budget_50_2006096_76.out
│   ├── batch_ref_3_budget_50_2006096_77.err
│   ├── batch_ref_3_budget_50_2006096_77.out
│   ├── batch_ref_3_budget_50_2006096_78.err
│   ├── batch_ref_3_budget_50_2006096_78.out
│   ├── batch_ref_3_budget_50_2006096_79.err
│   ├── batch_ref_3_budget_50_2006096_79.out
│   ├── batch_ref_3_budget_50_2006096_8.err
│   ├── batch_ref_3_budget_50_2006096_8.out
│   ├── batch_ref_3_budget_50_2006096_80.err
│   ├── batch_ref_3_budget_50_2006096_80.out
│   ├── batch_ref_3_budget_50_2006096_81.err
│   ├── batch_ref_3_budget_50_2006096_81.out
│   ├── batch_ref_3_budget_50_2006096_9.err
│   ├── batch_ref_3_budget_50_2006096_9.out
│   ├── batch_ref_3_budget_50_2024531_1.err
│   ├── batch_ref_3_budget_50_2024531_1.out
│   ├── batch_ref_3_budget_50_2024531_10.err
│   ├── batch_ref_3_budget_50_2024531_10.out
│   ├── batch_ref_3_budget_50_2024531_11.err
│   ├── batch_ref_3_budget_50_2024531_11.out
│   ├── batch_ref_3_budget_50_2024531_12.err
│   ├── batch_ref_3_budget_50_2024531_12.out
│   ├── batch_ref_3_budget_50_2024531_13.err
│   ├── batch_ref_3_budget_50_2024531_13.out
│   ├── batch_ref_3_budget_50_2024531_14.err
│   ├── batch_ref_3_budget_50_2024531_14.out
│   ├── batch_ref_3_budget_50_2024531_15.err
│   ├── batch_ref_3_budget_50_2024531_15.out
│   ├── batch_ref_3_budget_50_2024531_16.err
│   ├── batch_ref_3_budget_50_2024531_16.out
│   ├── batch_ref_3_budget_50_2024531_17.err
│   ├── batch_ref_3_budget_50_2024531_17.out
│   ├── batch_ref_3_budget_50_2024531_18.err
│   ├── batch_ref_3_budget_50_2024531_18.out
│   ├── batch_ref_3_budget_50_2024531_19.err
│   ├── batch_ref_3_budget_50_2024531_19.out
│   ├── batch_ref_3_budget_50_2024531_2.err
│   ├── batch_ref_3_budget_50_2024531_2.out
│   ├── batch_ref_3_budget_50_2024531_20.err
│   ├── batch_ref_3_budget_50_2024531_20.out
│   ├── batch_ref_3_budget_50_2024531_21.err
│   ├── batch_ref_3_budget_50_2024531_21.out
│   ├── batch_ref_3_budget_50_2024531_22.err
│   ├── batch_ref_3_budget_50_2024531_22.out
│   ├── batch_ref_3_budget_50_2024531_23.err
│   ├── batch_ref_3_budget_50_2024531_23.out
│   ├── batch_ref_3_budget_50_2024531_24.err
│   ├── batch_ref_3_budget_50_2024531_24.out
│   ├── batch_ref_3_budget_50_2024531_25.err
│   ├── batch_ref_3_budget_50_2024531_25.out
│   ├── batch_ref_3_budget_50_2024531_26.err
│   ├── batch_ref_3_budget_50_2024531_26.out
│   ├── batch_ref_3_budget_50_2024531_27.err
│   ├── batch_ref_3_budget_50_2024531_27.out
│   ├── batch_ref_3_budget_50_2024531_28.err
│   ├── batch_ref_3_budget_50_2024531_28.out
│   ├── batch_ref_3_budget_50_2024531_29.err
│   ├── batch_ref_3_budget_50_2024531_29.out
│   ├── batch_ref_3_budget_50_2024531_3.err
│   ├── batch_ref_3_budget_50_2024531_3.out
│   ├── batch_ref_3_budget_50_2024531_30.err
│   ├── batch_ref_3_budget_50_2024531_30.out
│   ├── batch_ref_3_budget_50_2024531_31.err
│   ├── batch_ref_3_budget_50_2024531_31.out
│   ├── batch_ref_3_budget_50_2024531_32.err
│   ├── batch_ref_3_budget_50_2024531_32.out
│   ├── batch_ref_3_budget_50_2024531_33.err
│   ├── batch_ref_3_budget_50_2024531_33.out
│   ├── batch_ref_3_budget_50_2024531_34.err
│   ├── batch_ref_3_budget_50_2024531_34.out
│   ├── batch_ref_3_budget_50_2024531_35.err
│   ├── batch_ref_3_budget_50_2024531_35.out
│   ├── batch_ref_3_budget_50_2024531_36.err
│   ├── batch_ref_3_budget_50_2024531_36.out
│   ├── batch_ref_3_budget_50_2024531_37.err
│   ├── batch_ref_3_budget_50_2024531_37.out
│   ├── batch_ref_3_budget_50_2024531_38.err
│   ├── batch_ref_3_budget_50_2024531_38.out
│   ├── batch_ref_3_budget_50_2024531_39.err
│   ├── batch_ref_3_budget_50_2024531_39.out
│   ├── batch_ref_3_budget_50_2024531_4.err
│   ├── batch_ref_3_budget_50_2024531_4.out
│   ├── batch_ref_3_budget_50_2024531_40.err
│   ├── batch_ref_3_budget_50_2024531_40.out
│   ├── batch_ref_3_budget_50_2024531_41.err
│   ├── batch_ref_3_budget_50_2024531_41.out
│   ├── batch_ref_3_budget_50_2024531_42.err
│   ├── batch_ref_3_budget_50_2024531_42.out
│   ├── batch_ref_3_budget_50_2024531_43.err
│   ├── batch_ref_3_budget_50_2024531_43.out
│   ├── batch_ref_3_budget_50_2024531_44.err
│   ├── batch_ref_3_budget_50_2024531_44.out
│   ├── batch_ref_3_budget_50_2024531_45.err
│   ├── batch_ref_3_budget_50_2024531_45.out
│   ├── batch_ref_3_budget_50_2024531_46.err
│   ├── batch_ref_3_budget_50_2024531_46.out
│   ├── batch_ref_3_budget_50_2024531_47.err
│   ├── batch_ref_3_budget_50_2024531_47.out
│   ├── batch_ref_3_budget_50_2024531_48.err
│   ├── batch_ref_3_budget_50_2024531_48.out
│   ├── batch_ref_3_budget_50_2024531_49.err
│   ├── batch_ref_3_budget_50_2024531_49.out
│   ├── batch_ref_3_budget_50_2024531_5.err
│   ├── batch_ref_3_budget_50_2024531_5.out
│   ├── batch_ref_3_budget_50_2024531_50.err
│   ├── batch_ref_3_budget_50_2024531_50.out
│   ├── batch_ref_3_budget_50_2024531_51.err
│   ├── batch_ref_3_budget_50_2024531_51.out
│   ├── batch_ref_3_budget_50_2024531_52.err
│   ├── batch_ref_3_budget_50_2024531_52.out
│   ├── batch_ref_3_budget_50_2024531_53.err
│   ├── batch_ref_3_budget_50_2024531_53.out
│   ├── batch_ref_3_budget_50_2024531_54.err
│   ├── batch_ref_3_budget_50_2024531_54.out
│   ├── batch_ref_3_budget_50_2024531_55.err
│   ├── batch_ref_3_budget_50_2024531_55.out
│   ├── batch_ref_3_budget_50_2024531_56.err
│   ├── batch_ref_3_budget_50_2024531_56.out
│   ├── batch_ref_3_budget_50_2024531_57.err
│   ├── batch_ref_3_budget_50_2024531_57.out
│   ├── batch_ref_3_budget_50_2024531_58.err
│   ├── batch_ref_3_budget_50_2024531_58.out
│   ├── batch_ref_3_budget_50_2024531_59.err
│   ├── batch_ref_3_budget_50_2024531_59.out
│   ├── batch_ref_3_budget_50_2024531_6.err
│   ├── batch_ref_3_budget_50_2024531_6.out
│   ├── batch_ref_3_budget_50_2024531_60.err
│   ├── batch_ref_3_budget_50_2024531_60.out
│   ├── batch_ref_3_budget_50_2024531_61.err
│   ├── batch_ref_3_budget_50_2024531_61.out
│   ├── batch_ref_3_budget_50_2024531_62.err
│   ├── batch_ref_3_budget_50_2024531_62.out
│   ├── batch_ref_3_budget_50_2024531_63.err
│   ├── batch_ref_3_budget_50_2024531_63.out
│   ├── batch_ref_3_budget_50_2024531_64.err
│   ├── batch_ref_3_budget_50_2024531_64.out
│   ├── batch_ref_3_budget_50_2024531_65.err
│   ├── batch_ref_3_budget_50_2024531_65.out
│   ├── batch_ref_3_budget_50_2024531_66.err
│   ├── batch_ref_3_budget_50_2024531_66.out
│   ├── batch_ref_3_budget_50_2024531_67.err
│   ├── batch_ref_3_budget_50_2024531_67.out
│   ├── batch_ref_3_budget_50_2024531_68.err
│   ├── batch_ref_3_budget_50_2024531_68.out
│   ├── batch_ref_3_budget_50_2024531_69.err
│   ├── batch_ref_3_budget_50_2024531_69.out
│   ├── batch_ref_3_budget_50_2024531_7.err
│   ├── batch_ref_3_budget_50_2024531_7.out
│   ├── batch_ref_3_budget_50_2024531_70.err
│   ├── batch_ref_3_budget_50_2024531_70.out
│   ├── batch_ref_3_budget_50_2024531_71.err
│   ├── batch_ref_3_budget_50_2024531_71.out
│   ├── batch_ref_3_budget_50_2024531_72.err
│   ├── batch_ref_3_budget_50_2024531_72.out
│   ├── batch_ref_3_budget_50_2024531_73.err
│   ├── batch_ref_3_budget_50_2024531_73.out
│   ├── batch_ref_3_budget_50_2024531_74.err
│   ├── batch_ref_3_budget_50_2024531_74.out
│   ├── batch_ref_3_budget_50_2024531_75.err
│   ├── batch_ref_3_budget_50_2024531_75.out
│   ├── batch_ref_3_budget_50_2024531_76.err
│   ├── batch_ref_3_budget_50_2024531_76.out
│   ├── batch_ref_3_budget_50_2024531_77.err
│   ├── batch_ref_3_budget_50_2024531_77.out
│   ├── batch_ref_3_budget_50_2024531_78.err
│   ├── batch_ref_3_budget_50_2024531_78.out
│   ├── batch_ref_3_budget_50_2024531_79.err
│   ├── batch_ref_3_budget_50_2024531_79.out
│   ├── batch_ref_3_budget_50_2024531_8.err
│   ├── batch_ref_3_budget_50_2024531_8.out
│   ├── batch_ref_3_budget_50_2024531_80.err
│   ├── batch_ref_3_budget_50_2024531_80.out
│   ├── batch_ref_3_budget_50_2024531_81.err
│   ├── batch_ref_3_budget_50_2024531_81.out
│   ├── batch_ref_3_budget_50_2024531_9.err
│   ├── batch_ref_3_budget_50_2024531_9.out
│   ├── batch_ref_3_budget_50_2038464_1.err
│   ├── batch_ref_3_budget_50_2038464_1.out
│   ├── batch_ref_3_budget_50_2038464_10.err
│   ├── batch_ref_3_budget_50_2038464_10.out
│   ├── batch_ref_3_budget_50_2038464_11.err
│   ├── batch_ref_3_budget_50_2038464_11.out
│   ├── batch_ref_3_budget_50_2038464_12.err
│   ├── batch_ref_3_budget_50_2038464_12.out
│   ├── batch_ref_3_budget_50_2038464_13.err
│   ├── batch_ref_3_budget_50_2038464_13.out
│   ├── batch_ref_3_budget_50_2038464_14.err
│   ├── batch_ref_3_budget_50_2038464_14.out
│   ├── batch_ref_3_budget_50_2038464_15.err
│   ├── batch_ref_3_budget_50_2038464_15.out
│   ├── batch_ref_3_budget_50_2038464_16.err
│   ├── batch_ref_3_budget_50_2038464_16.out
│   ├── batch_ref_3_budget_50_2038464_17.err
│   ├── batch_ref_3_budget_50_2038464_17.out
│   ├── batch_ref_3_budget_50_2038464_18.err
│   ├── batch_ref_3_budget_50_2038464_18.out
│   ├── batch_ref_3_budget_50_2038464_19.err
│   ├── batch_ref_3_budget_50_2038464_19.out
│   ├── batch_ref_3_budget_50_2038464_2.err
│   ├── batch_ref_3_budget_50_2038464_2.out
│   ├── batch_ref_3_budget_50_2038464_20.err
│   ├── batch_ref_3_budget_50_2038464_20.out
│   ├── batch_ref_3_budget_50_2038464_21.err
│   ├── batch_ref_3_budget_50_2038464_21.out
│   ├── batch_ref_3_budget_50_2038464_22.err
│   ├── batch_ref_3_budget_50_2038464_22.out
│   ├── batch_ref_3_budget_50_2038464_23.err
│   ├── batch_ref_3_budget_50_2038464_23.out
│   ├── batch_ref_3_budget_50_2038464_24.err
│   ├── batch_ref_3_budget_50_2038464_24.out
│   ├── batch_ref_3_budget_50_2038464_25.err
│   ├── batch_ref_3_budget_50_2038464_25.out
│   ├── batch_ref_3_budget_50_2038464_26.err
│   ├── batch_ref_3_budget_50_2038464_26.out
│   ├── batch_ref_3_budget_50_2038464_27.err
│   ├── batch_ref_3_budget_50_2038464_27.out
│   ├── batch_ref_3_budget_50_2038464_28.err
│   ├── batch_ref_3_budget_50_2038464_28.out
│   ├── batch_ref_3_budget_50_2038464_29.err
│   ├── batch_ref_3_budget_50_2038464_29.out
│   ├── batch_ref_3_budget_50_2038464_3.err
│   ├── batch_ref_3_budget_50_2038464_3.out
│   ├── batch_ref_3_budget_50_2038464_30.err
│   ├── batch_ref_3_budget_50_2038464_30.out
│   ├── batch_ref_3_budget_50_2038464_31.err
│   ├── batch_ref_3_budget_50_2038464_31.out
│   ├── batch_ref_3_budget_50_2038464_32.err
│   ├── batch_ref_3_budget_50_2038464_32.out
│   ├── batch_ref_3_budget_50_2038464_33.err
│   ├── batch_ref_3_budget_50_2038464_33.out
│   ├── batch_ref_3_budget_50_2038464_34.err
│   ├── batch_ref_3_budget_50_2038464_34.out
│   ├── batch_ref_3_budget_50_2038464_35.err
│   ├── batch_ref_3_budget_50_2038464_35.out
│   ├── batch_ref_3_budget_50_2038464_36.err
│   ├── batch_ref_3_budget_50_2038464_36.out
│   ├── batch_ref_3_budget_50_2038464_37.err
│   ├── batch_ref_3_budget_50_2038464_37.out
│   ├── batch_ref_3_budget_50_2038464_38.err
│   ├── batch_ref_3_budget_50_2038464_38.out
│   ├── batch_ref_3_budget_50_2038464_39.err
│   ├── batch_ref_3_budget_50_2038464_39.out
│   ├── batch_ref_3_budget_50_2038464_4.err
│   ├── batch_ref_3_budget_50_2038464_4.out
│   ├── batch_ref_3_budget_50_2038464_40.err
│   ├── batch_ref_3_budget_50_2038464_40.out
│   ├── batch_ref_3_budget_50_2038464_41.err
│   ├── batch_ref_3_budget_50_2038464_41.out
│   ├── batch_ref_3_budget_50_2038464_42.err
│   ├── batch_ref_3_budget_50_2038464_42.out
│   ├── batch_ref_3_budget_50_2038464_43.err
│   ├── batch_ref_3_budget_50_2038464_43.out
│   ├── batch_ref_3_budget_50_2038464_44.err
│   ├── batch_ref_3_budget_50_2038464_44.out
│   ├── batch_ref_3_budget_50_2038464_45.err
│   ├── batch_ref_3_budget_50_2038464_45.out
│   ├── batch_ref_3_budget_50_2038464_46.err
│   ├── batch_ref_3_budget_50_2038464_46.out
│   ├── batch_ref_3_budget_50_2038464_47.err
│   ├── batch_ref_3_budget_50_2038464_47.out
│   ├── batch_ref_3_budget_50_2038464_48.err
│   ├── batch_ref_3_budget_50_2038464_48.out
│   ├── batch_ref_3_budget_50_2038464_49.err
│   ├── batch_ref_3_budget_50_2038464_49.out
│   ├── batch_ref_3_budget_50_2038464_5.err
│   ├── batch_ref_3_budget_50_2038464_5.out
│   ├── batch_ref_3_budget_50_2038464_50.err
│   ├── batch_ref_3_budget_50_2038464_50.out
│   ├── batch_ref_3_budget_50_2038464_51.err
│   ├── batch_ref_3_budget_50_2038464_51.out
│   ├── batch_ref_3_budget_50_2038464_52.err
│   ├── batch_ref_3_budget_50_2038464_52.out
│   ├── batch_ref_3_budget_50_2038464_53.err
│   ├── batch_ref_3_budget_50_2038464_53.out
│   ├── batch_ref_3_budget_50_2038464_54.err
│   ├── batch_ref_3_budget_50_2038464_54.out
│   ├── batch_ref_3_budget_50_2038464_55.err
│   ├── batch_ref_3_budget_50_2038464_55.out
│   ├── batch_ref_3_budget_50_2038464_56.err
│   ├── batch_ref_3_budget_50_2038464_56.out
│   ├── batch_ref_3_budget_50_2038464_57.err
│   ├── batch_ref_3_budget_50_2038464_57.out
│   ├── batch_ref_3_budget_50_2038464_58.err
│   ├── batch_ref_3_budget_50_2038464_58.out
│   ├── batch_ref_3_budget_50_2038464_59.err
│   ├── batch_ref_3_budget_50_2038464_59.out
│   ├── batch_ref_3_budget_50_2038464_6.err
│   ├── batch_ref_3_budget_50_2038464_6.out
│   ├── batch_ref_3_budget_50_2038464_60.err
│   ├── batch_ref_3_budget_50_2038464_60.out
│   ├── batch_ref_3_budget_50_2038464_61.err
│   ├── batch_ref_3_budget_50_2038464_61.out
│   ├── batch_ref_3_budget_50_2038464_62.err
│   ├── batch_ref_3_budget_50_2038464_62.out
│   ├── batch_ref_3_budget_50_2038464_63.err
│   ├── batch_ref_3_budget_50_2038464_63.out
│   ├── batch_ref_3_budget_50_2038464_64.err
│   ├── batch_ref_3_budget_50_2038464_64.out
│   ├── batch_ref_3_budget_50_2038464_65.err
│   ├── batch_ref_3_budget_50_2038464_65.out
│   ├── batch_ref_3_budget_50_2038464_66.err
│   ├── batch_ref_3_budget_50_2038464_66.out
│   ├── batch_ref_3_budget_50_2038464_67.err
│   ├── batch_ref_3_budget_50_2038464_67.out
│   ├── batch_ref_3_budget_50_2038464_68.err
│   ├── batch_ref_3_budget_50_2038464_68.out
│   ├── batch_ref_3_budget_50_2038464_69.err
│   ├── batch_ref_3_budget_50_2038464_69.out
│   ├── batch_ref_3_budget_50_2038464_7.err
│   ├── batch_ref_3_budget_50_2038464_7.out
│   ├── batch_ref_3_budget_50_2038464_70.err
│   ├── batch_ref_3_budget_50_2038464_70.out
│   ├── batch_ref_3_budget_50_2038464_71.err
│   ├── batch_ref_3_budget_50_2038464_71.out
│   ├── batch_ref_3_budget_50_2038464_72.err
│   ├── batch_ref_3_budget_50_2038464_72.out
│   ├── batch_ref_3_budget_50_2038464_73.err
│   ├── batch_ref_3_budget_50_2038464_73.out
│   ├── batch_ref_3_budget_50_2038464_74.err
│   ├── batch_ref_3_budget_50_2038464_74.out
│   ├── batch_ref_3_budget_50_2038464_75.err
│   ├── batch_ref_3_budget_50_2038464_75.out
│   ├── batch_ref_3_budget_50_2038464_76.err
│   ├── batch_ref_3_budget_50_2038464_76.out
│   ├── batch_ref_3_budget_50_2038464_77.err
│   ├── batch_ref_3_budget_50_2038464_77.out
│   ├── batch_ref_3_budget_50_2038464_78.err
│   ├── batch_ref_3_budget_50_2038464_78.out
│   ├── batch_ref_3_budget_50_2038464_79.err
│   ├── batch_ref_3_budget_50_2038464_79.out
│   ├── batch_ref_3_budget_50_2038464_8.err
│   ├── batch_ref_3_budget_50_2038464_8.out
│   ├── batch_ref_3_budget_50_2038464_80.err
│   ├── batch_ref_3_budget_50_2038464_80.out
│   ├── batch_ref_3_budget_50_2038464_81.err
│   ├── batch_ref_3_budget_50_2038464_81.out
│   ├── batch_ref_3_budget_50_2038464_9.err
│   ├── batch_ref_3_budget_50_2038464_9.out
│   ├── batch_ref_3_budget_50_2040019_1.err
│   ├── batch_ref_3_budget_50_2040019_1.out
│   ├── batch_ref_3_budget_50_2040019_10.err
│   ├── batch_ref_3_budget_50_2040019_10.out
│   ├── batch_ref_3_budget_50_2040019_11.err
│   ├── batch_ref_3_budget_50_2040019_11.out
│   ├── batch_ref_3_budget_50_2040019_12.err
│   ├── batch_ref_3_budget_50_2040019_12.out
│   ├── batch_ref_3_budget_50_2040019_13.err
│   ├── batch_ref_3_budget_50_2040019_13.out
│   ├── batch_ref_3_budget_50_2040019_14.err
│   ├── batch_ref_3_budget_50_2040019_14.out
│   ├── batch_ref_3_budget_50_2040019_15.err
│   ├── batch_ref_3_budget_50_2040019_15.out
│   ├── batch_ref_3_budget_50_2040019_16.err
│   ├── batch_ref_3_budget_50_2040019_16.out
│   ├── batch_ref_3_budget_50_2040019_17.err
│   ├── batch_ref_3_budget_50_2040019_17.out
│   ├── batch_ref_3_budget_50_2040019_18.err
│   ├── batch_ref_3_budget_50_2040019_18.out
│   ├── batch_ref_3_budget_50_2040019_19.err
│   ├── batch_ref_3_budget_50_2040019_19.out
│   ├── batch_ref_3_budget_50_2040019_2.err
│   ├── batch_ref_3_budget_50_2040019_2.out
│   ├── batch_ref_3_budget_50_2040019_20.err
│   ├── batch_ref_3_budget_50_2040019_20.out
│   ├── batch_ref_3_budget_50_2040019_21.err
│   ├── batch_ref_3_budget_50_2040019_21.out
│   ├── batch_ref_3_budget_50_2040019_22.err
│   ├── batch_ref_3_budget_50_2040019_22.out
│   ├── batch_ref_3_budget_50_2040019_23.err
│   ├── batch_ref_3_budget_50_2040019_23.out
│   ├── batch_ref_3_budget_50_2040019_24.err
│   ├── batch_ref_3_budget_50_2040019_24.out
│   ├── batch_ref_3_budget_50_2040019_25.err
│   ├── batch_ref_3_budget_50_2040019_25.out
│   ├── batch_ref_3_budget_50_2040019_26.err
│   ├── batch_ref_3_budget_50_2040019_26.out
│   ├── batch_ref_3_budget_50_2040019_27.err
│   ├── batch_ref_3_budget_50_2040019_27.out
│   ├── batch_ref_3_budget_50_2040019_28.err
│   ├── batch_ref_3_budget_50_2040019_28.out
│   ├── batch_ref_3_budget_50_2040019_29.err
│   ├── batch_ref_3_budget_50_2040019_29.out
│   ├── batch_ref_3_budget_50_2040019_3.err
│   ├── batch_ref_3_budget_50_2040019_3.out
│   ├── batch_ref_3_budget_50_2040019_30.err
│   ├── batch_ref_3_budget_50_2040019_30.out
│   ├── batch_ref_3_budget_50_2040019_31.err
│   ├── batch_ref_3_budget_50_2040019_31.out
│   ├── batch_ref_3_budget_50_2040019_32.err
│   ├── batch_ref_3_budget_50_2040019_32.out
│   ├── batch_ref_3_budget_50_2040019_33.err
│   ├── batch_ref_3_budget_50_2040019_33.out
│   ├── batch_ref_3_budget_50_2040019_34.err
│   ├── batch_ref_3_budget_50_2040019_34.out
│   ├── batch_ref_3_budget_50_2040019_35.err
│   ├── batch_ref_3_budget_50_2040019_35.out
│   ├── batch_ref_3_budget_50_2040019_36.err
│   ├── batch_ref_3_budget_50_2040019_36.out
│   ├── batch_ref_3_budget_50_2040019_37.err
│   ├── batch_ref_3_budget_50_2040019_37.out
│   ├── batch_ref_3_budget_50_2040019_38.err
│   ├── batch_ref_3_budget_50_2040019_38.out
│   ├── batch_ref_3_budget_50_2040019_39.err
│   ├── batch_ref_3_budget_50_2040019_39.out
│   ├── batch_ref_3_budget_50_2040019_4.err
│   ├── batch_ref_3_budget_50_2040019_4.out
│   ├── batch_ref_3_budget_50_2040019_40.err
│   ├── batch_ref_3_budget_50_2040019_40.out
│   ├── batch_ref_3_budget_50_2040019_41.err
│   ├── batch_ref_3_budget_50_2040019_41.out
│   ├── batch_ref_3_budget_50_2040019_42.err
│   ├── batch_ref_3_budget_50_2040019_42.out
│   ├── batch_ref_3_budget_50_2040019_43.err
│   ├── batch_ref_3_budget_50_2040019_43.out
│   ├── batch_ref_3_budget_50_2040019_44.err
│   ├── batch_ref_3_budget_50_2040019_44.out
│   ├── batch_ref_3_budget_50_2040019_45.err
│   ├── batch_ref_3_budget_50_2040019_45.out
│   ├── batch_ref_3_budget_50_2040019_46.err
│   ├── batch_ref_3_budget_50_2040019_46.out
│   ├── batch_ref_3_budget_50_2040019_47.err
│   ├── batch_ref_3_budget_50_2040019_47.out
│   ├── batch_ref_3_budget_50_2040019_48.err
│   ├── batch_ref_3_budget_50_2040019_48.out
│   ├── batch_ref_3_budget_50_2040019_49.err
│   ├── batch_ref_3_budget_50_2040019_49.out
│   ├── batch_ref_3_budget_50_2040019_5.err
│   ├── batch_ref_3_budget_50_2040019_5.out
│   ├── batch_ref_3_budget_50_2040019_50.err
│   ├── batch_ref_3_budget_50_2040019_50.out
│   ├── batch_ref_3_budget_50_2040019_51.err
│   ├── batch_ref_3_budget_50_2040019_51.out
│   ├── batch_ref_3_budget_50_2040019_52.err
│   ├── batch_ref_3_budget_50_2040019_52.out
│   ├── batch_ref_3_budget_50_2040019_53.err
│   ├── batch_ref_3_budget_50_2040019_53.out
│   ├── batch_ref_3_budget_50_2040019_54.err
│   ├── batch_ref_3_budget_50_2040019_54.out
│   ├── batch_ref_3_budget_50_2040019_55.err
│   ├── batch_ref_3_budget_50_2040019_55.out
│   ├── batch_ref_3_budget_50_2040019_56.err
│   ├── batch_ref_3_budget_50_2040019_56.out
│   ├── batch_ref_3_budget_50_2040019_57.err
│   ├── batch_ref_3_budget_50_2040019_57.out
│   ├── batch_ref_3_budget_50_2040019_58.err
│   ├── batch_ref_3_budget_50_2040019_58.out
│   ├── batch_ref_3_budget_50_2040019_59.err
│   ├── batch_ref_3_budget_50_2040019_59.out
│   ├── batch_ref_3_budget_50_2040019_6.err
│   ├── batch_ref_3_budget_50_2040019_6.out
│   ├── batch_ref_3_budget_50_2040019_60.err
│   ├── batch_ref_3_budget_50_2040019_60.out
│   ├── batch_ref_3_budget_50_2040019_61.err
│   ├── batch_ref_3_budget_50_2040019_61.out
│   ├── batch_ref_3_budget_50_2040019_62.err
│   ├── batch_ref_3_budget_50_2040019_62.out
│   ├── batch_ref_3_budget_50_2040019_63.err
│   ├── batch_ref_3_budget_50_2040019_63.out
│   ├── batch_ref_3_budget_50_2040019_64.err
│   ├── batch_ref_3_budget_50_2040019_64.out
│   ├── batch_ref_3_budget_50_2040019_65.err
│   ├── batch_ref_3_budget_50_2040019_65.out
│   ├── batch_ref_3_budget_50_2040019_66.err
│   ├── batch_ref_3_budget_50_2040019_66.out
│   ├── batch_ref_3_budget_50_2040019_67.err
│   ├── batch_ref_3_budget_50_2040019_67.out
│   ├── batch_ref_3_budget_50_2040019_68.err
│   ├── batch_ref_3_budget_50_2040019_68.out
│   ├── batch_ref_3_budget_50_2040019_69.err
│   ├── batch_ref_3_budget_50_2040019_69.out
│   ├── batch_ref_3_budget_50_2040019_7.err
│   ├── batch_ref_3_budget_50_2040019_7.out
│   ├── batch_ref_3_budget_50_2040019_70.err
│   ├── batch_ref_3_budget_50_2040019_70.out
│   ├── batch_ref_3_budget_50_2040019_71.err
│   ├── batch_ref_3_budget_50_2040019_71.out
│   ├── batch_ref_3_budget_50_2040019_72.err
│   ├── batch_ref_3_budget_50_2040019_72.out
│   ├── batch_ref_3_budget_50_2040019_73.err
│   ├── batch_ref_3_budget_50_2040019_73.out
│   ├── batch_ref_3_budget_50_2040019_74.err
│   ├── batch_ref_3_budget_50_2040019_74.out
│   ├── batch_ref_3_budget_50_2040019_75.err
│   ├── batch_ref_3_budget_50_2040019_75.out
│   ├── batch_ref_3_budget_50_2040019_76.err
│   ├── batch_ref_3_budget_50_2040019_76.out
│   ├── batch_ref_3_budget_50_2040019_77.err
│   ├── batch_ref_3_budget_50_2040019_77.out
│   ├── batch_ref_3_budget_50_2040019_78.err
│   ├── batch_ref_3_budget_50_2040019_78.out
│   ├── batch_ref_3_budget_50_2040019_79.err
│   ├── batch_ref_3_budget_50_2040019_79.out
│   ├── batch_ref_3_budget_50_2040019_8.err
│   ├── batch_ref_3_budget_50_2040019_8.out
│   ├── batch_ref_3_budget_50_2040019_80.err
│   ├── batch_ref_3_budget_50_2040019_80.out
│   ├── batch_ref_3_budget_50_2040019_81.err
│   ├── batch_ref_3_budget_50_2040019_81.out
│   ├── batch_ref_3_budget_50_2040019_9.err
│   ├── batch_ref_3_budget_50_2040019_9.out
│   ├── batch_ref_3_budget_80_2038465_1.err
│   ├── batch_ref_3_budget_80_2038465_1.out
│   ├── batch_ref_3_budget_80_2038465_10.err
│   ├── batch_ref_3_budget_80_2038465_10.out
│   ├── batch_ref_3_budget_80_2038465_11.err
│   ├── batch_ref_3_budget_80_2038465_11.out
│   ├── batch_ref_3_budget_80_2038465_12.err
│   ├── batch_ref_3_budget_80_2038465_12.out
│   ├── batch_ref_3_budget_80_2038465_13.err
│   ├── batch_ref_3_budget_80_2038465_13.out
│   ├── batch_ref_3_budget_80_2038465_14.err
│   ├── batch_ref_3_budget_80_2038465_14.out
│   ├── batch_ref_3_budget_80_2038465_15.err
│   ├── batch_ref_3_budget_80_2038465_15.out
│   ├── batch_ref_3_budget_80_2038465_16.err
│   ├── batch_ref_3_budget_80_2038465_16.out
│   ├── batch_ref_3_budget_80_2038465_17.err
│   ├── batch_ref_3_budget_80_2038465_17.out
│   ├── batch_ref_3_budget_80_2038465_18.err
│   ├── batch_ref_3_budget_80_2038465_18.out
│   ├── batch_ref_3_budget_80_2038465_19.err
│   ├── batch_ref_3_budget_80_2038465_19.out
│   ├── batch_ref_3_budget_80_2038465_2.err
│   ├── batch_ref_3_budget_80_2038465_2.out
│   ├── batch_ref_3_budget_80_2038465_20.err
│   ├── batch_ref_3_budget_80_2038465_20.out
│   ├── batch_ref_3_budget_80_2038465_21.err
│   ├── batch_ref_3_budget_80_2038465_21.out
│   ├── batch_ref_3_budget_80_2038465_22.err
│   ├── batch_ref_3_budget_80_2038465_22.out
│   ├── batch_ref_3_budget_80_2038465_23.err
│   ├── batch_ref_3_budget_80_2038465_23.out
│   ├── batch_ref_3_budget_80_2038465_24.err
│   ├── batch_ref_3_budget_80_2038465_24.out
│   ├── batch_ref_3_budget_80_2038465_25.err
│   ├── batch_ref_3_budget_80_2038465_25.out
│   ├── batch_ref_3_budget_80_2038465_26.err
│   ├── batch_ref_3_budget_80_2038465_26.out
│   ├── batch_ref_3_budget_80_2038465_27.err
│   ├── batch_ref_3_budget_80_2038465_27.out
│   ├── batch_ref_3_budget_80_2038465_28.err
│   ├── batch_ref_3_budget_80_2038465_28.out
│   ├── batch_ref_3_budget_80_2038465_29.err
│   ├── batch_ref_3_budget_80_2038465_29.out
│   ├── batch_ref_3_budget_80_2038465_3.err
│   ├── batch_ref_3_budget_80_2038465_3.out
│   ├── batch_ref_3_budget_80_2038465_30.err
│   ├── batch_ref_3_budget_80_2038465_30.out
│   ├── batch_ref_3_budget_80_2038465_31.err
│   ├── batch_ref_3_budget_80_2038465_31.out
│   ├── batch_ref_3_budget_80_2038465_32.err
│   ├── batch_ref_3_budget_80_2038465_32.out
│   ├── batch_ref_3_budget_80_2038465_33.err
│   ├── batch_ref_3_budget_80_2038465_33.out
│   ├── batch_ref_3_budget_80_2038465_34.err
│   ├── batch_ref_3_budget_80_2038465_34.out
│   ├── batch_ref_3_budget_80_2038465_35.err
│   ├── batch_ref_3_budget_80_2038465_35.out
│   ├── batch_ref_3_budget_80_2038465_36.err
│   ├── batch_ref_3_budget_80_2038465_36.out
│   ├── batch_ref_3_budget_80_2038465_37.err
│   ├── batch_ref_3_budget_80_2038465_37.out
│   ├── batch_ref_3_budget_80_2038465_38.err
│   ├── batch_ref_3_budget_80_2038465_38.out
│   ├── batch_ref_3_budget_80_2038465_39.err
│   ├── batch_ref_3_budget_80_2038465_39.out
│   ├── batch_ref_3_budget_80_2038465_4.err
│   ├── batch_ref_3_budget_80_2038465_4.out
│   ├── batch_ref_3_budget_80_2038465_40.err
│   ├── batch_ref_3_budget_80_2038465_40.out
│   ├── batch_ref_3_budget_80_2038465_41.err
│   ├── batch_ref_3_budget_80_2038465_41.out
│   ├── batch_ref_3_budget_80_2038465_42.err
│   ├── batch_ref_3_budget_80_2038465_42.out
│   ├── batch_ref_3_budget_80_2038465_43.err
│   ├── batch_ref_3_budget_80_2038465_43.out
│   ├── batch_ref_3_budget_80_2038465_44.err
│   ├── batch_ref_3_budget_80_2038465_44.out
│   ├── batch_ref_3_budget_80_2038465_45.err
│   ├── batch_ref_3_budget_80_2038465_45.out
│   ├── batch_ref_3_budget_80_2038465_46.err
│   ├── batch_ref_3_budget_80_2038465_46.out
│   ├── batch_ref_3_budget_80_2038465_47.err
│   ├── batch_ref_3_budget_80_2038465_47.out
│   ├── batch_ref_3_budget_80_2038465_48.err
│   ├── batch_ref_3_budget_80_2038465_48.out
│   ├── batch_ref_3_budget_80_2038465_49.err
│   ├── batch_ref_3_budget_80_2038465_49.out
│   ├── batch_ref_3_budget_80_2038465_5.err
│   ├── batch_ref_3_budget_80_2038465_5.out
│   ├── batch_ref_3_budget_80_2038465_50.err
│   ├── batch_ref_3_budget_80_2038465_50.out
│   ├── batch_ref_3_budget_80_2038465_51.err
│   ├── batch_ref_3_budget_80_2038465_51.out
│   ├── batch_ref_3_budget_80_2038465_52.err
│   ├── batch_ref_3_budget_80_2038465_52.out
│   ├── batch_ref_3_budget_80_2038465_53.err
│   ├── batch_ref_3_budget_80_2038465_53.out
│   ├── batch_ref_3_budget_80_2038465_54.err
│   ├── batch_ref_3_budget_80_2038465_54.out
│   ├── batch_ref_3_budget_80_2038465_55.err
│   ├── batch_ref_3_budget_80_2038465_55.out
│   ├── batch_ref_3_budget_80_2038465_56.err
│   ├── batch_ref_3_budget_80_2038465_56.out
│   ├── batch_ref_3_budget_80_2038465_57.err
│   ├── batch_ref_3_budget_80_2038465_57.out
│   ├── batch_ref_3_budget_80_2038465_58.err
│   ├── batch_ref_3_budget_80_2038465_58.out
│   ├── batch_ref_3_budget_80_2038465_59.err
│   ├── batch_ref_3_budget_80_2038465_59.out
│   ├── batch_ref_3_budget_80_2038465_6.err
│   ├── batch_ref_3_budget_80_2038465_6.out
│   ├── batch_ref_3_budget_80_2038465_60.err
│   ├── batch_ref_3_budget_80_2038465_60.out
│   ├── batch_ref_3_budget_80_2038465_61.err
│   ├── batch_ref_3_budget_80_2038465_61.out
│   ├── batch_ref_3_budget_80_2038465_62.err
│   ├── batch_ref_3_budget_80_2038465_62.out
│   ├── batch_ref_3_budget_80_2038465_63.err
│   ├── batch_ref_3_budget_80_2038465_63.out
│   ├── batch_ref_3_budget_80_2038465_64.err
│   ├── batch_ref_3_budget_80_2038465_64.out
│   ├── batch_ref_3_budget_80_2038465_65.err
│   ├── batch_ref_3_budget_80_2038465_65.out
│   ├── batch_ref_3_budget_80_2038465_66.err
│   ├── batch_ref_3_budget_80_2038465_66.out
│   ├── batch_ref_3_budget_80_2038465_67.err
│   ├── batch_ref_3_budget_80_2038465_67.out
│   ├── batch_ref_3_budget_80_2038465_68.err
│   ├── batch_ref_3_budget_80_2038465_68.out
│   ├── batch_ref_3_budget_80_2038465_69.err
│   ├── batch_ref_3_budget_80_2038465_69.out
│   ├── batch_ref_3_budget_80_2038465_7.err
│   ├── batch_ref_3_budget_80_2038465_7.out
│   ├── batch_ref_3_budget_80_2038465_70.err
│   ├── batch_ref_3_budget_80_2038465_70.out
│   ├── batch_ref_3_budget_80_2038465_71.err
│   ├── batch_ref_3_budget_80_2038465_71.out
│   ├── batch_ref_3_budget_80_2038465_72.err
│   ├── batch_ref_3_budget_80_2038465_72.out
│   ├── batch_ref_3_budget_80_2038465_73.err
│   ├── batch_ref_3_budget_80_2038465_73.out
│   ├── batch_ref_3_budget_80_2038465_74.err
│   ├── batch_ref_3_budget_80_2038465_74.out
│   ├── batch_ref_3_budget_80_2038465_75.err
│   ├── batch_ref_3_budget_80_2038465_75.out
│   ├── batch_ref_3_budget_80_2038465_76.err
│   ├── batch_ref_3_budget_80_2038465_76.out
│   ├── batch_ref_3_budget_80_2038465_77.err
│   ├── batch_ref_3_budget_80_2038465_77.out
│   ├── batch_ref_3_budget_80_2038465_78.err
│   ├── batch_ref_3_budget_80_2038465_78.out
│   ├── batch_ref_3_budget_80_2038465_79.err
│   ├── batch_ref_3_budget_80_2038465_79.out
│   ├── batch_ref_3_budget_80_2038465_8.err
│   ├── batch_ref_3_budget_80_2038465_8.out
│   ├── batch_ref_3_budget_80_2038465_80.err
│   ├── batch_ref_3_budget_80_2038465_80.out
│   ├── batch_ref_3_budget_80_2038465_81.err
│   ├── batch_ref_3_budget_80_2038465_81.out
│   ├── batch_ref_3_budget_80_2038465_9.err
│   ├── batch_ref_3_budget_80_2038465_9.out
│   ├── batch_ref_3_budget_80_2040020_1.err
│   ├── batch_ref_3_budget_80_2040020_1.out
│   ├── batch_ref_3_budget_80_2040020_10.err
│   ├── batch_ref_3_budget_80_2040020_10.out
│   ├── batch_ref_3_budget_80_2040020_11.err
│   ├── batch_ref_3_budget_80_2040020_11.out
│   ├── batch_ref_3_budget_80_2040020_12.err
│   ├── batch_ref_3_budget_80_2040020_12.out
│   ├── batch_ref_3_budget_80_2040020_13.err
│   ├── batch_ref_3_budget_80_2040020_13.out
│   ├── batch_ref_3_budget_80_2040020_14.err
│   ├── batch_ref_3_budget_80_2040020_14.out
│   ├── batch_ref_3_budget_80_2040020_15.err
│   ├── batch_ref_3_budget_80_2040020_15.out
│   ├── batch_ref_3_budget_80_2040020_16.err
│   ├── batch_ref_3_budget_80_2040020_16.out
│   ├── batch_ref_3_budget_80_2040020_17.err
│   ├── batch_ref_3_budget_80_2040020_17.out
│   ├── batch_ref_3_budget_80_2040020_18.err
│   ├── batch_ref_3_budget_80_2040020_18.out
│   ├── batch_ref_3_budget_80_2040020_19.err
│   ├── batch_ref_3_budget_80_2040020_19.out
│   ├── batch_ref_3_budget_80_2040020_2.err
│   ├── batch_ref_3_budget_80_2040020_2.out
│   ├── batch_ref_3_budget_80_2040020_20.err
│   ├── batch_ref_3_budget_80_2040020_20.out
│   ├── batch_ref_3_budget_80_2040020_21.err
│   ├── batch_ref_3_budget_80_2040020_21.out
│   ├── batch_ref_3_budget_80_2040020_22.err
│   ├── batch_ref_3_budget_80_2040020_22.out
│   ├── batch_ref_3_budget_80_2040020_23.err
│   ├── batch_ref_3_budget_80_2040020_23.out
│   ├── batch_ref_3_budget_80_2040020_24.err
│   ├── batch_ref_3_budget_80_2040020_24.out
│   ├── batch_ref_3_budget_80_2040020_25.err
│   ├── batch_ref_3_budget_80_2040020_25.out
│   ├── batch_ref_3_budget_80_2040020_26.err
│   ├── batch_ref_3_budget_80_2040020_26.out
│   ├── batch_ref_3_budget_80_2040020_27.err
│   ├── batch_ref_3_budget_80_2040020_27.out
│   ├── batch_ref_3_budget_80_2040020_28.err
│   ├── batch_ref_3_budget_80_2040020_28.out
│   ├── batch_ref_3_budget_80_2040020_29.err
│   ├── batch_ref_3_budget_80_2040020_29.out
│   ├── batch_ref_3_budget_80_2040020_3.err
│   ├── batch_ref_3_budget_80_2040020_3.out
│   ├── batch_ref_3_budget_80_2040020_30.err
│   ├── batch_ref_3_budget_80_2040020_30.out
│   ├── batch_ref_3_budget_80_2040020_31.err
│   ├── batch_ref_3_budget_80_2040020_31.out
│   ├── batch_ref_3_budget_80_2040020_32.err
│   ├── batch_ref_3_budget_80_2040020_32.out
│   ├── batch_ref_3_budget_80_2040020_33.err
│   ├── batch_ref_3_budget_80_2040020_33.out
│   ├── batch_ref_3_budget_80_2040020_34.err
│   ├── batch_ref_3_budget_80_2040020_34.out
│   ├── batch_ref_3_budget_80_2040020_35.err
│   ├── batch_ref_3_budget_80_2040020_35.out
│   ├── batch_ref_3_budget_80_2040020_36.err
│   ├── batch_ref_3_budget_80_2040020_36.out
│   ├── batch_ref_3_budget_80_2040020_37.err
│   ├── batch_ref_3_budget_80_2040020_37.out
│   ├── batch_ref_3_budget_80_2040020_38.err
│   ├── batch_ref_3_budget_80_2040020_38.out
│   ├── batch_ref_3_budget_80_2040020_39.err
│   ├── batch_ref_3_budget_80_2040020_39.out
│   ├── batch_ref_3_budget_80_2040020_4.err
│   ├── batch_ref_3_budget_80_2040020_4.out
│   ├── batch_ref_3_budget_80_2040020_40.err
│   ├── batch_ref_3_budget_80_2040020_40.out
│   ├── batch_ref_3_budget_80_2040020_41.err
│   ├── batch_ref_3_budget_80_2040020_41.out
│   ├── batch_ref_3_budget_80_2040020_42.err
│   ├── batch_ref_3_budget_80_2040020_42.out
│   ├── batch_ref_3_budget_80_2040020_43.err
│   ├── batch_ref_3_budget_80_2040020_43.out
│   ├── batch_ref_3_budget_80_2040020_44.err
│   ├── batch_ref_3_budget_80_2040020_44.out
│   ├── batch_ref_3_budget_80_2040020_45.err
│   ├── batch_ref_3_budget_80_2040020_45.out
│   ├── batch_ref_3_budget_80_2040020_46.err
│   ├── batch_ref_3_budget_80_2040020_46.out
│   ├── batch_ref_3_budget_80_2040020_47.err
│   ├── batch_ref_3_budget_80_2040020_47.out
│   ├── batch_ref_3_budget_80_2040020_48.err
│   ├── batch_ref_3_budget_80_2040020_48.out
│   ├── batch_ref_3_budget_80_2040020_49.err
│   ├── batch_ref_3_budget_80_2040020_49.out
│   ├── batch_ref_3_budget_80_2040020_5.err
│   ├── batch_ref_3_budget_80_2040020_5.out
│   ├── batch_ref_3_budget_80_2040020_50.err
│   ├── batch_ref_3_budget_80_2040020_50.out
│   ├── batch_ref_3_budget_80_2040020_51.err
│   ├── batch_ref_3_budget_80_2040020_51.out
│   ├── batch_ref_3_budget_80_2040020_52.err
│   ├── batch_ref_3_budget_80_2040020_52.out
│   ├── batch_ref_3_budget_80_2040020_53.err
│   ├── batch_ref_3_budget_80_2040020_53.out
│   ├── batch_ref_3_budget_80_2040020_54.err
│   ├── batch_ref_3_budget_80_2040020_54.out
│   ├── batch_ref_3_budget_80_2040020_55.err
│   ├── batch_ref_3_budget_80_2040020_55.out
│   ├── batch_ref_3_budget_80_2040020_56.err
│   ├── batch_ref_3_budget_80_2040020_56.out
│   ├── batch_ref_3_budget_80_2040020_57.err
│   ├── batch_ref_3_budget_80_2040020_57.out
│   ├── batch_ref_3_budget_80_2040020_58.err
│   ├── batch_ref_3_budget_80_2040020_58.out
│   ├── batch_ref_3_budget_80_2040020_59.err
│   ├── batch_ref_3_budget_80_2040020_59.out
│   ├── batch_ref_3_budget_80_2040020_6.err
│   ├── batch_ref_3_budget_80_2040020_6.out
│   ├── batch_ref_3_budget_80_2040020_60.err
│   ├── batch_ref_3_budget_80_2040020_60.out
│   ├── batch_ref_3_budget_80_2040020_61.err
│   ├── batch_ref_3_budget_80_2040020_61.out
│   ├── batch_ref_3_budget_80_2040020_62.err
│   ├── batch_ref_3_budget_80_2040020_62.out
│   ├── batch_ref_3_budget_80_2040020_63.err
│   ├── batch_ref_3_budget_80_2040020_63.out
│   ├── batch_ref_3_budget_80_2040020_64.err
│   ├── batch_ref_3_budget_80_2040020_64.out
│   ├── batch_ref_3_budget_80_2040020_65.err
│   ├── batch_ref_3_budget_80_2040020_65.out
│   ├── batch_ref_3_budget_80_2040020_66.err
│   ├── batch_ref_3_budget_80_2040020_66.out
│   ├── batch_ref_3_budget_80_2040020_67.err
│   ├── batch_ref_3_budget_80_2040020_67.out
│   ├── batch_ref_3_budget_80_2040020_68.err
│   ├── batch_ref_3_budget_80_2040020_68.out
│   ├── batch_ref_3_budget_80_2040020_69.err
│   ├── batch_ref_3_budget_80_2040020_69.out
│   ├── batch_ref_3_budget_80_2040020_7.err
│   ├── batch_ref_3_budget_80_2040020_7.out
│   ├── batch_ref_3_budget_80_2040020_70.err
│   ├── batch_ref_3_budget_80_2040020_70.out
│   ├── batch_ref_3_budget_80_2040020_71.err
│   ├── batch_ref_3_budget_80_2040020_71.out
│   ├── batch_ref_3_budget_80_2040020_72.err
│   ├── batch_ref_3_budget_80_2040020_72.out
│   ├── batch_ref_3_budget_80_2040020_73.err
│   ├── batch_ref_3_budget_80_2040020_73.out
│   ├── batch_ref_3_budget_80_2040020_74.err
│   ├── batch_ref_3_budget_80_2040020_74.out
│   ├── batch_ref_3_budget_80_2040020_75.err
│   ├── batch_ref_3_budget_80_2040020_75.out
│   ├── batch_ref_3_budget_80_2040020_76.err
│   ├── batch_ref_3_budget_80_2040020_76.out
│   ├── batch_ref_3_budget_80_2040020_77.err
│   ├── batch_ref_3_budget_80_2040020_77.out
│   ├── batch_ref_3_budget_80_2040020_78.err
│   ├── batch_ref_3_budget_80_2040020_78.out
│   ├── batch_ref_3_budget_80_2040020_79.err
│   ├── batch_ref_3_budget_80_2040020_79.out
│   ├── batch_ref_3_budget_80_2040020_8.err
│   ├── batch_ref_3_budget_80_2040020_8.out
│   ├── batch_ref_3_budget_80_2040020_80.err
│   ├── batch_ref_3_budget_80_2040020_80.out
│   ├── batch_ref_3_budget_80_2040020_81.err
│   ├── batch_ref_3_budget_80_2040020_81.out
│   ├── batch_ref_3_budget_80_2040020_9.err
│   ├── batch_ref_3_budget_80_2040020_9.out
│   ├── batch_ref_4_budget_100_2024958_1.err
│   ├── batch_ref_4_budget_100_2024958_1.out
│   ├── batch_ref_4_budget_100_2024958_10.err
│   ├── batch_ref_4_budget_100_2024958_10.out
│   ├── batch_ref_4_budget_100_2024958_11.err
│   ├── batch_ref_4_budget_100_2024958_11.out
│   ├── batch_ref_4_budget_100_2024958_12.err
│   ├── batch_ref_4_budget_100_2024958_12.out
│   ├── batch_ref_4_budget_100_2024958_13.err
│   ├── batch_ref_4_budget_100_2024958_13.out
│   ├── batch_ref_4_budget_100_2024958_14.err
│   ├── batch_ref_4_budget_100_2024958_14.out
│   ├── batch_ref_4_budget_100_2024958_15.err
│   ├── batch_ref_4_budget_100_2024958_15.out
│   ├── batch_ref_4_budget_100_2024958_16.err
│   ├── batch_ref_4_budget_100_2024958_16.out
│   ├── batch_ref_4_budget_100_2024958_17.err
│   ├── batch_ref_4_budget_100_2024958_17.out
│   ├── batch_ref_4_budget_100_2024958_18.err
│   ├── batch_ref_4_budget_100_2024958_18.out
│   ├── batch_ref_4_budget_100_2024958_19.err
│   ├── batch_ref_4_budget_100_2024958_19.out
│   ├── batch_ref_4_budget_100_2024958_2.err
│   ├── batch_ref_4_budget_100_2024958_2.out
│   ├── batch_ref_4_budget_100_2024958_20.err
│   ├── batch_ref_4_budget_100_2024958_20.out
│   ├── batch_ref_4_budget_100_2024958_21.err
│   ├── batch_ref_4_budget_100_2024958_21.out
│   ├── batch_ref_4_budget_100_2024958_22.err
│   ├── batch_ref_4_budget_100_2024958_22.out
│   ├── batch_ref_4_budget_100_2024958_23.err
│   ├── batch_ref_4_budget_100_2024958_23.out
│   ├── batch_ref_4_budget_100_2024958_24.err
│   ├── batch_ref_4_budget_100_2024958_24.out
│   ├── batch_ref_4_budget_100_2024958_25.err
│   ├── batch_ref_4_budget_100_2024958_25.out
│   ├── batch_ref_4_budget_100_2024958_26.err
│   ├── batch_ref_4_budget_100_2024958_26.out
│   ├── batch_ref_4_budget_100_2024958_27.err
│   ├── batch_ref_4_budget_100_2024958_27.out
│   ├── batch_ref_4_budget_100_2024958_28.err
│   ├── batch_ref_4_budget_100_2024958_28.out
│   ├── batch_ref_4_budget_100_2024958_29.err
│   ├── batch_ref_4_budget_100_2024958_29.out
│   ├── batch_ref_4_budget_100_2024958_3.err
│   ├── batch_ref_4_budget_100_2024958_3.out
│   ├── batch_ref_4_budget_100_2024958_30.err
│   ├── batch_ref_4_budget_100_2024958_30.out
│   ├── batch_ref_4_budget_100_2024958_31.err
│   ├── batch_ref_4_budget_100_2024958_31.out
│   ├── batch_ref_4_budget_100_2024958_32.err
│   ├── batch_ref_4_budget_100_2024958_32.out
│   ├── batch_ref_4_budget_100_2024958_33.err
│   ├── batch_ref_4_budget_100_2024958_33.out
│   ├── batch_ref_4_budget_100_2024958_34.err
│   ├── batch_ref_4_budget_100_2024958_34.out
│   ├── batch_ref_4_budget_100_2024958_35.err
│   ├── batch_ref_4_budget_100_2024958_35.out
│   ├── batch_ref_4_budget_100_2024958_36.err
│   ├── batch_ref_4_budget_100_2024958_36.out
│   ├── batch_ref_4_budget_100_2024958_37.err
│   ├── batch_ref_4_budget_100_2024958_37.out
│   ├── batch_ref_4_budget_100_2024958_38.err
│   ├── batch_ref_4_budget_100_2024958_38.out
│   ├── batch_ref_4_budget_100_2024958_39.err
│   ├── batch_ref_4_budget_100_2024958_39.out
│   ├── batch_ref_4_budget_100_2024958_4.err
│   ├── batch_ref_4_budget_100_2024958_4.out
│   ├── batch_ref_4_budget_100_2024958_40.err
│   ├── batch_ref_4_budget_100_2024958_40.out
│   ├── batch_ref_4_budget_100_2024958_41.err
│   ├── batch_ref_4_budget_100_2024958_41.out
│   ├── batch_ref_4_budget_100_2024958_42.err
│   ├── batch_ref_4_budget_100_2024958_42.out
│   ├── batch_ref_4_budget_100_2024958_43.err
│   ├── batch_ref_4_budget_100_2024958_43.out
│   ├── batch_ref_4_budget_100_2024958_44.err
│   ├── batch_ref_4_budget_100_2024958_44.out
│   ├── batch_ref_4_budget_100_2024958_45.err
│   ├── batch_ref_4_budget_100_2024958_45.out
│   ├── batch_ref_4_budget_100_2024958_46.err
│   ├── batch_ref_4_budget_100_2024958_46.out
│   ├── batch_ref_4_budget_100_2024958_47.err
│   ├── batch_ref_4_budget_100_2024958_47.out
│   ├── batch_ref_4_budget_100_2024958_48.err
│   ├── batch_ref_4_budget_100_2024958_48.out
│   ├── batch_ref_4_budget_100_2024958_49.err
│   ├── batch_ref_4_budget_100_2024958_49.out
│   ├── batch_ref_4_budget_100_2024958_5.err
│   ├── batch_ref_4_budget_100_2024958_5.out
│   ├── batch_ref_4_budget_100_2024958_50.err
│   ├── batch_ref_4_budget_100_2024958_50.out
│   ├── batch_ref_4_budget_100_2024958_51.err
│   ├── batch_ref_4_budget_100_2024958_51.out
│   ├── batch_ref_4_budget_100_2024958_52.err
│   ├── batch_ref_4_budget_100_2024958_52.out
│   ├── batch_ref_4_budget_100_2024958_53.err
│   ├── batch_ref_4_budget_100_2024958_53.out
│   ├── batch_ref_4_budget_100_2024958_54.err
│   ├── batch_ref_4_budget_100_2024958_54.out
│   ├── batch_ref_4_budget_100_2024958_55.err
│   ├── batch_ref_4_budget_100_2024958_55.out
│   ├── batch_ref_4_budget_100_2024958_56.err
│   ├── batch_ref_4_budget_100_2024958_56.out
│   ├── batch_ref_4_budget_100_2024958_57.err
│   ├── batch_ref_4_budget_100_2024958_57.out
│   ├── batch_ref_4_budget_100_2024958_58.err
│   ├── batch_ref_4_budget_100_2024958_58.out
│   ├── batch_ref_4_budget_100_2024958_59.err
│   ├── batch_ref_4_budget_100_2024958_59.out
│   ├── batch_ref_4_budget_100_2024958_6.err
│   ├── batch_ref_4_budget_100_2024958_6.out
│   ├── batch_ref_4_budget_100_2024958_60.err
│   ├── batch_ref_4_budget_100_2024958_60.out
│   ├── batch_ref_4_budget_100_2024958_61.err
│   ├── batch_ref_4_budget_100_2024958_61.out
│   ├── batch_ref_4_budget_100_2024958_62.err
│   ├── batch_ref_4_budget_100_2024958_62.out
│   ├── batch_ref_4_budget_100_2024958_63.err
│   ├── batch_ref_4_budget_100_2024958_63.out
│   ├── batch_ref_4_budget_100_2024958_64.err
│   ├── batch_ref_4_budget_100_2024958_64.out
│   ├── batch_ref_4_budget_100_2024958_65.err
│   ├── batch_ref_4_budget_100_2024958_65.out
│   ├── batch_ref_4_budget_100_2024958_66.err
│   ├── batch_ref_4_budget_100_2024958_66.out
│   ├── batch_ref_4_budget_100_2024958_67.err
│   ├── batch_ref_4_budget_100_2024958_67.out
│   ├── batch_ref_4_budget_100_2024958_68.err
│   ├── batch_ref_4_budget_100_2024958_68.out
│   ├── batch_ref_4_budget_100_2024958_69.err
│   ├── batch_ref_4_budget_100_2024958_69.out
│   ├── batch_ref_4_budget_100_2024958_7.err
│   ├── batch_ref_4_budget_100_2024958_7.out
│   ├── batch_ref_4_budget_100_2024958_70.err
│   ├── batch_ref_4_budget_100_2024958_70.out
│   ├── batch_ref_4_budget_100_2024958_71.err
│   ├── batch_ref_4_budget_100_2024958_71.out
│   ├── batch_ref_4_budget_100_2024958_72.err
│   ├── batch_ref_4_budget_100_2024958_72.out
│   ├── batch_ref_4_budget_100_2024958_73.err
│   ├── batch_ref_4_budget_100_2024958_73.out
│   ├── batch_ref_4_budget_100_2024958_74.err
│   ├── batch_ref_4_budget_100_2024958_74.out
│   ├── batch_ref_4_budget_100_2024958_75.err
│   ├── batch_ref_4_budget_100_2024958_75.out
│   ├── batch_ref_4_budget_100_2024958_76.err
│   ├── batch_ref_4_budget_100_2024958_76.out
│   ├── batch_ref_4_budget_100_2024958_77.err
│   ├── batch_ref_4_budget_100_2024958_77.out
│   ├── batch_ref_4_budget_100_2024958_78.err
│   ├── batch_ref_4_budget_100_2024958_78.out
│   ├── batch_ref_4_budget_100_2024958_79.err
│   ├── batch_ref_4_budget_100_2024958_79.out
│   ├── batch_ref_4_budget_100_2024958_8.err
│   ├── batch_ref_4_budget_100_2024958_8.out
│   ├── batch_ref_4_budget_100_2024958_80.err
│   ├── batch_ref_4_budget_100_2024958_80.out
│   ├── batch_ref_4_budget_100_2024958_81.err
│   ├── batch_ref_4_budget_100_2024958_81.out
│   ├── batch_ref_4_budget_100_2024958_9.err
│   ├── batch_ref_4_budget_100_2024958_9.out
│   ├── batch_ref_4_budget_100_2040021_1.err
│   ├── batch_ref_4_budget_100_2040021_1.out
│   ├── batch_ref_4_budget_100_2040021_10.err
│   ├── batch_ref_4_budget_100_2040021_10.out
│   ├── batch_ref_4_budget_100_2040021_11.err
│   ├── batch_ref_4_budget_100_2040021_11.out
│   ├── batch_ref_4_budget_100_2040021_12.err
│   ├── batch_ref_4_budget_100_2040021_12.out
│   ├── batch_ref_4_budget_100_2040021_13.err
│   ├── batch_ref_4_budget_100_2040021_13.out
│   ├── batch_ref_4_budget_100_2040021_14.err
│   ├── batch_ref_4_budget_100_2040021_14.out
│   ├── batch_ref_4_budget_100_2040021_15.err
│   ├── batch_ref_4_budget_100_2040021_15.out
│   ├── batch_ref_4_budget_100_2040021_16.err
│   ├── batch_ref_4_budget_100_2040021_16.out
│   ├── batch_ref_4_budget_100_2040021_17.err
│   ├── batch_ref_4_budget_100_2040021_17.out
│   ├── batch_ref_4_budget_100_2040021_18.err
│   ├── batch_ref_4_budget_100_2040021_18.out
│   ├── batch_ref_4_budget_100_2040021_19.err
│   ├── batch_ref_4_budget_100_2040021_19.out
│   ├── batch_ref_4_budget_100_2040021_2.err
│   ├── batch_ref_4_budget_100_2040021_2.out
│   ├── batch_ref_4_budget_100_2040021_20.err
│   ├── batch_ref_4_budget_100_2040021_20.out
│   ├── batch_ref_4_budget_100_2040021_21.err
│   ├── batch_ref_4_budget_100_2040021_21.out
│   ├── batch_ref_4_budget_100_2040021_22.err
│   ├── batch_ref_4_budget_100_2040021_22.out
│   ├── batch_ref_4_budget_100_2040021_23.err
│   ├── batch_ref_4_budget_100_2040021_23.out
│   ├── batch_ref_4_budget_100_2040021_24.err
│   ├── batch_ref_4_budget_100_2040021_24.out
│   ├── batch_ref_4_budget_100_2040021_25.err
│   ├── batch_ref_4_budget_100_2040021_25.out
│   ├── batch_ref_4_budget_100_2040021_26.err
│   ├── batch_ref_4_budget_100_2040021_26.out
│   ├── batch_ref_4_budget_100_2040021_27.err
│   ├── batch_ref_4_budget_100_2040021_27.out
│   ├── batch_ref_4_budget_100_2040021_28.err
│   ├── batch_ref_4_budget_100_2040021_28.out
│   ├── batch_ref_4_budget_100_2040021_29.err
│   ├── batch_ref_4_budget_100_2040021_29.out
│   ├── batch_ref_4_budget_100_2040021_3.err
│   ├── batch_ref_4_budget_100_2040021_3.out
│   ├── batch_ref_4_budget_100_2040021_30.err
│   ├── batch_ref_4_budget_100_2040021_30.out
│   ├── batch_ref_4_budget_100_2040021_31.err
│   ├── batch_ref_4_budget_100_2040021_31.out
│   ├── batch_ref_4_budget_100_2040021_32.err
│   ├── batch_ref_4_budget_100_2040021_32.out
│   ├── batch_ref_4_budget_100_2040021_33.err
│   ├── batch_ref_4_budget_100_2040021_33.out
│   ├── batch_ref_4_budget_100_2040021_34.err
│   ├── batch_ref_4_budget_100_2040021_34.out
│   ├── batch_ref_4_budget_100_2040021_35.err
│   ├── batch_ref_4_budget_100_2040021_35.out
│   ├── batch_ref_4_budget_100_2040021_36.err
│   ├── batch_ref_4_budget_100_2040021_36.out
│   ├── batch_ref_4_budget_100_2040021_37.err
│   ├── batch_ref_4_budget_100_2040021_37.out
│   ├── batch_ref_4_budget_100_2040021_38.err
│   ├── batch_ref_4_budget_100_2040021_38.out
│   ├── batch_ref_4_budget_100_2040021_39.err
│   ├── batch_ref_4_budget_100_2040021_39.out
│   ├── batch_ref_4_budget_100_2040021_4.err
│   ├── batch_ref_4_budget_100_2040021_4.out
│   ├── batch_ref_4_budget_100_2040021_40.err
│   ├── batch_ref_4_budget_100_2040021_40.out
│   ├── batch_ref_4_budget_100_2040021_41.err
│   ├── batch_ref_4_budget_100_2040021_41.out
│   ├── batch_ref_4_budget_100_2040021_42.err
│   ├── batch_ref_4_budget_100_2040021_42.out
│   ├── batch_ref_4_budget_100_2040021_43.err
│   ├── batch_ref_4_budget_100_2040021_43.out
│   ├── batch_ref_4_budget_100_2040021_44.err
│   ├── batch_ref_4_budget_100_2040021_44.out
│   ├── batch_ref_4_budget_100_2040021_45.err
│   ├── batch_ref_4_budget_100_2040021_45.out
│   ├── batch_ref_4_budget_100_2040021_46.err
│   ├── batch_ref_4_budget_100_2040021_46.out
│   ├── batch_ref_4_budget_100_2040021_47.err
│   ├── batch_ref_4_budget_100_2040021_47.out
│   ├── batch_ref_4_budget_100_2040021_48.err
│   ├── batch_ref_4_budget_100_2040021_48.out
│   ├── batch_ref_4_budget_100_2040021_49.err
│   ├── batch_ref_4_budget_100_2040021_49.out
│   ├── batch_ref_4_budget_100_2040021_5.err
│   ├── batch_ref_4_budget_100_2040021_5.out
│   ├── batch_ref_4_budget_100_2040021_50.err
│   ├── batch_ref_4_budget_100_2040021_50.out
│   ├── batch_ref_4_budget_100_2040021_51.err
│   ├── batch_ref_4_budget_100_2040021_51.out
│   ├── batch_ref_4_budget_100_2040021_52.err
│   ├── batch_ref_4_budget_100_2040021_52.out
│   ├── batch_ref_4_budget_100_2040021_53.err
│   ├── batch_ref_4_budget_100_2040021_53.out
│   ├── batch_ref_4_budget_100_2040021_54.err
│   ├── batch_ref_4_budget_100_2040021_54.out
│   ├── batch_ref_4_budget_100_2040021_55.err
│   ├── batch_ref_4_budget_100_2040021_55.out
│   ├── batch_ref_4_budget_100_2040021_56.err
│   ├── batch_ref_4_budget_100_2040021_56.out
│   ├── batch_ref_4_budget_100_2040021_57.err
│   ├── batch_ref_4_budget_100_2040021_57.out
│   ├── batch_ref_4_budget_100_2040021_58.err
│   ├── batch_ref_4_budget_100_2040021_58.out
│   ├── batch_ref_4_budget_100_2040021_59.err
│   ├── batch_ref_4_budget_100_2040021_59.out
│   ├── batch_ref_4_budget_100_2040021_6.err
│   ├── batch_ref_4_budget_100_2040021_6.out
│   ├── batch_ref_4_budget_100_2040021_60.err
│   ├── batch_ref_4_budget_100_2040021_60.out
│   ├── batch_ref_4_budget_100_2040021_61.err
│   ├── batch_ref_4_budget_100_2040021_61.out
│   ├── batch_ref_4_budget_100_2040021_62.err
│   ├── batch_ref_4_budget_100_2040021_62.out
│   ├── batch_ref_4_budget_100_2040021_63.err
│   ├── batch_ref_4_budget_100_2040021_63.out
│   ├── batch_ref_4_budget_100_2040021_64.err
│   ├── batch_ref_4_budget_100_2040021_64.out
│   ├── batch_ref_4_budget_100_2040021_65.err
│   ├── batch_ref_4_budget_100_2040021_65.out
│   ├── batch_ref_4_budget_100_2040021_66.err
│   ├── batch_ref_4_budget_100_2040021_66.out
│   ├── batch_ref_4_budget_100_2040021_67.err
│   ├── batch_ref_4_budget_100_2040021_67.out
│   ├── batch_ref_4_budget_100_2040021_68.err
│   ├── batch_ref_4_budget_100_2040021_68.out
│   ├── batch_ref_4_budget_100_2040021_69.err
│   ├── batch_ref_4_budget_100_2040021_69.out
│   ├── batch_ref_4_budget_100_2040021_7.err
│   ├── batch_ref_4_budget_100_2040021_7.out
│   ├── batch_ref_4_budget_100_2040021_70.err
│   ├── batch_ref_4_budget_100_2040021_70.out
│   ├── batch_ref_4_budget_100_2040021_71.err
│   ├── batch_ref_4_budget_100_2040021_71.out
│   ├── batch_ref_4_budget_100_2040021_72.err
│   ├── batch_ref_4_budget_100_2040021_72.out
│   ├── batch_ref_4_budget_100_2040021_73.err
│   ├── batch_ref_4_budget_100_2040021_73.out
│   ├── batch_ref_4_budget_100_2040021_74.err
│   ├── batch_ref_4_budget_100_2040021_74.out
│   ├── batch_ref_4_budget_100_2040021_75.err
│   ├── batch_ref_4_budget_100_2040021_75.out
│   ├── batch_ref_4_budget_100_2040021_76.err
│   ├── batch_ref_4_budget_100_2040021_76.out
│   ├── batch_ref_4_budget_100_2040021_77.err
│   ├── batch_ref_4_budget_100_2040021_77.out
│   ├── batch_ref_4_budget_100_2040021_78.err
│   ├── batch_ref_4_budget_100_2040021_78.out
│   ├── batch_ref_4_budget_100_2040021_79.err
│   ├── batch_ref_4_budget_100_2040021_79.out
│   ├── batch_ref_4_budget_100_2040021_8.err
│   ├── batch_ref_4_budget_100_2040021_8.out
│   ├── batch_ref_4_budget_100_2040021_80.err
│   ├── batch_ref_4_budget_100_2040021_80.out
│   ├── batch_ref_4_budget_100_2040021_81.err
│   ├── batch_ref_4_budget_100_2040021_81.out
│   ├── batch_ref_4_budget_100_2040021_9.err
│   ├── batch_ref_4_budget_100_2040021_9.out
│   ├── batch_ref_4_budget_100_max_4_2067209_1.err
│   ├── batch_ref_4_budget_100_max_4_2067209_1.out
│   ├── batch_ref_4_budget_100_max_4_2067209_10.err
│   ├── batch_ref_4_budget_100_max_4_2067209_10.out
│   ├── batch_ref_4_budget_100_max_4_2067209_11.err
│   ├── batch_ref_4_budget_100_max_4_2067209_11.out
│   ├── batch_ref_4_budget_100_max_4_2067209_12.err
│   ├── batch_ref_4_budget_100_max_4_2067209_12.out
│   ├── batch_ref_4_budget_100_max_4_2067209_13.err
│   ├── batch_ref_4_budget_100_max_4_2067209_13.out
│   ├── batch_ref_4_budget_100_max_4_2067209_14.err
│   ├── batch_ref_4_budget_100_max_4_2067209_14.out
│   ├── batch_ref_4_budget_100_max_4_2067209_15.err
│   ├── batch_ref_4_budget_100_max_4_2067209_15.out
│   ├── batch_ref_4_budget_100_max_4_2067209_16.err
│   ├── batch_ref_4_budget_100_max_4_2067209_16.out
│   ├── batch_ref_4_budget_100_max_4_2067209_17.err
│   ├── batch_ref_4_budget_100_max_4_2067209_17.out
│   ├── batch_ref_4_budget_100_max_4_2067209_18.err
│   ├── batch_ref_4_budget_100_max_4_2067209_18.out
│   ├── batch_ref_4_budget_100_max_4_2067209_19.err
│   ├── batch_ref_4_budget_100_max_4_2067209_19.out
│   ├── batch_ref_4_budget_100_max_4_2067209_2.err
│   ├── batch_ref_4_budget_100_max_4_2067209_2.out
│   ├── batch_ref_4_budget_100_max_4_2067209_20.err
│   ├── batch_ref_4_budget_100_max_4_2067209_20.out
│   ├── batch_ref_4_budget_100_max_4_2067209_21.err
│   ├── batch_ref_4_budget_100_max_4_2067209_21.out
│   ├── batch_ref_4_budget_100_max_4_2067209_22.err
│   ├── batch_ref_4_budget_100_max_4_2067209_22.out
│   ├── batch_ref_4_budget_100_max_4_2067209_23.err
│   ├── batch_ref_4_budget_100_max_4_2067209_23.out
│   ├── batch_ref_4_budget_100_max_4_2067209_24.err
│   ├── batch_ref_4_budget_100_max_4_2067209_24.out
│   ├── batch_ref_4_budget_100_max_4_2067209_25.err
│   ├── batch_ref_4_budget_100_max_4_2067209_25.out
│   ├── batch_ref_4_budget_100_max_4_2067209_26.err
│   ├── batch_ref_4_budget_100_max_4_2067209_26.out
│   ├── batch_ref_4_budget_100_max_4_2067209_27.err
│   ├── batch_ref_4_budget_100_max_4_2067209_27.out
│   ├── batch_ref_4_budget_100_max_4_2067209_28.err
│   ├── batch_ref_4_budget_100_max_4_2067209_28.out
│   ├── batch_ref_4_budget_100_max_4_2067209_29.err
│   ├── batch_ref_4_budget_100_max_4_2067209_29.out
│   ├── batch_ref_4_budget_100_max_4_2067209_3.err
│   ├── batch_ref_4_budget_100_max_4_2067209_3.out
│   ├── batch_ref_4_budget_100_max_4_2067209_30.err
│   ├── batch_ref_4_budget_100_max_4_2067209_30.out
│   ├── batch_ref_4_budget_100_max_4_2067209_31.err
│   ├── batch_ref_4_budget_100_max_4_2067209_31.out
│   ├── batch_ref_4_budget_100_max_4_2067209_32.err
│   ├── batch_ref_4_budget_100_max_4_2067209_32.out
│   ├── batch_ref_4_budget_100_max_4_2067209_33.err
│   ├── batch_ref_4_budget_100_max_4_2067209_33.out
│   ├── batch_ref_4_budget_100_max_4_2067209_34.err
│   ├── batch_ref_4_budget_100_max_4_2067209_34.out
│   ├── batch_ref_4_budget_100_max_4_2067209_35.err
│   ├── batch_ref_4_budget_100_max_4_2067209_35.out
│   ├── batch_ref_4_budget_100_max_4_2067209_36.err
│   ├── batch_ref_4_budget_100_max_4_2067209_36.out
│   ├── batch_ref_4_budget_100_max_4_2067209_37.err
│   ├── batch_ref_4_budget_100_max_4_2067209_37.out
│   ├── batch_ref_4_budget_100_max_4_2067209_38.err
│   ├── batch_ref_4_budget_100_max_4_2067209_38.out
│   ├── batch_ref_4_budget_100_max_4_2067209_39.err
│   ├── batch_ref_4_budget_100_max_4_2067209_39.out
│   ├── batch_ref_4_budget_100_max_4_2067209_4.err
│   ├── batch_ref_4_budget_100_max_4_2067209_4.out
│   ├── batch_ref_4_budget_100_max_4_2067209_40.err
│   ├── batch_ref_4_budget_100_max_4_2067209_40.out
│   ├── batch_ref_4_budget_100_max_4_2067209_41.err
│   ├── batch_ref_4_budget_100_max_4_2067209_41.out
│   ├── batch_ref_4_budget_100_max_4_2067209_42.err
│   ├── batch_ref_4_budget_100_max_4_2067209_42.out
│   ├── batch_ref_4_budget_100_max_4_2067209_43.err
│   ├── batch_ref_4_budget_100_max_4_2067209_43.out
│   ├── batch_ref_4_budget_100_max_4_2067209_44.err
│   ├── batch_ref_4_budget_100_max_4_2067209_44.out
│   ├── batch_ref_4_budget_100_max_4_2067209_45.err
│   ├── batch_ref_4_budget_100_max_4_2067209_45.out
│   ├── batch_ref_4_budget_100_max_4_2067209_46.err
│   ├── batch_ref_4_budget_100_max_4_2067209_46.out
│   ├── batch_ref_4_budget_100_max_4_2067209_47.err
│   ├── batch_ref_4_budget_100_max_4_2067209_47.out
│   ├── batch_ref_4_budget_100_max_4_2067209_48.err
│   ├── batch_ref_4_budget_100_max_4_2067209_48.out
│   ├── batch_ref_4_budget_100_max_4_2067209_49.err
│   ├── batch_ref_4_budget_100_max_4_2067209_49.out
│   ├── batch_ref_4_budget_100_max_4_2067209_5.err
│   ├── batch_ref_4_budget_100_max_4_2067209_5.out
│   ├── batch_ref_4_budget_100_max_4_2067209_50.err
│   ├── batch_ref_4_budget_100_max_4_2067209_50.out
│   ├── batch_ref_4_budget_100_max_4_2067209_51.err
│   ├── batch_ref_4_budget_100_max_4_2067209_51.out
│   ├── batch_ref_4_budget_100_max_4_2067209_52.err
│   ├── batch_ref_4_budget_100_max_4_2067209_52.out
│   ├── batch_ref_4_budget_100_max_4_2067209_53.err
│   ├── batch_ref_4_budget_100_max_4_2067209_53.out
│   ├── batch_ref_4_budget_100_max_4_2067209_54.err
│   ├── batch_ref_4_budget_100_max_4_2067209_54.out
│   ├── batch_ref_4_budget_100_max_4_2067209_55.err
│   ├── batch_ref_4_budget_100_max_4_2067209_55.out
│   ├── batch_ref_4_budget_100_max_4_2067209_56.err
│   ├── batch_ref_4_budget_100_max_4_2067209_56.out
│   ├── batch_ref_4_budget_100_max_4_2067209_57.err
│   ├── batch_ref_4_budget_100_max_4_2067209_57.out
│   ├── batch_ref_4_budget_100_max_4_2067209_58.err
│   ├── batch_ref_4_budget_100_max_4_2067209_58.out
│   ├── batch_ref_4_budget_100_max_4_2067209_59.err
│   ├── batch_ref_4_budget_100_max_4_2067209_59.out
│   ├── batch_ref_4_budget_100_max_4_2067209_6.err
│   ├── batch_ref_4_budget_100_max_4_2067209_6.out
│   ├── batch_ref_4_budget_100_max_4_2067209_60.err
│   ├── batch_ref_4_budget_100_max_4_2067209_60.out
│   ├── batch_ref_4_budget_100_max_4_2067209_61.err
│   ├── batch_ref_4_budget_100_max_4_2067209_61.out
│   ├── batch_ref_4_budget_100_max_4_2067209_62.err
│   ├── batch_ref_4_budget_100_max_4_2067209_62.out
│   ├── batch_ref_4_budget_100_max_4_2067209_63.err
│   ├── batch_ref_4_budget_100_max_4_2067209_63.out
│   ├── batch_ref_4_budget_100_max_4_2067209_64.err
│   ├── batch_ref_4_budget_100_max_4_2067209_64.out
│   ├── batch_ref_4_budget_100_max_4_2067209_65.err
│   ├── batch_ref_4_budget_100_max_4_2067209_65.out
│   ├── batch_ref_4_budget_100_max_4_2067209_66.err
│   ├── batch_ref_4_budget_100_max_4_2067209_66.out
│   ├── batch_ref_4_budget_100_max_4_2067209_67.err
│   ├── batch_ref_4_budget_100_max_4_2067209_67.out
│   ├── batch_ref_4_budget_100_max_4_2067209_68.err
│   ├── batch_ref_4_budget_100_max_4_2067209_68.out
│   ├── batch_ref_4_budget_100_max_4_2067209_69.err
│   ├── batch_ref_4_budget_100_max_4_2067209_69.out
│   ├── batch_ref_4_budget_100_max_4_2067209_7.err
│   ├── batch_ref_4_budget_100_max_4_2067209_7.out
│   ├── batch_ref_4_budget_100_max_4_2067209_70.err
│   ├── batch_ref_4_budget_100_max_4_2067209_70.out
│   ├── batch_ref_4_budget_100_max_4_2067209_71.err
│   ├── batch_ref_4_budget_100_max_4_2067209_71.out
│   ├── batch_ref_4_budget_100_max_4_2067209_72.err
│   ├── batch_ref_4_budget_100_max_4_2067209_72.out
│   ├── batch_ref_4_budget_100_max_4_2067209_73.err
│   ├── batch_ref_4_budget_100_max_4_2067209_73.out
│   ├── batch_ref_4_budget_100_max_4_2067209_74.err
│   ├── batch_ref_4_budget_100_max_4_2067209_74.out
│   ├── batch_ref_4_budget_100_max_4_2067209_75.err
│   ├── batch_ref_4_budget_100_max_4_2067209_75.out
│   ├── batch_ref_4_budget_100_max_4_2067209_76.err
│   ├── batch_ref_4_budget_100_max_4_2067209_76.out
│   ├── batch_ref_4_budget_100_max_4_2067209_77.err
│   ├── batch_ref_4_budget_100_max_4_2067209_77.out
│   ├── batch_ref_4_budget_100_max_4_2067209_78.err
│   ├── batch_ref_4_budget_100_max_4_2067209_78.out
│   ├── batch_ref_4_budget_100_max_4_2067209_79.err
│   ├── batch_ref_4_budget_100_max_4_2067209_79.out
│   ├── batch_ref_4_budget_100_max_4_2067209_8.err
│   ├── batch_ref_4_budget_100_max_4_2067209_8.out
│   ├── batch_ref_4_budget_100_max_4_2067209_80.err
│   ├── batch_ref_4_budget_100_max_4_2067209_80.out
│   ├── batch_ref_4_budget_100_max_4_2067209_81.err
│   ├── batch_ref_4_budget_100_max_4_2067209_81.out
│   ├── batch_ref_4_budget_100_max_4_2067209_9.err
│   ├── batch_ref_4_budget_100_max_4_2067209_9.out
│   ├── batch_ref_4_budget_150_2038355_1.err
│   ├── batch_ref_4_budget_150_2038355_1.out
│   ├── batch_ref_4_budget_150_2038355_10.err
│   ├── batch_ref_4_budget_150_2038355_10.out
│   ├── batch_ref_4_budget_150_2038355_11.err
│   ├── batch_ref_4_budget_150_2038355_11.out
│   ├── batch_ref_4_budget_150_2038355_12.err
│   ├── batch_ref_4_budget_150_2038355_12.out
│   ├── batch_ref_4_budget_150_2038355_13.err
│   ├── batch_ref_4_budget_150_2038355_13.out
│   ├── batch_ref_4_budget_150_2038355_14.err
│   ├── batch_ref_4_budget_150_2038355_14.out
│   ├── batch_ref_4_budget_150_2038355_15.err
│   ├── batch_ref_4_budget_150_2038355_15.out
│   ├── batch_ref_4_budget_150_2038355_16.err
│   ├── batch_ref_4_budget_150_2038355_16.out
│   ├── batch_ref_4_budget_150_2038355_17.err
│   ├── batch_ref_4_budget_150_2038355_17.out
│   ├── batch_ref_4_budget_150_2038355_18.err
│   ├── batch_ref_4_budget_150_2038355_18.out
│   ├── batch_ref_4_budget_150_2038355_19.err
│   ├── batch_ref_4_budget_150_2038355_19.out
│   ├── batch_ref_4_budget_150_2038355_2.err
│   ├── batch_ref_4_budget_150_2038355_2.out
│   ├── batch_ref_4_budget_150_2038355_20.err
│   ├── batch_ref_4_budget_150_2038355_20.out
│   ├── batch_ref_4_budget_150_2038355_21.err
│   ├── batch_ref_4_budget_150_2038355_21.out
│   ├── batch_ref_4_budget_150_2038355_22.err
│   ├── batch_ref_4_budget_150_2038355_22.out
│   ├── batch_ref_4_budget_150_2038355_23.err
│   ├── batch_ref_4_budget_150_2038355_23.out
│   ├── batch_ref_4_budget_150_2038355_24.err
│   ├── batch_ref_4_budget_150_2038355_24.out
│   ├── batch_ref_4_budget_150_2038355_25.err
│   ├── batch_ref_4_budget_150_2038355_25.out
│   ├── batch_ref_4_budget_150_2038355_26.err
│   ├── batch_ref_4_budget_150_2038355_26.out
│   ├── batch_ref_4_budget_150_2038355_27.err
│   ├── batch_ref_4_budget_150_2038355_27.out
│   ├── batch_ref_4_budget_150_2038355_28.err
│   ├── batch_ref_4_budget_150_2038355_28.out
│   ├── batch_ref_4_budget_150_2038355_29.err
│   ├── batch_ref_4_budget_150_2038355_29.out
│   ├── batch_ref_4_budget_150_2038355_3.err
│   ├── batch_ref_4_budget_150_2038355_3.out
│   ├── batch_ref_4_budget_150_2038355_30.err
│   ├── batch_ref_4_budget_150_2038355_30.out
│   ├── batch_ref_4_budget_150_2038355_31.err
│   ├── batch_ref_4_budget_150_2038355_31.out
│   ├── batch_ref_4_budget_150_2038355_32.err
│   ├── batch_ref_4_budget_150_2038355_32.out
│   ├── batch_ref_4_budget_150_2038355_33.err
│   ├── batch_ref_4_budget_150_2038355_33.out
│   ├── batch_ref_4_budget_150_2038355_34.err
│   ├── batch_ref_4_budget_150_2038355_34.out
│   ├── batch_ref_4_budget_150_2038355_35.err
│   ├── batch_ref_4_budget_150_2038355_35.out
│   ├── batch_ref_4_budget_150_2038355_36.err
│   ├── batch_ref_4_budget_150_2038355_36.out
│   ├── batch_ref_4_budget_150_2038355_37.err
│   ├── batch_ref_4_budget_150_2038355_37.out
│   ├── batch_ref_4_budget_150_2038355_38.err
│   ├── batch_ref_4_budget_150_2038355_38.out
│   ├── batch_ref_4_budget_150_2038355_39.err
│   ├── batch_ref_4_budget_150_2038355_39.out
│   ├── batch_ref_4_budget_150_2038355_4.err
│   ├── batch_ref_4_budget_150_2038355_4.out
│   ├── batch_ref_4_budget_150_2038355_40.err
│   ├── batch_ref_4_budget_150_2038355_40.out
│   ├── batch_ref_4_budget_150_2038355_41.err
│   ├── batch_ref_4_budget_150_2038355_41.out
│   ├── batch_ref_4_budget_150_2038355_42.err
│   ├── batch_ref_4_budget_150_2038355_42.out
│   ├── batch_ref_4_budget_150_2038355_43.err
│   ├── batch_ref_4_budget_150_2038355_43.out
│   ├── batch_ref_4_budget_150_2038355_44.err
│   ├── batch_ref_4_budget_150_2038355_44.out
│   ├── batch_ref_4_budget_150_2038355_45.err
│   ├── batch_ref_4_budget_150_2038355_45.out
│   ├── batch_ref_4_budget_150_2038355_46.err
│   ├── batch_ref_4_budget_150_2038355_46.out
│   ├── batch_ref_4_budget_150_2038355_47.err
│   ├── batch_ref_4_budget_150_2038355_47.out
│   ├── batch_ref_4_budget_150_2038355_48.err
│   ├── batch_ref_4_budget_150_2038355_48.out
│   ├── batch_ref_4_budget_150_2038355_49.err
│   ├── batch_ref_4_budget_150_2038355_49.out
│   ├── batch_ref_4_budget_150_2038355_5.err
│   ├── batch_ref_4_budget_150_2038355_5.out
│   ├── batch_ref_4_budget_150_2038355_50.err
│   ├── batch_ref_4_budget_150_2038355_50.out
│   ├── batch_ref_4_budget_150_2038355_51.err
│   ├── batch_ref_4_budget_150_2038355_51.out
│   ├── batch_ref_4_budget_150_2038355_52.err
│   ├── batch_ref_4_budget_150_2038355_52.out
│   ├── batch_ref_4_budget_150_2038355_53.err
│   ├── batch_ref_4_budget_150_2038355_53.out
│   ├── batch_ref_4_budget_150_2038355_54.err
│   ├── batch_ref_4_budget_150_2038355_54.out
│   ├── batch_ref_4_budget_150_2038355_55.err
│   ├── batch_ref_4_budget_150_2038355_55.out
│   ├── batch_ref_4_budget_150_2038355_56.err
│   ├── batch_ref_4_budget_150_2038355_56.out
│   ├── batch_ref_4_budget_150_2038355_57.err
│   ├── batch_ref_4_budget_150_2038355_57.out
│   ├── batch_ref_4_budget_150_2038355_58.err
│   ├── batch_ref_4_budget_150_2038355_58.out
│   ├── batch_ref_4_budget_150_2038355_59.err
│   ├── batch_ref_4_budget_150_2038355_59.out
│   ├── batch_ref_4_budget_150_2038355_6.err
│   ├── batch_ref_4_budget_150_2038355_6.out
│   ├── batch_ref_4_budget_150_2038355_60.err
│   ├── batch_ref_4_budget_150_2038355_60.out
│   ├── batch_ref_4_budget_150_2038355_61.err
│   ├── batch_ref_4_budget_150_2038355_61.out
│   ├── batch_ref_4_budget_150_2038355_62.err
│   ├── batch_ref_4_budget_150_2038355_62.out
│   ├── batch_ref_4_budget_150_2038355_63.err
│   ├── batch_ref_4_budget_150_2038355_63.out
│   ├── batch_ref_4_budget_150_2038355_64.err
│   ├── batch_ref_4_budget_150_2038355_64.out
│   ├── batch_ref_4_budget_150_2038355_65.err
│   ├── batch_ref_4_budget_150_2038355_65.out
│   ├── batch_ref_4_budget_150_2038355_66.err
│   ├── batch_ref_4_budget_150_2038355_66.out
│   ├── batch_ref_4_budget_150_2038355_67.err
│   ├── batch_ref_4_budget_150_2038355_67.out
│   ├── batch_ref_4_budget_150_2038355_68.err
│   ├── batch_ref_4_budget_150_2038355_68.out
│   ├── batch_ref_4_budget_150_2038355_69.err
│   ├── batch_ref_4_budget_150_2038355_69.out
│   ├── batch_ref_4_budget_150_2038355_7.err
│   ├── batch_ref_4_budget_150_2038355_7.out
│   ├── batch_ref_4_budget_150_2038355_70.err
│   ├── batch_ref_4_budget_150_2038355_70.out
│   ├── batch_ref_4_budget_150_2038355_71.err
│   ├── batch_ref_4_budget_150_2038355_71.out
│   ├── batch_ref_4_budget_150_2038355_72.err
│   ├── batch_ref_4_budget_150_2038355_72.out
│   ├── batch_ref_4_budget_150_2038355_73.err
│   ├── batch_ref_4_budget_150_2038355_73.out
│   ├── batch_ref_4_budget_150_2038355_74.err
│   ├── batch_ref_4_budget_150_2038355_74.out
│   ├── batch_ref_4_budget_150_2038355_75.err
│   ├── batch_ref_4_budget_150_2038355_75.out
│   ├── batch_ref_4_budget_150_2038355_76.err
│   ├── batch_ref_4_budget_150_2038355_76.out
│   ├── batch_ref_4_budget_150_2038355_77.err
│   ├── batch_ref_4_budget_150_2038355_77.out
│   ├── batch_ref_4_budget_150_2038355_78.err
│   ├── batch_ref_4_budget_150_2038355_78.out
│   ├── batch_ref_4_budget_150_2038355_79.err
│   ├── batch_ref_4_budget_150_2038355_79.out
│   ├── batch_ref_4_budget_150_2038355_8.err
│   ├── batch_ref_4_budget_150_2038355_8.out
│   ├── batch_ref_4_budget_150_2038355_80.err
│   ├── batch_ref_4_budget_150_2038355_80.out
│   ├── batch_ref_4_budget_150_2038355_81.err
│   ├── batch_ref_4_budget_150_2038355_81.out
│   ├── batch_ref_4_budget_150_2038355_9.err
│   ├── batch_ref_4_budget_150_2038355_9.out
│   ├── batch_ref_4_budget_150_2040022_1.err
│   ├── batch_ref_4_budget_150_2040022_1.out
│   ├── batch_ref_4_budget_150_2040022_10.err
│   ├── batch_ref_4_budget_150_2040022_10.out
│   ├── batch_ref_4_budget_150_2040022_11.err
│   ├── batch_ref_4_budget_150_2040022_11.out
│   ├── batch_ref_4_budget_150_2040022_12.err
│   ├── batch_ref_4_budget_150_2040022_12.out
│   ├── batch_ref_4_budget_150_2040022_13.err
│   ├── batch_ref_4_budget_150_2040022_13.out
│   ├── batch_ref_4_budget_150_2040022_14.err
│   ├── batch_ref_4_budget_150_2040022_14.out
│   ├── batch_ref_4_budget_150_2040022_15.err
│   ├── batch_ref_4_budget_150_2040022_15.out
│   ├── batch_ref_4_budget_150_2040022_16.err
│   ├── batch_ref_4_budget_150_2040022_16.out
│   ├── batch_ref_4_budget_150_2040022_17.err
│   ├── batch_ref_4_budget_150_2040022_17.out
│   ├── batch_ref_4_budget_150_2040022_18.err
│   ├── batch_ref_4_budget_150_2040022_18.out
│   ├── batch_ref_4_budget_150_2040022_19.err
│   ├── batch_ref_4_budget_150_2040022_19.out
│   ├── batch_ref_4_budget_150_2040022_2.err
│   ├── batch_ref_4_budget_150_2040022_2.out
│   ├── batch_ref_4_budget_150_2040022_20.err
│   ├── batch_ref_4_budget_150_2040022_20.out
│   ├── batch_ref_4_budget_150_2040022_21.err
│   ├── batch_ref_4_budget_150_2040022_21.out
│   ├── batch_ref_4_budget_150_2040022_22.err
│   ├── batch_ref_4_budget_150_2040022_22.out
│   ├── batch_ref_4_budget_150_2040022_23.err
│   ├── batch_ref_4_budget_150_2040022_23.out
│   ├── batch_ref_4_budget_150_2040022_24.err
│   ├── batch_ref_4_budget_150_2040022_24.out
│   ├── batch_ref_4_budget_150_2040022_25.err
│   ├── batch_ref_4_budget_150_2040022_25.out
│   ├── batch_ref_4_budget_150_2040022_26.err
│   ├── batch_ref_4_budget_150_2040022_26.out
│   ├── batch_ref_4_budget_150_2040022_27.err
│   ├── batch_ref_4_budget_150_2040022_27.out
│   ├── batch_ref_4_budget_150_2040022_28.err
│   ├── batch_ref_4_budget_150_2040022_28.out
│   ├── batch_ref_4_budget_150_2040022_29.err
│   ├── batch_ref_4_budget_150_2040022_29.out
│   ├── batch_ref_4_budget_150_2040022_3.err
│   ├── batch_ref_4_budget_150_2040022_3.out
│   ├── batch_ref_4_budget_150_2040022_30.err
│   ├── batch_ref_4_budget_150_2040022_30.out
│   ├── batch_ref_4_budget_150_2040022_31.err
│   ├── batch_ref_4_budget_150_2040022_31.out
│   ├── batch_ref_4_budget_150_2040022_32.err
│   ├── batch_ref_4_budget_150_2040022_32.out
│   ├── batch_ref_4_budget_150_2040022_33.err
│   ├── batch_ref_4_budget_150_2040022_33.out
│   ├── batch_ref_4_budget_150_2040022_34.err
│   ├── batch_ref_4_budget_150_2040022_34.out
│   ├── batch_ref_4_budget_150_2040022_35.err
│   ├── batch_ref_4_budget_150_2040022_35.out
│   ├── batch_ref_4_budget_150_2040022_36.err
│   ├── batch_ref_4_budget_150_2040022_36.out
│   ├── batch_ref_4_budget_150_2040022_37.err
│   ├── batch_ref_4_budget_150_2040022_37.out
│   ├── batch_ref_4_budget_150_2040022_38.err
│   ├── batch_ref_4_budget_150_2040022_38.out
│   ├── batch_ref_4_budget_150_2040022_39.err
│   ├── batch_ref_4_budget_150_2040022_39.out
│   ├── batch_ref_4_budget_150_2040022_4.err
│   ├── batch_ref_4_budget_150_2040022_4.out
│   ├── batch_ref_4_budget_150_2040022_40.err
│   ├── batch_ref_4_budget_150_2040022_40.out
│   ├── batch_ref_4_budget_150_2040022_41.err
│   ├── batch_ref_4_budget_150_2040022_41.out
│   ├── batch_ref_4_budget_150_2040022_42.err
│   ├── batch_ref_4_budget_150_2040022_42.out
│   ├── batch_ref_4_budget_150_2040022_43.err
│   ├── batch_ref_4_budget_150_2040022_43.out
│   ├── batch_ref_4_budget_150_2040022_44.err
│   ├── batch_ref_4_budget_150_2040022_44.out
│   ├── batch_ref_4_budget_150_2040022_45.err
│   ├── batch_ref_4_budget_150_2040022_45.out
│   ├── batch_ref_4_budget_150_2040022_46.err
│   ├── batch_ref_4_budget_150_2040022_46.out
│   ├── batch_ref_4_budget_150_2040022_47.err
│   ├── batch_ref_4_budget_150_2040022_47.out
│   ├── batch_ref_4_budget_150_2040022_48.err
│   ├── batch_ref_4_budget_150_2040022_48.out
│   ├── batch_ref_4_budget_150_2040022_49.err
│   ├── batch_ref_4_budget_150_2040022_49.out
│   ├── batch_ref_4_budget_150_2040022_5.err
│   ├── batch_ref_4_budget_150_2040022_5.out
│   ├── batch_ref_4_budget_150_2040022_50.err
│   ├── batch_ref_4_budget_150_2040022_50.out
│   ├── batch_ref_4_budget_150_2040022_51.err
│   ├── batch_ref_4_budget_150_2040022_51.out
│   ├── batch_ref_4_budget_150_2040022_52.err
│   ├── batch_ref_4_budget_150_2040022_52.out
│   ├── batch_ref_4_budget_150_2040022_53.err
│   ├── batch_ref_4_budget_150_2040022_53.out
│   ├── batch_ref_4_budget_150_2040022_54.err
│   ├── batch_ref_4_budget_150_2040022_54.out
│   ├── batch_ref_4_budget_150_2040022_55.err
│   ├── batch_ref_4_budget_150_2040022_55.out
│   ├── batch_ref_4_budget_150_2040022_56.err
│   ├── batch_ref_4_budget_150_2040022_56.out
│   ├── batch_ref_4_budget_150_2040022_57.err
│   ├── batch_ref_4_budget_150_2040022_57.out
│   ├── batch_ref_4_budget_150_2040022_58.err
│   ├── batch_ref_4_budget_150_2040022_58.out
│   ├── batch_ref_4_budget_150_2040022_59.err
│   ├── batch_ref_4_budget_150_2040022_59.out
│   ├── batch_ref_4_budget_150_2040022_6.err
│   ├── batch_ref_4_budget_150_2040022_6.out
│   ├── batch_ref_4_budget_150_2040022_60.err
│   ├── batch_ref_4_budget_150_2040022_60.out
│   ├── batch_ref_4_budget_150_2040022_61.err
│   ├── batch_ref_4_budget_150_2040022_61.out
│   ├── batch_ref_4_budget_150_2040022_62.err
│   ├── batch_ref_4_budget_150_2040022_62.out
│   ├── batch_ref_4_budget_150_2040022_63.err
│   ├── batch_ref_4_budget_150_2040022_63.out
│   ├── batch_ref_4_budget_150_2040022_64.err
│   ├── batch_ref_4_budget_150_2040022_64.out
│   ├── batch_ref_4_budget_150_2040022_65.err
│   ├── batch_ref_4_budget_150_2040022_65.out
│   ├── batch_ref_4_budget_150_2040022_66.err
│   ├── batch_ref_4_budget_150_2040022_66.out
│   ├── batch_ref_4_budget_150_2040022_67.err
│   ├── batch_ref_4_budget_150_2040022_67.out
│   ├── batch_ref_4_budget_150_2040022_68.err
│   ├── batch_ref_4_budget_150_2040022_68.out
│   ├── batch_ref_4_budget_150_2040022_69.err
│   ├── batch_ref_4_budget_150_2040022_69.out
│   ├── batch_ref_4_budget_150_2040022_7.err
│   ├── batch_ref_4_budget_150_2040022_7.out
│   ├── batch_ref_4_budget_150_2040022_70.err
│   ├── batch_ref_4_budget_150_2040022_70.out
│   ├── batch_ref_4_budget_150_2040022_71.err
│   ├── batch_ref_4_budget_150_2040022_71.out
│   ├── batch_ref_4_budget_150_2040022_72.err
│   ├── batch_ref_4_budget_150_2040022_72.out
│   ├── batch_ref_4_budget_150_2040022_73.err
│   ├── batch_ref_4_budget_150_2040022_73.out
│   ├── batch_ref_4_budget_150_2040022_74.err
│   ├── batch_ref_4_budget_150_2040022_74.out
│   ├── batch_ref_4_budget_150_2040022_75.err
│   ├── batch_ref_4_budget_150_2040022_75.out
│   ├── batch_ref_4_budget_150_2040022_76.err
│   ├── batch_ref_4_budget_150_2040022_76.out
│   ├── batch_ref_4_budget_150_2040022_77.err
│   ├── batch_ref_4_budget_150_2040022_77.out
│   ├── batch_ref_4_budget_150_2040022_78.err
│   ├── batch_ref_4_budget_150_2040022_78.out
│   ├── batch_ref_4_budget_150_2040022_79.err
│   ├── batch_ref_4_budget_150_2040022_79.out
│   ├── batch_ref_4_budget_150_2040022_8.err
│   ├── batch_ref_4_budget_150_2040022_8.out
│   ├── batch_ref_4_budget_150_2040022_80.err
│   ├── batch_ref_4_budget_150_2040022_80.out
│   ├── batch_ref_4_budget_150_2040022_81.err
│   ├── batch_ref_4_budget_150_2040022_81.out
│   ├── batch_ref_4_budget_150_2040022_9.err
│   ├── batch_ref_4_budget_150_2040022_9.out
│   ├── batch_ref_4_budget_200_2038356_1.err
│   ├── batch_ref_4_budget_200_2038356_1.out
│   ├── batch_ref_4_budget_200_2038356_10.err
│   ├── batch_ref_4_budget_200_2038356_10.out
│   ├── batch_ref_4_budget_200_2038356_11.err
│   ├── batch_ref_4_budget_200_2038356_11.out
│   ├── batch_ref_4_budget_200_2038356_12.err
│   ├── batch_ref_4_budget_200_2038356_12.out
│   ├── batch_ref_4_budget_200_2038356_13.err
│   ├── batch_ref_4_budget_200_2038356_13.out
│   ├── batch_ref_4_budget_200_2038356_14.err
│   ├── batch_ref_4_budget_200_2038356_14.out
│   ├── batch_ref_4_budget_200_2038356_15.err
│   ├── batch_ref_4_budget_200_2038356_15.out
│   ├── batch_ref_4_budget_200_2038356_16.err
│   ├── batch_ref_4_budget_200_2038356_16.out
│   ├── batch_ref_4_budget_200_2038356_17.err
│   ├── batch_ref_4_budget_200_2038356_17.out
│   ├── batch_ref_4_budget_200_2038356_18.err
│   ├── batch_ref_4_budget_200_2038356_18.out
│   ├── batch_ref_4_budget_200_2038356_19.err
│   ├── batch_ref_4_budget_200_2038356_19.out
│   ├── batch_ref_4_budget_200_2038356_2.err
│   ├── batch_ref_4_budget_200_2038356_2.out
│   ├── batch_ref_4_budget_200_2038356_20.err
│   ├── batch_ref_4_budget_200_2038356_20.out
│   ├── batch_ref_4_budget_200_2038356_21.err
│   ├── batch_ref_4_budget_200_2038356_21.out
│   ├── batch_ref_4_budget_200_2038356_22.err
│   ├── batch_ref_4_budget_200_2038356_22.out
│   ├── batch_ref_4_budget_200_2038356_23.err
│   ├── batch_ref_4_budget_200_2038356_23.out
│   ├── batch_ref_4_budget_200_2038356_24.err
│   ├── batch_ref_4_budget_200_2038356_24.out
│   ├── batch_ref_4_budget_200_2038356_25.err
│   ├── batch_ref_4_budget_200_2038356_25.out
│   ├── batch_ref_4_budget_200_2038356_26.err
│   ├── batch_ref_4_budget_200_2038356_26.out
│   ├── batch_ref_4_budget_200_2038356_27.err
│   ├── batch_ref_4_budget_200_2038356_27.out
│   ├── batch_ref_4_budget_200_2038356_28.err
│   ├── batch_ref_4_budget_200_2038356_28.out
│   ├── batch_ref_4_budget_200_2038356_29.err
│   ├── batch_ref_4_budget_200_2038356_29.out
│   ├── batch_ref_4_budget_200_2038356_3.err
│   ├── batch_ref_4_budget_200_2038356_3.out
│   ├── batch_ref_4_budget_200_2038356_30.err
│   ├── batch_ref_4_budget_200_2038356_30.out
│   ├── batch_ref_4_budget_200_2038356_31.err
│   ├── batch_ref_4_budget_200_2038356_31.out
│   ├── batch_ref_4_budget_200_2038356_32.err
│   ├── batch_ref_4_budget_200_2038356_32.out
│   ├── batch_ref_4_budget_200_2038356_33.err
│   ├── batch_ref_4_budget_200_2038356_33.out
│   ├── batch_ref_4_budget_200_2038356_34.err
│   ├── batch_ref_4_budget_200_2038356_34.out
│   ├── batch_ref_4_budget_200_2038356_35.err
│   ├── batch_ref_4_budget_200_2038356_35.out
│   ├── batch_ref_4_budget_200_2038356_36.err
│   ├── batch_ref_4_budget_200_2038356_36.out
│   ├── batch_ref_4_budget_200_2038356_37.err
│   ├── batch_ref_4_budget_200_2038356_37.out
│   ├── batch_ref_4_budget_200_2038356_38.err
│   ├── batch_ref_4_budget_200_2038356_38.out
│   ├── batch_ref_4_budget_200_2038356_39.err
│   ├── batch_ref_4_budget_200_2038356_39.out
│   ├── batch_ref_4_budget_200_2038356_4.err
│   ├── batch_ref_4_budget_200_2038356_4.out
│   ├── batch_ref_4_budget_200_2038356_40.err
│   ├── batch_ref_4_budget_200_2038356_40.out
│   ├── batch_ref_4_budget_200_2038356_41.err
│   ├── batch_ref_4_budget_200_2038356_41.out
│   ├── batch_ref_4_budget_200_2038356_42.err
│   ├── batch_ref_4_budget_200_2038356_42.out
│   ├── batch_ref_4_budget_200_2038356_43.err
│   ├── batch_ref_4_budget_200_2038356_43.out
│   ├── batch_ref_4_budget_200_2038356_44.err
│   ├── batch_ref_4_budget_200_2038356_44.out
│   ├── batch_ref_4_budget_200_2038356_45.err
│   ├── batch_ref_4_budget_200_2038356_45.out
│   ├── batch_ref_4_budget_200_2038356_46.err
│   ├── batch_ref_4_budget_200_2038356_46.out
│   ├── batch_ref_4_budget_200_2038356_47.err
│   ├── batch_ref_4_budget_200_2038356_47.out
│   ├── batch_ref_4_budget_200_2038356_48.err
│   ├── batch_ref_4_budget_200_2038356_48.out
│   ├── batch_ref_4_budget_200_2038356_49.err
│   ├── batch_ref_4_budget_200_2038356_49.out
│   ├── batch_ref_4_budget_200_2038356_5.err
│   ├── batch_ref_4_budget_200_2038356_5.out
│   ├── batch_ref_4_budget_200_2038356_50.err
│   ├── batch_ref_4_budget_200_2038356_50.out
│   ├── batch_ref_4_budget_200_2038356_51.err
│   ├── batch_ref_4_budget_200_2038356_51.out
│   ├── batch_ref_4_budget_200_2038356_52.err
│   ├── batch_ref_4_budget_200_2038356_52.out
│   ├── batch_ref_4_budget_200_2038356_53.err
│   ├── batch_ref_4_budget_200_2038356_53.out
│   ├── batch_ref_4_budget_200_2038356_54.err
│   ├── batch_ref_4_budget_200_2038356_54.out
│   ├── batch_ref_4_budget_200_2038356_55.err
│   ├── batch_ref_4_budget_200_2038356_55.out
│   ├── batch_ref_4_budget_200_2038356_56.err
│   ├── batch_ref_4_budget_200_2038356_56.out
│   ├── batch_ref_4_budget_200_2038356_57.err
│   ├── batch_ref_4_budget_200_2038356_57.out
│   ├── batch_ref_4_budget_200_2038356_58.err
│   ├── batch_ref_4_budget_200_2038356_58.out
│   ├── batch_ref_4_budget_200_2038356_59.err
│   ├── batch_ref_4_budget_200_2038356_59.out
│   ├── batch_ref_4_budget_200_2038356_6.err
│   ├── batch_ref_4_budget_200_2038356_6.out
│   ├── batch_ref_4_budget_200_2038356_60.err
│   ├── batch_ref_4_budget_200_2038356_60.out
│   ├── batch_ref_4_budget_200_2038356_61.err
│   ├── batch_ref_4_budget_200_2038356_61.out
│   ├── batch_ref_4_budget_200_2038356_62.err
│   ├── batch_ref_4_budget_200_2038356_62.out
│   ├── batch_ref_4_budget_200_2038356_63.err
│   ├── batch_ref_4_budget_200_2038356_63.out
│   ├── batch_ref_4_budget_200_2038356_64.err
│   ├── batch_ref_4_budget_200_2038356_64.out
│   ├── batch_ref_4_budget_200_2038356_65.err
│   ├── batch_ref_4_budget_200_2038356_65.out
│   ├── batch_ref_4_budget_200_2038356_66.err
│   ├── batch_ref_4_budget_200_2038356_66.out
│   ├── batch_ref_4_budget_200_2038356_67.err
│   ├── batch_ref_4_budget_200_2038356_67.out
│   ├── batch_ref_4_budget_200_2038356_68.err
│   ├── batch_ref_4_budget_200_2038356_68.out
│   ├── batch_ref_4_budget_200_2038356_69.err
│   ├── batch_ref_4_budget_200_2038356_69.out
│   ├── batch_ref_4_budget_200_2038356_7.err
│   ├── batch_ref_4_budget_200_2038356_7.out
│   ├── batch_ref_4_budget_200_2038356_70.err
│   ├── batch_ref_4_budget_200_2038356_70.out
│   ├── batch_ref_4_budget_200_2038356_71.err
│   ├── batch_ref_4_budget_200_2038356_71.out
│   ├── batch_ref_4_budget_200_2038356_72.err
│   ├── batch_ref_4_budget_200_2038356_72.out
│   ├── batch_ref_4_budget_200_2038356_73.err
│   ├── batch_ref_4_budget_200_2038356_73.out
│   ├── batch_ref_4_budget_200_2038356_74.err
│   ├── batch_ref_4_budget_200_2038356_74.out
│   ├── batch_ref_4_budget_200_2038356_75.err
│   ├── batch_ref_4_budget_200_2038356_75.out
│   ├── batch_ref_4_budget_200_2038356_76.err
│   ├── batch_ref_4_budget_200_2038356_76.out
│   ├── batch_ref_4_budget_200_2038356_77.err
│   ├── batch_ref_4_budget_200_2038356_77.out
│   ├── batch_ref_4_budget_200_2038356_78.err
│   ├── batch_ref_4_budget_200_2038356_78.out
│   ├── batch_ref_4_budget_200_2038356_79.err
│   ├── batch_ref_4_budget_200_2038356_79.out
│   ├── batch_ref_4_budget_200_2038356_8.err
│   ├── batch_ref_4_budget_200_2038356_8.out
│   ├── batch_ref_4_budget_200_2038356_80.err
│   ├── batch_ref_4_budget_200_2038356_80.out
│   ├── batch_ref_4_budget_200_2038356_81.err
│   ├── batch_ref_4_budget_200_2038356_81.out
│   ├── batch_ref_4_budget_200_2038356_9.err
│   ├── batch_ref_4_budget_200_2038356_9.out
│   ├── batch_ref_4_budget_200_2040023_1.err
│   ├── batch_ref_4_budget_200_2040023_1.out
│   ├── batch_ref_4_budget_200_2040023_10.err
│   ├── batch_ref_4_budget_200_2040023_10.out
│   ├── batch_ref_4_budget_200_2040023_11.err
│   ├── batch_ref_4_budget_200_2040023_11.out
│   ├── batch_ref_4_budget_200_2040023_12.err
│   ├── batch_ref_4_budget_200_2040023_12.out
│   ├── batch_ref_4_budget_200_2040023_13.err
│   ├── batch_ref_4_budget_200_2040023_13.out
│   ├── batch_ref_4_budget_200_2040023_14.err
│   ├── batch_ref_4_budget_200_2040023_14.out
│   ├── batch_ref_4_budget_200_2040023_15.err
│   ├── batch_ref_4_budget_200_2040023_15.out
│   ├── batch_ref_4_budget_200_2040023_16.err
│   ├── batch_ref_4_budget_200_2040023_16.out
│   ├── batch_ref_4_budget_200_2040023_17.err
│   ├── batch_ref_4_budget_200_2040023_17.out
│   ├── batch_ref_4_budget_200_2040023_18.err
│   ├── batch_ref_4_budget_200_2040023_18.out
│   ├── batch_ref_4_budget_200_2040023_19.err
│   ├── batch_ref_4_budget_200_2040023_19.out
│   ├── batch_ref_4_budget_200_2040023_2.err
│   ├── batch_ref_4_budget_200_2040023_2.out
│   ├── batch_ref_4_budget_200_2040023_20.err
│   ├── batch_ref_4_budget_200_2040023_20.out
│   ├── batch_ref_4_budget_200_2040023_21.err
│   ├── batch_ref_4_budget_200_2040023_21.out
│   ├── batch_ref_4_budget_200_2040023_22.err
│   ├── batch_ref_4_budget_200_2040023_22.out
│   ├── batch_ref_4_budget_200_2040023_23.err
│   ├── batch_ref_4_budget_200_2040023_23.out
│   ├── batch_ref_4_budget_200_2040023_24.err
│   ├── batch_ref_4_budget_200_2040023_24.out
│   ├── batch_ref_4_budget_200_2040023_25.err
│   ├── batch_ref_4_budget_200_2040023_25.out
│   ├── batch_ref_4_budget_200_2040023_26.err
│   ├── batch_ref_4_budget_200_2040023_26.out
│   ├── batch_ref_4_budget_200_2040023_27.err
│   ├── batch_ref_4_budget_200_2040023_27.out
│   ├── batch_ref_4_budget_200_2040023_28.err
│   ├── batch_ref_4_budget_200_2040023_28.out
│   ├── batch_ref_4_budget_200_2040023_29.err
│   ├── batch_ref_4_budget_200_2040023_29.out
│   ├── batch_ref_4_budget_200_2040023_3.err
│   ├── batch_ref_4_budget_200_2040023_3.out
│   ├── batch_ref_4_budget_200_2040023_30.err
│   ├── batch_ref_4_budget_200_2040023_30.out
│   ├── batch_ref_4_budget_200_2040023_31.err
│   ├── batch_ref_4_budget_200_2040023_31.out
│   ├── batch_ref_4_budget_200_2040023_32.err
│   ├── batch_ref_4_budget_200_2040023_32.out
│   ├── batch_ref_4_budget_200_2040023_33.err
│   ├── batch_ref_4_budget_200_2040023_33.out
│   ├── batch_ref_4_budget_200_2040023_34.err
│   ├── batch_ref_4_budget_200_2040023_34.out
│   ├── batch_ref_4_budget_200_2040023_35.err
│   ├── batch_ref_4_budget_200_2040023_35.out
│   ├── batch_ref_4_budget_200_2040023_36.err
│   ├── batch_ref_4_budget_200_2040023_36.out
│   ├── batch_ref_4_budget_200_2040023_37.err
│   ├── batch_ref_4_budget_200_2040023_37.out
│   ├── batch_ref_4_budget_200_2040023_38.err
│   ├── batch_ref_4_budget_200_2040023_38.out
│   ├── batch_ref_4_budget_200_2040023_39.err
│   ├── batch_ref_4_budget_200_2040023_39.out
│   ├── batch_ref_4_budget_200_2040023_4.err
│   ├── batch_ref_4_budget_200_2040023_4.out
│   ├── batch_ref_4_budget_200_2040023_40.err
│   ├── batch_ref_4_budget_200_2040023_40.out
│   ├── batch_ref_4_budget_200_2040023_41.err
│   ├── batch_ref_4_budget_200_2040023_41.out
│   ├── batch_ref_4_budget_200_2040023_42.err
│   ├── batch_ref_4_budget_200_2040023_42.out
│   ├── batch_ref_4_budget_200_2040023_43.err
│   ├── batch_ref_4_budget_200_2040023_43.out
│   ├── batch_ref_4_budget_200_2040023_44.err
│   ├── batch_ref_4_budget_200_2040023_44.out
│   ├── batch_ref_4_budget_200_2040023_45.err
│   ├── batch_ref_4_budget_200_2040023_45.out
│   ├── batch_ref_4_budget_200_2040023_46.err
│   ├── batch_ref_4_budget_200_2040023_46.out
│   ├── batch_ref_4_budget_200_2040023_47.err
│   ├── batch_ref_4_budget_200_2040023_47.out
│   ├── batch_ref_4_budget_200_2040023_48.err
│   ├── batch_ref_4_budget_200_2040023_48.out
│   ├── batch_ref_4_budget_200_2040023_49.err
│   ├── batch_ref_4_budget_200_2040023_49.out
│   ├── batch_ref_4_budget_200_2040023_5.err
│   ├── batch_ref_4_budget_200_2040023_5.out
│   ├── batch_ref_4_budget_200_2040023_50.err
│   ├── batch_ref_4_budget_200_2040023_50.out
│   ├── batch_ref_4_budget_200_2040023_51.err
│   ├── batch_ref_4_budget_200_2040023_51.out
│   ├── batch_ref_4_budget_200_2040023_52.err
│   ├── batch_ref_4_budget_200_2040023_52.out
│   ├── batch_ref_4_budget_200_2040023_53.err
│   ├── batch_ref_4_budget_200_2040023_53.out
│   ├── batch_ref_4_budget_200_2040023_54.err
│   ├── batch_ref_4_budget_200_2040023_54.out
│   ├── batch_ref_4_budget_200_2040023_55.err
│   ├── batch_ref_4_budget_200_2040023_55.out
│   ├── batch_ref_4_budget_200_2040023_56.err
│   ├── batch_ref_4_budget_200_2040023_56.out
│   ├── batch_ref_4_budget_200_2040023_57.err
│   ├── batch_ref_4_budget_200_2040023_57.out
│   ├── batch_ref_4_budget_200_2040023_58.err
│   ├── batch_ref_4_budget_200_2040023_58.out
│   ├── batch_ref_4_budget_200_2040023_59.err
│   ├── batch_ref_4_budget_200_2040023_59.out
│   ├── batch_ref_4_budget_200_2040023_6.err
│   ├── batch_ref_4_budget_200_2040023_6.out
│   ├── batch_ref_4_budget_200_2040023_60.err
│   ├── batch_ref_4_budget_200_2040023_60.out
│   ├── batch_ref_4_budget_200_2040023_61.err
│   ├── batch_ref_4_budget_200_2040023_61.out
│   ├── batch_ref_4_budget_200_2040023_62.err
│   ├── batch_ref_4_budget_200_2040023_62.out
│   ├── batch_ref_4_budget_200_2040023_63.err
│   ├── batch_ref_4_budget_200_2040023_63.out
│   ├── batch_ref_4_budget_200_2040023_64.err
│   ├── batch_ref_4_budget_200_2040023_64.out
│   ├── batch_ref_4_budget_200_2040023_65.err
│   ├── batch_ref_4_budget_200_2040023_65.out
│   ├── batch_ref_4_budget_200_2040023_66.err
│   ├── batch_ref_4_budget_200_2040023_66.out
│   ├── batch_ref_4_budget_200_2040023_67.err
│   ├── batch_ref_4_budget_200_2040023_67.out
│   ├── batch_ref_4_budget_200_2040023_68.err
│   ├── batch_ref_4_budget_200_2040023_68.out
│   ├── batch_ref_4_budget_200_2040023_69.err
│   ├── batch_ref_4_budget_200_2040023_69.out
│   ├── batch_ref_4_budget_200_2040023_7.err
│   ├── batch_ref_4_budget_200_2040023_7.out
│   ├── batch_ref_4_budget_200_2040023_70.err
│   ├── batch_ref_4_budget_200_2040023_70.out
│   ├── batch_ref_4_budget_200_2040023_71.err
│   ├── batch_ref_4_budget_200_2040023_71.out
│   ├── batch_ref_4_budget_200_2040023_72.err
│   ├── batch_ref_4_budget_200_2040023_72.out
│   ├── batch_ref_4_budget_200_2040023_73.err
│   ├── batch_ref_4_budget_200_2040023_73.out
│   ├── batch_ref_4_budget_200_2040023_74.err
│   ├── batch_ref_4_budget_200_2040023_74.out
│   ├── batch_ref_4_budget_200_2040023_75.err
│   ├── batch_ref_4_budget_200_2040023_75.out
│   ├── batch_ref_4_budget_200_2040023_76.err
│   ├── batch_ref_4_budget_200_2040023_76.out
│   ├── batch_ref_4_budget_200_2040023_77.err
│   ├── batch_ref_4_budget_200_2040023_77.out
│   ├── batch_ref_4_budget_200_2040023_78.err
│   ├── batch_ref_4_budget_200_2040023_78.out
│   ├── batch_ref_4_budget_200_2040023_79.err
│   ├── batch_ref_4_budget_200_2040023_79.out
│   ├── batch_ref_4_budget_200_2040023_8.err
│   ├── batch_ref_4_budget_200_2040023_8.out
│   ├── batch_ref_4_budget_200_2040023_80.err
│   ├── batch_ref_4_budget_200_2040023_80.out
│   ├── batch_ref_4_budget_200_2040023_81.err
│   ├── batch_ref_4_budget_200_2040023_81.out
│   ├── batch_ref_4_budget_200_2040023_9.err
│   ├── batch_ref_4_budget_200_2040023_9.out
│   ├── batch_ref_4_budget_50_2024613_1.err
│   ├── batch_ref_4_budget_50_2024613_1.out
│   ├── batch_ref_4_budget_50_2024613_10.err
│   ├── batch_ref_4_budget_50_2024613_10.out
│   ├── batch_ref_4_budget_50_2024613_11.err
│   ├── batch_ref_4_budget_50_2024613_11.out
│   ├── batch_ref_4_budget_50_2024613_12.err
│   ├── batch_ref_4_budget_50_2024613_12.out
│   ├── batch_ref_4_budget_50_2024613_13.err
│   ├── batch_ref_4_budget_50_2024613_13.out
│   ├── batch_ref_4_budget_50_2024613_14.err
│   ├── batch_ref_4_budget_50_2024613_14.out
│   ├── batch_ref_4_budget_50_2024613_15.err
│   ├── batch_ref_4_budget_50_2024613_15.out
│   ├── batch_ref_4_budget_50_2024613_16.err
│   ├── batch_ref_4_budget_50_2024613_16.out
│   ├── batch_ref_4_budget_50_2024613_17.err
│   ├── batch_ref_4_budget_50_2024613_17.out
│   ├── batch_ref_4_budget_50_2024613_18.err
│   ├── batch_ref_4_budget_50_2024613_18.out
│   ├── batch_ref_4_budget_50_2024613_19.err
│   ├── batch_ref_4_budget_50_2024613_19.out
│   ├── batch_ref_4_budget_50_2024613_2.err
│   ├── batch_ref_4_budget_50_2024613_2.out
│   ├── batch_ref_4_budget_50_2024613_20.err
│   ├── batch_ref_4_budget_50_2024613_20.out
│   ├── batch_ref_4_budget_50_2024613_21.err
│   ├── batch_ref_4_budget_50_2024613_21.out
│   ├── batch_ref_4_budget_50_2024613_22.err
│   ├── batch_ref_4_budget_50_2024613_22.out
│   ├── batch_ref_4_budget_50_2024613_23.err
│   ├── batch_ref_4_budget_50_2024613_23.out
│   ├── batch_ref_4_budget_50_2024613_24.err
│   ├── batch_ref_4_budget_50_2024613_24.out
│   ├── batch_ref_4_budget_50_2024613_25.err
│   ├── batch_ref_4_budget_50_2024613_25.out
│   ├── batch_ref_4_budget_50_2024613_26.err
│   ├── batch_ref_4_budget_50_2024613_26.out
│   ├── batch_ref_4_budget_50_2024613_27.err
│   ├── batch_ref_4_budget_50_2024613_27.out
│   ├── batch_ref_4_budget_50_2024613_28.err
│   ├── batch_ref_4_budget_50_2024613_28.out
│   ├── batch_ref_4_budget_50_2024613_29.err
│   ├── batch_ref_4_budget_50_2024613_29.out
│   ├── batch_ref_4_budget_50_2024613_3.err
│   ├── batch_ref_4_budget_50_2024613_3.out
│   ├── batch_ref_4_budget_50_2024613_30.err
│   ├── batch_ref_4_budget_50_2024613_30.out
│   ├── batch_ref_4_budget_50_2024613_31.err
│   ├── batch_ref_4_budget_50_2024613_31.out
│   ├── batch_ref_4_budget_50_2024613_32.err
│   ├── batch_ref_4_budget_50_2024613_32.out
│   ├── batch_ref_4_budget_50_2024613_33.err
│   ├── batch_ref_4_budget_50_2024613_33.out
│   ├── batch_ref_4_budget_50_2024613_34.err
│   ├── batch_ref_4_budget_50_2024613_34.out
│   ├── batch_ref_4_budget_50_2024613_35.err
│   ├── batch_ref_4_budget_50_2024613_35.out
│   ├── batch_ref_4_budget_50_2024613_36.err
│   ├── batch_ref_4_budget_50_2024613_36.out
│   ├── batch_ref_4_budget_50_2024613_37.err
│   ├── batch_ref_4_budget_50_2024613_37.out
│   ├── batch_ref_4_budget_50_2024613_38.err
│   ├── batch_ref_4_budget_50_2024613_38.out
│   ├── batch_ref_4_budget_50_2024613_39.err
│   ├── batch_ref_4_budget_50_2024613_39.out
│   ├── batch_ref_4_budget_50_2024613_4.err
│   ├── batch_ref_4_budget_50_2024613_4.out
│   ├── batch_ref_4_budget_50_2024613_40.err
│   ├── batch_ref_4_budget_50_2024613_40.out
│   ├── batch_ref_4_budget_50_2024613_41.err
│   ├── batch_ref_4_budget_50_2024613_41.out
│   ├── batch_ref_4_budget_50_2024613_42.err
│   ├── batch_ref_4_budget_50_2024613_42.out
│   ├── batch_ref_4_budget_50_2024613_43.err
│   ├── batch_ref_4_budget_50_2024613_43.out
│   ├── batch_ref_4_budget_50_2024613_44.err
│   ├── batch_ref_4_budget_50_2024613_44.out
│   ├── batch_ref_4_budget_50_2024613_45.err
│   ├── batch_ref_4_budget_50_2024613_45.out
│   ├── batch_ref_4_budget_50_2024613_46.err
│   ├── batch_ref_4_budget_50_2024613_46.out
│   ├── batch_ref_4_budget_50_2024613_47.err
│   ├── batch_ref_4_budget_50_2024613_47.out
│   ├── batch_ref_4_budget_50_2024613_48.err
│   ├── batch_ref_4_budget_50_2024613_48.out
│   ├── batch_ref_4_budget_50_2024613_49.err
│   ├── batch_ref_4_budget_50_2024613_49.out
│   ├── batch_ref_4_budget_50_2024613_5.err
│   ├── batch_ref_4_budget_50_2024613_5.out
│   ├── batch_ref_4_budget_50_2024613_50.err
│   ├── batch_ref_4_budget_50_2024613_50.out
│   ├── batch_ref_4_budget_50_2024613_51.err
│   ├── batch_ref_4_budget_50_2024613_51.out
│   ├── batch_ref_4_budget_50_2024613_52.err
│   ├── batch_ref_4_budget_50_2024613_52.out
│   ├── batch_ref_4_budget_50_2024613_53.err
│   ├── batch_ref_4_budget_50_2024613_53.out
│   ├── batch_ref_4_budget_50_2024613_54.err
│   ├── batch_ref_4_budget_50_2024613_54.out
│   ├── batch_ref_4_budget_50_2024613_55.err
│   ├── batch_ref_4_budget_50_2024613_55.out
│   ├── batch_ref_4_budget_50_2024613_56.err
│   ├── batch_ref_4_budget_50_2024613_56.out
│   ├── batch_ref_4_budget_50_2024613_57.err
│   ├── batch_ref_4_budget_50_2024613_57.out
│   ├── batch_ref_4_budget_50_2024613_58.err
│   ├── batch_ref_4_budget_50_2024613_58.out
│   ├── batch_ref_4_budget_50_2024613_59.err
│   ├── batch_ref_4_budget_50_2024613_59.out
│   ├── batch_ref_4_budget_50_2024613_6.err
│   ├── batch_ref_4_budget_50_2024613_6.out
│   ├── batch_ref_4_budget_50_2024613_60.err
│   ├── batch_ref_4_budget_50_2024613_60.out
│   ├── batch_ref_4_budget_50_2024613_61.err
│   ├── batch_ref_4_budget_50_2024613_61.out
│   ├── batch_ref_4_budget_50_2024613_62.err
│   ├── batch_ref_4_budget_50_2024613_62.out
│   ├── batch_ref_4_budget_50_2024613_63.err
│   ├── batch_ref_4_budget_50_2024613_63.out
│   ├── batch_ref_4_budget_50_2024613_64.err
│   ├── batch_ref_4_budget_50_2024613_64.out
│   ├── batch_ref_4_budget_50_2024613_65.err
│   ├── batch_ref_4_budget_50_2024613_65.out
│   ├── batch_ref_4_budget_50_2024613_66.err
│   ├── batch_ref_4_budget_50_2024613_66.out
│   ├── batch_ref_4_budget_50_2024613_67.err
│   ├── batch_ref_4_budget_50_2024613_67.out
│   ├── batch_ref_4_budget_50_2024613_68.err
│   ├── batch_ref_4_budget_50_2024613_68.out
│   ├── batch_ref_4_budget_50_2024613_69.err
│   ├── batch_ref_4_budget_50_2024613_69.out
│   ├── batch_ref_4_budget_50_2024613_7.err
│   ├── batch_ref_4_budget_50_2024613_7.out
│   ├── batch_ref_4_budget_50_2024613_70.err
│   ├── batch_ref_4_budget_50_2024613_70.out
│   ├── batch_ref_4_budget_50_2024613_71.err
│   ├── batch_ref_4_budget_50_2024613_71.out
│   ├── batch_ref_4_budget_50_2024613_72.err
│   ├── batch_ref_4_budget_50_2024613_72.out
│   ├── batch_ref_4_budget_50_2024613_73.err
│   ├── batch_ref_4_budget_50_2024613_73.out
│   ├── batch_ref_4_budget_50_2024613_74.err
│   ├── batch_ref_4_budget_50_2024613_74.out
│   ├── batch_ref_4_budget_50_2024613_75.err
│   ├── batch_ref_4_budget_50_2024613_75.out
│   ├── batch_ref_4_budget_50_2024613_76.err
│   ├── batch_ref_4_budget_50_2024613_76.out
│   ├── batch_ref_4_budget_50_2024613_77.err
│   ├── batch_ref_4_budget_50_2024613_77.out
│   ├── batch_ref_4_budget_50_2024613_78.err
│   ├── batch_ref_4_budget_50_2024613_78.out
│   ├── batch_ref_4_budget_50_2024613_79.err
│   ├── batch_ref_4_budget_50_2024613_79.out
│   ├── batch_ref_4_budget_50_2024613_8.err
│   ├── batch_ref_4_budget_50_2024613_8.out
│   ├── batch_ref_4_budget_50_2024613_80.err
│   ├── batch_ref_4_budget_50_2024613_80.out
│   ├── batch_ref_4_budget_50_2024613_81.err
│   ├── batch_ref_4_budget_50_2024613_81.out
│   ├── batch_ref_4_budget_50_2024613_9.err
│   ├── batch_ref_4_budget_50_2024613_9.out
│   ├── batch_ref_4_budget_50_2028089_1.err
│   ├── batch_ref_4_budget_50_2028089_1.out
│   ├── batch_ref_4_budget_50_2028089_10.err
│   ├── batch_ref_4_budget_50_2028089_10.out
│   ├── batch_ref_4_budget_50_2028089_11.err
│   ├── batch_ref_4_budget_50_2028089_11.out
│   ├── batch_ref_4_budget_50_2028089_12.err
│   ├── batch_ref_4_budget_50_2028089_12.out
│   ├── batch_ref_4_budget_50_2028089_13.err
│   ├── batch_ref_4_budget_50_2028089_13.out
│   ├── batch_ref_4_budget_50_2028089_14.err
│   ├── batch_ref_4_budget_50_2028089_14.out
│   ├── batch_ref_4_budget_50_2028089_15.err
│   ├── batch_ref_4_budget_50_2028089_15.out
│   ├── batch_ref_4_budget_50_2028089_16.err
│   ├── batch_ref_4_budget_50_2028089_16.out
│   ├── batch_ref_4_budget_50_2028089_17.err
│   ├── batch_ref_4_budget_50_2028089_17.out
│   ├── batch_ref_4_budget_50_2028089_18.err
│   ├── batch_ref_4_budget_50_2028089_18.out
│   ├── batch_ref_4_budget_50_2028089_19.err
│   ├── batch_ref_4_budget_50_2028089_19.out
│   ├── batch_ref_4_budget_50_2028089_2.err
│   ├── batch_ref_4_budget_50_2028089_2.out
│   ├── batch_ref_4_budget_50_2028089_20.err
│   ├── batch_ref_4_budget_50_2028089_20.out
│   ├── batch_ref_4_budget_50_2028089_21.err
│   ├── batch_ref_4_budget_50_2028089_21.out
│   ├── batch_ref_4_budget_50_2028089_22.err
│   ├── batch_ref_4_budget_50_2028089_22.out
│   ├── batch_ref_4_budget_50_2028089_23.err
│   ├── batch_ref_4_budget_50_2028089_23.out
│   ├── batch_ref_4_budget_50_2028089_24.err
│   ├── batch_ref_4_budget_50_2028089_24.out
│   ├── batch_ref_4_budget_50_2028089_25.err
│   ├── batch_ref_4_budget_50_2028089_25.out
│   ├── batch_ref_4_budget_50_2028089_26.err
│   ├── batch_ref_4_budget_50_2028089_26.out
│   ├── batch_ref_4_budget_50_2028089_27.err
│   ├── batch_ref_4_budget_50_2028089_27.out
│   ├── batch_ref_4_budget_50_2028089_28.err
│   ├── batch_ref_4_budget_50_2028089_28.out
│   ├── batch_ref_4_budget_50_2028089_29.err
│   ├── batch_ref_4_budget_50_2028089_29.out
│   ├── batch_ref_4_budget_50_2028089_3.err
│   ├── batch_ref_4_budget_50_2028089_3.out
│   ├── batch_ref_4_budget_50_2028089_30.err
│   ├── batch_ref_4_budget_50_2028089_30.out
│   ├── batch_ref_4_budget_50_2028089_31.err
│   ├── batch_ref_4_budget_50_2028089_31.out
│   ├── batch_ref_4_budget_50_2028089_32.err
│   ├── batch_ref_4_budget_50_2028089_32.out
│   ├── batch_ref_4_budget_50_2028089_33.err
│   ├── batch_ref_4_budget_50_2028089_33.out
│   ├── batch_ref_4_budget_50_2028089_34.err
│   ├── batch_ref_4_budget_50_2028089_34.out
│   ├── batch_ref_4_budget_50_2028089_35.err
│   ├── batch_ref_4_budget_50_2028089_35.out
│   ├── batch_ref_4_budget_50_2028089_36.err
│   ├── batch_ref_4_budget_50_2028089_36.out
│   ├── batch_ref_4_budget_50_2028089_37.err
│   ├── batch_ref_4_budget_50_2028089_37.out
│   ├── batch_ref_4_budget_50_2028089_38.err
│   ├── batch_ref_4_budget_50_2028089_38.out
│   ├── batch_ref_4_budget_50_2028089_39.err
│   ├── batch_ref_4_budget_50_2028089_39.out
│   ├── batch_ref_4_budget_50_2028089_4.err
│   ├── batch_ref_4_budget_50_2028089_4.out
│   ├── batch_ref_4_budget_50_2028089_40.err
│   ├── batch_ref_4_budget_50_2028089_40.out
│   ├── batch_ref_4_budget_50_2028089_41.err
│   ├── batch_ref_4_budget_50_2028089_41.out
│   ├── batch_ref_4_budget_50_2028089_42.err
│   ├── batch_ref_4_budget_50_2028089_42.out
│   ├── batch_ref_4_budget_50_2028089_43.err
│   ├── batch_ref_4_budget_50_2028089_43.out
│   ├── batch_ref_4_budget_50_2028089_44.err
│   ├── batch_ref_4_budget_50_2028089_44.out
│   ├── batch_ref_4_budget_50_2028089_45.err
│   ├── batch_ref_4_budget_50_2028089_45.out
│   ├── batch_ref_4_budget_50_2028089_46.err
│   ├── batch_ref_4_budget_50_2028089_46.out
│   ├── batch_ref_4_budget_50_2028089_47.err
│   ├── batch_ref_4_budget_50_2028089_47.out
│   ├── batch_ref_4_budget_50_2028089_48.err
│   ├── batch_ref_4_budget_50_2028089_48.out
│   ├── batch_ref_4_budget_50_2028089_49.err
│   ├── batch_ref_4_budget_50_2028089_49.out
│   ├── batch_ref_4_budget_50_2028089_5.err
│   ├── batch_ref_4_budget_50_2028089_5.out
│   ├── batch_ref_4_budget_50_2028089_50.err
│   ├── batch_ref_4_budget_50_2028089_50.out
│   ├── batch_ref_4_budget_50_2028089_51.err
│   ├── batch_ref_4_budget_50_2028089_51.out
│   ├── batch_ref_4_budget_50_2028089_52.err
│   ├── batch_ref_4_budget_50_2028089_52.out
│   ├── batch_ref_4_budget_50_2028089_53.err
│   ├── batch_ref_4_budget_50_2028089_53.out
│   ├── batch_ref_4_budget_50_2028089_54.err
│   ├── batch_ref_4_budget_50_2028089_54.out
│   ├── batch_ref_4_budget_50_2028089_55.err
│   ├── batch_ref_4_budget_50_2028089_55.out
│   ├── batch_ref_4_budget_50_2028089_56.err
│   ├── batch_ref_4_budget_50_2028089_56.out
│   ├── batch_ref_4_budget_50_2028089_57.err
│   ├── batch_ref_4_budget_50_2028089_57.out
│   ├── batch_ref_4_budget_50_2028089_58.err
│   ├── batch_ref_4_budget_50_2028089_58.out
│   ├── batch_ref_4_budget_50_2028089_59.err
│   ├── batch_ref_4_budget_50_2028089_59.out
│   ├── batch_ref_4_budget_50_2028089_6.err
│   ├── batch_ref_4_budget_50_2028089_6.out
│   ├── batch_ref_4_budget_50_2028089_60.err
│   ├── batch_ref_4_budget_50_2028089_60.out
│   ├── batch_ref_4_budget_50_2028089_61.err
│   ├── batch_ref_4_budget_50_2028089_61.out
│   ├── batch_ref_4_budget_50_2028089_62.err
│   ├── batch_ref_4_budget_50_2028089_62.out
│   ├── batch_ref_4_budget_50_2028089_63.err
│   ├── batch_ref_4_budget_50_2028089_63.out
│   ├── batch_ref_4_budget_50_2028089_64.err
│   ├── batch_ref_4_budget_50_2028089_64.out
│   ├── batch_ref_4_budget_50_2028089_65.err
│   ├── batch_ref_4_budget_50_2028089_65.out
│   ├── batch_ref_4_budget_50_2028089_66.err
│   ├── batch_ref_4_budget_50_2028089_66.out
│   ├── batch_ref_4_budget_50_2028089_67.err
│   ├── batch_ref_4_budget_50_2028089_67.out
│   ├── batch_ref_4_budget_50_2028089_68.err
│   ├── batch_ref_4_budget_50_2028089_68.out
│   ├── batch_ref_4_budget_50_2028089_69.err
│   ├── batch_ref_4_budget_50_2028089_69.out
│   ├── batch_ref_4_budget_50_2028089_7.err
│   ├── batch_ref_4_budget_50_2028089_7.out
│   ├── batch_ref_4_budget_50_2028089_70.err
│   ├── batch_ref_4_budget_50_2028089_70.out
│   ├── batch_ref_4_budget_50_2028089_71.err
│   ├── batch_ref_4_budget_50_2028089_71.out
│   ├── batch_ref_4_budget_50_2028089_72.err
│   ├── batch_ref_4_budget_50_2028089_72.out
│   ├── batch_ref_4_budget_50_2028089_73.err
│   ├── batch_ref_4_budget_50_2028089_73.out
│   ├── batch_ref_4_budget_50_2028089_74.err
│   ├── batch_ref_4_budget_50_2028089_74.out
│   ├── batch_ref_4_budget_50_2028089_75.err
│   ├── batch_ref_4_budget_50_2028089_75.out
│   ├── batch_ref_4_budget_50_2028089_76.err
│   ├── batch_ref_4_budget_50_2028089_76.out
│   ├── batch_ref_4_budget_50_2028089_77.err
│   ├── batch_ref_4_budget_50_2028089_77.out
│   ├── batch_ref_4_budget_50_2028089_78.err
│   ├── batch_ref_4_budget_50_2028089_78.out
│   ├── batch_ref_4_budget_50_2028089_79.err
│   ├── batch_ref_4_budget_50_2028089_79.out
│   ├── batch_ref_4_budget_50_2028089_8.err
│   ├── batch_ref_4_budget_50_2028089_8.out
│   ├── batch_ref_4_budget_50_2028089_80.err
│   ├── batch_ref_4_budget_50_2028089_80.out
│   ├── batch_ref_4_budget_50_2028089_81.err
│   ├── batch_ref_4_budget_50_2028089_81.out
│   ├── batch_ref_4_budget_50_2028089_9.err
│   ├── batch_ref_4_budget_50_2028089_9.out
│   ├── batch_ref_4_budget_50_2040024_1.err
│   ├── batch_ref_4_budget_50_2040024_1.out
│   ├── batch_ref_4_budget_50_2040024_10.err
│   ├── batch_ref_4_budget_50_2040024_10.out
│   ├── batch_ref_4_budget_50_2040024_11.err
│   ├── batch_ref_4_budget_50_2040024_11.out
│   ├── batch_ref_4_budget_50_2040024_12.err
│   ├── batch_ref_4_budget_50_2040024_12.out
│   ├── batch_ref_4_budget_50_2040024_13.err
│   ├── batch_ref_4_budget_50_2040024_13.out
│   ├── batch_ref_4_budget_50_2040024_14.err
│   ├── batch_ref_4_budget_50_2040024_14.out
│   ├── batch_ref_4_budget_50_2040024_15.err
│   ├── batch_ref_4_budget_50_2040024_15.out
│   ├── batch_ref_4_budget_50_2040024_16.err
│   ├── batch_ref_4_budget_50_2040024_16.out
│   ├── batch_ref_4_budget_50_2040024_17.err
│   ├── batch_ref_4_budget_50_2040024_17.out
│   ├── batch_ref_4_budget_50_2040024_18.err
│   ├── batch_ref_4_budget_50_2040024_18.out
│   ├── batch_ref_4_budget_50_2040024_19.err
│   ├── batch_ref_4_budget_50_2040024_19.out
│   ├── batch_ref_4_budget_50_2040024_2.err
│   ├── batch_ref_4_budget_50_2040024_2.out
│   ├── batch_ref_4_budget_50_2040024_20.err
│   ├── batch_ref_4_budget_50_2040024_20.out
│   ├── batch_ref_4_budget_50_2040024_21.err
│   ├── batch_ref_4_budget_50_2040024_21.out
│   ├── batch_ref_4_budget_50_2040024_22.err
│   ├── batch_ref_4_budget_50_2040024_22.out
│   ├── batch_ref_4_budget_50_2040024_23.err
│   ├── batch_ref_4_budget_50_2040024_23.out
│   ├── batch_ref_4_budget_50_2040024_24.err
│   ├── batch_ref_4_budget_50_2040024_24.out
│   ├── batch_ref_4_budget_50_2040024_25.err
│   ├── batch_ref_4_budget_50_2040024_25.out
│   ├── batch_ref_4_budget_50_2040024_26.err
│   ├── batch_ref_4_budget_50_2040024_26.out
│   ├── batch_ref_4_budget_50_2040024_27.err
│   ├── batch_ref_4_budget_50_2040024_27.out
│   ├── batch_ref_4_budget_50_2040024_28.err
│   ├── batch_ref_4_budget_50_2040024_28.out
│   ├── batch_ref_4_budget_50_2040024_29.err
│   ├── batch_ref_4_budget_50_2040024_29.out
│   ├── batch_ref_4_budget_50_2040024_3.err
│   ├── batch_ref_4_budget_50_2040024_3.out
│   ├── batch_ref_4_budget_50_2040024_30.err
│   ├── batch_ref_4_budget_50_2040024_30.out
│   ├── batch_ref_4_budget_50_2040024_31.err
│   ├── batch_ref_4_budget_50_2040024_31.out
│   ├── batch_ref_4_budget_50_2040024_32.err
│   ├── batch_ref_4_budget_50_2040024_32.out
│   ├── batch_ref_4_budget_50_2040024_33.err
│   ├── batch_ref_4_budget_50_2040024_33.out
│   ├── batch_ref_4_budget_50_2040024_34.err
│   ├── batch_ref_4_budget_50_2040024_34.out
│   ├── batch_ref_4_budget_50_2040024_35.err
│   ├── batch_ref_4_budget_50_2040024_35.out
│   ├── batch_ref_4_budget_50_2040024_36.err
│   ├── batch_ref_4_budget_50_2040024_36.out
│   ├── batch_ref_4_budget_50_2040024_37.err
│   ├── batch_ref_4_budget_50_2040024_37.out
│   ├── batch_ref_4_budget_50_2040024_38.err
│   ├── batch_ref_4_budget_50_2040024_38.out
│   ├── batch_ref_4_budget_50_2040024_39.err
│   ├── batch_ref_4_budget_50_2040024_39.out
│   ├── batch_ref_4_budget_50_2040024_4.err
│   ├── batch_ref_4_budget_50_2040024_4.out
│   ├── batch_ref_4_budget_50_2040024_40.err
│   ├── batch_ref_4_budget_50_2040024_40.out
│   ├── batch_ref_4_budget_50_2040024_41.err
│   ├── batch_ref_4_budget_50_2040024_41.out
│   ├── batch_ref_4_budget_50_2040024_42.err
│   ├── batch_ref_4_budget_50_2040024_42.out
│   ├── batch_ref_4_budget_50_2040024_43.err
│   ├── batch_ref_4_budget_50_2040024_43.out
│   ├── batch_ref_4_budget_50_2040024_44.err
│   ├── batch_ref_4_budget_50_2040024_44.out
│   ├── batch_ref_4_budget_50_2040024_45.err
│   ├── batch_ref_4_budget_50_2040024_45.out
│   ├── batch_ref_4_budget_50_2040024_46.err
│   ├── batch_ref_4_budget_50_2040024_46.out
│   ├── batch_ref_4_budget_50_2040024_47.err
│   ├── batch_ref_4_budget_50_2040024_47.out
│   ├── batch_ref_4_budget_50_2040024_48.err
│   ├── batch_ref_4_budget_50_2040024_48.out
│   ├── batch_ref_4_budget_50_2040024_49.err
│   ├── batch_ref_4_budget_50_2040024_49.out
│   ├── batch_ref_4_budget_50_2040024_5.err
│   ├── batch_ref_4_budget_50_2040024_5.out
│   ├── batch_ref_4_budget_50_2040024_50.err
│   ├── batch_ref_4_budget_50_2040024_50.out
│   ├── batch_ref_4_budget_50_2040024_51.err
│   ├── batch_ref_4_budget_50_2040024_51.out
│   ├── batch_ref_4_budget_50_2040024_52.err
│   ├── batch_ref_4_budget_50_2040024_52.out
│   ├── batch_ref_4_budget_50_2040024_53.err
│   ├── batch_ref_4_budget_50_2040024_53.out
│   ├── batch_ref_4_budget_50_2040024_54.err
│   ├── batch_ref_4_budget_50_2040024_54.out
│   ├── batch_ref_4_budget_50_2040024_55.err
│   ├── batch_ref_4_budget_50_2040024_55.out
│   ├── batch_ref_4_budget_50_2040024_56.err
│   ├── batch_ref_4_budget_50_2040024_56.out
│   ├── batch_ref_4_budget_50_2040024_57.err
│   ├── batch_ref_4_budget_50_2040024_57.out
│   ├── batch_ref_4_budget_50_2040024_58.err
│   ├── batch_ref_4_budget_50_2040024_58.out
│   ├── batch_ref_4_budget_50_2040024_59.err
│   ├── batch_ref_4_budget_50_2040024_59.out
│   ├── batch_ref_4_budget_50_2040024_6.err
│   ├── batch_ref_4_budget_50_2040024_6.out
│   ├── batch_ref_4_budget_50_2040024_60.err
│   ├── batch_ref_4_budget_50_2040024_60.out
│   ├── batch_ref_4_budget_50_2040024_61.err
│   ├── batch_ref_4_budget_50_2040024_61.out
│   ├── batch_ref_4_budget_50_2040024_62.err
│   ├── batch_ref_4_budget_50_2040024_62.out
│   ├── batch_ref_4_budget_50_2040024_63.err
│   ├── batch_ref_4_budget_50_2040024_63.out
│   ├── batch_ref_4_budget_50_2040024_64.err
│   ├── batch_ref_4_budget_50_2040024_64.out
│   ├── batch_ref_4_budget_50_2040024_65.err
│   ├── batch_ref_4_budget_50_2040024_65.out
│   ├── batch_ref_4_budget_50_2040024_66.err
│   ├── batch_ref_4_budget_50_2040024_66.out
│   ├── batch_ref_4_budget_50_2040024_67.err
│   ├── batch_ref_4_budget_50_2040024_67.out
│   ├── batch_ref_4_budget_50_2040024_68.err
│   ├── batch_ref_4_budget_50_2040024_68.out
│   ├── batch_ref_4_budget_50_2040024_69.err
│   ├── batch_ref_4_budget_50_2040024_69.out
│   ├── batch_ref_4_budget_50_2040024_7.err
│   ├── batch_ref_4_budget_50_2040024_7.out
│   ├── batch_ref_4_budget_50_2040024_70.err
│   ├── batch_ref_4_budget_50_2040024_70.out
│   ├── batch_ref_4_budget_50_2040024_71.err
│   ├── batch_ref_4_budget_50_2040024_71.out
│   ├── batch_ref_4_budget_50_2040024_72.err
│   ├── batch_ref_4_budget_50_2040024_72.out
│   ├── batch_ref_4_budget_50_2040024_73.err
│   ├── batch_ref_4_budget_50_2040024_73.out
│   ├── batch_ref_4_budget_50_2040024_74.err
│   ├── batch_ref_4_budget_50_2040024_74.out
│   ├── batch_ref_4_budget_50_2040024_75.err
│   ├── batch_ref_4_budget_50_2040024_75.out
│   ├── batch_ref_4_budget_50_2040024_76.err
│   ├── batch_ref_4_budget_50_2040024_76.out
│   ├── batch_ref_4_budget_50_2040024_77.err
│   ├── batch_ref_4_budget_50_2040024_77.out
│   ├── batch_ref_4_budget_50_2040024_78.err
│   ├── batch_ref_4_budget_50_2040024_78.out
│   ├── batch_ref_4_budget_50_2040024_79.err
│   ├── batch_ref_4_budget_50_2040024_79.out
│   ├── batch_ref_4_budget_50_2040024_8.err
│   ├── batch_ref_4_budget_50_2040024_8.out
│   ├── batch_ref_4_budget_50_2040024_80.err
│   ├── batch_ref_4_budget_50_2040024_80.out
│   ├── batch_ref_4_budget_50_2040024_81.err
│   ├── batch_ref_4_budget_50_2040024_81.out
│   ├── batch_ref_4_budget_50_2040024_9.err
│   ├── batch_ref_4_budget_50_2040024_9.out
│   ├── batch_ref_4_budget_50_max_4_2067047_1.err
│   ├── batch_ref_4_budget_50_max_4_2067047_1.out
│   ├── batch_ref_4_budget_50_max_4_2067047_10.err
│   ├── batch_ref_4_budget_50_max_4_2067047_10.out
│   ├── batch_ref_4_budget_50_max_4_2067047_11.err
│   ├── batch_ref_4_budget_50_max_4_2067047_11.out
│   ├── batch_ref_4_budget_50_max_4_2067047_12.err
│   ├── batch_ref_4_budget_50_max_4_2067047_12.out
│   ├── batch_ref_4_budget_50_max_4_2067047_13.err
│   ├── batch_ref_4_budget_50_max_4_2067047_13.out
│   ├── batch_ref_4_budget_50_max_4_2067047_14.err
│   ├── batch_ref_4_budget_50_max_4_2067047_14.out
│   ├── batch_ref_4_budget_50_max_4_2067047_15.err
│   ├── batch_ref_4_budget_50_max_4_2067047_15.out
│   ├── batch_ref_4_budget_50_max_4_2067047_16.err
│   ├── batch_ref_4_budget_50_max_4_2067047_16.out
│   ├── batch_ref_4_budget_50_max_4_2067047_17.err
│   ├── batch_ref_4_budget_50_max_4_2067047_17.out
│   ├── batch_ref_4_budget_50_max_4_2067047_18.err
│   ├── batch_ref_4_budget_50_max_4_2067047_18.out
│   ├── batch_ref_4_budget_50_max_4_2067047_19.err
│   ├── batch_ref_4_budget_50_max_4_2067047_19.out
│   ├── batch_ref_4_budget_50_max_4_2067047_2.err
│   ├── batch_ref_4_budget_50_max_4_2067047_2.out
│   ├── batch_ref_4_budget_50_max_4_2067047_20.err
│   ├── batch_ref_4_budget_50_max_4_2067047_20.out
│   ├── batch_ref_4_budget_50_max_4_2067047_21.err
│   ├── batch_ref_4_budget_50_max_4_2067047_21.out
│   ├── batch_ref_4_budget_50_max_4_2067047_22.err
│   ├── batch_ref_4_budget_50_max_4_2067047_22.out
│   ├── batch_ref_4_budget_50_max_4_2067047_23.err
│   ├── batch_ref_4_budget_50_max_4_2067047_23.out
│   ├── batch_ref_4_budget_50_max_4_2067047_24.err
│   ├── batch_ref_4_budget_50_max_4_2067047_24.out
│   ├── batch_ref_4_budget_50_max_4_2067047_25.err
│   ├── batch_ref_4_budget_50_max_4_2067047_25.out
│   ├── batch_ref_4_budget_50_max_4_2067047_26.err
│   ├── batch_ref_4_budget_50_max_4_2067047_26.out
│   ├── batch_ref_4_budget_50_max_4_2067047_27.err
│   ├── batch_ref_4_budget_50_max_4_2067047_27.out
│   ├── batch_ref_4_budget_50_max_4_2067047_28.err
│   ├── batch_ref_4_budget_50_max_4_2067047_28.out
│   ├── batch_ref_4_budget_50_max_4_2067047_29.err
│   ├── batch_ref_4_budget_50_max_4_2067047_29.out
│   ├── batch_ref_4_budget_50_max_4_2067047_3.err
│   ├── batch_ref_4_budget_50_max_4_2067047_3.out
│   ├── batch_ref_4_budget_50_max_4_2067047_30.err
│   ├── batch_ref_4_budget_50_max_4_2067047_30.out
│   ├── batch_ref_4_budget_50_max_4_2067047_31.err
│   ├── batch_ref_4_budget_50_max_4_2067047_31.out
│   ├── batch_ref_4_budget_50_max_4_2067047_32.err
│   ├── batch_ref_4_budget_50_max_4_2067047_32.out
│   ├── batch_ref_4_budget_50_max_4_2067047_33.err
│   ├── batch_ref_4_budget_50_max_4_2067047_33.out
│   ├── batch_ref_4_budget_50_max_4_2067047_34.err
│   ├── batch_ref_4_budget_50_max_4_2067047_34.out
│   ├── batch_ref_4_budget_50_max_4_2067047_35.err
│   ├── batch_ref_4_budget_50_max_4_2067047_35.out
│   ├── batch_ref_4_budget_50_max_4_2067047_36.err
│   ├── batch_ref_4_budget_50_max_4_2067047_36.out
│   ├── batch_ref_4_budget_50_max_4_2067047_37.err
│   ├── batch_ref_4_budget_50_max_4_2067047_37.out
│   ├── batch_ref_4_budget_50_max_4_2067047_38.err
│   ├── batch_ref_4_budget_50_max_4_2067047_38.out
│   ├── batch_ref_4_budget_50_max_4_2067047_39.err
│   ├── batch_ref_4_budget_50_max_4_2067047_39.out
│   ├── batch_ref_4_budget_50_max_4_2067047_4.err
│   ├── batch_ref_4_budget_50_max_4_2067047_4.out
│   ├── batch_ref_4_budget_50_max_4_2067047_40.err
│   ├── batch_ref_4_budget_50_max_4_2067047_40.out
│   ├── batch_ref_4_budget_50_max_4_2067047_41.err
│   ├── batch_ref_4_budget_50_max_4_2067047_41.out
│   ├── batch_ref_4_budget_50_max_4_2067047_42.err
│   ├── batch_ref_4_budget_50_max_4_2067047_42.out
│   ├── batch_ref_4_budget_50_max_4_2067047_43.err
│   ├── batch_ref_4_budget_50_max_4_2067047_43.out
│   ├── batch_ref_4_budget_50_max_4_2067047_44.err
│   ├── batch_ref_4_budget_50_max_4_2067047_44.out
│   ├── batch_ref_4_budget_50_max_4_2067047_45.err
│   ├── batch_ref_4_budget_50_max_4_2067047_45.out
│   ├── batch_ref_4_budget_50_max_4_2067047_46.err
│   ├── batch_ref_4_budget_50_max_4_2067047_46.out
│   ├── batch_ref_4_budget_50_max_4_2067047_47.err
│   ├── batch_ref_4_budget_50_max_4_2067047_47.out
│   ├── batch_ref_4_budget_50_max_4_2067047_48.err
│   ├── batch_ref_4_budget_50_max_4_2067047_48.out
│   ├── batch_ref_4_budget_50_max_4_2067047_49.err
│   ├── batch_ref_4_budget_50_max_4_2067047_49.out
│   ├── batch_ref_4_budget_50_max_4_2067047_5.err
│   ├── batch_ref_4_budget_50_max_4_2067047_5.out
│   ├── batch_ref_4_budget_50_max_4_2067047_50.err
│   ├── batch_ref_4_budget_50_max_4_2067047_50.out
│   ├── batch_ref_4_budget_50_max_4_2067047_51.err
│   ├── batch_ref_4_budget_50_max_4_2067047_51.out
│   ├── batch_ref_4_budget_50_max_4_2067047_52.err
│   ├── batch_ref_4_budget_50_max_4_2067047_52.out
│   ├── batch_ref_4_budget_50_max_4_2067047_53.err
│   ├── batch_ref_4_budget_50_max_4_2067047_53.out
│   ├── batch_ref_4_budget_50_max_4_2067047_54.err
│   ├── batch_ref_4_budget_50_max_4_2067047_54.out
│   ├── batch_ref_4_budget_50_max_4_2067047_55.err
│   ├── batch_ref_4_budget_50_max_4_2067047_55.out
│   ├── batch_ref_4_budget_50_max_4_2067047_56.err
│   ├── batch_ref_4_budget_50_max_4_2067047_56.out
│   ├── batch_ref_4_budget_50_max_4_2067047_57.err
│   ├── batch_ref_4_budget_50_max_4_2067047_57.out
│   ├── batch_ref_4_budget_50_max_4_2067047_58.err
│   ├── batch_ref_4_budget_50_max_4_2067047_58.out
│   ├── batch_ref_4_budget_50_max_4_2067047_59.err
│   ├── batch_ref_4_budget_50_max_4_2067047_59.out
│   ├── batch_ref_4_budget_50_max_4_2067047_6.err
│   ├── batch_ref_4_budget_50_max_4_2067047_6.out
│   ├── batch_ref_4_budget_50_max_4_2067047_60.err
│   ├── batch_ref_4_budget_50_max_4_2067047_60.out
│   ├── batch_ref_4_budget_50_max_4_2067047_61.err
│   ├── batch_ref_4_budget_50_max_4_2067047_61.out
│   ├── batch_ref_4_budget_50_max_4_2067047_62.err
│   ├── batch_ref_4_budget_50_max_4_2067047_62.out
│   ├── batch_ref_4_budget_50_max_4_2067047_63.err
│   ├── batch_ref_4_budget_50_max_4_2067047_63.out
│   ├── batch_ref_4_budget_50_max_4_2067047_64.err
│   ├── batch_ref_4_budget_50_max_4_2067047_64.out
│   ├── batch_ref_4_budget_50_max_4_2067047_65.err
│   ├── batch_ref_4_budget_50_max_4_2067047_65.out
│   ├── batch_ref_4_budget_50_max_4_2067047_66.err
│   ├── batch_ref_4_budget_50_max_4_2067047_66.out
│   ├── batch_ref_4_budget_50_max_4_2067047_67.err
│   ├── batch_ref_4_budget_50_max_4_2067047_67.out
│   ├── batch_ref_4_budget_50_max_4_2067047_68.err
│   ├── batch_ref_4_budget_50_max_4_2067047_68.out
│   ├── batch_ref_4_budget_50_max_4_2067047_69.err
│   ├── batch_ref_4_budget_50_max_4_2067047_69.out
│   ├── batch_ref_4_budget_50_max_4_2067047_7.err
│   ├── batch_ref_4_budget_50_max_4_2067047_7.out
│   ├── batch_ref_4_budget_50_max_4_2067047_70.err
│   ├── batch_ref_4_budget_50_max_4_2067047_70.out
│   ├── batch_ref_4_budget_50_max_4_2067047_71.err
│   ├── batch_ref_4_budget_50_max_4_2067047_71.out
│   ├── batch_ref_4_budget_50_max_4_2067047_72.err
│   ├── batch_ref_4_budget_50_max_4_2067047_72.out
│   ├── batch_ref_4_budget_50_max_4_2067047_73.err
│   ├── batch_ref_4_budget_50_max_4_2067047_73.out
│   ├── batch_ref_4_budget_50_max_4_2067047_74.err
│   ├── batch_ref_4_budget_50_max_4_2067047_74.out
│   ├── batch_ref_4_budget_50_max_4_2067047_75.err
│   ├── batch_ref_4_budget_50_max_4_2067047_75.out
│   ├── batch_ref_4_budget_50_max_4_2067047_76.err
│   ├── batch_ref_4_budget_50_max_4_2067047_76.out
│   ├── batch_ref_4_budget_50_max_4_2067047_77.err
│   ├── batch_ref_4_budget_50_max_4_2067047_77.out
│   ├── batch_ref_4_budget_50_max_4_2067047_78.err
│   ├── batch_ref_4_budget_50_max_4_2067047_78.out
│   ├── batch_ref_4_budget_50_max_4_2067047_79.err
│   ├── batch_ref_4_budget_50_max_4_2067047_79.out
│   ├── batch_ref_4_budget_50_max_4_2067047_8.err
│   ├── batch_ref_4_budget_50_max_4_2067047_8.out
│   ├── batch_ref_4_budget_50_max_4_2067047_80.err
│   ├── batch_ref_4_budget_50_max_4_2067047_80.out
│   ├── batch_ref_4_budget_50_max_4_2067047_81.err
│   ├── batch_ref_4_budget_50_max_4_2067047_81.out
│   ├── batch_ref_4_budget_50_max_4_2067047_9.err
│   ├── batch_ref_4_budget_50_max_4_2067047_9.out
│   ├── batch_ref_4_budget_80_2000367_1.err
│   ├── batch_ref_4_budget_80_2000367_1.out
│   ├── batch_ref_4_budget_80_2000367_10.err
│   ├── batch_ref_4_budget_80_2000367_10.out
│   ├── batch_ref_4_budget_80_2000367_11.err
│   ├── batch_ref_4_budget_80_2000367_11.out
│   ├── batch_ref_4_budget_80_2000367_12.err
│   ├── batch_ref_4_budget_80_2000367_12.out
│   ├── batch_ref_4_budget_80_2000367_13.err
│   ├── batch_ref_4_budget_80_2000367_13.out
│   ├── batch_ref_4_budget_80_2000367_14.err
│   ├── batch_ref_4_budget_80_2000367_14.out
│   ├── batch_ref_4_budget_80_2000367_15.err
│   ├── batch_ref_4_budget_80_2000367_15.out
│   ├── batch_ref_4_budget_80_2000367_16.err
│   ├── batch_ref_4_budget_80_2000367_16.out
│   ├── batch_ref_4_budget_80_2000367_17.err
│   ├── batch_ref_4_budget_80_2000367_17.out
│   ├── batch_ref_4_budget_80_2000367_18.err
│   ├── batch_ref_4_budget_80_2000367_18.out
│   ├── batch_ref_4_budget_80_2000367_19.err
│   ├── batch_ref_4_budget_80_2000367_19.out
│   ├── batch_ref_4_budget_80_2000367_2.err
│   ├── batch_ref_4_budget_80_2000367_2.out
│   ├── batch_ref_4_budget_80_2000367_20.err
│   ├── batch_ref_4_budget_80_2000367_20.out
│   ├── batch_ref_4_budget_80_2000367_21.err
│   ├── batch_ref_4_budget_80_2000367_21.out
│   ├── batch_ref_4_budget_80_2000367_22.err
│   ├── batch_ref_4_budget_80_2000367_22.out
│   ├── batch_ref_4_budget_80_2000367_23.err
│   ├── batch_ref_4_budget_80_2000367_23.out
│   ├── batch_ref_4_budget_80_2000367_24.err
│   ├── batch_ref_4_budget_80_2000367_24.out
│   ├── batch_ref_4_budget_80_2000367_25.err
│   ├── batch_ref_4_budget_80_2000367_25.out
│   ├── batch_ref_4_budget_80_2000367_26.err
│   ├── batch_ref_4_budget_80_2000367_26.out
│   ├── batch_ref_4_budget_80_2000367_27.err
│   ├── batch_ref_4_budget_80_2000367_27.out
│   ├── batch_ref_4_budget_80_2000367_28.err
│   ├── batch_ref_4_budget_80_2000367_28.out
│   ├── batch_ref_4_budget_80_2000367_29.err
│   ├── batch_ref_4_budget_80_2000367_29.out
│   ├── batch_ref_4_budget_80_2000367_3.err
│   ├── batch_ref_4_budget_80_2000367_3.out
│   ├── batch_ref_4_budget_80_2000367_30.err
│   ├── batch_ref_4_budget_80_2000367_30.out
│   ├── batch_ref_4_budget_80_2000367_31.err
│   ├── batch_ref_4_budget_80_2000367_31.out
│   ├── batch_ref_4_budget_80_2000367_32.err
│   ├── batch_ref_4_budget_80_2000367_32.out
│   ├── batch_ref_4_budget_80_2000367_33.err
│   ├── batch_ref_4_budget_80_2000367_33.out
│   ├── batch_ref_4_budget_80_2000367_34.err
│   ├── batch_ref_4_budget_80_2000367_34.out
│   ├── batch_ref_4_budget_80_2000367_35.err
│   ├── batch_ref_4_budget_80_2000367_35.out
│   ├── batch_ref_4_budget_80_2000367_36.err
│   ├── batch_ref_4_budget_80_2000367_36.out
│   ├── batch_ref_4_budget_80_2000367_37.err
│   ├── batch_ref_4_budget_80_2000367_37.out
│   ├── batch_ref_4_budget_80_2000367_38.err
│   ├── batch_ref_4_budget_80_2000367_38.out
│   ├── batch_ref_4_budget_80_2000367_39.err
│   ├── batch_ref_4_budget_80_2000367_39.out
│   ├── batch_ref_4_budget_80_2000367_4.err
│   ├── batch_ref_4_budget_80_2000367_4.out
│   ├── batch_ref_4_budget_80_2000367_40.err
│   ├── batch_ref_4_budget_80_2000367_40.out
│   ├── batch_ref_4_budget_80_2000367_41.err
│   ├── batch_ref_4_budget_80_2000367_41.out
│   ├── batch_ref_4_budget_80_2000367_42.err
│   ├── batch_ref_4_budget_80_2000367_42.out
│   ├── batch_ref_4_budget_80_2000367_43.err
│   ├── batch_ref_4_budget_80_2000367_43.out
│   ├── batch_ref_4_budget_80_2000367_44.err
│   ├── batch_ref_4_budget_80_2000367_44.out
│   ├── batch_ref_4_budget_80_2000367_45.err
│   ├── batch_ref_4_budget_80_2000367_45.out
│   ├── batch_ref_4_budget_80_2000367_46.err
│   ├── batch_ref_4_budget_80_2000367_46.out
│   ├── batch_ref_4_budget_80_2000367_47.err
│   ├── batch_ref_4_budget_80_2000367_47.out
│   ├── batch_ref_4_budget_80_2000367_48.err
│   ├── batch_ref_4_budget_80_2000367_48.out
│   ├── batch_ref_4_budget_80_2000367_49.err
│   ├── batch_ref_4_budget_80_2000367_49.out
│   ├── batch_ref_4_budget_80_2000367_5.err
│   ├── batch_ref_4_budget_80_2000367_5.out
│   ├── batch_ref_4_budget_80_2000367_50.err
│   ├── batch_ref_4_budget_80_2000367_50.out
│   ├── batch_ref_4_budget_80_2000367_51.err
│   ├── batch_ref_4_budget_80_2000367_51.out
│   ├── batch_ref_4_budget_80_2000367_52.err
│   ├── batch_ref_4_budget_80_2000367_52.out
│   ├── batch_ref_4_budget_80_2000367_53.err
│   ├── batch_ref_4_budget_80_2000367_53.out
│   ├── batch_ref_4_budget_80_2000367_54.err
│   ├── batch_ref_4_budget_80_2000367_54.out
│   ├── batch_ref_4_budget_80_2000367_55.err
│   ├── batch_ref_4_budget_80_2000367_55.out
│   ├── batch_ref_4_budget_80_2000367_56.err
│   ├── batch_ref_4_budget_80_2000367_56.out
│   ├── batch_ref_4_budget_80_2000367_57.err
│   ├── batch_ref_4_budget_80_2000367_57.out
│   ├── batch_ref_4_budget_80_2000367_58.err
│   ├── batch_ref_4_budget_80_2000367_58.out
│   ├── batch_ref_4_budget_80_2000367_59.err
│   ├── batch_ref_4_budget_80_2000367_59.out
│   ├── batch_ref_4_budget_80_2000367_6.err
│   ├── batch_ref_4_budget_80_2000367_6.out
│   ├── batch_ref_4_budget_80_2000367_60.err
│   ├── batch_ref_4_budget_80_2000367_60.out
│   ├── batch_ref_4_budget_80_2000367_61.err
│   ├── batch_ref_4_budget_80_2000367_61.out
│   ├── batch_ref_4_budget_80_2000367_62.err
│   ├── batch_ref_4_budget_80_2000367_62.out
│   ├── batch_ref_4_budget_80_2000367_63.err
│   ├── batch_ref_4_budget_80_2000367_63.out
│   ├── batch_ref_4_budget_80_2000367_64.err
│   ├── batch_ref_4_budget_80_2000367_64.out
│   ├── batch_ref_4_budget_80_2000367_65.err
│   ├── batch_ref_4_budget_80_2000367_65.out
│   ├── batch_ref_4_budget_80_2000367_66.err
│   ├── batch_ref_4_budget_80_2000367_66.out
│   ├── batch_ref_4_budget_80_2000367_67.err
│   ├── batch_ref_4_budget_80_2000367_67.out
│   ├── batch_ref_4_budget_80_2000367_68.err
│   ├── batch_ref_4_budget_80_2000367_68.out
│   ├── batch_ref_4_budget_80_2000367_69.err
│   ├── batch_ref_4_budget_80_2000367_69.out
│   ├── batch_ref_4_budget_80_2000367_7.err
│   ├── batch_ref_4_budget_80_2000367_7.out
│   ├── batch_ref_4_budget_80_2000367_70.err
│   ├── batch_ref_4_budget_80_2000367_70.out
│   ├── batch_ref_4_budget_80_2000367_71.err
│   ├── batch_ref_4_budget_80_2000367_71.out
│   ├── batch_ref_4_budget_80_2000367_72.err
│   ├── batch_ref_4_budget_80_2000367_72.out
│   ├── batch_ref_4_budget_80_2000367_73.err
│   ├── batch_ref_4_budget_80_2000367_73.out
│   ├── batch_ref_4_budget_80_2000367_74.err
│   ├── batch_ref_4_budget_80_2000367_74.out
│   ├── batch_ref_4_budget_80_2000367_75.err
│   ├── batch_ref_4_budget_80_2000367_75.out
│   ├── batch_ref_4_budget_80_2000367_76.err
│   ├── batch_ref_4_budget_80_2000367_76.out
│   ├── batch_ref_4_budget_80_2000367_77.err
│   ├── batch_ref_4_budget_80_2000367_77.out
│   ├── batch_ref_4_budget_80_2000367_78.err
│   ├── batch_ref_4_budget_80_2000367_78.out
│   ├── batch_ref_4_budget_80_2000367_79.err
│   ├── batch_ref_4_budget_80_2000367_79.out
│   ├── batch_ref_4_budget_80_2000367_8.err
│   ├── batch_ref_4_budget_80_2000367_8.out
│   ├── batch_ref_4_budget_80_2000367_80.err
│   ├── batch_ref_4_budget_80_2000367_80.out
│   ├── batch_ref_4_budget_80_2000367_81.err
│   ├── batch_ref_4_budget_80_2000367_81.out
│   ├── batch_ref_4_budget_80_2000367_9.err
│   ├── batch_ref_4_budget_80_2000367_9.out
│   ├── batch_ref_4_budget_80_2004600_1.err
│   ├── batch_ref_4_budget_80_2004600_1.out
│   ├── batch_ref_4_budget_80_2004600_10.err
│   ├── batch_ref_4_budget_80_2004600_10.out
│   ├── batch_ref_4_budget_80_2004600_11.err
│   ├── batch_ref_4_budget_80_2004600_11.out
│   ├── batch_ref_4_budget_80_2004600_12.err
│   ├── batch_ref_4_budget_80_2004600_12.out
│   ├── batch_ref_4_budget_80_2004600_13.err
│   ├── batch_ref_4_budget_80_2004600_13.out
│   ├── batch_ref_4_budget_80_2004600_14.err
│   ├── batch_ref_4_budget_80_2004600_14.out
│   ├── batch_ref_4_budget_80_2004600_15.err
│   ├── batch_ref_4_budget_80_2004600_15.out
│   ├── batch_ref_4_budget_80_2004600_16.err
│   ├── batch_ref_4_budget_80_2004600_16.out
│   ├── batch_ref_4_budget_80_2004600_17.err
│   ├── batch_ref_4_budget_80_2004600_17.out
│   ├── batch_ref_4_budget_80_2004600_18.err
│   ├── batch_ref_4_budget_80_2004600_18.out
│   ├── batch_ref_4_budget_80_2004600_19.err
│   ├── batch_ref_4_budget_80_2004600_19.out
│   ├── batch_ref_4_budget_80_2004600_2.err
│   ├── batch_ref_4_budget_80_2004600_2.out
│   ├── batch_ref_4_budget_80_2004600_20.err
│   ├── batch_ref_4_budget_80_2004600_20.out
│   ├── batch_ref_4_budget_80_2004600_21.err
│   ├── batch_ref_4_budget_80_2004600_21.out
│   ├── batch_ref_4_budget_80_2004600_22.err
│   ├── batch_ref_4_budget_80_2004600_22.out
│   ├── batch_ref_4_budget_80_2004600_23.err
│   ├── batch_ref_4_budget_80_2004600_23.out
│   ├── batch_ref_4_budget_80_2004600_24.err
│   ├── batch_ref_4_budget_80_2004600_24.out
│   ├── batch_ref_4_budget_80_2004600_25.err
│   ├── batch_ref_4_budget_80_2004600_25.out
│   ├── batch_ref_4_budget_80_2004600_26.err
│   ├── batch_ref_4_budget_80_2004600_26.out
│   ├── batch_ref_4_budget_80_2004600_27.err
│   ├── batch_ref_4_budget_80_2004600_27.out
│   ├── batch_ref_4_budget_80_2004600_28.err
│   ├── batch_ref_4_budget_80_2004600_28.out
│   ├── batch_ref_4_budget_80_2004600_29.err
│   ├── batch_ref_4_budget_80_2004600_29.out
│   ├── batch_ref_4_budget_80_2004600_3.err
│   ├── batch_ref_4_budget_80_2004600_3.out
│   ├── batch_ref_4_budget_80_2004600_30.err
│   ├── batch_ref_4_budget_80_2004600_30.out
│   ├── batch_ref_4_budget_80_2004600_31.err
│   ├── batch_ref_4_budget_80_2004600_31.out
│   ├── batch_ref_4_budget_80_2004600_32.err
│   ├── batch_ref_4_budget_80_2004600_32.out
│   ├── batch_ref_4_budget_80_2004600_33.err
│   ├── batch_ref_4_budget_80_2004600_33.out
│   ├── batch_ref_4_budget_80_2004600_34.err
│   ├── batch_ref_4_budget_80_2004600_34.out
│   ├── batch_ref_4_budget_80_2004600_35.err
│   ├── batch_ref_4_budget_80_2004600_35.out
│   ├── batch_ref_4_budget_80_2004600_36.err
│   ├── batch_ref_4_budget_80_2004600_36.out
│   ├── batch_ref_4_budget_80_2004600_37.err
│   ├── batch_ref_4_budget_80_2004600_37.out
│   ├── batch_ref_4_budget_80_2004600_38.err
│   ├── batch_ref_4_budget_80_2004600_38.out
│   ├── batch_ref_4_budget_80_2004600_39.err
│   ├── batch_ref_4_budget_80_2004600_39.out
│   ├── batch_ref_4_budget_80_2004600_4.err
│   ├── batch_ref_4_budget_80_2004600_4.out
│   ├── batch_ref_4_budget_80_2004600_40.err
│   ├── batch_ref_4_budget_80_2004600_40.out
│   ├── batch_ref_4_budget_80_2004600_41.err
│   ├── batch_ref_4_budget_80_2004600_41.out
│   ├── batch_ref_4_budget_80_2004600_42.err
│   ├── batch_ref_4_budget_80_2004600_42.out
│   ├── batch_ref_4_budget_80_2004600_43.err
│   ├── batch_ref_4_budget_80_2004600_43.out
│   ├── batch_ref_4_budget_80_2004600_44.err
│   ├── batch_ref_4_budget_80_2004600_44.out
│   ├── batch_ref_4_budget_80_2004600_45.err
│   ├── batch_ref_4_budget_80_2004600_45.out
│   ├── batch_ref_4_budget_80_2004600_46.err
│   ├── batch_ref_4_budget_80_2004600_46.out
│   ├── batch_ref_4_budget_80_2004600_47.err
│   ├── batch_ref_4_budget_80_2004600_47.out
│   ├── batch_ref_4_budget_80_2004600_48.err
│   ├── batch_ref_4_budget_80_2004600_48.out
│   ├── batch_ref_4_budget_80_2004600_49.err
│   ├── batch_ref_4_budget_80_2004600_49.out
│   ├── batch_ref_4_budget_80_2004600_5.err
│   ├── batch_ref_4_budget_80_2004600_5.out
│   ├── batch_ref_4_budget_80_2004600_50.err
│   ├── batch_ref_4_budget_80_2004600_50.out
│   ├── batch_ref_4_budget_80_2004600_51.err
│   ├── batch_ref_4_budget_80_2004600_51.out
│   ├── batch_ref_4_budget_80_2004600_52.err
│   ├── batch_ref_4_budget_80_2004600_52.out
│   ├── batch_ref_4_budget_80_2004600_53.err
│   ├── batch_ref_4_budget_80_2004600_53.out
│   ├── batch_ref_4_budget_80_2004600_54.err
│   ├── batch_ref_4_budget_80_2004600_54.out
│   ├── batch_ref_4_budget_80_2004600_55.err
│   ├── batch_ref_4_budget_80_2004600_55.out
│   ├── batch_ref_4_budget_80_2004600_56.err
│   ├── batch_ref_4_budget_80_2004600_56.out
│   ├── batch_ref_4_budget_80_2004600_57.err
│   ├── batch_ref_4_budget_80_2004600_57.out
│   ├── batch_ref_4_budget_80_2004600_58.err
│   ├── batch_ref_4_budget_80_2004600_58.out
│   ├── batch_ref_4_budget_80_2004600_59.err
│   ├── batch_ref_4_budget_80_2004600_59.out
│   ├── batch_ref_4_budget_80_2004600_6.err
│   ├── batch_ref_4_budget_80_2004600_6.out
│   ├── batch_ref_4_budget_80_2004600_60.err
│   ├── batch_ref_4_budget_80_2004600_60.out
│   ├── batch_ref_4_budget_80_2004600_61.err
│   ├── batch_ref_4_budget_80_2004600_61.out
│   ├── batch_ref_4_budget_80_2004600_62.err
│   ├── batch_ref_4_budget_80_2004600_62.out
│   ├── batch_ref_4_budget_80_2004600_63.err
│   ├── batch_ref_4_budget_80_2004600_63.out
│   ├── batch_ref_4_budget_80_2004600_64.err
│   ├── batch_ref_4_budget_80_2004600_64.out
│   ├── batch_ref_4_budget_80_2004600_65.err
│   ├── batch_ref_4_budget_80_2004600_65.out
│   ├── batch_ref_4_budget_80_2004600_66.err
│   ├── batch_ref_4_budget_80_2004600_66.out
│   ├── batch_ref_4_budget_80_2004600_67.err
│   ├── batch_ref_4_budget_80_2004600_67.out
│   ├── batch_ref_4_budget_80_2004600_68.err
│   ├── batch_ref_4_budget_80_2004600_68.out
│   ├── batch_ref_4_budget_80_2004600_69.err
│   ├── batch_ref_4_budget_80_2004600_69.out
│   ├── batch_ref_4_budget_80_2004600_7.err
│   ├── batch_ref_4_budget_80_2004600_7.out
│   ├── batch_ref_4_budget_80_2004600_70.err
│   ├── batch_ref_4_budget_80_2004600_70.out
│   ├── batch_ref_4_budget_80_2004600_71.err
│   ├── batch_ref_4_budget_80_2004600_71.out
│   ├── batch_ref_4_budget_80_2004600_72.err
│   ├── batch_ref_4_budget_80_2004600_72.out
│   ├── batch_ref_4_budget_80_2004600_73.err
│   ├── batch_ref_4_budget_80_2004600_73.out
│   ├── batch_ref_4_budget_80_2004600_74.err
│   ├── batch_ref_4_budget_80_2004600_74.out
│   ├── batch_ref_4_budget_80_2004600_75.err
│   ├── batch_ref_4_budget_80_2004600_75.out
│   ├── batch_ref_4_budget_80_2004600_76.err
│   ├── batch_ref_4_budget_80_2004600_76.out
│   ├── batch_ref_4_budget_80_2004600_77.err
│   ├── batch_ref_4_budget_80_2004600_77.out
│   ├── batch_ref_4_budget_80_2004600_78.err
│   ├── batch_ref_4_budget_80_2004600_78.out
│   ├── batch_ref_4_budget_80_2004600_79.err
│   ├── batch_ref_4_budget_80_2004600_79.out
│   ├── batch_ref_4_budget_80_2004600_8.err
│   ├── batch_ref_4_budget_80_2004600_8.out
│   ├── batch_ref_4_budget_80_2004600_80.err
│   ├── batch_ref_4_budget_80_2004600_80.out
│   ├── batch_ref_4_budget_80_2004600_81.err
│   ├── batch_ref_4_budget_80_2004600_81.out
│   ├── batch_ref_4_budget_80_2004600_9.err
│   ├── batch_ref_4_budget_80_2004600_9.out
│   ├── batch_ref_4_budget_80_2005608_1.err
│   ├── batch_ref_4_budget_80_2005608_1.out
│   ├── batch_ref_4_budget_80_2005608_10.err
│   ├── batch_ref_4_budget_80_2005608_10.out
│   ├── batch_ref_4_budget_80_2005608_11.err
│   ├── batch_ref_4_budget_80_2005608_11.out
│   ├── batch_ref_4_budget_80_2005608_12.err
│   ├── batch_ref_4_budget_80_2005608_12.out
│   ├── batch_ref_4_budget_80_2005608_13.err
│   ├── batch_ref_4_budget_80_2005608_13.out
│   ├── batch_ref_4_budget_80_2005608_14.err
│   ├── batch_ref_4_budget_80_2005608_14.out
│   ├── batch_ref_4_budget_80_2005608_15.err
│   ├── batch_ref_4_budget_80_2005608_15.out
│   ├── batch_ref_4_budget_80_2005608_16.err
│   ├── batch_ref_4_budget_80_2005608_16.out
│   ├── batch_ref_4_budget_80_2005608_17.err
│   ├── batch_ref_4_budget_80_2005608_17.out
│   ├── batch_ref_4_budget_80_2005608_18.err
│   ├── batch_ref_4_budget_80_2005608_18.out
│   ├── batch_ref_4_budget_80_2005608_19.err
│   ├── batch_ref_4_budget_80_2005608_19.out
│   ├── batch_ref_4_budget_80_2005608_2.err
│   ├── batch_ref_4_budget_80_2005608_2.out
│   ├── batch_ref_4_budget_80_2005608_20.err
│   ├── batch_ref_4_budget_80_2005608_20.out
│   ├── batch_ref_4_budget_80_2005608_21.err
│   ├── batch_ref_4_budget_80_2005608_21.out
│   ├── batch_ref_4_budget_80_2005608_22.err
│   ├── batch_ref_4_budget_80_2005608_22.out
│   ├── batch_ref_4_budget_80_2005608_23.err
│   ├── batch_ref_4_budget_80_2005608_23.out
│   ├── batch_ref_4_budget_80_2005608_24.err
│   ├── batch_ref_4_budget_80_2005608_24.out
│   ├── batch_ref_4_budget_80_2005608_25.err
│   ├── batch_ref_4_budget_80_2005608_25.out
│   ├── batch_ref_4_budget_80_2005608_26.err
│   ├── batch_ref_4_budget_80_2005608_26.out
│   ├── batch_ref_4_budget_80_2005608_27.err
│   ├── batch_ref_4_budget_80_2005608_27.out
│   ├── batch_ref_4_budget_80_2005608_28.err
│   ├── batch_ref_4_budget_80_2005608_28.out
│   ├── batch_ref_4_budget_80_2005608_29.err
│   ├── batch_ref_4_budget_80_2005608_29.out
│   ├── batch_ref_4_budget_80_2005608_3.err
│   ├── batch_ref_4_budget_80_2005608_3.out
│   ├── batch_ref_4_budget_80_2005608_30.err
│   ├── batch_ref_4_budget_80_2005608_30.out
│   ├── batch_ref_4_budget_80_2005608_31.err
│   ├── batch_ref_4_budget_80_2005608_31.out
│   ├── batch_ref_4_budget_80_2005608_32.err
│   ├── batch_ref_4_budget_80_2005608_32.out
│   ├── batch_ref_4_budget_80_2005608_33.err
│   ├── batch_ref_4_budget_80_2005608_33.out
│   ├── batch_ref_4_budget_80_2005608_34.err
│   ├── batch_ref_4_budget_80_2005608_34.out
│   ├── batch_ref_4_budget_80_2005608_35.err
│   ├── batch_ref_4_budget_80_2005608_35.out
│   ├── batch_ref_4_budget_80_2005608_36.err
│   ├── batch_ref_4_budget_80_2005608_36.out
│   ├── batch_ref_4_budget_80_2005608_37.err
│   ├── batch_ref_4_budget_80_2005608_37.out
│   ├── batch_ref_4_budget_80_2005608_38.err
│   ├── batch_ref_4_budget_80_2005608_38.out
│   ├── batch_ref_4_budget_80_2005608_39.err
│   ├── batch_ref_4_budget_80_2005608_39.out
│   ├── batch_ref_4_budget_80_2005608_4.err
│   ├── batch_ref_4_budget_80_2005608_4.out
│   ├── batch_ref_4_budget_80_2005608_40.err
│   ├── batch_ref_4_budget_80_2005608_40.out
│   ├── batch_ref_4_budget_80_2005608_41.err
│   ├── batch_ref_4_budget_80_2005608_41.out
│   ├── batch_ref_4_budget_80_2005608_42.err
│   ├── batch_ref_4_budget_80_2005608_42.out
│   ├── batch_ref_4_budget_80_2005608_43.err
│   ├── batch_ref_4_budget_80_2005608_43.out
│   ├── batch_ref_4_budget_80_2005608_44.err
│   ├── batch_ref_4_budget_80_2005608_44.out
│   ├── batch_ref_4_budget_80_2005608_45.err
│   ├── batch_ref_4_budget_80_2005608_45.out
│   ├── batch_ref_4_budget_80_2005608_46.err
│   ├── batch_ref_4_budget_80_2005608_46.out
│   ├── batch_ref_4_budget_80_2005608_47.err
│   ├── batch_ref_4_budget_80_2005608_47.out
│   ├── batch_ref_4_budget_80_2005608_48.err
│   ├── batch_ref_4_budget_80_2005608_48.out
│   ├── batch_ref_4_budget_80_2005608_49.err
│   ├── batch_ref_4_budget_80_2005608_49.out
│   ├── batch_ref_4_budget_80_2005608_5.err
│   ├── batch_ref_4_budget_80_2005608_5.out
│   ├── batch_ref_4_budget_80_2005608_50.err
│   ├── batch_ref_4_budget_80_2005608_50.out
│   ├── batch_ref_4_budget_80_2005608_51.err
│   ├── batch_ref_4_budget_80_2005608_51.out
│   ├── batch_ref_4_budget_80_2005608_52.err
│   ├── batch_ref_4_budget_80_2005608_52.out
│   ├── batch_ref_4_budget_80_2005608_53.err
│   ├── batch_ref_4_budget_80_2005608_53.out
│   ├── batch_ref_4_budget_80_2005608_54.err
│   ├── batch_ref_4_budget_80_2005608_54.out
│   ├── batch_ref_4_budget_80_2005608_55.err
│   ├── batch_ref_4_budget_80_2005608_55.out
│   ├── batch_ref_4_budget_80_2005608_56.err
│   ├── batch_ref_4_budget_80_2005608_56.out
│   ├── batch_ref_4_budget_80_2005608_57.err
│   ├── batch_ref_4_budget_80_2005608_57.out
│   ├── batch_ref_4_budget_80_2005608_58.err
│   ├── batch_ref_4_budget_80_2005608_58.out
│   ├── batch_ref_4_budget_80_2005608_59.err
│   ├── batch_ref_4_budget_80_2005608_59.out
│   ├── batch_ref_4_budget_80_2005608_6.err
│   ├── batch_ref_4_budget_80_2005608_6.out
│   ├── batch_ref_4_budget_80_2005608_60.err
│   ├── batch_ref_4_budget_80_2005608_60.out
│   ├── batch_ref_4_budget_80_2005608_61.err
│   ├── batch_ref_4_budget_80_2005608_61.out
│   ├── batch_ref_4_budget_80_2005608_62.err
│   ├── batch_ref_4_budget_80_2005608_62.out
│   ├── batch_ref_4_budget_80_2005608_63.err
│   ├── batch_ref_4_budget_80_2005608_63.out
│   ├── batch_ref_4_budget_80_2005608_64.err
│   ├── batch_ref_4_budget_80_2005608_64.out
│   ├── batch_ref_4_budget_80_2005608_65.err
│   ├── batch_ref_4_budget_80_2005608_65.out
│   ├── batch_ref_4_budget_80_2005608_66.err
│   ├── batch_ref_4_budget_80_2005608_66.out
│   ├── batch_ref_4_budget_80_2005608_67.err
│   ├── batch_ref_4_budget_80_2005608_67.out
│   ├── batch_ref_4_budget_80_2005608_68.err
│   ├── batch_ref_4_budget_80_2005608_68.out
│   ├── batch_ref_4_budget_80_2005608_69.err
│   ├── batch_ref_4_budget_80_2005608_69.out
│   ├── batch_ref_4_budget_80_2005608_7.err
│   ├── batch_ref_4_budget_80_2005608_7.out
│   ├── batch_ref_4_budget_80_2005608_70.err
│   ├── batch_ref_4_budget_80_2005608_70.out
│   ├── batch_ref_4_budget_80_2005608_71.err
│   ├── batch_ref_4_budget_80_2005608_71.out
│   ├── batch_ref_4_budget_80_2005608_72.err
│   ├── batch_ref_4_budget_80_2005608_72.out
│   ├── batch_ref_4_budget_80_2005608_73.err
│   ├── batch_ref_4_budget_80_2005608_73.out
│   ├── batch_ref_4_budget_80_2005608_74.err
│   ├── batch_ref_4_budget_80_2005608_74.out
│   ├── batch_ref_4_budget_80_2005608_75.err
│   ├── batch_ref_4_budget_80_2005608_75.out
│   ├── batch_ref_4_budget_80_2005608_76.err
│   ├── batch_ref_4_budget_80_2005608_76.out
│   ├── batch_ref_4_budget_80_2005608_77.err
│   ├── batch_ref_4_budget_80_2005608_77.out
│   ├── batch_ref_4_budget_80_2005608_78.err
│   ├── batch_ref_4_budget_80_2005608_78.out
│   ├── batch_ref_4_budget_80_2005608_79.err
│   ├── batch_ref_4_budget_80_2005608_79.out
│   ├── batch_ref_4_budget_80_2005608_8.err
│   ├── batch_ref_4_budget_80_2005608_8.out
│   ├── batch_ref_4_budget_80_2005608_80.err
│   ├── batch_ref_4_budget_80_2005608_80.out
│   ├── batch_ref_4_budget_80_2005608_81.err
│   ├── batch_ref_4_budget_80_2005608_81.out
│   ├── batch_ref_4_budget_80_2005608_9.err
│   ├── batch_ref_4_budget_80_2005608_9.out
│   ├── batch_ref_4_budget_80_2005995_1.err
│   ├── batch_ref_4_budget_80_2005995_1.out
│   ├── batch_ref_4_budget_80_2005995_10.err
│   ├── batch_ref_4_budget_80_2005995_10.out
│   ├── batch_ref_4_budget_80_2005995_11.err
│   ├── batch_ref_4_budget_80_2005995_11.out
│   ├── batch_ref_4_budget_80_2005995_12.err
│   ├── batch_ref_4_budget_80_2005995_12.out
│   ├── batch_ref_4_budget_80_2005995_13.err
│   ├── batch_ref_4_budget_80_2005995_13.out
│   ├── batch_ref_4_budget_80_2005995_14.err
│   ├── batch_ref_4_budget_80_2005995_14.out
│   ├── batch_ref_4_budget_80_2005995_15.err
│   ├── batch_ref_4_budget_80_2005995_15.out
│   ├── batch_ref_4_budget_80_2005995_16.err
│   ├── batch_ref_4_budget_80_2005995_16.out
│   ├── batch_ref_4_budget_80_2005995_17.err
│   ├── batch_ref_4_budget_80_2005995_17.out
│   ├── batch_ref_4_budget_80_2005995_18.err
│   ├── batch_ref_4_budget_80_2005995_18.out
│   ├── batch_ref_4_budget_80_2005995_19.err
│   ├── batch_ref_4_budget_80_2005995_19.out
│   ├── batch_ref_4_budget_80_2005995_2.err
│   ├── batch_ref_4_budget_80_2005995_2.out
│   ├── batch_ref_4_budget_80_2005995_20.err
│   ├── batch_ref_4_budget_80_2005995_20.out
│   ├── batch_ref_4_budget_80_2005995_21.err
│   ├── batch_ref_4_budget_80_2005995_21.out
│   ├── batch_ref_4_budget_80_2005995_22.err
│   ├── batch_ref_4_budget_80_2005995_22.out
│   ├── batch_ref_4_budget_80_2005995_23.err
│   ├── batch_ref_4_budget_80_2005995_23.out
│   ├── batch_ref_4_budget_80_2005995_24.err
│   ├── batch_ref_4_budget_80_2005995_24.out
│   ├── batch_ref_4_budget_80_2005995_25.err
│   ├── batch_ref_4_budget_80_2005995_25.out
│   ├── batch_ref_4_budget_80_2005995_26.err
│   ├── batch_ref_4_budget_80_2005995_26.out
│   ├── batch_ref_4_budget_80_2005995_27.err
│   ├── batch_ref_4_budget_80_2005995_27.out
│   ├── batch_ref_4_budget_80_2005995_28.err
│   ├── batch_ref_4_budget_80_2005995_28.out
│   ├── batch_ref_4_budget_80_2005995_29.err
│   ├── batch_ref_4_budget_80_2005995_29.out
│   ├── batch_ref_4_budget_80_2005995_3.err
│   ├── batch_ref_4_budget_80_2005995_3.out
│   ├── batch_ref_4_budget_80_2005995_30.err
│   ├── batch_ref_4_budget_80_2005995_30.out
│   ├── batch_ref_4_budget_80_2005995_31.err
│   ├── batch_ref_4_budget_80_2005995_31.out
│   ├── batch_ref_4_budget_80_2005995_32.err
│   ├── batch_ref_4_budget_80_2005995_32.out
│   ├── batch_ref_4_budget_80_2005995_33.err
│   ├── batch_ref_4_budget_80_2005995_33.out
│   ├── batch_ref_4_budget_80_2005995_34.err
│   ├── batch_ref_4_budget_80_2005995_34.out
│   ├── batch_ref_4_budget_80_2005995_35.err
│   ├── batch_ref_4_budget_80_2005995_35.out
│   ├── batch_ref_4_budget_80_2005995_36.err
│   ├── batch_ref_4_budget_80_2005995_36.out
│   ├── batch_ref_4_budget_80_2005995_37.err
│   ├── batch_ref_4_budget_80_2005995_37.out
│   ├── batch_ref_4_budget_80_2005995_38.err
│   ├── batch_ref_4_budget_80_2005995_38.out
│   ├── batch_ref_4_budget_80_2005995_39.err
│   ├── batch_ref_4_budget_80_2005995_39.out
│   ├── batch_ref_4_budget_80_2005995_4.err
│   ├── batch_ref_4_budget_80_2005995_4.out
│   ├── batch_ref_4_budget_80_2005995_40.err
│   ├── batch_ref_4_budget_80_2005995_40.out
│   ├── batch_ref_4_budget_80_2005995_41.err
│   ├── batch_ref_4_budget_80_2005995_41.out
│   ├── batch_ref_4_budget_80_2005995_42.err
│   ├── batch_ref_4_budget_80_2005995_42.out
│   ├── batch_ref_4_budget_80_2005995_43.err
│   ├── batch_ref_4_budget_80_2005995_43.out
│   ├── batch_ref_4_budget_80_2005995_44.err
│   ├── batch_ref_4_budget_80_2005995_44.out
│   ├── batch_ref_4_budget_80_2005995_45.err
│   ├── batch_ref_4_budget_80_2005995_45.out
│   ├── batch_ref_4_budget_80_2005995_46.err
│   ├── batch_ref_4_budget_80_2005995_46.out
│   ├── batch_ref_4_budget_80_2005995_47.err
│   ├── batch_ref_4_budget_80_2005995_47.out
│   ├── batch_ref_4_budget_80_2005995_48.err
│   ├── batch_ref_4_budget_80_2005995_48.out
│   ├── batch_ref_4_budget_80_2005995_49.err
│   ├── batch_ref_4_budget_80_2005995_49.out
│   ├── batch_ref_4_budget_80_2005995_5.err
│   ├── batch_ref_4_budget_80_2005995_5.out
│   ├── batch_ref_4_budget_80_2005995_50.err
│   ├── batch_ref_4_budget_80_2005995_50.out
│   ├── batch_ref_4_budget_80_2005995_51.err
│   ├── batch_ref_4_budget_80_2005995_51.out
│   ├── batch_ref_4_budget_80_2005995_52.err
│   ├── batch_ref_4_budget_80_2005995_52.out
│   ├── batch_ref_4_budget_80_2005995_53.err
│   ├── batch_ref_4_budget_80_2005995_53.out
│   ├── batch_ref_4_budget_80_2005995_54.err
│   ├── batch_ref_4_budget_80_2005995_54.out
│   ├── batch_ref_4_budget_80_2005995_55.err
│   ├── batch_ref_4_budget_80_2005995_55.out
│   ├── batch_ref_4_budget_80_2005995_56.err
│   ├── batch_ref_4_budget_80_2005995_56.out
│   ├── batch_ref_4_budget_80_2005995_57.err
│   ├── batch_ref_4_budget_80_2005995_57.out
│   ├── batch_ref_4_budget_80_2005995_58.err
│   ├── batch_ref_4_budget_80_2005995_58.out
│   ├── batch_ref_4_budget_80_2005995_59.err
│   ├── batch_ref_4_budget_80_2005995_59.out
│   ├── batch_ref_4_budget_80_2005995_6.err
│   ├── batch_ref_4_budget_80_2005995_6.out
│   ├── batch_ref_4_budget_80_2005995_60.err
│   ├── batch_ref_4_budget_80_2005995_60.out
│   ├── batch_ref_4_budget_80_2005995_61.err
│   ├── batch_ref_4_budget_80_2005995_61.out
│   ├── batch_ref_4_budget_80_2005995_62.err
│   ├── batch_ref_4_budget_80_2005995_62.out
│   ├── batch_ref_4_budget_80_2005995_63.err
│   ├── batch_ref_4_budget_80_2005995_63.out
│   ├── batch_ref_4_budget_80_2005995_64.err
│   ├── batch_ref_4_budget_80_2005995_64.out
│   ├── batch_ref_4_budget_80_2005995_65.err
│   ├── batch_ref_4_budget_80_2005995_65.out
│   ├── batch_ref_4_budget_80_2005995_66.err
│   ├── batch_ref_4_budget_80_2005995_66.out
│   ├── batch_ref_4_budget_80_2005995_67.err
│   ├── batch_ref_4_budget_80_2005995_67.out
│   ├── batch_ref_4_budget_80_2005995_68.err
│   ├── batch_ref_4_budget_80_2005995_68.out
│   ├── batch_ref_4_budget_80_2005995_69.err
│   ├── batch_ref_4_budget_80_2005995_69.out
│   ├── batch_ref_4_budget_80_2005995_7.err
│   ├── batch_ref_4_budget_80_2005995_7.out
│   ├── batch_ref_4_budget_80_2005995_70.err
│   ├── batch_ref_4_budget_80_2005995_70.out
│   ├── batch_ref_4_budget_80_2005995_71.err
│   ├── batch_ref_4_budget_80_2005995_71.out
│   ├── batch_ref_4_budget_80_2005995_72.err
│   ├── batch_ref_4_budget_80_2005995_72.out
│   ├── batch_ref_4_budget_80_2005995_73.err
│   ├── batch_ref_4_budget_80_2005995_73.out
│   ├── batch_ref_4_budget_80_2005995_74.err
│   ├── batch_ref_4_budget_80_2005995_74.out
│   ├── batch_ref_4_budget_80_2005995_75.err
│   ├── batch_ref_4_budget_80_2005995_75.out
│   ├── batch_ref_4_budget_80_2005995_76.err
│   ├── batch_ref_4_budget_80_2005995_76.out
│   ├── batch_ref_4_budget_80_2005995_77.err
│   ├── batch_ref_4_budget_80_2005995_77.out
│   ├── batch_ref_4_budget_80_2005995_78.err
│   ├── batch_ref_4_budget_80_2005995_78.out
│   ├── batch_ref_4_budget_80_2005995_79.err
│   ├── batch_ref_4_budget_80_2005995_79.out
│   ├── batch_ref_4_budget_80_2005995_8.err
│   ├── batch_ref_4_budget_80_2005995_8.out
│   ├── batch_ref_4_budget_80_2005995_80.err
│   ├── batch_ref_4_budget_80_2005995_80.out
│   ├── batch_ref_4_budget_80_2005995_81.err
│   ├── batch_ref_4_budget_80_2005995_81.out
│   ├── batch_ref_4_budget_80_2005995_9.err
│   ├── batch_ref_4_budget_80_2005995_9.out
│   ├── batch_ref_4_budget_80_2027853_1.err
│   ├── batch_ref_4_budget_80_2027853_1.out
│   ├── batch_ref_4_budget_80_2027853_10.err
│   ├── batch_ref_4_budget_80_2027853_10.out
│   ├── batch_ref_4_budget_80_2027853_11.err
│   ├── batch_ref_4_budget_80_2027853_11.out
│   ├── batch_ref_4_budget_80_2027853_12.err
│   ├── batch_ref_4_budget_80_2027853_12.out
│   ├── batch_ref_4_budget_80_2027853_13.err
│   ├── batch_ref_4_budget_80_2027853_13.out
│   ├── batch_ref_4_budget_80_2027853_14.err
│   ├── batch_ref_4_budget_80_2027853_14.out
│   ├── batch_ref_4_budget_80_2027853_15.err
│   ├── batch_ref_4_budget_80_2027853_15.out
│   ├── batch_ref_4_budget_80_2027853_16.err
│   ├── batch_ref_4_budget_80_2027853_16.out
│   ├── batch_ref_4_budget_80_2027853_17.err
│   ├── batch_ref_4_budget_80_2027853_17.out
│   ├── batch_ref_4_budget_80_2027853_18.err
│   ├── batch_ref_4_budget_80_2027853_18.out
│   ├── batch_ref_4_budget_80_2027853_19.err
│   ├── batch_ref_4_budget_80_2027853_19.out
│   ├── batch_ref_4_budget_80_2027853_2.err
│   ├── batch_ref_4_budget_80_2027853_2.out
│   ├── batch_ref_4_budget_80_2027853_20.err
│   ├── batch_ref_4_budget_80_2027853_20.out
│   ├── batch_ref_4_budget_80_2027853_21.err
│   ├── batch_ref_4_budget_80_2027853_21.out
│   ├── batch_ref_4_budget_80_2027853_22.err
│   ├── batch_ref_4_budget_80_2027853_22.out
│   ├── batch_ref_4_budget_80_2027853_23.err
│   ├── batch_ref_4_budget_80_2027853_23.out
│   ├── batch_ref_4_budget_80_2027853_24.err
│   ├── batch_ref_4_budget_80_2027853_24.out
│   ├── batch_ref_4_budget_80_2027853_25.err
│   ├── batch_ref_4_budget_80_2027853_25.out
│   ├── batch_ref_4_budget_80_2027853_26.err
│   ├── batch_ref_4_budget_80_2027853_26.out
│   ├── batch_ref_4_budget_80_2027853_27.err
│   ├── batch_ref_4_budget_80_2027853_27.out
│   ├── batch_ref_4_budget_80_2027853_28.err
│   ├── batch_ref_4_budget_80_2027853_28.out
│   ├── batch_ref_4_budget_80_2027853_29.err
│   ├── batch_ref_4_budget_80_2027853_29.out
│   ├── batch_ref_4_budget_80_2027853_3.err
│   ├── batch_ref_4_budget_80_2027853_3.out
│   ├── batch_ref_4_budget_80_2027853_30.err
│   ├── batch_ref_4_budget_80_2027853_30.out
│   ├── batch_ref_4_budget_80_2027853_31.err
│   ├── batch_ref_4_budget_80_2027853_31.out
│   ├── batch_ref_4_budget_80_2027853_32.err
│   ├── batch_ref_4_budget_80_2027853_32.out
│   ├── batch_ref_4_budget_80_2027853_33.err
│   ├── batch_ref_4_budget_80_2027853_33.out
│   ├── batch_ref_4_budget_80_2027853_34.err
│   ├── batch_ref_4_budget_80_2027853_34.out
│   ├── batch_ref_4_budget_80_2027853_35.err
│   ├── batch_ref_4_budget_80_2027853_35.out
│   ├── batch_ref_4_budget_80_2027853_36.err
│   ├── batch_ref_4_budget_80_2027853_36.out
│   ├── batch_ref_4_budget_80_2027853_37.err
│   ├── batch_ref_4_budget_80_2027853_37.out
│   ├── batch_ref_4_budget_80_2027853_38.err
│   ├── batch_ref_4_budget_80_2027853_38.out
│   ├── batch_ref_4_budget_80_2027853_39.err
│   ├── batch_ref_4_budget_80_2027853_39.out
│   ├── batch_ref_4_budget_80_2027853_4.err
│   ├── batch_ref_4_budget_80_2027853_4.out
│   ├── batch_ref_4_budget_80_2027853_40.err
│   ├── batch_ref_4_budget_80_2027853_40.out
│   ├── batch_ref_4_budget_80_2027853_41.err
│   ├── batch_ref_4_budget_80_2027853_41.out
│   ├── batch_ref_4_budget_80_2027853_42.err
│   ├── batch_ref_4_budget_80_2027853_42.out
│   ├── batch_ref_4_budget_80_2027853_43.err
│   ├── batch_ref_4_budget_80_2027853_43.out
│   ├── batch_ref_4_budget_80_2027853_44.err
│   ├── batch_ref_4_budget_80_2027853_44.out
│   ├── batch_ref_4_budget_80_2027853_45.err
│   ├── batch_ref_4_budget_80_2027853_45.out
│   ├── batch_ref_4_budget_80_2027853_46.err
│   ├── batch_ref_4_budget_80_2027853_46.out
│   ├── batch_ref_4_budget_80_2027853_47.err
│   ├── batch_ref_4_budget_80_2027853_47.out
│   ├── batch_ref_4_budget_80_2027853_48.err
│   ├── batch_ref_4_budget_80_2027853_48.out
│   ├── batch_ref_4_budget_80_2027853_49.err
│   ├── batch_ref_4_budget_80_2027853_49.out
│   ├── batch_ref_4_budget_80_2027853_5.err
│   ├── batch_ref_4_budget_80_2027853_5.out
│   ├── batch_ref_4_budget_80_2027853_50.err
│   ├── batch_ref_4_budget_80_2027853_50.out
│   ├── batch_ref_4_budget_80_2027853_51.err
│   ├── batch_ref_4_budget_80_2027853_51.out
│   ├── batch_ref_4_budget_80_2027853_52.err
│   ├── batch_ref_4_budget_80_2027853_52.out
│   ├── batch_ref_4_budget_80_2027853_53.err
│   ├── batch_ref_4_budget_80_2027853_53.out
│   ├── batch_ref_4_budget_80_2027853_54.err
│   ├── batch_ref_4_budget_80_2027853_54.out
│   ├── batch_ref_4_budget_80_2027853_55.err
│   ├── batch_ref_4_budget_80_2027853_55.out
│   ├── batch_ref_4_budget_80_2027853_56.err
│   ├── batch_ref_4_budget_80_2027853_56.out
│   ├── batch_ref_4_budget_80_2027853_57.err
│   ├── batch_ref_4_budget_80_2027853_57.out
│   ├── batch_ref_4_budget_80_2027853_58.err
│   ├── batch_ref_4_budget_80_2027853_58.out
│   ├── batch_ref_4_budget_80_2027853_59.err
│   ├── batch_ref_4_budget_80_2027853_59.out
│   ├── batch_ref_4_budget_80_2027853_6.err
│   ├── batch_ref_4_budget_80_2027853_6.out
│   ├── batch_ref_4_budget_80_2027853_60.err
│   ├── batch_ref_4_budget_80_2027853_60.out
│   ├── batch_ref_4_budget_80_2027853_61.err
│   ├── batch_ref_4_budget_80_2027853_61.out
│   ├── batch_ref_4_budget_80_2027853_62.err
│   ├── batch_ref_4_budget_80_2027853_62.out
│   ├── batch_ref_4_budget_80_2027853_63.err
│   ├── batch_ref_4_budget_80_2027853_63.out
│   ├── batch_ref_4_budget_80_2027853_64.err
│   ├── batch_ref_4_budget_80_2027853_64.out
│   ├── batch_ref_4_budget_80_2027853_65.err
│   ├── batch_ref_4_budget_80_2027853_65.out
│   ├── batch_ref_4_budget_80_2027853_66.err
│   ├── batch_ref_4_budget_80_2027853_66.out
│   ├── batch_ref_4_budget_80_2027853_67.err
│   ├── batch_ref_4_budget_80_2027853_67.out
│   ├── batch_ref_4_budget_80_2027853_68.err
│   ├── batch_ref_4_budget_80_2027853_68.out
│   ├── batch_ref_4_budget_80_2027853_69.err
│   ├── batch_ref_4_budget_80_2027853_69.out
│   ├── batch_ref_4_budget_80_2027853_7.err
│   ├── batch_ref_4_budget_80_2027853_7.out
│   ├── batch_ref_4_budget_80_2027853_70.err
│   ├── batch_ref_4_budget_80_2027853_70.out
│   ├── batch_ref_4_budget_80_2027853_71.err
│   ├── batch_ref_4_budget_80_2027853_71.out
│   ├── batch_ref_4_budget_80_2027853_72.err
│   ├── batch_ref_4_budget_80_2027853_72.out
│   ├── batch_ref_4_budget_80_2027853_73.err
│   ├── batch_ref_4_budget_80_2027853_73.out
│   ├── batch_ref_4_budget_80_2027853_74.err
│   ├── batch_ref_4_budget_80_2027853_74.out
│   ├── batch_ref_4_budget_80_2027853_75.err
│   ├── batch_ref_4_budget_80_2027853_75.out
│   ├── batch_ref_4_budget_80_2027853_76.err
│   ├── batch_ref_4_budget_80_2027853_76.out
│   ├── batch_ref_4_budget_80_2027853_77.err
│   ├── batch_ref_4_budget_80_2027853_77.out
│   ├── batch_ref_4_budget_80_2027853_78.err
│   ├── batch_ref_4_budget_80_2027853_78.out
│   ├── batch_ref_4_budget_80_2027853_79.err
│   ├── batch_ref_4_budget_80_2027853_79.out
│   ├── batch_ref_4_budget_80_2027853_8.err
│   ├── batch_ref_4_budget_80_2027853_8.out
│   ├── batch_ref_4_budget_80_2027853_80.err
│   ├── batch_ref_4_budget_80_2027853_80.out
│   ├── batch_ref_4_budget_80_2027853_81.err
│   ├── batch_ref_4_budget_80_2027853_81.out
│   ├── batch_ref_4_budget_80_2027853_9.err
│   ├── batch_ref_4_budget_80_2027853_9.out
│   ├── batch_ref_4_budget_80_2027948_1.err
│   ├── batch_ref_4_budget_80_2027948_1.out
│   ├── batch_ref_4_budget_80_2027948_10.err
│   ├── batch_ref_4_budget_80_2027948_10.out
│   ├── batch_ref_4_budget_80_2027948_11.err
│   ├── batch_ref_4_budget_80_2027948_11.out
│   ├── batch_ref_4_budget_80_2027948_12.err
│   ├── batch_ref_4_budget_80_2027948_12.out
│   ├── batch_ref_4_budget_80_2027948_13.err
│   ├── batch_ref_4_budget_80_2027948_13.out
│   ├── batch_ref_4_budget_80_2027948_14.err
│   ├── batch_ref_4_budget_80_2027948_14.out
│   ├── batch_ref_4_budget_80_2027948_15.err
│   ├── batch_ref_4_budget_80_2027948_15.out
│   ├── batch_ref_4_budget_80_2027948_16.err
│   ├── batch_ref_4_budget_80_2027948_16.out
│   ├── batch_ref_4_budget_80_2027948_17.err
│   ├── batch_ref_4_budget_80_2027948_17.out
│   ├── batch_ref_4_budget_80_2027948_18.err
│   ├── batch_ref_4_budget_80_2027948_18.out
│   ├── batch_ref_4_budget_80_2027948_19.err
│   ├── batch_ref_4_budget_80_2027948_19.out
│   ├── batch_ref_4_budget_80_2027948_2.err
│   ├── batch_ref_4_budget_80_2027948_2.out
│   ├── batch_ref_4_budget_80_2027948_20.err
│   ├── batch_ref_4_budget_80_2027948_20.out
│   ├── batch_ref_4_budget_80_2027948_21.err
│   ├── batch_ref_4_budget_80_2027948_21.out
│   ├── batch_ref_4_budget_80_2027948_22.err
│   ├── batch_ref_4_budget_80_2027948_22.out
│   ├── batch_ref_4_budget_80_2027948_23.err
│   ├── batch_ref_4_budget_80_2027948_23.out
│   ├── batch_ref_4_budget_80_2027948_24.err
│   ├── batch_ref_4_budget_80_2027948_24.out
│   ├── batch_ref_4_budget_80_2027948_25.err
│   ├── batch_ref_4_budget_80_2027948_25.out
│   ├── batch_ref_4_budget_80_2027948_26.err
│   ├── batch_ref_4_budget_80_2027948_26.out
│   ├── batch_ref_4_budget_80_2027948_27.err
│   ├── batch_ref_4_budget_80_2027948_27.out
│   ├── batch_ref_4_budget_80_2027948_28.err
│   ├── batch_ref_4_budget_80_2027948_28.out
│   ├── batch_ref_4_budget_80_2027948_29.err
│   ├── batch_ref_4_budget_80_2027948_29.out
│   ├── batch_ref_4_budget_80_2027948_3.err
│   ├── batch_ref_4_budget_80_2027948_3.out
│   ├── batch_ref_4_budget_80_2027948_30.err
│   ├── batch_ref_4_budget_80_2027948_30.out
│   ├── batch_ref_4_budget_80_2027948_31.err
│   ├── batch_ref_4_budget_80_2027948_31.out
│   ├── batch_ref_4_budget_80_2027948_32.err
│   ├── batch_ref_4_budget_80_2027948_32.out
│   ├── batch_ref_4_budget_80_2027948_33.err
│   ├── batch_ref_4_budget_80_2027948_33.out
│   ├── batch_ref_4_budget_80_2027948_34.err
│   ├── batch_ref_4_budget_80_2027948_34.out
│   ├── batch_ref_4_budget_80_2027948_35.err
│   ├── batch_ref_4_budget_80_2027948_35.out
│   ├── batch_ref_4_budget_80_2027948_36.err
│   ├── batch_ref_4_budget_80_2027948_36.out
│   ├── batch_ref_4_budget_80_2027948_37.err
│   ├── batch_ref_4_budget_80_2027948_37.out
│   ├── batch_ref_4_budget_80_2027948_38.err
│   ├── batch_ref_4_budget_80_2027948_38.out
│   ├── batch_ref_4_budget_80_2027948_39.err
│   ├── batch_ref_4_budget_80_2027948_39.out
│   ├── batch_ref_4_budget_80_2027948_4.err
│   ├── batch_ref_4_budget_80_2027948_4.out
│   ├── batch_ref_4_budget_80_2027948_40.err
│   ├── batch_ref_4_budget_80_2027948_40.out
│   ├── batch_ref_4_budget_80_2027948_41.err
│   ├── batch_ref_4_budget_80_2027948_41.out
│   ├── batch_ref_4_budget_80_2027948_42.err
│   ├── batch_ref_4_budget_80_2027948_42.out
│   ├── batch_ref_4_budget_80_2027948_43.err
│   ├── batch_ref_4_budget_80_2027948_43.out
│   ├── batch_ref_4_budget_80_2027948_44.err
│   ├── batch_ref_4_budget_80_2027948_44.out
│   ├── batch_ref_4_budget_80_2027948_45.err
│   ├── batch_ref_4_budget_80_2027948_45.out
│   ├── batch_ref_4_budget_80_2027948_46.err
│   ├── batch_ref_4_budget_80_2027948_46.out
│   ├── batch_ref_4_budget_80_2027948_47.err
│   ├── batch_ref_4_budget_80_2027948_47.out
│   ├── batch_ref_4_budget_80_2027948_48.err
│   ├── batch_ref_4_budget_80_2027948_48.out
│   ├── batch_ref_4_budget_80_2027948_49.err
│   ├── batch_ref_4_budget_80_2027948_49.out
│   ├── batch_ref_4_budget_80_2027948_5.err
│   ├── batch_ref_4_budget_80_2027948_5.out
│   ├── batch_ref_4_budget_80_2027948_50.err
│   ├── batch_ref_4_budget_80_2027948_50.out
│   ├── batch_ref_4_budget_80_2027948_51.err
│   ├── batch_ref_4_budget_80_2027948_51.out
│   ├── batch_ref_4_budget_80_2027948_52.err
│   ├── batch_ref_4_budget_80_2027948_52.out
│   ├── batch_ref_4_budget_80_2027948_53.err
│   ├── batch_ref_4_budget_80_2027948_53.out
│   ├── batch_ref_4_budget_80_2027948_54.err
│   ├── batch_ref_4_budget_80_2027948_54.out
│   ├── batch_ref_4_budget_80_2027948_55.err
│   ├── batch_ref_4_budget_80_2027948_55.out
│   ├── batch_ref_4_budget_80_2027948_56.err
│   ├── batch_ref_4_budget_80_2027948_56.out
│   ├── batch_ref_4_budget_80_2027948_57.err
│   ├── batch_ref_4_budget_80_2027948_57.out
│   ├── batch_ref_4_budget_80_2027948_58.err
│   ├── batch_ref_4_budget_80_2027948_58.out
│   ├── batch_ref_4_budget_80_2027948_59.err
│   ├── batch_ref_4_budget_80_2027948_59.out
│   ├── batch_ref_4_budget_80_2027948_6.err
│   ├── batch_ref_4_budget_80_2027948_6.out
│   ├── batch_ref_4_budget_80_2027948_60.err
│   ├── batch_ref_4_budget_80_2027948_60.out
│   ├── batch_ref_4_budget_80_2027948_61.err
│   ├── batch_ref_4_budget_80_2027948_61.out
│   ├── batch_ref_4_budget_80_2027948_62.err
│   ├── batch_ref_4_budget_80_2027948_62.out
│   ├── batch_ref_4_budget_80_2027948_63.err
│   ├── batch_ref_4_budget_80_2027948_63.out
│   ├── batch_ref_4_budget_80_2027948_64.err
│   ├── batch_ref_4_budget_80_2027948_64.out
│   ├── batch_ref_4_budget_80_2027948_65.err
│   ├── batch_ref_4_budget_80_2027948_65.out
│   ├── batch_ref_4_budget_80_2027948_66.err
│   ├── batch_ref_4_budget_80_2027948_66.out
│   ├── batch_ref_4_budget_80_2027948_67.err
│   ├── batch_ref_4_budget_80_2027948_67.out
│   ├── batch_ref_4_budget_80_2027948_68.err
│   ├── batch_ref_4_budget_80_2027948_68.out
│   ├── batch_ref_4_budget_80_2027948_69.err
│   ├── batch_ref_4_budget_80_2027948_69.out
│   ├── batch_ref_4_budget_80_2027948_7.err
│   ├── batch_ref_4_budget_80_2027948_7.out
│   ├── batch_ref_4_budget_80_2027948_70.err
│   ├── batch_ref_4_budget_80_2027948_70.out
│   ├── batch_ref_4_budget_80_2027948_71.err
│   ├── batch_ref_4_budget_80_2027948_71.out
│   ├── batch_ref_4_budget_80_2027948_72.err
│   ├── batch_ref_4_budget_80_2027948_72.out
│   ├── batch_ref_4_budget_80_2027948_73.err
│   ├── batch_ref_4_budget_80_2027948_73.out
│   ├── batch_ref_4_budget_80_2027948_74.err
│   ├── batch_ref_4_budget_80_2027948_74.out
│   ├── batch_ref_4_budget_80_2027948_75.err
│   ├── batch_ref_4_budget_80_2027948_75.out
│   ├── batch_ref_4_budget_80_2027948_76.err
│   ├── batch_ref_4_budget_80_2027948_76.out
│   ├── batch_ref_4_budget_80_2027948_77.err
│   ├── batch_ref_4_budget_80_2027948_77.out
│   ├── batch_ref_4_budget_80_2027948_78.err
│   ├── batch_ref_4_budget_80_2027948_78.out
│   ├── batch_ref_4_budget_80_2027948_79.err
│   ├── batch_ref_4_budget_80_2027948_79.out
│   ├── batch_ref_4_budget_80_2027948_8.err
│   ├── batch_ref_4_budget_80_2027948_8.out
│   ├── batch_ref_4_budget_80_2027948_80.err
│   ├── batch_ref_4_budget_80_2027948_80.out
│   ├── batch_ref_4_budget_80_2027948_81.err
│   ├── batch_ref_4_budget_80_2027948_81.out
│   ├── batch_ref_4_budget_80_2027948_9.err
│   ├── batch_ref_4_budget_80_2027948_9.out
│   ├── batch_ref_4_budget_80_2028138_1.err
│   ├── batch_ref_4_budget_80_2028138_1.out
│   ├── batch_ref_4_budget_80_2028138_10.err
│   ├── batch_ref_4_budget_80_2028138_10.out
│   ├── batch_ref_4_budget_80_2028138_11.err
│   ├── batch_ref_4_budget_80_2028138_11.out
│   ├── batch_ref_4_budget_80_2028138_12.err
│   ├── batch_ref_4_budget_80_2028138_12.out
│   ├── batch_ref_4_budget_80_2028138_13.err
│   ├── batch_ref_4_budget_80_2028138_13.out
│   ├── batch_ref_4_budget_80_2028138_14.err
│   ├── batch_ref_4_budget_80_2028138_14.out
│   ├── batch_ref_4_budget_80_2028138_15.err
│   ├── batch_ref_4_budget_80_2028138_15.out
│   ├── batch_ref_4_budget_80_2028138_16.err
│   ├── batch_ref_4_budget_80_2028138_16.out
│   ├── batch_ref_4_budget_80_2028138_17.err
│   ├── batch_ref_4_budget_80_2028138_17.out
│   ├── batch_ref_4_budget_80_2028138_18.err
│   ├── batch_ref_4_budget_80_2028138_18.out
│   ├── batch_ref_4_budget_80_2028138_19.err
│   ├── batch_ref_4_budget_80_2028138_19.out
│   ├── batch_ref_4_budget_80_2028138_2.err
│   ├── batch_ref_4_budget_80_2028138_2.out
│   ├── batch_ref_4_budget_80_2028138_20.err
│   ├── batch_ref_4_budget_80_2028138_20.out
│   ├── batch_ref_4_budget_80_2028138_21.err
│   ├── batch_ref_4_budget_80_2028138_21.out
│   ├── batch_ref_4_budget_80_2028138_22.err
│   ├── batch_ref_4_budget_80_2028138_22.out
│   ├── batch_ref_4_budget_80_2028138_23.err
│   ├── batch_ref_4_budget_80_2028138_23.out
│   ├── batch_ref_4_budget_80_2028138_24.err
│   ├── batch_ref_4_budget_80_2028138_24.out
│   ├── batch_ref_4_budget_80_2028138_25.err
│   ├── batch_ref_4_budget_80_2028138_25.out
│   ├── batch_ref_4_budget_80_2028138_26.err
│   ├── batch_ref_4_budget_80_2028138_26.out
│   ├── batch_ref_4_budget_80_2028138_27.err
│   ├── batch_ref_4_budget_80_2028138_27.out
│   ├── batch_ref_4_budget_80_2028138_28.err
│   ├── batch_ref_4_budget_80_2028138_28.out
│   ├── batch_ref_4_budget_80_2028138_29.err
│   ├── batch_ref_4_budget_80_2028138_29.out
│   ├── batch_ref_4_budget_80_2028138_3.err
│   ├── batch_ref_4_budget_80_2028138_3.out
│   ├── batch_ref_4_budget_80_2028138_30.err
│   ├── batch_ref_4_budget_80_2028138_30.out
│   ├── batch_ref_4_budget_80_2028138_31.err
│   ├── batch_ref_4_budget_80_2028138_31.out
│   ├── batch_ref_4_budget_80_2028138_32.err
│   ├── batch_ref_4_budget_80_2028138_32.out
│   ├── batch_ref_4_budget_80_2028138_33.err
│   ├── batch_ref_4_budget_80_2028138_33.out
│   ├── batch_ref_4_budget_80_2028138_34.err
│   ├── batch_ref_4_budget_80_2028138_34.out
│   ├── batch_ref_4_budget_80_2028138_35.err
│   ├── batch_ref_4_budget_80_2028138_35.out
│   ├── batch_ref_4_budget_80_2028138_36.err
│   ├── batch_ref_4_budget_80_2028138_36.out
│   ├── batch_ref_4_budget_80_2028138_37.err
│   ├── batch_ref_4_budget_80_2028138_37.out
│   ├── batch_ref_4_budget_80_2028138_38.err
│   ├── batch_ref_4_budget_80_2028138_38.out
│   ├── batch_ref_4_budget_80_2028138_39.err
│   ├── batch_ref_4_budget_80_2028138_39.out
│   ├── batch_ref_4_budget_80_2028138_4.err
│   ├── batch_ref_4_budget_80_2028138_4.out
│   ├── batch_ref_4_budget_80_2028138_40.err
│   ├── batch_ref_4_budget_80_2028138_40.out
│   ├── batch_ref_4_budget_80_2028138_41.err
│   ├── batch_ref_4_budget_80_2028138_41.out
│   ├── batch_ref_4_budget_80_2028138_42.err
│   ├── batch_ref_4_budget_80_2028138_42.out
│   ├── batch_ref_4_budget_80_2028138_43.err
│   ├── batch_ref_4_budget_80_2028138_43.out
│   ├── batch_ref_4_budget_80_2028138_44.err
│   ├── batch_ref_4_budget_80_2028138_44.out
│   ├── batch_ref_4_budget_80_2028138_45.err
│   ├── batch_ref_4_budget_80_2028138_45.out
│   ├── batch_ref_4_budget_80_2028138_46.err
│   ├── batch_ref_4_budget_80_2028138_46.out
│   ├── batch_ref_4_budget_80_2028138_47.err
│   ├── batch_ref_4_budget_80_2028138_47.out
│   ├── batch_ref_4_budget_80_2028138_48.err
│   ├── batch_ref_4_budget_80_2028138_48.out
│   ├── batch_ref_4_budget_80_2028138_49.err
│   ├── batch_ref_4_budget_80_2028138_49.out
│   ├── batch_ref_4_budget_80_2028138_5.err
│   ├── batch_ref_4_budget_80_2028138_5.out
│   ├── batch_ref_4_budget_80_2028138_50.err
│   ├── batch_ref_4_budget_80_2028138_50.out
│   ├── batch_ref_4_budget_80_2028138_51.err
│   ├── batch_ref_4_budget_80_2028138_51.out
│   ├── batch_ref_4_budget_80_2028138_52.err
│   ├── batch_ref_4_budget_80_2028138_52.out
│   ├── batch_ref_4_budget_80_2028138_53.err
│   ├── batch_ref_4_budget_80_2028138_53.out
│   ├── batch_ref_4_budget_80_2028138_54.err
│   ├── batch_ref_4_budget_80_2028138_54.out
│   ├── batch_ref_4_budget_80_2028138_55.err
│   ├── batch_ref_4_budget_80_2028138_55.out
│   ├── batch_ref_4_budget_80_2028138_56.err
│   ├── batch_ref_4_budget_80_2028138_56.out
│   ├── batch_ref_4_budget_80_2028138_57.err
│   ├── batch_ref_4_budget_80_2028138_57.out
│   ├── batch_ref_4_budget_80_2028138_58.err
│   ├── batch_ref_4_budget_80_2028138_58.out
│   ├── batch_ref_4_budget_80_2028138_59.err
│   ├── batch_ref_4_budget_80_2028138_59.out
│   ├── batch_ref_4_budget_80_2028138_6.err
│   ├── batch_ref_4_budget_80_2028138_6.out
│   ├── batch_ref_4_budget_80_2028138_60.err
│   ├── batch_ref_4_budget_80_2028138_60.out
│   ├── batch_ref_4_budget_80_2028138_61.err
│   ├── batch_ref_4_budget_80_2028138_61.out
│   ├── batch_ref_4_budget_80_2028138_62.err
│   ├── batch_ref_4_budget_80_2028138_62.out
│   ├── batch_ref_4_budget_80_2028138_63.err
│   ├── batch_ref_4_budget_80_2028138_63.out
│   ├── batch_ref_4_budget_80_2028138_64.err
│   ├── batch_ref_4_budget_80_2028138_64.out
│   ├── batch_ref_4_budget_80_2028138_65.err
│   ├── batch_ref_4_budget_80_2028138_65.out
│   ├── batch_ref_4_budget_80_2028138_66.err
│   ├── batch_ref_4_budget_80_2028138_66.out
│   ├── batch_ref_4_budget_80_2028138_67.err
│   ├── batch_ref_4_budget_80_2028138_67.out
│   ├── batch_ref_4_budget_80_2028138_68.err
│   ├── batch_ref_4_budget_80_2028138_68.out
│   ├── batch_ref_4_budget_80_2028138_69.err
│   ├── batch_ref_4_budget_80_2028138_69.out
│   ├── batch_ref_4_budget_80_2028138_7.err
│   ├── batch_ref_4_budget_80_2028138_7.out
│   ├── batch_ref_4_budget_80_2028138_70.err
│   ├── batch_ref_4_budget_80_2028138_70.out
│   ├── batch_ref_4_budget_80_2028138_71.err
│   ├── batch_ref_4_budget_80_2028138_71.out
│   ├── batch_ref_4_budget_80_2028138_72.err
│   ├── batch_ref_4_budget_80_2028138_72.out
│   ├── batch_ref_4_budget_80_2028138_73.err
│   ├── batch_ref_4_budget_80_2028138_73.out
│   ├── batch_ref_4_budget_80_2028138_74.err
│   ├── batch_ref_4_budget_80_2028138_74.out
│   ├── batch_ref_4_budget_80_2028138_75.err
│   ├── batch_ref_4_budget_80_2028138_75.out
│   ├── batch_ref_4_budget_80_2028138_76.err
│   ├── batch_ref_4_budget_80_2028138_76.out
│   ├── batch_ref_4_budget_80_2028138_77.err
│   ├── batch_ref_4_budget_80_2028138_77.out
│   ├── batch_ref_4_budget_80_2028138_78.err
│   ├── batch_ref_4_budget_80_2028138_78.out
│   ├── batch_ref_4_budget_80_2028138_79.err
│   ├── batch_ref_4_budget_80_2028138_79.out
│   ├── batch_ref_4_budget_80_2028138_8.err
│   ├── batch_ref_4_budget_80_2028138_8.out
│   ├── batch_ref_4_budget_80_2028138_80.err
│   ├── batch_ref_4_budget_80_2028138_80.out
│   ├── batch_ref_4_budget_80_2028138_81.err
│   ├── batch_ref_4_budget_80_2028138_81.out
│   ├── batch_ref_4_budget_80_2028138_9.err
│   ├── batch_ref_4_budget_80_2028138_9.out
│   ├── batch_ref_4_budget_80_2040025_1.err
│   ├── batch_ref_4_budget_80_2040025_1.out
│   ├── batch_ref_4_budget_80_2040025_10.err
│   ├── batch_ref_4_budget_80_2040025_10.out
│   ├── batch_ref_4_budget_80_2040025_11.err
│   ├── batch_ref_4_budget_80_2040025_11.out
│   ├── batch_ref_4_budget_80_2040025_12.err
│   ├── batch_ref_4_budget_80_2040025_12.out
│   ├── batch_ref_4_budget_80_2040025_13.err
│   ├── batch_ref_4_budget_80_2040025_13.out
│   ├── batch_ref_4_budget_80_2040025_14.err
│   ├── batch_ref_4_budget_80_2040025_14.out
│   ├── batch_ref_4_budget_80_2040025_15.err
│   ├── batch_ref_4_budget_80_2040025_15.out
│   ├── batch_ref_4_budget_80_2040025_16.err
│   ├── batch_ref_4_budget_80_2040025_16.out
│   ├── batch_ref_4_budget_80_2040025_17.err
│   ├── batch_ref_4_budget_80_2040025_17.out
│   ├── batch_ref_4_budget_80_2040025_18.err
│   ├── batch_ref_4_budget_80_2040025_18.out
│   ├── batch_ref_4_budget_80_2040025_19.err
│   ├── batch_ref_4_budget_80_2040025_19.out
│   ├── batch_ref_4_budget_80_2040025_2.err
│   ├── batch_ref_4_budget_80_2040025_2.out
│   ├── batch_ref_4_budget_80_2040025_20.err
│   ├── batch_ref_4_budget_80_2040025_20.out
│   ├── batch_ref_4_budget_80_2040025_21.err
│   ├── batch_ref_4_budget_80_2040025_21.out
│   ├── batch_ref_4_budget_80_2040025_22.err
│   ├── batch_ref_4_budget_80_2040025_22.out
│   ├── batch_ref_4_budget_80_2040025_23.err
│   ├── batch_ref_4_budget_80_2040025_23.out
│   ├── batch_ref_4_budget_80_2040025_24.err
│   ├── batch_ref_4_budget_80_2040025_24.out
│   ├── batch_ref_4_budget_80_2040025_25.err
│   ├── batch_ref_4_budget_80_2040025_25.out
│   ├── batch_ref_4_budget_80_2040025_26.err
│   ├── batch_ref_4_budget_80_2040025_26.out
│   ├── batch_ref_4_budget_80_2040025_27.err
│   ├── batch_ref_4_budget_80_2040025_27.out
│   ├── batch_ref_4_budget_80_2040025_28.err
│   ├── batch_ref_4_budget_80_2040025_28.out
│   ├── batch_ref_4_budget_80_2040025_29.err
│   ├── batch_ref_4_budget_80_2040025_29.out
│   ├── batch_ref_4_budget_80_2040025_3.err
│   ├── batch_ref_4_budget_80_2040025_3.out
│   ├── batch_ref_4_budget_80_2040025_30.err
│   ├── batch_ref_4_budget_80_2040025_30.out
│   ├── batch_ref_4_budget_80_2040025_31.err
│   ├── batch_ref_4_budget_80_2040025_31.out
│   ├── batch_ref_4_budget_80_2040025_32.err
│   ├── batch_ref_4_budget_80_2040025_32.out
│   ├── batch_ref_4_budget_80_2040025_33.err
│   ├── batch_ref_4_budget_80_2040025_33.out
│   ├── batch_ref_4_budget_80_2040025_34.err
│   ├── batch_ref_4_budget_80_2040025_34.out
│   ├── batch_ref_4_budget_80_2040025_35.err
│   ├── batch_ref_4_budget_80_2040025_35.out
│   ├── batch_ref_4_budget_80_2040025_36.err
│   ├── batch_ref_4_budget_80_2040025_36.out
│   ├── batch_ref_4_budget_80_2040025_37.err
│   ├── batch_ref_4_budget_80_2040025_37.out
│   ├── batch_ref_4_budget_80_2040025_38.err
│   ├── batch_ref_4_budget_80_2040025_38.out
│   ├── batch_ref_4_budget_80_2040025_39.err
│   ├── batch_ref_4_budget_80_2040025_39.out
│   ├── batch_ref_4_budget_80_2040025_4.err
│   ├── batch_ref_4_budget_80_2040025_4.out
│   ├── batch_ref_4_budget_80_2040025_40.err
│   ├── batch_ref_4_budget_80_2040025_40.out
│   ├── batch_ref_4_budget_80_2040025_41.err
│   ├── batch_ref_4_budget_80_2040025_41.out
│   ├── batch_ref_4_budget_80_2040025_42.err
│   ├── batch_ref_4_budget_80_2040025_42.out
│   ├── batch_ref_4_budget_80_2040025_43.err
│   ├── batch_ref_4_budget_80_2040025_43.out
│   ├── batch_ref_4_budget_80_2040025_44.err
│   ├── batch_ref_4_budget_80_2040025_44.out
│   ├── batch_ref_4_budget_80_2040025_45.err
│   ├── batch_ref_4_budget_80_2040025_45.out
│   ├── batch_ref_4_budget_80_2040025_46.err
│   ├── batch_ref_4_budget_80_2040025_46.out
│   ├── batch_ref_4_budget_80_2040025_47.err
│   ├── batch_ref_4_budget_80_2040025_47.out
│   ├── batch_ref_4_budget_80_2040025_48.err
│   ├── batch_ref_4_budget_80_2040025_48.out
│   ├── batch_ref_4_budget_80_2040025_49.err
│   ├── batch_ref_4_budget_80_2040025_49.out
│   ├── batch_ref_4_budget_80_2040025_5.err
│   ├── batch_ref_4_budget_80_2040025_5.out
│   ├── batch_ref_4_budget_80_2040025_50.err
│   ├── batch_ref_4_budget_80_2040025_50.out
│   ├── batch_ref_4_budget_80_2040025_51.err
│   ├── batch_ref_4_budget_80_2040025_51.out
│   ├── batch_ref_4_budget_80_2040025_52.err
│   ├── batch_ref_4_budget_80_2040025_52.out
│   ├── batch_ref_4_budget_80_2040025_53.err
│   ├── batch_ref_4_budget_80_2040025_53.out
│   ├── batch_ref_4_budget_80_2040025_54.err
│   ├── batch_ref_4_budget_80_2040025_54.out
│   ├── batch_ref_4_budget_80_2040025_55.err
│   ├── batch_ref_4_budget_80_2040025_55.out
│   ├── batch_ref_4_budget_80_2040025_56.err
│   ├── batch_ref_4_budget_80_2040025_56.out
│   ├── batch_ref_4_budget_80_2040025_57.err
│   ├── batch_ref_4_budget_80_2040025_57.out
│   ├── batch_ref_4_budget_80_2040025_58.err
│   ├── batch_ref_4_budget_80_2040025_58.out
│   ├── batch_ref_4_budget_80_2040025_59.err
│   ├── batch_ref_4_budget_80_2040025_59.out
│   ├── batch_ref_4_budget_80_2040025_6.err
│   ├── batch_ref_4_budget_80_2040025_6.out
│   ├── batch_ref_4_budget_80_2040025_60.err
│   ├── batch_ref_4_budget_80_2040025_60.out
│   ├── batch_ref_4_budget_80_2040025_61.err
│   ├── batch_ref_4_budget_80_2040025_61.out
│   ├── batch_ref_4_budget_80_2040025_62.err
│   ├── batch_ref_4_budget_80_2040025_62.out
│   ├── batch_ref_4_budget_80_2040025_63.err
│   ├── batch_ref_4_budget_80_2040025_63.out
│   ├── batch_ref_4_budget_80_2040025_64.err
│   ├── batch_ref_4_budget_80_2040025_64.out
│   ├── batch_ref_4_budget_80_2040025_65.err
│   ├── batch_ref_4_budget_80_2040025_65.out
│   ├── batch_ref_4_budget_80_2040025_66.err
│   ├── batch_ref_4_budget_80_2040025_66.out
│   ├── batch_ref_4_budget_80_2040025_67.err
│   ├── batch_ref_4_budget_80_2040025_67.out
│   ├── batch_ref_4_budget_80_2040025_68.err
│   ├── batch_ref_4_budget_80_2040025_68.out
│   ├── batch_ref_4_budget_80_2040025_69.err
│   ├── batch_ref_4_budget_80_2040025_69.out
│   ├── batch_ref_4_budget_80_2040025_7.err
│   ├── batch_ref_4_budget_80_2040025_7.out
│   ├── batch_ref_4_budget_80_2040025_70.err
│   ├── batch_ref_4_budget_80_2040025_70.out
│   ├── batch_ref_4_budget_80_2040025_71.err
│   ├── batch_ref_4_budget_80_2040025_71.out
│   ├── batch_ref_4_budget_80_2040025_72.err
│   ├── batch_ref_4_budget_80_2040025_72.out
│   ├── batch_ref_4_budget_80_2040025_73.err
│   ├── batch_ref_4_budget_80_2040025_73.out
│   ├── batch_ref_4_budget_80_2040025_74.err
│   ├── batch_ref_4_budget_80_2040025_74.out
│   ├── batch_ref_4_budget_80_2040025_75.err
│   ├── batch_ref_4_budget_80_2040025_75.out
│   ├── batch_ref_4_budget_80_2040025_76.err
│   ├── batch_ref_4_budget_80_2040025_76.out
│   ├── batch_ref_4_budget_80_2040025_77.err
│   ├── batch_ref_4_budget_80_2040025_77.out
│   ├── batch_ref_4_budget_80_2040025_78.err
│   ├── batch_ref_4_budget_80_2040025_78.out
│   ├── batch_ref_4_budget_80_2040025_79.err
│   ├── batch_ref_4_budget_80_2040025_79.out
│   ├── batch_ref_4_budget_80_2040025_8.err
│   ├── batch_ref_4_budget_80_2040025_8.out
│   ├── batch_ref_4_budget_80_2040025_80.err
│   ├── batch_ref_4_budget_80_2040025_80.out
│   ├── batch_ref_4_budget_80_2040025_81.err
│   ├── batch_ref_4_budget_80_2040025_81.out
│   ├── batch_ref_4_budget_80_2040025_9.err
│   ├── batch_ref_4_budget_80_2040025_9.out
│   ├── batch_ref_4_budget_80_max_4_2067128_1.err
│   ├── batch_ref_4_budget_80_max_4_2067128_1.out
│   ├── batch_ref_4_budget_80_max_4_2067128_10.err
│   ├── batch_ref_4_budget_80_max_4_2067128_10.out
│   ├── batch_ref_4_budget_80_max_4_2067128_11.err
│   ├── batch_ref_4_budget_80_max_4_2067128_11.out
│   ├── batch_ref_4_budget_80_max_4_2067128_12.err
│   ├── batch_ref_4_budget_80_max_4_2067128_12.out
│   ├── batch_ref_4_budget_80_max_4_2067128_13.err
│   ├── batch_ref_4_budget_80_max_4_2067128_13.out
│   ├── batch_ref_4_budget_80_max_4_2067128_14.err
│   ├── batch_ref_4_budget_80_max_4_2067128_14.out
│   ├── batch_ref_4_budget_80_max_4_2067128_15.err
│   ├── batch_ref_4_budget_80_max_4_2067128_15.out
│   ├── batch_ref_4_budget_80_max_4_2067128_16.err
│   ├── batch_ref_4_budget_80_max_4_2067128_16.out
│   ├── batch_ref_4_budget_80_max_4_2067128_17.err
│   ├── batch_ref_4_budget_80_max_4_2067128_17.out
│   ├── batch_ref_4_budget_80_max_4_2067128_18.err
│   ├── batch_ref_4_budget_80_max_4_2067128_18.out
│   ├── batch_ref_4_budget_80_max_4_2067128_19.err
│   ├── batch_ref_4_budget_80_max_4_2067128_19.out
│   ├── batch_ref_4_budget_80_max_4_2067128_2.err
│   ├── batch_ref_4_budget_80_max_4_2067128_2.out
│   ├── batch_ref_4_budget_80_max_4_2067128_20.err
│   ├── batch_ref_4_budget_80_max_4_2067128_20.out
│   ├── batch_ref_4_budget_80_max_4_2067128_21.err
│   ├── batch_ref_4_budget_80_max_4_2067128_21.out
│   ├── batch_ref_4_budget_80_max_4_2067128_22.err
│   ├── batch_ref_4_budget_80_max_4_2067128_22.out
│   ├── batch_ref_4_budget_80_max_4_2067128_23.err
│   ├── batch_ref_4_budget_80_max_4_2067128_23.out
│   ├── batch_ref_4_budget_80_max_4_2067128_24.err
│   ├── batch_ref_4_budget_80_max_4_2067128_24.out
│   ├── batch_ref_4_budget_80_max_4_2067128_25.err
│   ├── batch_ref_4_budget_80_max_4_2067128_25.out
│   ├── batch_ref_4_budget_80_max_4_2067128_26.err
│   ├── batch_ref_4_budget_80_max_4_2067128_26.out
│   ├── batch_ref_4_budget_80_max_4_2067128_27.err
│   ├── batch_ref_4_budget_80_max_4_2067128_27.out
│   ├── batch_ref_4_budget_80_max_4_2067128_28.err
│   ├── batch_ref_4_budget_80_max_4_2067128_28.out
│   ├── batch_ref_4_budget_80_max_4_2067128_29.err
│   ├── batch_ref_4_budget_80_max_4_2067128_29.out
│   ├── batch_ref_4_budget_80_max_4_2067128_3.err
│   ├── batch_ref_4_budget_80_max_4_2067128_3.out
│   ├── batch_ref_4_budget_80_max_4_2067128_30.err
│   ├── batch_ref_4_budget_80_max_4_2067128_30.out
│   ├── batch_ref_4_budget_80_max_4_2067128_31.err
│   ├── batch_ref_4_budget_80_max_4_2067128_31.out
│   ├── batch_ref_4_budget_80_max_4_2067128_32.err
│   ├── batch_ref_4_budget_80_max_4_2067128_32.out
│   ├── batch_ref_4_budget_80_max_4_2067128_33.err
│   ├── batch_ref_4_budget_80_max_4_2067128_33.out
│   ├── batch_ref_4_budget_80_max_4_2067128_34.err
│   ├── batch_ref_4_budget_80_max_4_2067128_34.out
│   ├── batch_ref_4_budget_80_max_4_2067128_35.err
│   ├── batch_ref_4_budget_80_max_4_2067128_35.out
│   ├── batch_ref_4_budget_80_max_4_2067128_36.err
│   ├── batch_ref_4_budget_80_max_4_2067128_36.out
│   ├── batch_ref_4_budget_80_max_4_2067128_37.err
│   ├── batch_ref_4_budget_80_max_4_2067128_37.out
│   ├── batch_ref_4_budget_80_max_4_2067128_38.err
│   ├── batch_ref_4_budget_80_max_4_2067128_38.out
│   ├── batch_ref_4_budget_80_max_4_2067128_39.err
│   ├── batch_ref_4_budget_80_max_4_2067128_39.out
│   ├── batch_ref_4_budget_80_max_4_2067128_4.err
│   ├── batch_ref_4_budget_80_max_4_2067128_4.out
│   ├── batch_ref_4_budget_80_max_4_2067128_40.err
│   ├── batch_ref_4_budget_80_max_4_2067128_40.out
│   ├── batch_ref_4_budget_80_max_4_2067128_41.err
│   ├── batch_ref_4_budget_80_max_4_2067128_41.out
│   ├── batch_ref_4_budget_80_max_4_2067128_42.err
│   ├── batch_ref_4_budget_80_max_4_2067128_42.out
│   ├── batch_ref_4_budget_80_max_4_2067128_43.err
│   ├── batch_ref_4_budget_80_max_4_2067128_43.out
│   ├── batch_ref_4_budget_80_max_4_2067128_44.err
│   ├── batch_ref_4_budget_80_max_4_2067128_44.out
│   ├── batch_ref_4_budget_80_max_4_2067128_45.err
│   ├── batch_ref_4_budget_80_max_4_2067128_45.out
│   ├── batch_ref_4_budget_80_max_4_2067128_46.err
│   ├── batch_ref_4_budget_80_max_4_2067128_46.out
│   ├── batch_ref_4_budget_80_max_4_2067128_47.err
│   ├── batch_ref_4_budget_80_max_4_2067128_47.out
│   ├── batch_ref_4_budget_80_max_4_2067128_48.err
│   ├── batch_ref_4_budget_80_max_4_2067128_48.out
│   ├── batch_ref_4_budget_80_max_4_2067128_49.err
│   ├── batch_ref_4_budget_80_max_4_2067128_49.out
│   ├── batch_ref_4_budget_80_max_4_2067128_5.err
│   ├── batch_ref_4_budget_80_max_4_2067128_5.out
│   ├── batch_ref_4_budget_80_max_4_2067128_50.err
│   ├── batch_ref_4_budget_80_max_4_2067128_50.out
│   ├── batch_ref_4_budget_80_max_4_2067128_51.err
│   ├── batch_ref_4_budget_80_max_4_2067128_51.out
│   ├── batch_ref_4_budget_80_max_4_2067128_52.err
│   ├── batch_ref_4_budget_80_max_4_2067128_52.out
│   ├── batch_ref_4_budget_80_max_4_2067128_53.err
│   ├── batch_ref_4_budget_80_max_4_2067128_53.out
│   ├── batch_ref_4_budget_80_max_4_2067128_54.err
│   ├── batch_ref_4_budget_80_max_4_2067128_54.out
│   ├── batch_ref_4_budget_80_max_4_2067128_55.err
│   ├── batch_ref_4_budget_80_max_4_2067128_55.out
│   ├── batch_ref_4_budget_80_max_4_2067128_56.err
│   ├── batch_ref_4_budget_80_max_4_2067128_56.out
│   ├── batch_ref_4_budget_80_max_4_2067128_57.err
│   ├── batch_ref_4_budget_80_max_4_2067128_57.out
│   ├── batch_ref_4_budget_80_max_4_2067128_58.err
│   ├── batch_ref_4_budget_80_max_4_2067128_58.out
│   ├── batch_ref_4_budget_80_max_4_2067128_59.err
│   ├── batch_ref_4_budget_80_max_4_2067128_59.out
│   ├── batch_ref_4_budget_80_max_4_2067128_6.err
│   ├── batch_ref_4_budget_80_max_4_2067128_6.out
│   ├── batch_ref_4_budget_80_max_4_2067128_60.err
│   ├── batch_ref_4_budget_80_max_4_2067128_60.out
│   ├── batch_ref_4_budget_80_max_4_2067128_61.err
│   ├── batch_ref_4_budget_80_max_4_2067128_61.out
│   ├── batch_ref_4_budget_80_max_4_2067128_62.err
│   ├── batch_ref_4_budget_80_max_4_2067128_62.out
│   ├── batch_ref_4_budget_80_max_4_2067128_63.err
│   ├── batch_ref_4_budget_80_max_4_2067128_63.out
│   ├── batch_ref_4_budget_80_max_4_2067128_64.err
│   ├── batch_ref_4_budget_80_max_4_2067128_64.out
│   ├── batch_ref_4_budget_80_max_4_2067128_65.err
│   ├── batch_ref_4_budget_80_max_4_2067128_65.out
│   ├── batch_ref_4_budget_80_max_4_2067128_66.err
│   ├── batch_ref_4_budget_80_max_4_2067128_66.out
│   ├── batch_ref_4_budget_80_max_4_2067128_67.err
│   ├── batch_ref_4_budget_80_max_4_2067128_67.out
│   ├── batch_ref_4_budget_80_max_4_2067128_68.err
│   ├── batch_ref_4_budget_80_max_4_2067128_68.out
│   ├── batch_ref_4_budget_80_max_4_2067128_69.err
│   ├── batch_ref_4_budget_80_max_4_2067128_69.out
│   ├── batch_ref_4_budget_80_max_4_2067128_7.err
│   ├── batch_ref_4_budget_80_max_4_2067128_7.out
│   ├── batch_ref_4_budget_80_max_4_2067128_70.err
│   ├── batch_ref_4_budget_80_max_4_2067128_70.out
│   ├── batch_ref_4_budget_80_max_4_2067128_71.err
│   ├── batch_ref_4_budget_80_max_4_2067128_71.out
│   ├── batch_ref_4_budget_80_max_4_2067128_72.err
│   ├── batch_ref_4_budget_80_max_4_2067128_72.out
│   ├── batch_ref_4_budget_80_max_4_2067128_73.err
│   ├── batch_ref_4_budget_80_max_4_2067128_73.out
│   ├── batch_ref_4_budget_80_max_4_2067128_74.err
│   ├── batch_ref_4_budget_80_max_4_2067128_74.out
│   ├── batch_ref_4_budget_80_max_4_2067128_75.err
│   ├── batch_ref_4_budget_80_max_4_2067128_75.out
│   ├── batch_ref_4_budget_80_max_4_2067128_76.err
│   ├── batch_ref_4_budget_80_max_4_2067128_76.out
│   ├── batch_ref_4_budget_80_max_4_2067128_77.err
│   ├── batch_ref_4_budget_80_max_4_2067128_77.out
│   ├── batch_ref_4_budget_80_max_4_2067128_78.err
│   ├── batch_ref_4_budget_80_max_4_2067128_78.out
│   ├── batch_ref_4_budget_80_max_4_2067128_79.err
│   ├── batch_ref_4_budget_80_max_4_2067128_79.out
│   ├── batch_ref_4_budget_80_max_4_2067128_8.err
│   ├── batch_ref_4_budget_80_max_4_2067128_8.out
│   ├── batch_ref_4_budget_80_max_4_2067128_80.err
│   ├── batch_ref_4_budget_80_max_4_2067128_80.out
│   ├── batch_ref_4_budget_80_max_4_2067128_81.err
│   ├── batch_ref_4_budget_80_max_4_2067128_81.out
│   ├── batch_ref_4_budget_80_max_4_2067128_9.err
│   ├── batch_ref_4_budget_80_max_4_2067128_9.out
│   ├── batch_ref_5_budget_100_2025039_1.err
│   ├── batch_ref_5_budget_100_2025039_1.out
│   ├── batch_ref_5_budget_100_2025039_10.err
│   ├── batch_ref_5_budget_100_2025039_10.out
│   ├── batch_ref_5_budget_100_2025039_11.err
│   ├── batch_ref_5_budget_100_2025039_11.out
│   ├── batch_ref_5_budget_100_2025039_12.err
│   ├── batch_ref_5_budget_100_2025039_12.out
│   ├── batch_ref_5_budget_100_2025039_13.err
│   ├── batch_ref_5_budget_100_2025039_13.out
│   ├── batch_ref_5_budget_100_2025039_14.err
│   ├── batch_ref_5_budget_100_2025039_14.out
│   ├── batch_ref_5_budget_100_2025039_15.err
│   ├── batch_ref_5_budget_100_2025039_15.out
│   ├── batch_ref_5_budget_100_2025039_16.err
│   ├── batch_ref_5_budget_100_2025039_16.out
│   ├── batch_ref_5_budget_100_2025039_17.err
│   ├── batch_ref_5_budget_100_2025039_17.out
│   ├── batch_ref_5_budget_100_2025039_18.err
│   ├── batch_ref_5_budget_100_2025039_18.out
│   ├── batch_ref_5_budget_100_2025039_19.err
│   ├── batch_ref_5_budget_100_2025039_19.out
│   ├── batch_ref_5_budget_100_2025039_2.err
│   ├── batch_ref_5_budget_100_2025039_2.out
│   ├── batch_ref_5_budget_100_2025039_20.err
│   ├── batch_ref_5_budget_100_2025039_20.out
│   ├── batch_ref_5_budget_100_2025039_21.err
│   ├── batch_ref_5_budget_100_2025039_21.out
│   ├── batch_ref_5_budget_100_2025039_22.err
│   ├── batch_ref_5_budget_100_2025039_22.out
│   ├── batch_ref_5_budget_100_2025039_23.err
│   ├── batch_ref_5_budget_100_2025039_23.out
│   ├── batch_ref_5_budget_100_2025039_24.err
│   ├── batch_ref_5_budget_100_2025039_24.out
│   ├── batch_ref_5_budget_100_2025039_25.err
│   ├── batch_ref_5_budget_100_2025039_25.out
│   ├── batch_ref_5_budget_100_2025039_26.err
│   ├── batch_ref_5_budget_100_2025039_26.out
│   ├── batch_ref_5_budget_100_2025039_27.err
│   ├── batch_ref_5_budget_100_2025039_27.out
│   ├── batch_ref_5_budget_100_2025039_28.err
│   ├── batch_ref_5_budget_100_2025039_28.out
│   ├── batch_ref_5_budget_100_2025039_29.err
│   ├── batch_ref_5_budget_100_2025039_29.out
│   ├── batch_ref_5_budget_100_2025039_3.err
│   ├── batch_ref_5_budget_100_2025039_3.out
│   ├── batch_ref_5_budget_100_2025039_30.err
│   ├── batch_ref_5_budget_100_2025039_30.out
│   ├── batch_ref_5_budget_100_2025039_31.err
│   ├── batch_ref_5_budget_100_2025039_31.out
│   ├── batch_ref_5_budget_100_2025039_32.err
│   ├── batch_ref_5_budget_100_2025039_32.out
│   ├── batch_ref_5_budget_100_2025039_33.err
│   ├── batch_ref_5_budget_100_2025039_33.out
│   ├── batch_ref_5_budget_100_2025039_34.err
│   ├── batch_ref_5_budget_100_2025039_34.out
│   ├── batch_ref_5_budget_100_2025039_35.err
│   ├── batch_ref_5_budget_100_2025039_35.out
│   ├── batch_ref_5_budget_100_2025039_36.err
│   ├── batch_ref_5_budget_100_2025039_36.out
│   ├── batch_ref_5_budget_100_2025039_37.err
│   ├── batch_ref_5_budget_100_2025039_37.out
│   ├── batch_ref_5_budget_100_2025039_38.err
│   ├── batch_ref_5_budget_100_2025039_38.out
│   ├── batch_ref_5_budget_100_2025039_39.err
│   ├── batch_ref_5_budget_100_2025039_39.out
│   ├── batch_ref_5_budget_100_2025039_4.err
│   ├── batch_ref_5_budget_100_2025039_4.out
│   ├── batch_ref_5_budget_100_2025039_40.err
│   ├── batch_ref_5_budget_100_2025039_40.out
│   ├── batch_ref_5_budget_100_2025039_41.err
│   ├── batch_ref_5_budget_100_2025039_41.out
│   ├── batch_ref_5_budget_100_2025039_42.err
│   ├── batch_ref_5_budget_100_2025039_42.out
│   ├── batch_ref_5_budget_100_2025039_43.err
│   ├── batch_ref_5_budget_100_2025039_43.out
│   ├── batch_ref_5_budget_100_2025039_44.err
│   ├── batch_ref_5_budget_100_2025039_44.out
│   ├── batch_ref_5_budget_100_2025039_45.err
│   ├── batch_ref_5_budget_100_2025039_45.out
│   ├── batch_ref_5_budget_100_2025039_46.err
│   ├── batch_ref_5_budget_100_2025039_46.out
│   ├── batch_ref_5_budget_100_2025039_47.err
│   ├── batch_ref_5_budget_100_2025039_47.out
│   ├── batch_ref_5_budget_100_2025039_48.err
│   ├── batch_ref_5_budget_100_2025039_48.out
│   ├── batch_ref_5_budget_100_2025039_49.err
│   ├── batch_ref_5_budget_100_2025039_49.out
│   ├── batch_ref_5_budget_100_2025039_5.err
│   ├── batch_ref_5_budget_100_2025039_5.out
│   ├── batch_ref_5_budget_100_2025039_50.err
│   ├── batch_ref_5_budget_100_2025039_50.out
│   ├── batch_ref_5_budget_100_2025039_51.err
│   ├── batch_ref_5_budget_100_2025039_51.out
│   ├── batch_ref_5_budget_100_2025039_52.err
│   ├── batch_ref_5_budget_100_2025039_52.out
│   ├── batch_ref_5_budget_100_2025039_53.err
│   ├── batch_ref_5_budget_100_2025039_53.out
│   ├── batch_ref_5_budget_100_2025039_54.err
│   ├── batch_ref_5_budget_100_2025039_54.out
│   ├── batch_ref_5_budget_100_2025039_55.err
│   ├── batch_ref_5_budget_100_2025039_55.out
│   ├── batch_ref_5_budget_100_2025039_56.err
│   ├── batch_ref_5_budget_100_2025039_56.out
│   ├── batch_ref_5_budget_100_2025039_57.err
│   ├── batch_ref_5_budget_100_2025039_57.out
│   ├── batch_ref_5_budget_100_2025039_58.err
│   ├── batch_ref_5_budget_100_2025039_58.out
│   ├── batch_ref_5_budget_100_2025039_59.err
│   ├── batch_ref_5_budget_100_2025039_59.out
│   ├── batch_ref_5_budget_100_2025039_6.err
│   ├── batch_ref_5_budget_100_2025039_6.out
│   ├── batch_ref_5_budget_100_2025039_60.err
│   ├── batch_ref_5_budget_100_2025039_60.out
│   ├── batch_ref_5_budget_100_2025039_61.err
│   ├── batch_ref_5_budget_100_2025039_61.out
│   ├── batch_ref_5_budget_100_2025039_62.err
│   ├── batch_ref_5_budget_100_2025039_62.out
│   ├── batch_ref_5_budget_100_2025039_63.err
│   ├── batch_ref_5_budget_100_2025039_63.out
│   ├── batch_ref_5_budget_100_2025039_64.err
│   ├── batch_ref_5_budget_100_2025039_64.out
│   ├── batch_ref_5_budget_100_2025039_65.err
│   ├── batch_ref_5_budget_100_2025039_65.out
│   ├── batch_ref_5_budget_100_2025039_66.err
│   ├── batch_ref_5_budget_100_2025039_66.out
│   ├── batch_ref_5_budget_100_2025039_67.err
│   ├── batch_ref_5_budget_100_2025039_67.out
│   ├── batch_ref_5_budget_100_2025039_68.err
│   ├── batch_ref_5_budget_100_2025039_68.out
│   ├── batch_ref_5_budget_100_2025039_69.err
│   ├── batch_ref_5_budget_100_2025039_69.out
│   ├── batch_ref_5_budget_100_2025039_7.err
│   ├── batch_ref_5_budget_100_2025039_7.out
│   ├── batch_ref_5_budget_100_2025039_70.err
│   ├── batch_ref_5_budget_100_2025039_70.out
│   ├── batch_ref_5_budget_100_2025039_71.err
│   ├── batch_ref_5_budget_100_2025039_71.out
│   ├── batch_ref_5_budget_100_2025039_72.err
│   ├── batch_ref_5_budget_100_2025039_72.out
│   ├── batch_ref_5_budget_100_2025039_73.err
│   ├── batch_ref_5_budget_100_2025039_73.out
│   ├── batch_ref_5_budget_100_2025039_74.err
│   ├── batch_ref_5_budget_100_2025039_74.out
│   ├── batch_ref_5_budget_100_2025039_75.err
│   ├── batch_ref_5_budget_100_2025039_75.out
│   ├── batch_ref_5_budget_100_2025039_76.err
│   ├── batch_ref_5_budget_100_2025039_76.out
│   ├── batch_ref_5_budget_100_2025039_77.err
│   ├── batch_ref_5_budget_100_2025039_77.out
│   ├── batch_ref_5_budget_100_2025039_78.err
│   ├── batch_ref_5_budget_100_2025039_78.out
│   ├── batch_ref_5_budget_100_2025039_79.err
│   ├── batch_ref_5_budget_100_2025039_79.out
│   ├── batch_ref_5_budget_100_2025039_8.err
│   ├── batch_ref_5_budget_100_2025039_8.out
│   ├── batch_ref_5_budget_100_2025039_80.err
│   ├── batch_ref_5_budget_100_2025039_80.out
│   ├── batch_ref_5_budget_100_2025039_81.err
│   ├── batch_ref_5_budget_100_2025039_81.out
│   ├── batch_ref_5_budget_100_2025039_9.err
│   ├── batch_ref_5_budget_100_2025039_9.out
│   ├── batch_ref_5_budget_100_2040026_1.err
│   ├── batch_ref_5_budget_100_2040026_1.out
│   ├── batch_ref_5_budget_100_2040026_10.err
│   ├── batch_ref_5_budget_100_2040026_10.out
│   ├── batch_ref_5_budget_100_2040026_11.err
│   ├── batch_ref_5_budget_100_2040026_11.out
│   ├── batch_ref_5_budget_100_2040026_12.err
│   ├── batch_ref_5_budget_100_2040026_12.out
│   ├── batch_ref_5_budget_100_2040026_13.err
│   ├── batch_ref_5_budget_100_2040026_13.out
│   ├── batch_ref_5_budget_100_2040026_14.err
│   ├── batch_ref_5_budget_100_2040026_14.out
│   ├── batch_ref_5_budget_100_2040026_15.err
│   ├── batch_ref_5_budget_100_2040026_15.out
│   ├── batch_ref_5_budget_100_2040026_16.err
│   ├── batch_ref_5_budget_100_2040026_16.out
│   ├── batch_ref_5_budget_100_2040026_17.err
│   ├── batch_ref_5_budget_100_2040026_17.out
│   ├── batch_ref_5_budget_100_2040026_18.err
│   ├── batch_ref_5_budget_100_2040026_18.out
│   ├── batch_ref_5_budget_100_2040026_19.err
│   ├── batch_ref_5_budget_100_2040026_19.out
│   ├── batch_ref_5_budget_100_2040026_2.err
│   ├── batch_ref_5_budget_100_2040026_2.out
│   ├── batch_ref_5_budget_100_2040026_20.err
│   ├── batch_ref_5_budget_100_2040026_20.out
│   ├── batch_ref_5_budget_100_2040026_21.err
│   ├── batch_ref_5_budget_100_2040026_21.out
│   ├── batch_ref_5_budget_100_2040026_22.err
│   ├── batch_ref_5_budget_100_2040026_22.out
│   ├── batch_ref_5_budget_100_2040026_23.err
│   ├── batch_ref_5_budget_100_2040026_23.out
│   ├── batch_ref_5_budget_100_2040026_24.err
│   ├── batch_ref_5_budget_100_2040026_24.out
│   ├── batch_ref_5_budget_100_2040026_25.err
│   ├── batch_ref_5_budget_100_2040026_25.out
│   ├── batch_ref_5_budget_100_2040026_26.err
│   ├── batch_ref_5_budget_100_2040026_26.out
│   ├── batch_ref_5_budget_100_2040026_27.err
│   ├── batch_ref_5_budget_100_2040026_27.out
│   ├── batch_ref_5_budget_100_2040026_28.err
│   ├── batch_ref_5_budget_100_2040026_28.out
│   ├── batch_ref_5_budget_100_2040026_29.err
│   ├── batch_ref_5_budget_100_2040026_29.out
│   ├── batch_ref_5_budget_100_2040026_3.err
│   ├── batch_ref_5_budget_100_2040026_3.out
│   ├── batch_ref_5_budget_100_2040026_30.err
│   ├── batch_ref_5_budget_100_2040026_30.out
│   ├── batch_ref_5_budget_100_2040026_31.err
│   ├── batch_ref_5_budget_100_2040026_31.out
│   ├── batch_ref_5_budget_100_2040026_32.err
│   ├── batch_ref_5_budget_100_2040026_32.out
│   ├── batch_ref_5_budget_100_2040026_33.err
│   ├── batch_ref_5_budget_100_2040026_33.out
│   ├── batch_ref_5_budget_100_2040026_34.err
│   ├── batch_ref_5_budget_100_2040026_34.out
│   ├── batch_ref_5_budget_100_2040026_35.err
│   ├── batch_ref_5_budget_100_2040026_35.out
│   ├── batch_ref_5_budget_100_2040026_36.err
│   ├── batch_ref_5_budget_100_2040026_36.out
│   ├── batch_ref_5_budget_100_2040026_37.err
│   ├── batch_ref_5_budget_100_2040026_37.out
│   ├── batch_ref_5_budget_100_2040026_38.err
│   ├── batch_ref_5_budget_100_2040026_38.out
│   ├── batch_ref_5_budget_100_2040026_39.err
│   ├── batch_ref_5_budget_100_2040026_39.out
│   ├── batch_ref_5_budget_100_2040026_4.err
│   ├── batch_ref_5_budget_100_2040026_4.out
│   ├── batch_ref_5_budget_100_2040026_40.err
│   ├── batch_ref_5_budget_100_2040026_40.out
│   ├── batch_ref_5_budget_100_2040026_41.err
│   ├── batch_ref_5_budget_100_2040026_41.out
│   ├── batch_ref_5_budget_100_2040026_42.err
│   ├── batch_ref_5_budget_100_2040026_42.out
│   ├── batch_ref_5_budget_100_2040026_43.err
│   ├── batch_ref_5_budget_100_2040026_43.out
│   ├── batch_ref_5_budget_100_2040026_44.err
│   ├── batch_ref_5_budget_100_2040026_44.out
│   ├── batch_ref_5_budget_100_2040026_45.err
│   ├── batch_ref_5_budget_100_2040026_45.out
│   ├── batch_ref_5_budget_100_2040026_46.err
│   ├── batch_ref_5_budget_100_2040026_46.out
│   ├── batch_ref_5_budget_100_2040026_47.err
│   ├── batch_ref_5_budget_100_2040026_47.out
│   ├── batch_ref_5_budget_100_2040026_48.err
│   ├── batch_ref_5_budget_100_2040026_48.out
│   ├── batch_ref_5_budget_100_2040026_49.err
│   ├── batch_ref_5_budget_100_2040026_49.out
│   ├── batch_ref_5_budget_100_2040026_5.err
│   ├── batch_ref_5_budget_100_2040026_5.out
│   ├── batch_ref_5_budget_100_2040026_50.err
│   ├── batch_ref_5_budget_100_2040026_50.out
│   ├── batch_ref_5_budget_100_2040026_51.err
│   ├── batch_ref_5_budget_100_2040026_51.out
│   ├── batch_ref_5_budget_100_2040026_52.err
│   ├── batch_ref_5_budget_100_2040026_52.out
│   ├── batch_ref_5_budget_100_2040026_53.err
│   ├── batch_ref_5_budget_100_2040026_53.out
│   ├── batch_ref_5_budget_100_2040026_54.err
│   ├── batch_ref_5_budget_100_2040026_54.out
│   ├── batch_ref_5_budget_100_2040026_55.err
│   ├── batch_ref_5_budget_100_2040026_55.out
│   ├── batch_ref_5_budget_100_2040026_56.err
│   ├── batch_ref_5_budget_100_2040026_56.out
│   ├── batch_ref_5_budget_100_2040026_57.err
│   ├── batch_ref_5_budget_100_2040026_57.out
│   ├── batch_ref_5_budget_100_2040026_58.err
│   ├── batch_ref_5_budget_100_2040026_58.out
│   ├── batch_ref_5_budget_100_2040026_59.err
│   ├── batch_ref_5_budget_100_2040026_59.out
│   ├── batch_ref_5_budget_100_2040026_6.err
│   ├── batch_ref_5_budget_100_2040026_6.out
│   ├── batch_ref_5_budget_100_2040026_60.err
│   ├── batch_ref_5_budget_100_2040026_60.out
│   ├── batch_ref_5_budget_100_2040026_61.err
│   ├── batch_ref_5_budget_100_2040026_61.out
│   ├── batch_ref_5_budget_100_2040026_62.err
│   ├── batch_ref_5_budget_100_2040026_62.out
│   ├── batch_ref_5_budget_100_2040026_63.err
│   ├── batch_ref_5_budget_100_2040026_63.out
│   ├── batch_ref_5_budget_100_2040026_64.err
│   ├── batch_ref_5_budget_100_2040026_64.out
│   ├── batch_ref_5_budget_100_2040026_65.err
│   ├── batch_ref_5_budget_100_2040026_65.out
│   ├── batch_ref_5_budget_100_2040026_66.err
│   ├── batch_ref_5_budget_100_2040026_66.out
│   ├── batch_ref_5_budget_100_2040026_67.err
│   ├── batch_ref_5_budget_100_2040026_67.out
│   ├── batch_ref_5_budget_100_2040026_68.err
│   ├── batch_ref_5_budget_100_2040026_68.out
│   ├── batch_ref_5_budget_100_2040026_69.err
│   ├── batch_ref_5_budget_100_2040026_69.out
│   ├── batch_ref_5_budget_100_2040026_7.err
│   ├── batch_ref_5_budget_100_2040026_7.out
│   ├── batch_ref_5_budget_100_2040026_70.err
│   ├── batch_ref_5_budget_100_2040026_70.out
│   ├── batch_ref_5_budget_100_2040026_71.err
│   ├── batch_ref_5_budget_100_2040026_71.out
│   ├── batch_ref_5_budget_100_2040026_72.err
│   ├── batch_ref_5_budget_100_2040026_72.out
│   ├── batch_ref_5_budget_100_2040026_73.err
│   ├── batch_ref_5_budget_100_2040026_73.out
│   ├── batch_ref_5_budget_100_2040026_74.err
│   ├── batch_ref_5_budget_100_2040026_74.out
│   ├── batch_ref_5_budget_100_2040026_75.err
│   ├── batch_ref_5_budget_100_2040026_75.out
│   ├── batch_ref_5_budget_100_2040026_76.err
│   ├── batch_ref_5_budget_100_2040026_76.out
│   ├── batch_ref_5_budget_100_2040026_77.err
│   ├── batch_ref_5_budget_100_2040026_77.out
│   ├── batch_ref_5_budget_100_2040026_78.err
│   ├── batch_ref_5_budget_100_2040026_78.out
│   ├── batch_ref_5_budget_100_2040026_79.err
│   ├── batch_ref_5_budget_100_2040026_79.out
│   ├── batch_ref_5_budget_100_2040026_8.err
│   ├── batch_ref_5_budget_100_2040026_8.out
│   ├── batch_ref_5_budget_100_2040026_80.err
│   ├── batch_ref_5_budget_100_2040026_80.out
│   ├── batch_ref_5_budget_100_2040026_81.err
│   ├── batch_ref_5_budget_100_2040026_81.out
│   ├── batch_ref_5_budget_100_2040026_9.err
│   ├── batch_ref_5_budget_100_2040026_9.out
│   ├── batch_ref_5_budget_100_max_5_2067311_1.err
│   ├── batch_ref_5_budget_100_max_5_2067311_1.out
│   ├── batch_ref_5_budget_100_max_5_2067311_10.err
│   ├── batch_ref_5_budget_100_max_5_2067311_10.out
│   ├── batch_ref_5_budget_100_max_5_2067311_11.err
│   ├── batch_ref_5_budget_100_max_5_2067311_11.out
│   ├── batch_ref_5_budget_100_max_5_2067311_12.err
│   ├── batch_ref_5_budget_100_max_5_2067311_12.out
│   ├── batch_ref_5_budget_100_max_5_2067311_13.err
│   ├── batch_ref_5_budget_100_max_5_2067311_13.out
│   ├── batch_ref_5_budget_100_max_5_2067311_14.err
│   ├── batch_ref_5_budget_100_max_5_2067311_14.out
│   ├── batch_ref_5_budget_100_max_5_2067311_15.err
│   ├── batch_ref_5_budget_100_max_5_2067311_15.out
│   ├── batch_ref_5_budget_100_max_5_2067311_16.err
│   ├── batch_ref_5_budget_100_max_5_2067311_16.out
│   ├── batch_ref_5_budget_100_max_5_2067311_17.err
│   ├── batch_ref_5_budget_100_max_5_2067311_17.out
│   ├── batch_ref_5_budget_100_max_5_2067311_18.err
│   ├── batch_ref_5_budget_100_max_5_2067311_18.out
│   ├── batch_ref_5_budget_100_max_5_2067311_19.err
│   ├── batch_ref_5_budget_100_max_5_2067311_19.out
│   ├── batch_ref_5_budget_100_max_5_2067311_2.err
│   ├── batch_ref_5_budget_100_max_5_2067311_2.out
│   ├── batch_ref_5_budget_100_max_5_2067311_20.err
│   ├── batch_ref_5_budget_100_max_5_2067311_20.out
│   ├── batch_ref_5_budget_100_max_5_2067311_21.err
│   ├── batch_ref_5_budget_100_max_5_2067311_21.out
│   ├── batch_ref_5_budget_100_max_5_2067311_22.err
│   ├── batch_ref_5_budget_100_max_5_2067311_22.out
│   ├── batch_ref_5_budget_100_max_5_2067311_23.err
│   ├── batch_ref_5_budget_100_max_5_2067311_23.out
│   ├── batch_ref_5_budget_100_max_5_2067311_24.err
│   ├── batch_ref_5_budget_100_max_5_2067311_24.out
│   ├── batch_ref_5_budget_100_max_5_2067311_25.err
│   ├── batch_ref_5_budget_100_max_5_2067311_25.out
│   ├── batch_ref_5_budget_100_max_5_2067311_26.err
│   ├── batch_ref_5_budget_100_max_5_2067311_26.out
│   ├── batch_ref_5_budget_100_max_5_2067311_27.err
│   ├── batch_ref_5_budget_100_max_5_2067311_27.out
│   ├── batch_ref_5_budget_100_max_5_2067311_28.err
│   ├── batch_ref_5_budget_100_max_5_2067311_28.out
│   ├── batch_ref_5_budget_100_max_5_2067311_29.err
│   ├── batch_ref_5_budget_100_max_5_2067311_29.out
│   ├── batch_ref_5_budget_100_max_5_2067311_3.err
│   ├── batch_ref_5_budget_100_max_5_2067311_3.out
│   ├── batch_ref_5_budget_100_max_5_2067311_30.err
│   ├── batch_ref_5_budget_100_max_5_2067311_30.out
│   ├── batch_ref_5_budget_100_max_5_2067311_31.err
│   ├── batch_ref_5_budget_100_max_5_2067311_31.out
│   ├── batch_ref_5_budget_100_max_5_2067311_32.err
│   ├── batch_ref_5_budget_100_max_5_2067311_32.out
│   ├── batch_ref_5_budget_100_max_5_2067311_33.err
│   ├── batch_ref_5_budget_100_max_5_2067311_33.out
│   ├── batch_ref_5_budget_100_max_5_2067311_34.err
│   ├── batch_ref_5_budget_100_max_5_2067311_34.out
│   ├── batch_ref_5_budget_100_max_5_2067311_35.err
│   ├── batch_ref_5_budget_100_max_5_2067311_35.out
│   ├── batch_ref_5_budget_100_max_5_2067311_36.err
│   ├── batch_ref_5_budget_100_max_5_2067311_36.out
│   ├── batch_ref_5_budget_100_max_5_2067311_37.err
│   ├── batch_ref_5_budget_100_max_5_2067311_37.out
│   ├── batch_ref_5_budget_100_max_5_2067311_38.err
│   ├── batch_ref_5_budget_100_max_5_2067311_38.out
│   ├── batch_ref_5_budget_100_max_5_2067311_39.err
│   ├── batch_ref_5_budget_100_max_5_2067311_39.out
│   ├── batch_ref_5_budget_100_max_5_2067311_4.err
│   ├── batch_ref_5_budget_100_max_5_2067311_4.out
│   ├── batch_ref_5_budget_100_max_5_2067311_40.err
│   ├── batch_ref_5_budget_100_max_5_2067311_40.out
│   ├── batch_ref_5_budget_100_max_5_2067311_41.err
│   ├── batch_ref_5_budget_100_max_5_2067311_41.out
│   ├── batch_ref_5_budget_100_max_5_2067311_42.err
│   ├── batch_ref_5_budget_100_max_5_2067311_42.out
│   ├── batch_ref_5_budget_100_max_5_2067311_43.err
│   ├── batch_ref_5_budget_100_max_5_2067311_43.out
│   ├── batch_ref_5_budget_100_max_5_2067311_44.err
│   ├── batch_ref_5_budget_100_max_5_2067311_44.out
│   ├── batch_ref_5_budget_100_max_5_2067311_45.err
│   ├── batch_ref_5_budget_100_max_5_2067311_45.out
│   ├── batch_ref_5_budget_100_max_5_2067311_46.err
│   ├── batch_ref_5_budget_100_max_5_2067311_46.out
│   ├── batch_ref_5_budget_100_max_5_2067311_47.err
│   ├── batch_ref_5_budget_100_max_5_2067311_47.out
│   ├── batch_ref_5_budget_100_max_5_2067311_48.err
│   ├── batch_ref_5_budget_100_max_5_2067311_48.out
│   ├── batch_ref_5_budget_100_max_5_2067311_49.err
│   ├── batch_ref_5_budget_100_max_5_2067311_49.out
│   ├── batch_ref_5_budget_100_max_5_2067311_5.err
│   ├── batch_ref_5_budget_100_max_5_2067311_5.out
│   ├── batch_ref_5_budget_100_max_5_2067311_50.err
│   ├── batch_ref_5_budget_100_max_5_2067311_50.out
│   ├── batch_ref_5_budget_100_max_5_2067311_51.err
│   ├── batch_ref_5_budget_100_max_5_2067311_51.out
│   ├── batch_ref_5_budget_100_max_5_2067311_52.err
│   ├── batch_ref_5_budget_100_max_5_2067311_52.out
│   ├── batch_ref_5_budget_100_max_5_2067311_53.err
│   ├── batch_ref_5_budget_100_max_5_2067311_53.out
│   ├── batch_ref_5_budget_100_max_5_2067311_54.err
│   ├── batch_ref_5_budget_100_max_5_2067311_54.out
│   ├── batch_ref_5_budget_100_max_5_2067311_55.err
│   ├── batch_ref_5_budget_100_max_5_2067311_55.out
│   ├── batch_ref_5_budget_100_max_5_2067311_56.err
│   ├── batch_ref_5_budget_100_max_5_2067311_56.out
│   ├── batch_ref_5_budget_100_max_5_2067311_57.err
│   ├── batch_ref_5_budget_100_max_5_2067311_57.out
│   ├── batch_ref_5_budget_100_max_5_2067311_58.err
│   ├── batch_ref_5_budget_100_max_5_2067311_58.out
│   ├── batch_ref_5_budget_100_max_5_2067311_59.err
│   ├── batch_ref_5_budget_100_max_5_2067311_59.out
│   ├── batch_ref_5_budget_100_max_5_2067311_6.err
│   ├── batch_ref_5_budget_100_max_5_2067311_6.out
│   ├── batch_ref_5_budget_100_max_5_2067311_60.err
│   ├── batch_ref_5_budget_100_max_5_2067311_60.out
│   ├── batch_ref_5_budget_100_max_5_2067311_61.err
│   ├── batch_ref_5_budget_100_max_5_2067311_61.out
│   ├── batch_ref_5_budget_100_max_5_2067311_62.err
│   ├── batch_ref_5_budget_100_max_5_2067311_62.out
│   ├── batch_ref_5_budget_100_max_5_2067311_63.err
│   ├── batch_ref_5_budget_100_max_5_2067311_63.out
│   ├── batch_ref_5_budget_100_max_5_2067311_64.err
│   ├── batch_ref_5_budget_100_max_5_2067311_64.out
│   ├── batch_ref_5_budget_100_max_5_2067311_65.err
│   ├── batch_ref_5_budget_100_max_5_2067311_65.out
│   ├── batch_ref_5_budget_100_max_5_2067311_66.err
│   ├── batch_ref_5_budget_100_max_5_2067311_66.out
│   ├── batch_ref_5_budget_100_max_5_2067311_67.err
│   ├── batch_ref_5_budget_100_max_5_2067311_67.out
│   ├── batch_ref_5_budget_100_max_5_2067311_68.err
│   ├── batch_ref_5_budget_100_max_5_2067311_68.out
│   ├── batch_ref_5_budget_100_max_5_2067311_69.err
│   ├── batch_ref_5_budget_100_max_5_2067311_69.out
│   ├── batch_ref_5_budget_100_max_5_2067311_7.err
│   ├── batch_ref_5_budget_100_max_5_2067311_7.out
│   ├── batch_ref_5_budget_100_max_5_2067311_70.err
│   ├── batch_ref_5_budget_100_max_5_2067311_70.out
│   ├── batch_ref_5_budget_100_max_5_2067311_71.err
│   ├── batch_ref_5_budget_100_max_5_2067311_71.out
│   ├── batch_ref_5_budget_100_max_5_2067311_72.err
│   ├── batch_ref_5_budget_100_max_5_2067311_72.out
│   ├── batch_ref_5_budget_100_max_5_2067311_73.err
│   ├── batch_ref_5_budget_100_max_5_2067311_73.out
│   ├── batch_ref_5_budget_100_max_5_2067311_74.err
│   ├── batch_ref_5_budget_100_max_5_2067311_74.out
│   ├── batch_ref_5_budget_100_max_5_2067311_75.err
│   ├── batch_ref_5_budget_100_max_5_2067311_75.out
│   ├── batch_ref_5_budget_100_max_5_2067311_76.err
│   ├── batch_ref_5_budget_100_max_5_2067311_76.out
│   ├── batch_ref_5_budget_100_max_5_2067311_77.err
│   ├── batch_ref_5_budget_100_max_5_2067311_77.out
│   ├── batch_ref_5_budget_100_max_5_2067311_78.err
│   ├── batch_ref_5_budget_100_max_5_2067311_78.out
│   ├── batch_ref_5_budget_100_max_5_2067311_79.err
│   ├── batch_ref_5_budget_100_max_5_2067311_79.out
│   ├── batch_ref_5_budget_100_max_5_2067311_8.err
│   ├── batch_ref_5_budget_100_max_5_2067311_8.out
│   ├── batch_ref_5_budget_100_max_5_2067311_80.err
│   ├── batch_ref_5_budget_100_max_5_2067311_80.out
│   ├── batch_ref_5_budget_100_max_5_2067311_81.err
│   ├── batch_ref_5_budget_100_max_5_2067311_81.out
│   ├── batch_ref_5_budget_100_max_5_2067311_9.err
│   ├── batch_ref_5_budget_100_max_5_2067311_9.out
│   ├── batch_ref_5_budget_110_2040027_1.err
│   ├── batch_ref_5_budget_110_2040027_1.out
│   ├── batch_ref_5_budget_110_2040027_10.err
│   ├── batch_ref_5_budget_110_2040027_10.out
│   ├── batch_ref_5_budget_110_2040027_11.err
│   ├── batch_ref_5_budget_110_2040027_11.out
│   ├── batch_ref_5_budget_110_2040027_12.err
│   ├── batch_ref_5_budget_110_2040027_12.out
│   ├── batch_ref_5_budget_110_2040027_13.err
│   ├── batch_ref_5_budget_110_2040027_13.out
│   ├── batch_ref_5_budget_110_2040027_14.err
│   ├── batch_ref_5_budget_110_2040027_14.out
│   ├── batch_ref_5_budget_110_2040027_15.err
│   ├── batch_ref_5_budget_110_2040027_15.out
│   ├── batch_ref_5_budget_110_2040027_16.err
│   ├── batch_ref_5_budget_110_2040027_16.out
│   ├── batch_ref_5_budget_110_2040027_17.err
│   ├── batch_ref_5_budget_110_2040027_17.out
│   ├── batch_ref_5_budget_110_2040027_18.err
│   ├── batch_ref_5_budget_110_2040027_18.out
│   ├── batch_ref_5_budget_110_2040027_19.err
│   ├── batch_ref_5_budget_110_2040027_19.out
│   ├── batch_ref_5_budget_110_2040027_2.err
│   ├── batch_ref_5_budget_110_2040027_2.out
│   ├── batch_ref_5_budget_110_2040027_20.err
│   ├── batch_ref_5_budget_110_2040027_20.out
│   ├── batch_ref_5_budget_110_2040027_21.err
│   ├── batch_ref_5_budget_110_2040027_21.out
│   ├── batch_ref_5_budget_110_2040027_22.err
│   ├── batch_ref_5_budget_110_2040027_22.out
│   ├── batch_ref_5_budget_110_2040027_23.err
│   ├── batch_ref_5_budget_110_2040027_23.out
│   ├── batch_ref_5_budget_110_2040027_24.err
│   ├── batch_ref_5_budget_110_2040027_24.out
│   ├── batch_ref_5_budget_110_2040027_25.err
│   ├── batch_ref_5_budget_110_2040027_25.out
│   ├── batch_ref_5_budget_110_2040027_26.err
│   ├── batch_ref_5_budget_110_2040027_26.out
│   ├── batch_ref_5_budget_110_2040027_27.err
│   ├── batch_ref_5_budget_110_2040027_27.out
│   ├── batch_ref_5_budget_110_2040027_28.err
│   ├── batch_ref_5_budget_110_2040027_28.out
│   ├── batch_ref_5_budget_110_2040027_29.err
│   ├── batch_ref_5_budget_110_2040027_29.out
│   ├── batch_ref_5_budget_110_2040027_3.err
│   ├── batch_ref_5_budget_110_2040027_3.out
│   ├── batch_ref_5_budget_110_2040027_30.err
│   ├── batch_ref_5_budget_110_2040027_30.out
│   ├── batch_ref_5_budget_110_2040027_31.err
│   ├── batch_ref_5_budget_110_2040027_31.out
│   ├── batch_ref_5_budget_110_2040027_32.err
│   ├── batch_ref_5_budget_110_2040027_32.out
│   ├── batch_ref_5_budget_110_2040027_33.err
│   ├── batch_ref_5_budget_110_2040027_33.out
│   ├── batch_ref_5_budget_110_2040027_34.err
│   ├── batch_ref_5_budget_110_2040027_34.out
│   ├── batch_ref_5_budget_110_2040027_35.err
│   ├── batch_ref_5_budget_110_2040027_35.out
│   ├── batch_ref_5_budget_110_2040027_36.err
│   ├── batch_ref_5_budget_110_2040027_36.out
│   ├── batch_ref_5_budget_110_2040027_37.err
│   ├── batch_ref_5_budget_110_2040027_37.out
│   ├── batch_ref_5_budget_110_2040027_38.err
│   ├── batch_ref_5_budget_110_2040027_38.out
│   ├── batch_ref_5_budget_110_2040027_39.err
│   ├── batch_ref_5_budget_110_2040027_39.out
│   ├── batch_ref_5_budget_110_2040027_4.err
│   ├── batch_ref_5_budget_110_2040027_4.out
│   ├── batch_ref_5_budget_110_2040027_40.err
│   ├── batch_ref_5_budget_110_2040027_40.out
│   ├── batch_ref_5_budget_110_2040027_41.err
│   ├── batch_ref_5_budget_110_2040027_41.out
│   ├── batch_ref_5_budget_110_2040027_42.err
│   ├── batch_ref_5_budget_110_2040027_42.out
│   ├── batch_ref_5_budget_110_2040027_43.err
│   ├── batch_ref_5_budget_110_2040027_43.out
│   ├── batch_ref_5_budget_110_2040027_44.err
│   ├── batch_ref_5_budget_110_2040027_44.out
│   ├── batch_ref_5_budget_110_2040027_45.err
│   ├── batch_ref_5_budget_110_2040027_45.out
│   ├── batch_ref_5_budget_110_2040027_46.err
│   ├── batch_ref_5_budget_110_2040027_46.out
│   ├── batch_ref_5_budget_110_2040027_47.err
│   ├── batch_ref_5_budget_110_2040027_47.out
│   ├── batch_ref_5_budget_110_2040027_48.err
│   ├── batch_ref_5_budget_110_2040027_48.out
│   ├── batch_ref_5_budget_110_2040027_49.err
│   ├── batch_ref_5_budget_110_2040027_49.out
│   ├── batch_ref_5_budget_110_2040027_5.err
│   ├── batch_ref_5_budget_110_2040027_5.out
│   ├── batch_ref_5_budget_110_2040027_50.err
│   ├── batch_ref_5_budget_110_2040027_50.out
│   ├── batch_ref_5_budget_110_2040027_51.err
│   ├── batch_ref_5_budget_110_2040027_51.out
│   ├── batch_ref_5_budget_110_2040027_52.err
│   ├── batch_ref_5_budget_110_2040027_52.out
│   ├── batch_ref_5_budget_110_2040027_53.err
│   ├── batch_ref_5_budget_110_2040027_53.out
│   ├── batch_ref_5_budget_110_2040027_54.err
│   ├── batch_ref_5_budget_110_2040027_54.out
│   ├── batch_ref_5_budget_110_2040027_55.err
│   ├── batch_ref_5_budget_110_2040027_55.out
│   ├── batch_ref_5_budget_110_2040027_56.err
│   ├── batch_ref_5_budget_110_2040027_56.out
│   ├── batch_ref_5_budget_110_2040027_57.err
│   ├── batch_ref_5_budget_110_2040027_57.out
│   ├── batch_ref_5_budget_110_2040027_58.err
│   ├── batch_ref_5_budget_110_2040027_58.out
│   ├── batch_ref_5_budget_110_2040027_59.err
│   ├── batch_ref_5_budget_110_2040027_59.out
│   ├── batch_ref_5_budget_110_2040027_6.err
│   ├── batch_ref_5_budget_110_2040027_6.out
│   ├── batch_ref_5_budget_110_2040027_60.err
│   ├── batch_ref_5_budget_110_2040027_60.out
│   ├── batch_ref_5_budget_110_2040027_61.err
│   ├── batch_ref_5_budget_110_2040027_61.out
│   ├── batch_ref_5_budget_110_2040027_62.err
│   ├── batch_ref_5_budget_110_2040027_62.out
│   ├── batch_ref_5_budget_110_2040027_63.err
│   ├── batch_ref_5_budget_110_2040027_63.out
│   ├── batch_ref_5_budget_110_2040027_64.err
│   ├── batch_ref_5_budget_110_2040027_64.out
│   ├── batch_ref_5_budget_110_2040027_65.err
│   ├── batch_ref_5_budget_110_2040027_65.out
│   ├── batch_ref_5_budget_110_2040027_66.err
│   ├── batch_ref_5_budget_110_2040027_66.out
│   ├── batch_ref_5_budget_110_2040027_67.err
│   ├── batch_ref_5_budget_110_2040027_67.out
│   ├── batch_ref_5_budget_110_2040027_68.err
│   ├── batch_ref_5_budget_110_2040027_68.out
│   ├── batch_ref_5_budget_110_2040027_69.err
│   ├── batch_ref_5_budget_110_2040027_69.out
│   ├── batch_ref_5_budget_110_2040027_7.err
│   ├── batch_ref_5_budget_110_2040027_7.out
│   ├── batch_ref_5_budget_110_2040027_70.err
│   ├── batch_ref_5_budget_110_2040027_70.out
│   ├── batch_ref_5_budget_110_2040027_71.err
│   ├── batch_ref_5_budget_110_2040027_71.out
│   ├── batch_ref_5_budget_110_2040027_72.err
│   ├── batch_ref_5_budget_110_2040027_72.out
│   ├── batch_ref_5_budget_110_2040027_73.err
│   ├── batch_ref_5_budget_110_2040027_73.out
│   ├── batch_ref_5_budget_110_2040027_74.err
│   ├── batch_ref_5_budget_110_2040027_74.out
│   ├── batch_ref_5_budget_110_2040027_75.err
│   ├── batch_ref_5_budget_110_2040027_75.out
│   ├── batch_ref_5_budget_110_2040027_76.err
│   ├── batch_ref_5_budget_110_2040027_76.out
│   ├── batch_ref_5_budget_110_2040027_77.err
│   ├── batch_ref_5_budget_110_2040027_77.out
│   ├── batch_ref_5_budget_110_2040027_78.err
│   ├── batch_ref_5_budget_110_2040027_78.out
│   ├── batch_ref_5_budget_110_2040027_79.err
│   ├── batch_ref_5_budget_110_2040027_79.out
│   ├── batch_ref_5_budget_110_2040027_8.err
│   ├── batch_ref_5_budget_110_2040027_8.out
│   ├── batch_ref_5_budget_110_2040027_80.err
│   ├── batch_ref_5_budget_110_2040027_80.out
│   ├── batch_ref_5_budget_110_2040027_81.err
│   ├── batch_ref_5_budget_110_2040027_81.out
│   ├── batch_ref_5_budget_110_2040027_9.err
│   ├── batch_ref_5_budget_110_2040027_9.out
│   ├── batch_ref_5_budget_120_2040028_1.err
│   ├── batch_ref_5_budget_120_2040028_1.out
│   ├── batch_ref_5_budget_120_2040028_10.err
│   ├── batch_ref_5_budget_120_2040028_10.out
│   ├── batch_ref_5_budget_120_2040028_11.err
│   ├── batch_ref_5_budget_120_2040028_11.out
│   ├── batch_ref_5_budget_120_2040028_12.err
│   ├── batch_ref_5_budget_120_2040028_12.out
│   ├── batch_ref_5_budget_120_2040028_13.err
│   ├── batch_ref_5_budget_120_2040028_13.out
│   ├── batch_ref_5_budget_120_2040028_14.err
│   ├── batch_ref_5_budget_120_2040028_14.out
│   ├── batch_ref_5_budget_120_2040028_15.err
│   ├── batch_ref_5_budget_120_2040028_15.out
│   ├── batch_ref_5_budget_120_2040028_16.err
│   ├── batch_ref_5_budget_120_2040028_16.out
│   ├── batch_ref_5_budget_120_2040028_17.err
│   ├── batch_ref_5_budget_120_2040028_17.out
│   ├── batch_ref_5_budget_120_2040028_18.err
│   ├── batch_ref_5_budget_120_2040028_18.out
│   ├── batch_ref_5_budget_120_2040028_19.err
│   ├── batch_ref_5_budget_120_2040028_19.out
│   ├── batch_ref_5_budget_120_2040028_2.err
│   ├── batch_ref_5_budget_120_2040028_2.out
│   ├── batch_ref_5_budget_120_2040028_20.err
│   ├── batch_ref_5_budget_120_2040028_20.out
│   ├── batch_ref_5_budget_120_2040028_21.err
│   ├── batch_ref_5_budget_120_2040028_21.out
│   ├── batch_ref_5_budget_120_2040028_22.err
│   ├── batch_ref_5_budget_120_2040028_22.out
│   ├── batch_ref_5_budget_120_2040028_23.err
│   ├── batch_ref_5_budget_120_2040028_23.out
│   ├── batch_ref_5_budget_120_2040028_24.err
│   ├── batch_ref_5_budget_120_2040028_24.out
│   ├── batch_ref_5_budget_120_2040028_25.err
│   ├── batch_ref_5_budget_120_2040028_25.out
│   ├── batch_ref_5_budget_120_2040028_26.err
│   ├── batch_ref_5_budget_120_2040028_26.out
│   ├── batch_ref_5_budget_120_2040028_27.err
│   ├── batch_ref_5_budget_120_2040028_27.out
│   ├── batch_ref_5_budget_120_2040028_28.err
│   ├── batch_ref_5_budget_120_2040028_28.out
│   ├── batch_ref_5_budget_120_2040028_29.err
│   ├── batch_ref_5_budget_120_2040028_29.out
│   ├── batch_ref_5_budget_120_2040028_3.err
│   ├── batch_ref_5_budget_120_2040028_3.out
│   ├── batch_ref_5_budget_120_2040028_30.err
│   ├── batch_ref_5_budget_120_2040028_30.out
│   ├── batch_ref_5_budget_120_2040028_31.err
│   ├── batch_ref_5_budget_120_2040028_31.out
│   ├── batch_ref_5_budget_120_2040028_32.err
│   ├── batch_ref_5_budget_120_2040028_32.out
│   ├── batch_ref_5_budget_120_2040028_33.err
│   ├── batch_ref_5_budget_120_2040028_33.out
│   ├── batch_ref_5_budget_120_2040028_34.err
│   ├── batch_ref_5_budget_120_2040028_34.out
│   ├── batch_ref_5_budget_120_2040028_35.err
│   ├── batch_ref_5_budget_120_2040028_35.out
│   ├── batch_ref_5_budget_120_2040028_36.err
│   ├── batch_ref_5_budget_120_2040028_36.out
│   ├── batch_ref_5_budget_120_2040028_37.err
│   ├── batch_ref_5_budget_120_2040028_37.out
│   ├── batch_ref_5_budget_120_2040028_38.err
│   ├── batch_ref_5_budget_120_2040028_38.out
│   ├── batch_ref_5_budget_120_2040028_39.err
│   ├── batch_ref_5_budget_120_2040028_39.out
│   ├── batch_ref_5_budget_120_2040028_4.err
│   ├── batch_ref_5_budget_120_2040028_4.out
│   ├── batch_ref_5_budget_120_2040028_40.err
│   ├── batch_ref_5_budget_120_2040028_40.out
│   ├── batch_ref_5_budget_120_2040028_41.err
│   ├── batch_ref_5_budget_120_2040028_41.out
│   ├── batch_ref_5_budget_120_2040028_42.err
│   ├── batch_ref_5_budget_120_2040028_42.out
│   ├── batch_ref_5_budget_120_2040028_43.err
│   ├── batch_ref_5_budget_120_2040028_43.out
│   ├── batch_ref_5_budget_120_2040028_44.err
│   ├── batch_ref_5_budget_120_2040028_44.out
│   ├── batch_ref_5_budget_120_2040028_45.err
│   ├── batch_ref_5_budget_120_2040028_45.out
│   ├── batch_ref_5_budget_120_2040028_46.err
│   ├── batch_ref_5_budget_120_2040028_46.out
│   ├── batch_ref_5_budget_120_2040028_47.err
│   ├── batch_ref_5_budget_120_2040028_47.out
│   ├── batch_ref_5_budget_120_2040028_48.err
│   ├── batch_ref_5_budget_120_2040028_48.out
│   ├── batch_ref_5_budget_120_2040028_49.err
│   ├── batch_ref_5_budget_120_2040028_49.out
│   ├── batch_ref_5_budget_120_2040028_5.err
│   ├── batch_ref_5_budget_120_2040028_5.out
│   ├── batch_ref_5_budget_120_2040028_50.err
│   ├── batch_ref_5_budget_120_2040028_50.out
│   ├── batch_ref_5_budget_120_2040028_51.err
│   ├── batch_ref_5_budget_120_2040028_51.out
│   ├── batch_ref_5_budget_120_2040028_52.err
│   ├── batch_ref_5_budget_120_2040028_52.out
│   ├── batch_ref_5_budget_120_2040028_53.err
│   ├── batch_ref_5_budget_120_2040028_53.out
│   ├── batch_ref_5_budget_120_2040028_54.err
│   ├── batch_ref_5_budget_120_2040028_54.out
│   ├── batch_ref_5_budget_120_2040028_55.err
│   ├── batch_ref_5_budget_120_2040028_55.out
│   ├── batch_ref_5_budget_120_2040028_56.err
│   ├── batch_ref_5_budget_120_2040028_56.out
│   ├── batch_ref_5_budget_120_2040028_57.err
│   ├── batch_ref_5_budget_120_2040028_57.out
│   ├── batch_ref_5_budget_120_2040028_58.err
│   ├── batch_ref_5_budget_120_2040028_58.out
│   ├── batch_ref_5_budget_120_2040028_59.err
│   ├── batch_ref_5_budget_120_2040028_59.out
│   ├── batch_ref_5_budget_120_2040028_6.err
│   ├── batch_ref_5_budget_120_2040028_6.out
│   ├── batch_ref_5_budget_120_2040028_60.err
│   ├── batch_ref_5_budget_120_2040028_60.out
│   ├── batch_ref_5_budget_120_2040028_61.err
│   ├── batch_ref_5_budget_120_2040028_61.out
│   ├── batch_ref_5_budget_120_2040028_62.err
│   ├── batch_ref_5_budget_120_2040028_62.out
│   ├── batch_ref_5_budget_120_2040028_63.err
│   ├── batch_ref_5_budget_120_2040028_63.out
│   ├── batch_ref_5_budget_120_2040028_64.err
│   ├── batch_ref_5_budget_120_2040028_64.out
│   ├── batch_ref_5_budget_120_2040028_65.err
│   ├── batch_ref_5_budget_120_2040028_65.out
│   ├── batch_ref_5_budget_120_2040028_66.err
│   ├── batch_ref_5_budget_120_2040028_66.out
│   ├── batch_ref_5_budget_120_2040028_67.err
│   ├── batch_ref_5_budget_120_2040028_67.out
│   ├── batch_ref_5_budget_120_2040028_68.err
│   ├── batch_ref_5_budget_120_2040028_68.out
│   ├── batch_ref_5_budget_120_2040028_69.err
│   ├── batch_ref_5_budget_120_2040028_69.out
│   ├── batch_ref_5_budget_120_2040028_7.err
│   ├── batch_ref_5_budget_120_2040028_7.out
│   ├── batch_ref_5_budget_120_2040028_70.err
│   ├── batch_ref_5_budget_120_2040028_70.out
│   ├── batch_ref_5_budget_120_2040028_71.err
│   ├── batch_ref_5_budget_120_2040028_71.out
│   ├── batch_ref_5_budget_120_2040028_72.err
│   ├── batch_ref_5_budget_120_2040028_72.out
│   ├── batch_ref_5_budget_120_2040028_73.err
│   ├── batch_ref_5_budget_120_2040028_73.out
│   ├── batch_ref_5_budget_120_2040028_74.err
│   ├── batch_ref_5_budget_120_2040028_74.out
│   ├── batch_ref_5_budget_120_2040028_75.err
│   ├── batch_ref_5_budget_120_2040028_75.out
│   ├── batch_ref_5_budget_120_2040028_76.err
│   ├── batch_ref_5_budget_120_2040028_76.out
│   ├── batch_ref_5_budget_120_2040028_77.err
│   ├── batch_ref_5_budget_120_2040028_77.out
│   ├── batch_ref_5_budget_120_2040028_78.err
│   ├── batch_ref_5_budget_120_2040028_78.out
│   ├── batch_ref_5_budget_120_2040028_79.err
│   ├── batch_ref_5_budget_120_2040028_79.out
│   ├── batch_ref_5_budget_120_2040028_8.err
│   ├── batch_ref_5_budget_120_2040028_8.out
│   ├── batch_ref_5_budget_120_2040028_80.err
│   ├── batch_ref_5_budget_120_2040028_80.out
│   ├── batch_ref_5_budget_120_2040028_81.err
│   ├── batch_ref_5_budget_120_2040028_81.out
│   ├── batch_ref_5_budget_120_2040028_9.err
│   ├── batch_ref_5_budget_120_2040028_9.out
│   ├── batch_ref_5_budget_130_2040029_1.err
│   ├── batch_ref_5_budget_130_2040029_1.out
│   ├── batch_ref_5_budget_130_2040029_10.err
│   ├── batch_ref_5_budget_130_2040029_10.out
│   ├── batch_ref_5_budget_130_2040029_11.err
│   ├── batch_ref_5_budget_130_2040029_11.out
│   ├── batch_ref_5_budget_130_2040029_12.err
│   ├── batch_ref_5_budget_130_2040029_12.out
│   ├── batch_ref_5_budget_130_2040029_13.err
│   ├── batch_ref_5_budget_130_2040029_13.out
│   ├── batch_ref_5_budget_130_2040029_14.err
│   ├── batch_ref_5_budget_130_2040029_14.out
│   ├── batch_ref_5_budget_130_2040029_15.err
│   ├── batch_ref_5_budget_130_2040029_15.out
│   ├── batch_ref_5_budget_130_2040029_16.err
│   ├── batch_ref_5_budget_130_2040029_16.out
│   ├── batch_ref_5_budget_130_2040029_17.err
│   ├── batch_ref_5_budget_130_2040029_17.out
│   ├── batch_ref_5_budget_130_2040029_18.err
│   ├── batch_ref_5_budget_130_2040029_18.out
│   ├── batch_ref_5_budget_130_2040029_19.err
│   ├── batch_ref_5_budget_130_2040029_19.out
│   ├── batch_ref_5_budget_130_2040029_2.err
│   ├── batch_ref_5_budget_130_2040029_2.out
│   ├── batch_ref_5_budget_130_2040029_20.err
│   ├── batch_ref_5_budget_130_2040029_20.out
│   ├── batch_ref_5_budget_130_2040029_21.err
│   ├── batch_ref_5_budget_130_2040029_21.out
│   ├── batch_ref_5_budget_130_2040029_22.err
│   ├── batch_ref_5_budget_130_2040029_22.out
│   ├── batch_ref_5_budget_130_2040029_23.err
│   ├── batch_ref_5_budget_130_2040029_23.out
│   ├── batch_ref_5_budget_130_2040029_24.err
│   ├── batch_ref_5_budget_130_2040029_24.out
│   ├── batch_ref_5_budget_130_2040029_25.err
│   ├── batch_ref_5_budget_130_2040029_25.out
│   ├── batch_ref_5_budget_130_2040029_26.err
│   ├── batch_ref_5_budget_130_2040029_26.out
│   ├── batch_ref_5_budget_130_2040029_27.err
│   ├── batch_ref_5_budget_130_2040029_27.out
│   ├── batch_ref_5_budget_130_2040029_28.err
│   ├── batch_ref_5_budget_130_2040029_28.out
│   ├── batch_ref_5_budget_130_2040029_29.err
│   ├── batch_ref_5_budget_130_2040029_29.out
│   ├── batch_ref_5_budget_130_2040029_3.err
│   ├── batch_ref_5_budget_130_2040029_3.out
│   ├── batch_ref_5_budget_130_2040029_30.err
│   ├── batch_ref_5_budget_130_2040029_30.out
│   ├── batch_ref_5_budget_130_2040029_31.err
│   ├── batch_ref_5_budget_130_2040029_31.out
│   ├── batch_ref_5_budget_130_2040029_32.err
│   ├── batch_ref_5_budget_130_2040029_32.out
│   ├── batch_ref_5_budget_130_2040029_33.err
│   ├── batch_ref_5_budget_130_2040029_33.out
│   ├── batch_ref_5_budget_130_2040029_34.err
│   ├── batch_ref_5_budget_130_2040029_34.out
│   ├── batch_ref_5_budget_130_2040029_35.err
│   ├── batch_ref_5_budget_130_2040029_35.out
│   ├── batch_ref_5_budget_130_2040029_36.err
│   ├── batch_ref_5_budget_130_2040029_36.out
│   ├── batch_ref_5_budget_130_2040029_37.err
│   ├── batch_ref_5_budget_130_2040029_37.out
│   ├── batch_ref_5_budget_130_2040029_38.err
│   ├── batch_ref_5_budget_130_2040029_38.out
│   ├── batch_ref_5_budget_130_2040029_39.err
│   ├── batch_ref_5_budget_130_2040029_39.out
│   ├── batch_ref_5_budget_130_2040029_4.err
│   ├── batch_ref_5_budget_130_2040029_4.out
│   ├── batch_ref_5_budget_130_2040029_40.err
│   ├── batch_ref_5_budget_130_2040029_40.out
│   ├── batch_ref_5_budget_130_2040029_41.err
│   ├── batch_ref_5_budget_130_2040029_41.out
│   ├── batch_ref_5_budget_130_2040029_42.err
│   ├── batch_ref_5_budget_130_2040029_42.out
│   ├── batch_ref_5_budget_130_2040029_43.err
│   ├── batch_ref_5_budget_130_2040029_43.out
│   ├── batch_ref_5_budget_130_2040029_44.err
│   ├── batch_ref_5_budget_130_2040029_44.out
│   ├── batch_ref_5_budget_130_2040029_45.err
│   ├── batch_ref_5_budget_130_2040029_45.out
│   ├── batch_ref_5_budget_130_2040029_46.err
│   ├── batch_ref_5_budget_130_2040029_46.out
│   ├── batch_ref_5_budget_130_2040029_47.err
│   ├── batch_ref_5_budget_130_2040029_47.out
│   ├── batch_ref_5_budget_130_2040029_48.err
│   ├── batch_ref_5_budget_130_2040029_48.out
│   ├── batch_ref_5_budget_130_2040029_49.err
│   ├── batch_ref_5_budget_130_2040029_49.out
│   ├── batch_ref_5_budget_130_2040029_5.err
│   ├── batch_ref_5_budget_130_2040029_5.out
│   ├── batch_ref_5_budget_130_2040029_50.err
│   ├── batch_ref_5_budget_130_2040029_50.out
│   ├── batch_ref_5_budget_130_2040029_51.err
│   ├── batch_ref_5_budget_130_2040029_51.out
│   ├── batch_ref_5_budget_130_2040029_52.err
│   ├── batch_ref_5_budget_130_2040029_52.out
│   ├── batch_ref_5_budget_130_2040029_53.err
│   ├── batch_ref_5_budget_130_2040029_53.out
│   ├── batch_ref_5_budget_130_2040029_54.err
│   ├── batch_ref_5_budget_130_2040029_54.out
│   ├── batch_ref_5_budget_130_2040029_55.err
│   ├── batch_ref_5_budget_130_2040029_55.out
│   ├── batch_ref_5_budget_130_2040029_56.err
│   ├── batch_ref_5_budget_130_2040029_56.out
│   ├── batch_ref_5_budget_130_2040029_57.err
│   ├── batch_ref_5_budget_130_2040029_57.out
│   ├── batch_ref_5_budget_130_2040029_58.err
│   ├── batch_ref_5_budget_130_2040029_58.out
│   ├── batch_ref_5_budget_130_2040029_59.err
│   ├── batch_ref_5_budget_130_2040029_59.out
│   ├── batch_ref_5_budget_130_2040029_6.err
│   ├── batch_ref_5_budget_130_2040029_6.out
│   ├── batch_ref_5_budget_130_2040029_60.err
│   ├── batch_ref_5_budget_130_2040029_60.out
│   ├── batch_ref_5_budget_130_2040029_61.err
│   ├── batch_ref_5_budget_130_2040029_61.out
│   ├── batch_ref_5_budget_130_2040029_62.err
│   ├── batch_ref_5_budget_130_2040029_62.out
│   ├── batch_ref_5_budget_130_2040029_63.err
│   ├── batch_ref_5_budget_130_2040029_63.out
│   ├── batch_ref_5_budget_130_2040029_64.err
│   ├── batch_ref_5_budget_130_2040029_64.out
│   ├── batch_ref_5_budget_130_2040029_65.err
│   ├── batch_ref_5_budget_130_2040029_65.out
│   ├── batch_ref_5_budget_130_2040029_66.err
│   ├── batch_ref_5_budget_130_2040029_66.out
│   ├── batch_ref_5_budget_130_2040029_67.err
│   ├── batch_ref_5_budget_130_2040029_67.out
│   ├── batch_ref_5_budget_130_2040029_68.err
│   ├── batch_ref_5_budget_130_2040029_68.out
│   ├── batch_ref_5_budget_130_2040029_69.err
│   ├── batch_ref_5_budget_130_2040029_69.out
│   ├── batch_ref_5_budget_130_2040029_7.err
│   ├── batch_ref_5_budget_130_2040029_7.out
│   ├── batch_ref_5_budget_130_2040029_70.err
│   ├── batch_ref_5_budget_130_2040029_70.out
│   ├── batch_ref_5_budget_130_2040029_71.err
│   ├── batch_ref_5_budget_130_2040029_71.out
│   ├── batch_ref_5_budget_130_2040029_72.err
│   ├── batch_ref_5_budget_130_2040029_72.out
│   ├── batch_ref_5_budget_130_2040029_73.err
│   ├── batch_ref_5_budget_130_2040029_73.out
│   ├── batch_ref_5_budget_130_2040029_74.err
│   ├── batch_ref_5_budget_130_2040029_74.out
│   ├── batch_ref_5_budget_130_2040029_75.err
│   ├── batch_ref_5_budget_130_2040029_75.out
│   ├── batch_ref_5_budget_130_2040029_76.err
│   ├── batch_ref_5_budget_130_2040029_76.out
│   ├── batch_ref_5_budget_130_2040029_77.err
│   ├── batch_ref_5_budget_130_2040029_77.out
│   ├── batch_ref_5_budget_130_2040029_78.err
│   ├── batch_ref_5_budget_130_2040029_78.out
│   ├── batch_ref_5_budget_130_2040029_79.err
│   ├── batch_ref_5_budget_130_2040029_79.out
│   ├── batch_ref_5_budget_130_2040029_8.err
│   ├── batch_ref_5_budget_130_2040029_8.out
│   ├── batch_ref_5_budget_130_2040029_80.err
│   ├── batch_ref_5_budget_130_2040029_80.out
│   ├── batch_ref_5_budget_130_2040029_81.err
│   ├── batch_ref_5_budget_130_2040029_81.out
│   ├── batch_ref_5_budget_130_2040029_9.err
│   ├── batch_ref_5_budget_130_2040029_9.out
│   ├── batch_ref_5_budget_140_2040030_1.err
│   ├── batch_ref_5_budget_140_2040030_1.out
│   ├── batch_ref_5_budget_140_2040030_10.err
│   ├── batch_ref_5_budget_140_2040030_10.out
│   ├── batch_ref_5_budget_140_2040030_11.err
│   ├── batch_ref_5_budget_140_2040030_11.out
│   ├── batch_ref_5_budget_140_2040030_12.err
│   ├── batch_ref_5_budget_140_2040030_12.out
│   ├── batch_ref_5_budget_140_2040030_13.err
│   ├── batch_ref_5_budget_140_2040030_13.out
│   ├── batch_ref_5_budget_140_2040030_14.err
│   ├── batch_ref_5_budget_140_2040030_14.out
│   ├── batch_ref_5_budget_140_2040030_15.err
│   ├── batch_ref_5_budget_140_2040030_15.out
│   ├── batch_ref_5_budget_140_2040030_16.err
│   ├── batch_ref_5_budget_140_2040030_16.out
│   ├── batch_ref_5_budget_140_2040030_17.err
│   ├── batch_ref_5_budget_140_2040030_17.out
│   ├── batch_ref_5_budget_140_2040030_18.err
│   ├── batch_ref_5_budget_140_2040030_18.out
│   ├── batch_ref_5_budget_140_2040030_19.err
│   ├── batch_ref_5_budget_140_2040030_19.out
│   ├── batch_ref_5_budget_140_2040030_2.err
│   ├── batch_ref_5_budget_140_2040030_2.out
│   ├── batch_ref_5_budget_140_2040030_20.err
│   ├── batch_ref_5_budget_140_2040030_20.out
│   ├── batch_ref_5_budget_140_2040030_21.err
│   ├── batch_ref_5_budget_140_2040030_21.out
│   ├── batch_ref_5_budget_140_2040030_22.err
│   ├── batch_ref_5_budget_140_2040030_22.out
│   ├── batch_ref_5_budget_140_2040030_23.err
│   ├── batch_ref_5_budget_140_2040030_23.out
│   ├── batch_ref_5_budget_140_2040030_24.err
│   ├── batch_ref_5_budget_140_2040030_24.out
│   ├── batch_ref_5_budget_140_2040030_25.err
│   ├── batch_ref_5_budget_140_2040030_25.out
│   ├── batch_ref_5_budget_140_2040030_26.err
│   ├── batch_ref_5_budget_140_2040030_26.out
│   ├── batch_ref_5_budget_140_2040030_27.err
│   ├── batch_ref_5_budget_140_2040030_27.out
│   ├── batch_ref_5_budget_140_2040030_28.err
│   ├── batch_ref_5_budget_140_2040030_28.out
│   ├── batch_ref_5_budget_140_2040030_29.err
│   ├── batch_ref_5_budget_140_2040030_29.out
│   ├── batch_ref_5_budget_140_2040030_3.err
│   ├── batch_ref_5_budget_140_2040030_3.out
│   ├── batch_ref_5_budget_140_2040030_30.err
│   ├── batch_ref_5_budget_140_2040030_30.out
│   ├── batch_ref_5_budget_140_2040030_31.err
│   ├── batch_ref_5_budget_140_2040030_31.out
│   ├── batch_ref_5_budget_140_2040030_32.err
│   ├── batch_ref_5_budget_140_2040030_32.out
│   ├── batch_ref_5_budget_140_2040030_33.err
│   ├── batch_ref_5_budget_140_2040030_33.out
│   ├── batch_ref_5_budget_140_2040030_34.err
│   ├── batch_ref_5_budget_140_2040030_34.out
│   ├── batch_ref_5_budget_140_2040030_35.err
│   ├── batch_ref_5_budget_140_2040030_35.out
│   ├── batch_ref_5_budget_140_2040030_36.err
│   ├── batch_ref_5_budget_140_2040030_36.out
│   ├── batch_ref_5_budget_140_2040030_37.err
│   ├── batch_ref_5_budget_140_2040030_37.out
│   ├── batch_ref_5_budget_140_2040030_38.err
│   ├── batch_ref_5_budget_140_2040030_38.out
│   ├── batch_ref_5_budget_140_2040030_39.err
│   ├── batch_ref_5_budget_140_2040030_39.out
│   ├── batch_ref_5_budget_140_2040030_4.err
│   ├── batch_ref_5_budget_140_2040030_4.out
│   ├── batch_ref_5_budget_140_2040030_40.err
│   ├── batch_ref_5_budget_140_2040030_40.out
│   ├── batch_ref_5_budget_140_2040030_41.err
│   ├── batch_ref_5_budget_140_2040030_41.out
│   ├── batch_ref_5_budget_140_2040030_42.err
│   ├── batch_ref_5_budget_140_2040030_42.out
│   ├── batch_ref_5_budget_140_2040030_43.err
│   ├── batch_ref_5_budget_140_2040030_43.out
│   ├── batch_ref_5_budget_140_2040030_44.err
│   ├── batch_ref_5_budget_140_2040030_44.out
│   ├── batch_ref_5_budget_140_2040030_45.err
│   ├── batch_ref_5_budget_140_2040030_45.out
│   ├── batch_ref_5_budget_140_2040030_46.err
│   ├── batch_ref_5_budget_140_2040030_46.out
│   ├── batch_ref_5_budget_140_2040030_47.err
│   ├── batch_ref_5_budget_140_2040030_47.out
│   ├── batch_ref_5_budget_140_2040030_48.err
│   ├── batch_ref_5_budget_140_2040030_48.out
│   ├── batch_ref_5_budget_140_2040030_49.err
│   ├── batch_ref_5_budget_140_2040030_49.out
│   ├── batch_ref_5_budget_140_2040030_5.err
│   ├── batch_ref_5_budget_140_2040030_5.out
│   ├── batch_ref_5_budget_140_2040030_50.err
│   ├── batch_ref_5_budget_140_2040030_50.out
│   ├── batch_ref_5_budget_140_2040030_51.err
│   ├── batch_ref_5_budget_140_2040030_51.out
│   ├── batch_ref_5_budget_140_2040030_52.err
│   ├── batch_ref_5_budget_140_2040030_52.out
│   ├── batch_ref_5_budget_140_2040030_53.err
│   ├── batch_ref_5_budget_140_2040030_53.out
│   ├── batch_ref_5_budget_140_2040030_54.err
│   ├── batch_ref_5_budget_140_2040030_54.out
│   ├── batch_ref_5_budget_140_2040030_55.err
│   ├── batch_ref_5_budget_140_2040030_55.out
│   ├── batch_ref_5_budget_140_2040030_56.err
│   ├── batch_ref_5_budget_140_2040030_56.out
│   ├── batch_ref_5_budget_140_2040030_57.err
│   ├── batch_ref_5_budget_140_2040030_57.out
│   ├── batch_ref_5_budget_140_2040030_58.err
│   ├── batch_ref_5_budget_140_2040030_58.out
│   ├── batch_ref_5_budget_140_2040030_59.err
│   ├── batch_ref_5_budget_140_2040030_59.out
│   ├── batch_ref_5_budget_140_2040030_6.err
│   ├── batch_ref_5_budget_140_2040030_6.out
│   ├── batch_ref_5_budget_140_2040030_60.err
│   ├── batch_ref_5_budget_140_2040030_60.out
│   ├── batch_ref_5_budget_140_2040030_61.err
│   ├── batch_ref_5_budget_140_2040030_61.out
│   ├── batch_ref_5_budget_140_2040030_62.err
│   ├── batch_ref_5_budget_140_2040030_62.out
│   ├── batch_ref_5_budget_140_2040030_63.err
│   ├── batch_ref_5_budget_140_2040030_63.out
│   ├── batch_ref_5_budget_140_2040030_64.err
│   ├── batch_ref_5_budget_140_2040030_64.out
│   ├── batch_ref_5_budget_140_2040030_65.err
│   ├── batch_ref_5_budget_140_2040030_65.out
│   ├── batch_ref_5_budget_140_2040030_66.err
│   ├── batch_ref_5_budget_140_2040030_66.out
│   ├── batch_ref_5_budget_140_2040030_67.err
│   ├── batch_ref_5_budget_140_2040030_67.out
│   ├── batch_ref_5_budget_140_2040030_68.err
│   ├── batch_ref_5_budget_140_2040030_68.out
│   ├── batch_ref_5_budget_140_2040030_69.err
│   ├── batch_ref_5_budget_140_2040030_69.out
│   ├── batch_ref_5_budget_140_2040030_7.err
│   ├── batch_ref_5_budget_140_2040030_7.out
│   ├── batch_ref_5_budget_140_2040030_70.err
│   ├── batch_ref_5_budget_140_2040030_70.out
│   ├── batch_ref_5_budget_140_2040030_71.err
│   ├── batch_ref_5_budget_140_2040030_71.out
│   ├── batch_ref_5_budget_140_2040030_72.err
│   ├── batch_ref_5_budget_140_2040030_72.out
│   ├── batch_ref_5_budget_140_2040030_73.err
│   ├── batch_ref_5_budget_140_2040030_73.out
│   ├── batch_ref_5_budget_140_2040030_74.err
│   ├── batch_ref_5_budget_140_2040030_74.out
│   ├── batch_ref_5_budget_140_2040030_75.err
│   ├── batch_ref_5_budget_140_2040030_75.out
│   ├── batch_ref_5_budget_140_2040030_76.err
│   ├── batch_ref_5_budget_140_2040030_76.out
│   ├── batch_ref_5_budget_140_2040030_77.err
│   ├── batch_ref_5_budget_140_2040030_77.out
│   ├── batch_ref_5_budget_140_2040030_78.err
│   ├── batch_ref_5_budget_140_2040030_78.out
│   ├── batch_ref_5_budget_140_2040030_79.err
│   ├── batch_ref_5_budget_140_2040030_79.out
│   ├── batch_ref_5_budget_140_2040030_8.err
│   ├── batch_ref_5_budget_140_2040030_8.out
│   ├── batch_ref_5_budget_140_2040030_80.err
│   ├── batch_ref_5_budget_140_2040030_80.out
│   ├── batch_ref_5_budget_140_2040030_81.err
│   ├── batch_ref_5_budget_140_2040030_81.out
│   ├── batch_ref_5_budget_140_2040030_9.err
│   ├── batch_ref_5_budget_140_2040030_9.out
│   ├── batch_ref_5_budget_150_1994126_1.err
│   ├── batch_ref_5_budget_150_1994126_1.out
│   ├── batch_ref_5_budget_150_1994126_10.err
│   ├── batch_ref_5_budget_150_1994126_10.out
│   ├── batch_ref_5_budget_150_1994126_11.err
│   ├── batch_ref_5_budget_150_1994126_11.out
│   ├── batch_ref_5_budget_150_1994126_12.err
│   ├── batch_ref_5_budget_150_1994126_12.out
│   ├── batch_ref_5_budget_150_1994126_13.err
│   ├── batch_ref_5_budget_150_1994126_13.out
│   ├── batch_ref_5_budget_150_1994126_14.err
│   ├── batch_ref_5_budget_150_1994126_14.out
│   ├── batch_ref_5_budget_150_1994126_15.err
│   ├── batch_ref_5_budget_150_1994126_15.out
│   ├── batch_ref_5_budget_150_1994126_16.err
│   ├── batch_ref_5_budget_150_1994126_16.out
│   ├── batch_ref_5_budget_150_1994126_17.err
│   ├── batch_ref_5_budget_150_1994126_17.out
│   ├── batch_ref_5_budget_150_1994126_18.err
│   ├── batch_ref_5_budget_150_1994126_18.out
│   ├── batch_ref_5_budget_150_1994126_19.err
│   ├── batch_ref_5_budget_150_1994126_19.out
│   ├── batch_ref_5_budget_150_1994126_2.err
│   ├── batch_ref_5_budget_150_1994126_2.out
│   ├── batch_ref_5_budget_150_1994126_20.err
│   ├── batch_ref_5_budget_150_1994126_20.out
│   ├── batch_ref_5_budget_150_1994126_21.err
│   ├── batch_ref_5_budget_150_1994126_21.out
│   ├── batch_ref_5_budget_150_1994126_22.err
│   ├── batch_ref_5_budget_150_1994126_22.out
│   ├── batch_ref_5_budget_150_1994126_23.err
│   ├── batch_ref_5_budget_150_1994126_23.out
│   ├── batch_ref_5_budget_150_1994126_24.err
│   ├── batch_ref_5_budget_150_1994126_24.out
│   ├── batch_ref_5_budget_150_1994126_25.err
│   ├── batch_ref_5_budget_150_1994126_25.out
│   ├── batch_ref_5_budget_150_1994126_26.err
│   ├── batch_ref_5_budget_150_1994126_26.out
│   ├── batch_ref_5_budget_150_1994126_27.err
│   ├── batch_ref_5_budget_150_1994126_27.out
│   ├── batch_ref_5_budget_150_1994126_28.err
│   ├── batch_ref_5_budget_150_1994126_28.out
│   ├── batch_ref_5_budget_150_1994126_29.err
│   ├── batch_ref_5_budget_150_1994126_29.out
│   ├── batch_ref_5_budget_150_1994126_3.err
│   ├── batch_ref_5_budget_150_1994126_3.out
│   ├── batch_ref_5_budget_150_1994126_30.err
│   ├── batch_ref_5_budget_150_1994126_30.out
│   ├── batch_ref_5_budget_150_1994126_31.err
│   ├── batch_ref_5_budget_150_1994126_31.out
│   ├── batch_ref_5_budget_150_1994126_32.err
│   ├── batch_ref_5_budget_150_1994126_32.out
│   ├── batch_ref_5_budget_150_1994126_33.err
│   ├── batch_ref_5_budget_150_1994126_33.out
│   ├── batch_ref_5_budget_150_1994126_34.err
│   ├── batch_ref_5_budget_150_1994126_34.out
│   ├── batch_ref_5_budget_150_1994126_35.err
│   ├── batch_ref_5_budget_150_1994126_35.out
│   ├── batch_ref_5_budget_150_1994126_36.err
│   ├── batch_ref_5_budget_150_1994126_36.out
│   ├── batch_ref_5_budget_150_1994126_37.err
│   ├── batch_ref_5_budget_150_1994126_37.out
│   ├── batch_ref_5_budget_150_1994126_38.err
│   ├── batch_ref_5_budget_150_1994126_38.out
│   ├── batch_ref_5_budget_150_1994126_39.err
│   ├── batch_ref_5_budget_150_1994126_39.out
│   ├── batch_ref_5_budget_150_1994126_4.err
│   ├── batch_ref_5_budget_150_1994126_4.out
│   ├── batch_ref_5_budget_150_1994126_40.err
│   ├── batch_ref_5_budget_150_1994126_40.out
│   ├── batch_ref_5_budget_150_1994126_41.err
│   ├── batch_ref_5_budget_150_1994126_41.out
│   ├── batch_ref_5_budget_150_1994126_42.err
│   ├── batch_ref_5_budget_150_1994126_42.out
│   ├── batch_ref_5_budget_150_1994126_43.err
│   ├── batch_ref_5_budget_150_1994126_43.out
│   ├── batch_ref_5_budget_150_1994126_44.err
│   ├── batch_ref_5_budget_150_1994126_44.out
│   ├── batch_ref_5_budget_150_1994126_45.err
│   ├── batch_ref_5_budget_150_1994126_45.out
│   ├── batch_ref_5_budget_150_1994126_46.err
│   ├── batch_ref_5_budget_150_1994126_46.out
│   ├── batch_ref_5_budget_150_1994126_47.err
│   ├── batch_ref_5_budget_150_1994126_47.out
│   ├── batch_ref_5_budget_150_1994126_48.err
│   ├── batch_ref_5_budget_150_1994126_48.out
│   ├── batch_ref_5_budget_150_1994126_49.err
│   ├── batch_ref_5_budget_150_1994126_49.out
│   ├── batch_ref_5_budget_150_1994126_5.err
│   ├── batch_ref_5_budget_150_1994126_5.out
│   ├── batch_ref_5_budget_150_1994126_50.err
│   ├── batch_ref_5_budget_150_1994126_50.out
│   ├── batch_ref_5_budget_150_1994126_51.err
│   ├── batch_ref_5_budget_150_1994126_51.out
│   ├── batch_ref_5_budget_150_1994126_52.err
│   ├── batch_ref_5_budget_150_1994126_52.out
│   ├── batch_ref_5_budget_150_1994126_53.err
│   ├── batch_ref_5_budget_150_1994126_53.out
│   ├── batch_ref_5_budget_150_1994126_54.err
│   ├── batch_ref_5_budget_150_1994126_54.out
│   ├── batch_ref_5_budget_150_1994126_55.err
│   ├── batch_ref_5_budget_150_1994126_55.out
│   ├── batch_ref_5_budget_150_1994126_56.err
│   ├── batch_ref_5_budget_150_1994126_56.out
│   ├── batch_ref_5_budget_150_1994126_57.err
│   ├── batch_ref_5_budget_150_1994126_57.out
│   ├── batch_ref_5_budget_150_1994126_58.err
│   ├── batch_ref_5_budget_150_1994126_58.out
│   ├── batch_ref_5_budget_150_1994126_59.err
│   ├── batch_ref_5_budget_150_1994126_59.out
│   ├── batch_ref_5_budget_150_1994126_6.err
│   ├── batch_ref_5_budget_150_1994126_6.out
│   ├── batch_ref_5_budget_150_1994126_60.err
│   ├── batch_ref_5_budget_150_1994126_60.out
│   ├── batch_ref_5_budget_150_1994126_61.err
│   ├── batch_ref_5_budget_150_1994126_61.out
│   ├── batch_ref_5_budget_150_1994126_62.err
│   ├── batch_ref_5_budget_150_1994126_62.out
│   ├── batch_ref_5_budget_150_1994126_63.err
│   ├── batch_ref_5_budget_150_1994126_63.out
│   ├── batch_ref_5_budget_150_1994126_64.err
│   ├── batch_ref_5_budget_150_1994126_64.out
│   ├── batch_ref_5_budget_150_1994126_65.err
│   ├── batch_ref_5_budget_150_1994126_65.out
│   ├── batch_ref_5_budget_150_1994126_66.err
│   ├── batch_ref_5_budget_150_1994126_66.out
│   ├── batch_ref_5_budget_150_1994126_67.err
│   ├── batch_ref_5_budget_150_1994126_67.out
│   ├── batch_ref_5_budget_150_1994126_68.err
│   ├── batch_ref_5_budget_150_1994126_68.out
│   ├── batch_ref_5_budget_150_1994126_69.err
│   ├── batch_ref_5_budget_150_1994126_69.out
│   ├── batch_ref_5_budget_150_1994126_7.err
│   ├── batch_ref_5_budget_150_1994126_7.out
│   ├── batch_ref_5_budget_150_1994126_70.err
│   ├── batch_ref_5_budget_150_1994126_70.out
│   ├── batch_ref_5_budget_150_1994126_71.err
│   ├── batch_ref_5_budget_150_1994126_71.out
│   ├── batch_ref_5_budget_150_1994126_72.err
│   ├── batch_ref_5_budget_150_1994126_72.out
│   ├── batch_ref_5_budget_150_1994126_73.err
│   ├── batch_ref_5_budget_150_1994126_73.out
│   ├── batch_ref_5_budget_150_1994126_74.err
│   ├── batch_ref_5_budget_150_1994126_74.out
│   ├── batch_ref_5_budget_150_1994126_75.err
│   ├── batch_ref_5_budget_150_1994126_75.out
│   ├── batch_ref_5_budget_150_1994126_76.err
│   ├── batch_ref_5_budget_150_1994126_76.out
│   ├── batch_ref_5_budget_150_1994126_77.err
│   ├── batch_ref_5_budget_150_1994126_77.out
│   ├── batch_ref_5_budget_150_1994126_78.err
│   ├── batch_ref_5_budget_150_1994126_78.out
│   ├── batch_ref_5_budget_150_1994126_79.err
│   ├── batch_ref_5_budget_150_1994126_79.out
│   ├── batch_ref_5_budget_150_1994126_8.err
│   ├── batch_ref_5_budget_150_1994126_8.out
│   ├── batch_ref_5_budget_150_1994126_80.err
│   ├── batch_ref_5_budget_150_1994126_80.out
│   ├── batch_ref_5_budget_150_1994126_81.err
│   ├── batch_ref_5_budget_150_1994126_81.out
│   ├── batch_ref_5_budget_150_1994126_9.err
│   ├── batch_ref_5_budget_150_1994126_9.out
│   ├── batch_ref_5_budget_150_2004519_1.err
│   ├── batch_ref_5_budget_150_2004519_1.out
│   ├── batch_ref_5_budget_150_2004519_10.err
│   ├── batch_ref_5_budget_150_2004519_10.out
│   ├── batch_ref_5_budget_150_2004519_11.err
│   ├── batch_ref_5_budget_150_2004519_11.out
│   ├── batch_ref_5_budget_150_2004519_12.err
│   ├── batch_ref_5_budget_150_2004519_12.out
│   ├── batch_ref_5_budget_150_2004519_13.err
│   ├── batch_ref_5_budget_150_2004519_13.out
│   ├── batch_ref_5_budget_150_2004519_14.err
│   ├── batch_ref_5_budget_150_2004519_14.out
│   ├── batch_ref_5_budget_150_2004519_15.err
│   ├── batch_ref_5_budget_150_2004519_15.out
│   ├── batch_ref_5_budget_150_2004519_16.err
│   ├── batch_ref_5_budget_150_2004519_16.out
│   ├── batch_ref_5_budget_150_2004519_17.err
│   ├── batch_ref_5_budget_150_2004519_17.out
│   ├── batch_ref_5_budget_150_2004519_18.err
│   ├── batch_ref_5_budget_150_2004519_18.out
│   ├── batch_ref_5_budget_150_2004519_19.err
│   ├── batch_ref_5_budget_150_2004519_19.out
│   ├── batch_ref_5_budget_150_2004519_2.err
│   ├── batch_ref_5_budget_150_2004519_2.out
│   ├── batch_ref_5_budget_150_2004519_20.err
│   ├── batch_ref_5_budget_150_2004519_20.out
│   ├── batch_ref_5_budget_150_2004519_21.err
│   ├── batch_ref_5_budget_150_2004519_21.out
│   ├── batch_ref_5_budget_150_2004519_22.err
│   ├── batch_ref_5_budget_150_2004519_22.out
│   ├── batch_ref_5_budget_150_2004519_23.err
│   ├── batch_ref_5_budget_150_2004519_23.out
│   ├── batch_ref_5_budget_150_2004519_24.err
│   ├── batch_ref_5_budget_150_2004519_24.out
│   ├── batch_ref_5_budget_150_2004519_25.err
│   ├── batch_ref_5_budget_150_2004519_25.out
│   ├── batch_ref_5_budget_150_2004519_26.err
│   ├── batch_ref_5_budget_150_2004519_26.out
│   ├── batch_ref_5_budget_150_2004519_27.err
│   ├── batch_ref_5_budget_150_2004519_27.out
│   ├── batch_ref_5_budget_150_2004519_28.err
│   ├── batch_ref_5_budget_150_2004519_28.out
│   ├── batch_ref_5_budget_150_2004519_29.err
│   ├── batch_ref_5_budget_150_2004519_29.out
│   ├── batch_ref_5_budget_150_2004519_3.err
│   ├── batch_ref_5_budget_150_2004519_3.out
│   ├── batch_ref_5_budget_150_2004519_30.err
│   ├── batch_ref_5_budget_150_2004519_30.out
│   ├── batch_ref_5_budget_150_2004519_31.err
│   ├── batch_ref_5_budget_150_2004519_31.out
│   ├── batch_ref_5_budget_150_2004519_32.err
│   ├── batch_ref_5_budget_150_2004519_32.out
│   ├── batch_ref_5_budget_150_2004519_33.err
│   ├── batch_ref_5_budget_150_2004519_33.out
│   ├── batch_ref_5_budget_150_2004519_34.err
│   ├── batch_ref_5_budget_150_2004519_34.out
│   ├── batch_ref_5_budget_150_2004519_35.err
│   ├── batch_ref_5_budget_150_2004519_35.out
│   ├── batch_ref_5_budget_150_2004519_36.err
│   ├── batch_ref_5_budget_150_2004519_36.out
│   ├── batch_ref_5_budget_150_2004519_37.err
│   ├── batch_ref_5_budget_150_2004519_37.out
│   ├── batch_ref_5_budget_150_2004519_38.err
│   ├── batch_ref_5_budget_150_2004519_38.out
│   ├── batch_ref_5_budget_150_2004519_39.err
│   ├── batch_ref_5_budget_150_2004519_39.out
│   ├── batch_ref_5_budget_150_2004519_4.err
│   ├── batch_ref_5_budget_150_2004519_4.out
│   ├── batch_ref_5_budget_150_2004519_40.err
│   ├── batch_ref_5_budget_150_2004519_40.out
│   ├── batch_ref_5_budget_150_2004519_41.err
│   ├── batch_ref_5_budget_150_2004519_41.out
│   ├── batch_ref_5_budget_150_2004519_42.err
│   ├── batch_ref_5_budget_150_2004519_42.out
│   ├── batch_ref_5_budget_150_2004519_43.err
│   ├── batch_ref_5_budget_150_2004519_43.out
│   ├── batch_ref_5_budget_150_2004519_44.err
│   ├── batch_ref_5_budget_150_2004519_44.out
│   ├── batch_ref_5_budget_150_2004519_45.err
│   ├── batch_ref_5_budget_150_2004519_45.out
│   ├── batch_ref_5_budget_150_2004519_46.err
│   ├── batch_ref_5_budget_150_2004519_46.out
│   ├── batch_ref_5_budget_150_2004519_47.err
│   ├── batch_ref_5_budget_150_2004519_47.out
│   ├── batch_ref_5_budget_150_2004519_48.err
│   ├── batch_ref_5_budget_150_2004519_48.out
│   ├── batch_ref_5_budget_150_2004519_49.err
│   ├── batch_ref_5_budget_150_2004519_49.out
│   ├── batch_ref_5_budget_150_2004519_5.err
│   ├── batch_ref_5_budget_150_2004519_5.out
│   ├── batch_ref_5_budget_150_2004519_50.err
│   ├── batch_ref_5_budget_150_2004519_50.out
│   ├── batch_ref_5_budget_150_2004519_51.err
│   ├── batch_ref_5_budget_150_2004519_51.out
│   ├── batch_ref_5_budget_150_2004519_52.err
│   ├── batch_ref_5_budget_150_2004519_52.out
│   ├── batch_ref_5_budget_150_2004519_53.err
│   ├── batch_ref_5_budget_150_2004519_53.out
│   ├── batch_ref_5_budget_150_2004519_54.err
│   ├── batch_ref_5_budget_150_2004519_54.out
│   ├── batch_ref_5_budget_150_2004519_55.err
│   ├── batch_ref_5_budget_150_2004519_55.out
│   ├── batch_ref_5_budget_150_2004519_56.err
│   ├── batch_ref_5_budget_150_2004519_56.out
│   ├── batch_ref_5_budget_150_2004519_57.err
│   ├── batch_ref_5_budget_150_2004519_57.out
│   ├── batch_ref_5_budget_150_2004519_58.err
│   ├── batch_ref_5_budget_150_2004519_58.out
│   ├── batch_ref_5_budget_150_2004519_59.err
│   ├── batch_ref_5_budget_150_2004519_59.out
│   ├── batch_ref_5_budget_150_2004519_6.err
│   ├── batch_ref_5_budget_150_2004519_6.out
│   ├── batch_ref_5_budget_150_2004519_60.err
│   ├── batch_ref_5_budget_150_2004519_60.out
│   ├── batch_ref_5_budget_150_2004519_61.err
│   ├── batch_ref_5_budget_150_2004519_61.out
│   ├── batch_ref_5_budget_150_2004519_62.err
│   ├── batch_ref_5_budget_150_2004519_62.out
│   ├── batch_ref_5_budget_150_2004519_63.err
│   ├── batch_ref_5_budget_150_2004519_63.out
│   ├── batch_ref_5_budget_150_2004519_64.err
│   ├── batch_ref_5_budget_150_2004519_64.out
│   ├── batch_ref_5_budget_150_2004519_65.err
│   ├── batch_ref_5_budget_150_2004519_65.out
│   ├── batch_ref_5_budget_150_2004519_66.err
│   ├── batch_ref_5_budget_150_2004519_66.out
│   ├── batch_ref_5_budget_150_2004519_67.err
│   ├── batch_ref_5_budget_150_2004519_67.out
│   ├── batch_ref_5_budget_150_2004519_68.err
│   ├── batch_ref_5_budget_150_2004519_68.out
│   ├── batch_ref_5_budget_150_2004519_69.err
│   ├── batch_ref_5_budget_150_2004519_69.out
│   ├── batch_ref_5_budget_150_2004519_7.err
│   ├── batch_ref_5_budget_150_2004519_7.out
│   ├── batch_ref_5_budget_150_2004519_70.err
│   ├── batch_ref_5_budget_150_2004519_70.out
│   ├── batch_ref_5_budget_150_2004519_71.err
│   ├── batch_ref_5_budget_150_2004519_71.out
│   ├── batch_ref_5_budget_150_2004519_72.err
│   ├── batch_ref_5_budget_150_2004519_72.out
│   ├── batch_ref_5_budget_150_2004519_73.err
│   ├── batch_ref_5_budget_150_2004519_73.out
│   ├── batch_ref_5_budget_150_2004519_74.err
│   ├── batch_ref_5_budget_150_2004519_74.out
│   ├── batch_ref_5_budget_150_2004519_75.err
│   ├── batch_ref_5_budget_150_2004519_75.out
│   ├── batch_ref_5_budget_150_2004519_76.err
│   ├── batch_ref_5_budget_150_2004519_76.out
│   ├── batch_ref_5_budget_150_2004519_77.err
│   ├── batch_ref_5_budget_150_2004519_77.out
│   ├── batch_ref_5_budget_150_2004519_78.err
│   ├── batch_ref_5_budget_150_2004519_78.out
│   ├── batch_ref_5_budget_150_2004519_79.err
│   ├── batch_ref_5_budget_150_2004519_79.out
│   ├── batch_ref_5_budget_150_2004519_8.err
│   ├── batch_ref_5_budget_150_2004519_8.out
│   ├── batch_ref_5_budget_150_2004519_80.err
│   ├── batch_ref_5_budget_150_2004519_80.out
│   ├── batch_ref_5_budget_150_2004519_81.err
│   ├── batch_ref_5_budget_150_2004519_81.out
│   ├── batch_ref_5_budget_150_2004519_9.err
│   ├── batch_ref_5_budget_150_2004519_9.out
│   ├── batch_ref_5_budget_150_2005607_1.err
│   ├── batch_ref_5_budget_150_2005607_1.out
│   ├── batch_ref_5_budget_150_2005607_10.err
│   ├── batch_ref_5_budget_150_2005607_10.out
│   ├── batch_ref_5_budget_150_2005607_11.err
│   ├── batch_ref_5_budget_150_2005607_11.out
│   ├── batch_ref_5_budget_150_2005607_12.err
│   ├── batch_ref_5_budget_150_2005607_12.out
│   ├── batch_ref_5_budget_150_2005607_13.err
│   ├── batch_ref_5_budget_150_2005607_13.out
│   ├── batch_ref_5_budget_150_2005607_14.err
│   ├── batch_ref_5_budget_150_2005607_14.out
│   ├── batch_ref_5_budget_150_2005607_15.err
│   ├── batch_ref_5_budget_150_2005607_15.out
│   ├── batch_ref_5_budget_150_2005607_16.err
│   ├── batch_ref_5_budget_150_2005607_16.out
│   ├── batch_ref_5_budget_150_2005607_17.err
│   ├── batch_ref_5_budget_150_2005607_17.out
│   ├── batch_ref_5_budget_150_2005607_18.err
│   ├── batch_ref_5_budget_150_2005607_18.out
│   ├── batch_ref_5_budget_150_2005607_19.err
│   ├── batch_ref_5_budget_150_2005607_19.out
│   ├── batch_ref_5_budget_150_2005607_2.err
│   ├── batch_ref_5_budget_150_2005607_2.out
│   ├── batch_ref_5_budget_150_2005607_20.err
│   ├── batch_ref_5_budget_150_2005607_20.out
│   ├── batch_ref_5_budget_150_2005607_21.err
│   ├── batch_ref_5_budget_150_2005607_21.out
│   ├── batch_ref_5_budget_150_2005607_22.err
│   ├── batch_ref_5_budget_150_2005607_22.out
│   ├── batch_ref_5_budget_150_2005607_23.err
│   ├── batch_ref_5_budget_150_2005607_23.out
│   ├── batch_ref_5_budget_150_2005607_24.err
│   ├── batch_ref_5_budget_150_2005607_24.out
│   ├── batch_ref_5_budget_150_2005607_25.err
│   ├── batch_ref_5_budget_150_2005607_25.out
│   ├── batch_ref_5_budget_150_2005607_26.err
│   ├── batch_ref_5_budget_150_2005607_26.out
│   ├── batch_ref_5_budget_150_2005607_27.err
│   ├── batch_ref_5_budget_150_2005607_27.out
│   ├── batch_ref_5_budget_150_2005607_28.err
│   ├── batch_ref_5_budget_150_2005607_28.out
│   ├── batch_ref_5_budget_150_2005607_29.err
│   ├── batch_ref_5_budget_150_2005607_29.out
│   ├── batch_ref_5_budget_150_2005607_3.err
│   ├── batch_ref_5_budget_150_2005607_3.out
│   ├── batch_ref_5_budget_150_2005607_30.err
│   ├── batch_ref_5_budget_150_2005607_30.out
│   ├── batch_ref_5_budget_150_2005607_31.err
│   ├── batch_ref_5_budget_150_2005607_31.out
│   ├── batch_ref_5_budget_150_2005607_32.err
│   ├── batch_ref_5_budget_150_2005607_32.out
│   ├── batch_ref_5_budget_150_2005607_33.err
│   ├── batch_ref_5_budget_150_2005607_33.out
│   ├── batch_ref_5_budget_150_2005607_34.err
│   ├── batch_ref_5_budget_150_2005607_34.out
│   ├── batch_ref_5_budget_150_2005607_35.err
│   ├── batch_ref_5_budget_150_2005607_35.out
│   ├── batch_ref_5_budget_150_2005607_36.err
│   ├── batch_ref_5_budget_150_2005607_36.out
│   ├── batch_ref_5_budget_150_2005607_37.err
│   ├── batch_ref_5_budget_150_2005607_37.out
│   ├── batch_ref_5_budget_150_2005607_38.err
│   ├── batch_ref_5_budget_150_2005607_38.out
│   ├── batch_ref_5_budget_150_2005607_39.err
│   ├── batch_ref_5_budget_150_2005607_39.out
│   ├── batch_ref_5_budget_150_2005607_4.err
│   ├── batch_ref_5_budget_150_2005607_4.out
│   ├── batch_ref_5_budget_150_2005607_40.err
│   ├── batch_ref_5_budget_150_2005607_40.out
│   ├── batch_ref_5_budget_150_2005607_41.err
│   ├── batch_ref_5_budget_150_2005607_41.out
│   ├── batch_ref_5_budget_150_2005607_42.err
│   ├── batch_ref_5_budget_150_2005607_42.out
│   ├── batch_ref_5_budget_150_2005607_43.err
│   ├── batch_ref_5_budget_150_2005607_43.out
│   ├── batch_ref_5_budget_150_2005607_44.err
│   ├── batch_ref_5_budget_150_2005607_44.out
│   ├── batch_ref_5_budget_150_2005607_45.err
│   ├── batch_ref_5_budget_150_2005607_45.out
│   ├── batch_ref_5_budget_150_2005607_46.err
│   ├── batch_ref_5_budget_150_2005607_46.out
│   ├── batch_ref_5_budget_150_2005607_47.err
│   ├── batch_ref_5_budget_150_2005607_47.out
│   ├── batch_ref_5_budget_150_2005607_48.err
│   ├── batch_ref_5_budget_150_2005607_48.out
│   ├── batch_ref_5_budget_150_2005607_49.err
│   ├── batch_ref_5_budget_150_2005607_49.out
│   ├── batch_ref_5_budget_150_2005607_5.err
│   ├── batch_ref_5_budget_150_2005607_5.out
│   ├── batch_ref_5_budget_150_2005607_50.err
│   ├── batch_ref_5_budget_150_2005607_50.out
│   ├── batch_ref_5_budget_150_2005607_51.err
│   ├── batch_ref_5_budget_150_2005607_51.out
│   ├── batch_ref_5_budget_150_2005607_52.err
│   ├── batch_ref_5_budget_150_2005607_52.out
│   ├── batch_ref_5_budget_150_2005607_53.err
│   ├── batch_ref_5_budget_150_2005607_53.out
│   ├── batch_ref_5_budget_150_2005607_54.err
│   ├── batch_ref_5_budget_150_2005607_54.out
│   ├── batch_ref_5_budget_150_2005607_55.err
│   ├── batch_ref_5_budget_150_2005607_55.out
│   ├── batch_ref_5_budget_150_2005607_56.err
│   ├── batch_ref_5_budget_150_2005607_56.out
│   ├── batch_ref_5_budget_150_2005607_57.err
│   ├── batch_ref_5_budget_150_2005607_57.out
│   ├── batch_ref_5_budget_150_2005607_58.err
│   ├── batch_ref_5_budget_150_2005607_58.out
│   ├── batch_ref_5_budget_150_2005607_59.err
│   ├── batch_ref_5_budget_150_2005607_59.out
│   ├── batch_ref_5_budget_150_2005607_6.err
│   ├── batch_ref_5_budget_150_2005607_6.out
│   ├── batch_ref_5_budget_150_2005607_60.err
│   ├── batch_ref_5_budget_150_2005607_60.out
│   ├── batch_ref_5_budget_150_2005607_61.err
│   ├── batch_ref_5_budget_150_2005607_61.out
│   ├── batch_ref_5_budget_150_2005607_62.err
│   ├── batch_ref_5_budget_150_2005607_62.out
│   ├── batch_ref_5_budget_150_2005607_63.err
│   ├── batch_ref_5_budget_150_2005607_63.out
│   ├── batch_ref_5_budget_150_2005607_64.err
│   ├── batch_ref_5_budget_150_2005607_64.out
│   ├── batch_ref_5_budget_150_2005607_65.err
│   ├── batch_ref_5_budget_150_2005607_65.out
│   ├── batch_ref_5_budget_150_2005607_66.err
│   ├── batch_ref_5_budget_150_2005607_66.out
│   ├── batch_ref_5_budget_150_2005607_67.err
│   ├── batch_ref_5_budget_150_2005607_67.out
│   ├── batch_ref_5_budget_150_2005607_68.err
│   ├── batch_ref_5_budget_150_2005607_68.out
│   ├── batch_ref_5_budget_150_2005607_69.err
│   ├── batch_ref_5_budget_150_2005607_69.out
│   ├── batch_ref_5_budget_150_2005607_7.err
│   ├── batch_ref_5_budget_150_2005607_7.out
│   ├── batch_ref_5_budget_150_2005607_70.err
│   ├── batch_ref_5_budget_150_2005607_70.out
│   ├── batch_ref_5_budget_150_2005607_71.err
│   ├── batch_ref_5_budget_150_2005607_71.out
│   ├── batch_ref_5_budget_150_2005607_72.err
│   ├── batch_ref_5_budget_150_2005607_72.out
│   ├── batch_ref_5_budget_150_2005607_73.err
│   ├── batch_ref_5_budget_150_2005607_73.out
│   ├── batch_ref_5_budget_150_2005607_74.err
│   ├── batch_ref_5_budget_150_2005607_74.out
│   ├── batch_ref_5_budget_150_2005607_75.err
│   ├── batch_ref_5_budget_150_2005607_75.out
│   ├── batch_ref_5_budget_150_2005607_76.err
│   ├── batch_ref_5_budget_150_2005607_76.out
│   ├── batch_ref_5_budget_150_2005607_77.err
│   ├── batch_ref_5_budget_150_2005607_77.out
│   ├── batch_ref_5_budget_150_2005607_78.err
│   ├── batch_ref_5_budget_150_2005607_78.out
│   ├── batch_ref_5_budget_150_2005607_79.err
│   ├── batch_ref_5_budget_150_2005607_79.out
│   ├── batch_ref_5_budget_150_2005607_8.err
│   ├── batch_ref_5_budget_150_2005607_8.out
│   ├── batch_ref_5_budget_150_2005607_80.err
│   ├── batch_ref_5_budget_150_2005607_80.out
│   ├── batch_ref_5_budget_150_2005607_81.err
│   ├── batch_ref_5_budget_150_2005607_81.out
│   ├── batch_ref_5_budget_150_2005607_9.err
│   ├── batch_ref_5_budget_150_2005607_9.out
│   ├── batch_ref_5_budget_150_2005994_1.err
│   ├── batch_ref_5_budget_150_2005994_1.out
│   ├── batch_ref_5_budget_150_2005994_10.err
│   ├── batch_ref_5_budget_150_2005994_10.out
│   ├── batch_ref_5_budget_150_2005994_11.err
│   ├── batch_ref_5_budget_150_2005994_11.out
│   ├── batch_ref_5_budget_150_2005994_12.err
│   ├── batch_ref_5_budget_150_2005994_12.out
│   ├── batch_ref_5_budget_150_2005994_13.err
│   ├── batch_ref_5_budget_150_2005994_13.out
│   ├── batch_ref_5_budget_150_2005994_14.err
│   ├── batch_ref_5_budget_150_2005994_14.out
│   ├── batch_ref_5_budget_150_2005994_15.err
│   ├── batch_ref_5_budget_150_2005994_15.out
│   ├── batch_ref_5_budget_150_2005994_16.err
│   ├── batch_ref_5_budget_150_2005994_16.out
│   ├── batch_ref_5_budget_150_2005994_17.err
│   ├── batch_ref_5_budget_150_2005994_17.out
│   ├── batch_ref_5_budget_150_2005994_18.err
│   ├── batch_ref_5_budget_150_2005994_18.out
│   ├── batch_ref_5_budget_150_2005994_19.err
│   ├── batch_ref_5_budget_150_2005994_19.out
│   ├── batch_ref_5_budget_150_2005994_2.err
│   ├── batch_ref_5_budget_150_2005994_2.out
│   ├── batch_ref_5_budget_150_2005994_20.err
│   ├── batch_ref_5_budget_150_2005994_20.out
│   ├── batch_ref_5_budget_150_2005994_21.err
│   ├── batch_ref_5_budget_150_2005994_21.out
│   ├── batch_ref_5_budget_150_2005994_22.err
│   ├── batch_ref_5_budget_150_2005994_22.out
│   ├── batch_ref_5_budget_150_2005994_23.err
│   ├── batch_ref_5_budget_150_2005994_23.out
│   ├── batch_ref_5_budget_150_2005994_24.err
│   ├── batch_ref_5_budget_150_2005994_24.out
│   ├── batch_ref_5_budget_150_2005994_25.err
│   ├── batch_ref_5_budget_150_2005994_25.out
│   ├── batch_ref_5_budget_150_2005994_26.err
│   ├── batch_ref_5_budget_150_2005994_26.out
│   ├── batch_ref_5_budget_150_2005994_27.err
│   ├── batch_ref_5_budget_150_2005994_27.out
│   ├── batch_ref_5_budget_150_2005994_28.err
│   ├── batch_ref_5_budget_150_2005994_28.out
│   ├── batch_ref_5_budget_150_2005994_29.err
│   ├── batch_ref_5_budget_150_2005994_29.out
│   ├── batch_ref_5_budget_150_2005994_3.err
│   ├── batch_ref_5_budget_150_2005994_3.out
│   ├── batch_ref_5_budget_150_2005994_30.err
│   ├── batch_ref_5_budget_150_2005994_30.out
│   ├── batch_ref_5_budget_150_2005994_31.err
│   ├── batch_ref_5_budget_150_2005994_31.out
│   ├── batch_ref_5_budget_150_2005994_32.err
│   ├── batch_ref_5_budget_150_2005994_32.out
│   ├── batch_ref_5_budget_150_2005994_33.err
│   ├── batch_ref_5_budget_150_2005994_33.out
│   ├── batch_ref_5_budget_150_2005994_34.err
│   ├── batch_ref_5_budget_150_2005994_34.out
│   ├── batch_ref_5_budget_150_2005994_35.err
│   ├── batch_ref_5_budget_150_2005994_35.out
│   ├── batch_ref_5_budget_150_2005994_36.err
│   ├── batch_ref_5_budget_150_2005994_36.out
│   ├── batch_ref_5_budget_150_2005994_37.err
│   ├── batch_ref_5_budget_150_2005994_37.out
│   ├── batch_ref_5_budget_150_2005994_38.err
│   ├── batch_ref_5_budget_150_2005994_38.out
│   ├── batch_ref_5_budget_150_2005994_39.err
│   ├── batch_ref_5_budget_150_2005994_39.out
│   ├── batch_ref_5_budget_150_2005994_4.err
│   ├── batch_ref_5_budget_150_2005994_4.out
│   ├── batch_ref_5_budget_150_2005994_40.err
│   ├── batch_ref_5_budget_150_2005994_40.out
│   ├── batch_ref_5_budget_150_2005994_41.err
│   ├── batch_ref_5_budget_150_2005994_41.out
│   ├── batch_ref_5_budget_150_2005994_42.err
│   ├── batch_ref_5_budget_150_2005994_42.out
│   ├── batch_ref_5_budget_150_2005994_43.err
│   ├── batch_ref_5_budget_150_2005994_43.out
│   ├── batch_ref_5_budget_150_2005994_44.err
│   ├── batch_ref_5_budget_150_2005994_44.out
│   ├── batch_ref_5_budget_150_2005994_45.err
│   ├── batch_ref_5_budget_150_2005994_45.out
│   ├── batch_ref_5_budget_150_2005994_46.err
│   ├── batch_ref_5_budget_150_2005994_46.out
│   ├── batch_ref_5_budget_150_2005994_47.err
│   ├── batch_ref_5_budget_150_2005994_47.out
│   ├── batch_ref_5_budget_150_2005994_48.err
│   ├── batch_ref_5_budget_150_2005994_48.out
│   ├── batch_ref_5_budget_150_2005994_49.err
│   ├── batch_ref_5_budget_150_2005994_49.out
│   ├── batch_ref_5_budget_150_2005994_5.err
│   ├── batch_ref_5_budget_150_2005994_5.out
│   ├── batch_ref_5_budget_150_2005994_50.err
│   ├── batch_ref_5_budget_150_2005994_50.out
│   ├── batch_ref_5_budget_150_2005994_51.err
│   ├── batch_ref_5_budget_150_2005994_51.out
│   ├── batch_ref_5_budget_150_2005994_52.err
│   ├── batch_ref_5_budget_150_2005994_52.out
│   ├── batch_ref_5_budget_150_2005994_53.err
│   ├── batch_ref_5_budget_150_2005994_53.out
│   ├── batch_ref_5_budget_150_2005994_54.err
│   ├── batch_ref_5_budget_150_2005994_54.out
│   ├── batch_ref_5_budget_150_2005994_55.err
│   ├── batch_ref_5_budget_150_2005994_55.out
│   ├── batch_ref_5_budget_150_2005994_56.err
│   ├── batch_ref_5_budget_150_2005994_56.out
│   ├── batch_ref_5_budget_150_2005994_57.err
│   ├── batch_ref_5_budget_150_2005994_57.out
│   ├── batch_ref_5_budget_150_2005994_58.err
│   ├── batch_ref_5_budget_150_2005994_58.out
│   ├── batch_ref_5_budget_150_2005994_59.err
│   ├── batch_ref_5_budget_150_2005994_59.out
│   ├── batch_ref_5_budget_150_2005994_6.err
│   ├── batch_ref_5_budget_150_2005994_6.out
│   ├── batch_ref_5_budget_150_2005994_60.err
│   ├── batch_ref_5_budget_150_2005994_60.out
│   ├── batch_ref_5_budget_150_2005994_61.err
│   ├── batch_ref_5_budget_150_2005994_61.out
│   ├── batch_ref_5_budget_150_2005994_62.err
│   ├── batch_ref_5_budget_150_2005994_62.out
│   ├── batch_ref_5_budget_150_2005994_63.err
│   ├── batch_ref_5_budget_150_2005994_63.out
│   ├── batch_ref_5_budget_150_2005994_64.err
│   ├── batch_ref_5_budget_150_2005994_64.out
│   ├── batch_ref_5_budget_150_2005994_65.err
│   ├── batch_ref_5_budget_150_2005994_65.out
│   ├── batch_ref_5_budget_150_2005994_66.err
│   ├── batch_ref_5_budget_150_2005994_66.out
│   ├── batch_ref_5_budget_150_2005994_67.err
│   ├── batch_ref_5_budget_150_2005994_67.out
│   ├── batch_ref_5_budget_150_2005994_68.err
│   ├── batch_ref_5_budget_150_2005994_68.out
│   ├── batch_ref_5_budget_150_2005994_69.err
│   ├── batch_ref_5_budget_150_2005994_69.out
│   ├── batch_ref_5_budget_150_2005994_7.err
│   ├── batch_ref_5_budget_150_2005994_7.out
│   ├── batch_ref_5_budget_150_2005994_70.err
│   ├── batch_ref_5_budget_150_2005994_70.out
│   ├── batch_ref_5_budget_150_2005994_71.err
│   ├── batch_ref_5_budget_150_2005994_71.out
│   ├── batch_ref_5_budget_150_2005994_72.err
│   ├── batch_ref_5_budget_150_2005994_72.out
│   ├── batch_ref_5_budget_150_2005994_73.err
│   ├── batch_ref_5_budget_150_2005994_73.out
│   ├── batch_ref_5_budget_150_2005994_74.err
│   ├── batch_ref_5_budget_150_2005994_74.out
│   ├── batch_ref_5_budget_150_2005994_75.err
│   ├── batch_ref_5_budget_150_2005994_75.out
│   ├── batch_ref_5_budget_150_2005994_76.err
│   ├── batch_ref_5_budget_150_2005994_76.out
│   ├── batch_ref_5_budget_150_2005994_77.err
│   ├── batch_ref_5_budget_150_2005994_77.out
│   ├── batch_ref_5_budget_150_2005994_78.err
│   ├── batch_ref_5_budget_150_2005994_78.out
│   ├── batch_ref_5_budget_150_2005994_79.err
│   ├── batch_ref_5_budget_150_2005994_79.out
│   ├── batch_ref_5_budget_150_2005994_8.err
│   ├── batch_ref_5_budget_150_2005994_8.out
│   ├── batch_ref_5_budget_150_2005994_80.err
│   ├── batch_ref_5_budget_150_2005994_80.out
│   ├── batch_ref_5_budget_150_2005994_81.err
│   ├── batch_ref_5_budget_150_2005994_81.out
│   ├── batch_ref_5_budget_150_2005994_9.err
│   ├── batch_ref_5_budget_150_2005994_9.out
│   ├── batch_ref_5_budget_150_2040031_1.err
│   ├── batch_ref_5_budget_150_2040031_1.out
│   ├── batch_ref_5_budget_150_2040031_10.err
│   ├── batch_ref_5_budget_150_2040031_10.out
│   ├── batch_ref_5_budget_150_2040031_11.err
│   ├── batch_ref_5_budget_150_2040031_11.out
│   ├── batch_ref_5_budget_150_2040031_12.err
│   ├── batch_ref_5_budget_150_2040031_12.out
│   ├── batch_ref_5_budget_150_2040031_13.err
│   ├── batch_ref_5_budget_150_2040031_13.out
│   ├── batch_ref_5_budget_150_2040031_14.err
│   ├── batch_ref_5_budget_150_2040031_14.out
│   ├── batch_ref_5_budget_150_2040031_15.err
│   ├── batch_ref_5_budget_150_2040031_15.out
│   ├── batch_ref_5_budget_150_2040031_16.err
│   ├── batch_ref_5_budget_150_2040031_16.out
│   ├── batch_ref_5_budget_150_2040031_17.err
│   ├── batch_ref_5_budget_150_2040031_17.out
│   ├── batch_ref_5_budget_150_2040031_18.err
│   ├── batch_ref_5_budget_150_2040031_18.out
│   ├── batch_ref_5_budget_150_2040031_19.err
│   ├── batch_ref_5_budget_150_2040031_19.out
│   ├── batch_ref_5_budget_150_2040031_2.err
│   ├── batch_ref_5_budget_150_2040031_2.out
│   ├── batch_ref_5_budget_150_2040031_20.err
│   ├── batch_ref_5_budget_150_2040031_20.out
│   ├── batch_ref_5_budget_150_2040031_21.err
│   ├── batch_ref_5_budget_150_2040031_21.out
│   ├── batch_ref_5_budget_150_2040031_22.err
│   ├── batch_ref_5_budget_150_2040031_22.out
│   ├── batch_ref_5_budget_150_2040031_23.err
│   ├── batch_ref_5_budget_150_2040031_23.out
│   ├── batch_ref_5_budget_150_2040031_24.err
│   ├── batch_ref_5_budget_150_2040031_24.out
│   ├── batch_ref_5_budget_150_2040031_25.err
│   ├── batch_ref_5_budget_150_2040031_25.out
│   ├── batch_ref_5_budget_150_2040031_26.err
│   ├── batch_ref_5_budget_150_2040031_26.out
│   ├── batch_ref_5_budget_150_2040031_27.err
│   ├── batch_ref_5_budget_150_2040031_27.out
│   ├── batch_ref_5_budget_150_2040031_28.err
│   ├── batch_ref_5_budget_150_2040031_28.out
│   ├── batch_ref_5_budget_150_2040031_29.err
│   ├── batch_ref_5_budget_150_2040031_29.out
│   ├── batch_ref_5_budget_150_2040031_3.err
│   ├── batch_ref_5_budget_150_2040031_3.out
│   ├── batch_ref_5_budget_150_2040031_30.err
│   ├── batch_ref_5_budget_150_2040031_30.out
│   ├── batch_ref_5_budget_150_2040031_31.err
│   ├── batch_ref_5_budget_150_2040031_31.out
│   ├── batch_ref_5_budget_150_2040031_32.err
│   ├── batch_ref_5_budget_150_2040031_32.out
│   ├── batch_ref_5_budget_150_2040031_33.err
│   ├── batch_ref_5_budget_150_2040031_33.out
│   ├── batch_ref_5_budget_150_2040031_34.err
│   ├── batch_ref_5_budget_150_2040031_34.out
│   ├── batch_ref_5_budget_150_2040031_35.err
│   ├── batch_ref_5_budget_150_2040031_35.out
│   ├── batch_ref_5_budget_150_2040031_36.err
│   ├── batch_ref_5_budget_150_2040031_36.out
│   ├── batch_ref_5_budget_150_2040031_37.err
│   ├── batch_ref_5_budget_150_2040031_37.out
│   ├── batch_ref_5_budget_150_2040031_38.err
│   ├── batch_ref_5_budget_150_2040031_38.out
│   ├── batch_ref_5_budget_150_2040031_39.err
│   ├── batch_ref_5_budget_150_2040031_39.out
│   ├── batch_ref_5_budget_150_2040031_4.err
│   ├── batch_ref_5_budget_150_2040031_4.out
│   ├── batch_ref_5_budget_150_2040031_40.err
│   ├── batch_ref_5_budget_150_2040031_40.out
│   ├── batch_ref_5_budget_150_2040031_41.err
│   ├── batch_ref_5_budget_150_2040031_41.out
│   ├── batch_ref_5_budget_150_2040031_42.err
│   ├── batch_ref_5_budget_150_2040031_42.out
│   ├── batch_ref_5_budget_150_2040031_43.err
│   ├── batch_ref_5_budget_150_2040031_43.out
│   ├── batch_ref_5_budget_150_2040031_44.err
│   ├── batch_ref_5_budget_150_2040031_44.out
│   ├── batch_ref_5_budget_150_2040031_45.err
│   ├── batch_ref_5_budget_150_2040031_45.out
│   ├── batch_ref_5_budget_150_2040031_46.err
│   ├── batch_ref_5_budget_150_2040031_46.out
│   ├── batch_ref_5_budget_150_2040031_47.err
│   ├── batch_ref_5_budget_150_2040031_47.out
│   ├── batch_ref_5_budget_150_2040031_48.err
│   ├── batch_ref_5_budget_150_2040031_48.out
│   ├── batch_ref_5_budget_150_2040031_49.err
│   ├── batch_ref_5_budget_150_2040031_49.out
│   ├── batch_ref_5_budget_150_2040031_5.err
│   ├── batch_ref_5_budget_150_2040031_5.out
│   ├── batch_ref_5_budget_150_2040031_50.err
│   ├── batch_ref_5_budget_150_2040031_50.out
│   ├── batch_ref_5_budget_150_2040031_51.err
│   ├── batch_ref_5_budget_150_2040031_51.out
│   ├── batch_ref_5_budget_150_2040031_52.err
│   ├── batch_ref_5_budget_150_2040031_52.out
│   ├── batch_ref_5_budget_150_2040031_53.err
│   ├── batch_ref_5_budget_150_2040031_53.out
│   ├── batch_ref_5_budget_150_2040031_54.err
│   ├── batch_ref_5_budget_150_2040031_54.out
│   ├── batch_ref_5_budget_150_2040031_55.err
│   ├── batch_ref_5_budget_150_2040031_55.out
│   ├── batch_ref_5_budget_150_2040031_56.err
│   ├── batch_ref_5_budget_150_2040031_56.out
│   ├── batch_ref_5_budget_150_2040031_57.err
│   ├── batch_ref_5_budget_150_2040031_57.out
│   ├── batch_ref_5_budget_150_2040031_58.err
│   ├── batch_ref_5_budget_150_2040031_58.out
│   ├── batch_ref_5_budget_150_2040031_59.err
│   ├── batch_ref_5_budget_150_2040031_59.out
│   ├── batch_ref_5_budget_150_2040031_6.err
│   ├── batch_ref_5_budget_150_2040031_6.out
│   ├── batch_ref_5_budget_150_2040031_60.err
│   ├── batch_ref_5_budget_150_2040031_60.out
│   ├── batch_ref_5_budget_150_2040031_61.err
│   ├── batch_ref_5_budget_150_2040031_61.out
│   ├── batch_ref_5_budget_150_2040031_62.err
│   ├── batch_ref_5_budget_150_2040031_62.out
│   ├── batch_ref_5_budget_150_2040031_63.err
│   ├── batch_ref_5_budget_150_2040031_63.out
│   ├── batch_ref_5_budget_150_2040031_64.err
│   ├── batch_ref_5_budget_150_2040031_64.out
│   ├── batch_ref_5_budget_150_2040031_65.err
│   ├── batch_ref_5_budget_150_2040031_65.out
│   ├── batch_ref_5_budget_150_2040031_66.err
│   ├── batch_ref_5_budget_150_2040031_66.out
│   ├── batch_ref_5_budget_150_2040031_67.err
│   ├── batch_ref_5_budget_150_2040031_67.out
│   ├── batch_ref_5_budget_150_2040031_68.err
│   ├── batch_ref_5_budget_150_2040031_68.out
│   ├── batch_ref_5_budget_150_2040031_69.err
│   ├── batch_ref_5_budget_150_2040031_69.out
│   ├── batch_ref_5_budget_150_2040031_7.err
│   ├── batch_ref_5_budget_150_2040031_7.out
│   ├── batch_ref_5_budget_150_2040031_70.err
│   ├── batch_ref_5_budget_150_2040031_70.out
│   ├── batch_ref_5_budget_150_2040031_71.err
│   ├── batch_ref_5_budget_150_2040031_71.out
│   ├── batch_ref_5_budget_150_2040031_72.err
│   ├── batch_ref_5_budget_150_2040031_72.out
│   ├── batch_ref_5_budget_150_2040031_73.err
│   ├── batch_ref_5_budget_150_2040031_73.out
│   ├── batch_ref_5_budget_150_2040031_74.err
│   ├── batch_ref_5_budget_150_2040031_74.out
│   ├── batch_ref_5_budget_150_2040031_75.err
│   ├── batch_ref_5_budget_150_2040031_75.out
│   ├── batch_ref_5_budget_150_2040031_76.err
│   ├── batch_ref_5_budget_150_2040031_76.out
│   ├── batch_ref_5_budget_150_2040031_77.err
│   ├── batch_ref_5_budget_150_2040031_77.out
│   ├── batch_ref_5_budget_150_2040031_78.err
│   ├── batch_ref_5_budget_150_2040031_78.out
│   ├── batch_ref_5_budget_150_2040031_79.err
│   ├── batch_ref_5_budget_150_2040031_79.out
│   ├── batch_ref_5_budget_150_2040031_8.err
│   ├── batch_ref_5_budget_150_2040031_8.out
│   ├── batch_ref_5_budget_150_2040031_80.err
│   ├── batch_ref_5_budget_150_2040031_80.out
│   ├── batch_ref_5_budget_150_2040031_81.err
│   ├── batch_ref_5_budget_150_2040031_81.out
│   ├── batch_ref_5_budget_150_2040031_9.err
│   ├── batch_ref_5_budget_150_2040031_9.out
│   ├── batch_ref_5_budget_200_2038358_1.err
│   ├── batch_ref_5_budget_200_2038358_1.out
│   ├── batch_ref_5_budget_200_2038358_10.err
│   ├── batch_ref_5_budget_200_2038358_10.out
│   ├── batch_ref_5_budget_200_2038358_11.err
│   ├── batch_ref_5_budget_200_2038358_11.out
│   ├── batch_ref_5_budget_200_2038358_12.err
│   ├── batch_ref_5_budget_200_2038358_12.out
│   ├── batch_ref_5_budget_200_2038358_13.err
│   ├── batch_ref_5_budget_200_2038358_13.out
│   ├── batch_ref_5_budget_200_2038358_14.err
│   ├── batch_ref_5_budget_200_2038358_14.out
│   ├── batch_ref_5_budget_200_2038358_15.err
│   ├── batch_ref_5_budget_200_2038358_15.out
│   ├── batch_ref_5_budget_200_2038358_16.err
│   ├── batch_ref_5_budget_200_2038358_16.out
│   ├── batch_ref_5_budget_200_2038358_17.err
│   ├── batch_ref_5_budget_200_2038358_17.out
│   ├── batch_ref_5_budget_200_2038358_18.err
│   ├── batch_ref_5_budget_200_2038358_18.out
│   ├── batch_ref_5_budget_200_2038358_19.err
│   ├── batch_ref_5_budget_200_2038358_19.out
│   ├── batch_ref_5_budget_200_2038358_2.err
│   ├── batch_ref_5_budget_200_2038358_2.out
│   ├── batch_ref_5_budget_200_2038358_20.err
│   ├── batch_ref_5_budget_200_2038358_20.out
│   ├── batch_ref_5_budget_200_2038358_21.err
│   ├── batch_ref_5_budget_200_2038358_21.out
│   ├── batch_ref_5_budget_200_2038358_22.err
│   ├── batch_ref_5_budget_200_2038358_22.out
│   ├── batch_ref_5_budget_200_2038358_23.err
│   ├── batch_ref_5_budget_200_2038358_23.out
│   ├── batch_ref_5_budget_200_2038358_24.err
│   ├── batch_ref_5_budget_200_2038358_24.out
│   ├── batch_ref_5_budget_200_2038358_25.err
│   ├── batch_ref_5_budget_200_2038358_25.out
│   ├── batch_ref_5_budget_200_2038358_26.err
│   ├── batch_ref_5_budget_200_2038358_26.out
│   ├── batch_ref_5_budget_200_2038358_27.err
│   ├── batch_ref_5_budget_200_2038358_27.out
│   ├── batch_ref_5_budget_200_2038358_28.err
│   ├── batch_ref_5_budget_200_2038358_28.out
│   ├── batch_ref_5_budget_200_2038358_29.err
│   ├── batch_ref_5_budget_200_2038358_29.out
│   ├── batch_ref_5_budget_200_2038358_3.err
│   ├── batch_ref_5_budget_200_2038358_3.out
│   ├── batch_ref_5_budget_200_2038358_30.err
│   ├── batch_ref_5_budget_200_2038358_30.out
│   ├── batch_ref_5_budget_200_2038358_31.err
│   ├── batch_ref_5_budget_200_2038358_31.out
│   ├── batch_ref_5_budget_200_2038358_32.err
│   ├── batch_ref_5_budget_200_2038358_32.out
│   ├── batch_ref_5_budget_200_2038358_33.err
│   ├── batch_ref_5_budget_200_2038358_33.out
│   ├── batch_ref_5_budget_200_2038358_34.err
│   ├── batch_ref_5_budget_200_2038358_34.out
│   ├── batch_ref_5_budget_200_2038358_35.err
│   ├── batch_ref_5_budget_200_2038358_35.out
│   ├── batch_ref_5_budget_200_2038358_36.err
│   ├── batch_ref_5_budget_200_2038358_36.out
│   ├── batch_ref_5_budget_200_2038358_37.err
│   ├── batch_ref_5_budget_200_2038358_37.out
│   ├── batch_ref_5_budget_200_2038358_38.err
│   ├── batch_ref_5_budget_200_2038358_38.out
│   ├── batch_ref_5_budget_200_2038358_39.err
│   ├── batch_ref_5_budget_200_2038358_39.out
│   ├── batch_ref_5_budget_200_2038358_4.err
│   ├── batch_ref_5_budget_200_2038358_4.out
│   ├── batch_ref_5_budget_200_2038358_40.err
│   ├── batch_ref_5_budget_200_2038358_40.out
│   ├── batch_ref_5_budget_200_2038358_41.err
│   ├── batch_ref_5_budget_200_2038358_41.out
│   ├── batch_ref_5_budget_200_2038358_42.err
│   ├── batch_ref_5_budget_200_2038358_42.out
│   ├── batch_ref_5_budget_200_2038358_43.err
│   ├── batch_ref_5_budget_200_2038358_43.out
│   ├── batch_ref_5_budget_200_2038358_44.err
│   ├── batch_ref_5_budget_200_2038358_44.out
│   ├── batch_ref_5_budget_200_2038358_45.err
│   ├── batch_ref_5_budget_200_2038358_45.out
│   ├── batch_ref_5_budget_200_2038358_46.err
│   ├── batch_ref_5_budget_200_2038358_46.out
│   ├── batch_ref_5_budget_200_2038358_47.err
│   ├── batch_ref_5_budget_200_2038358_47.out
│   ├── batch_ref_5_budget_200_2038358_48.err
│   ├── batch_ref_5_budget_200_2038358_48.out
│   ├── batch_ref_5_budget_200_2038358_49.err
│   ├── batch_ref_5_budget_200_2038358_49.out
│   ├── batch_ref_5_budget_200_2038358_5.err
│   ├── batch_ref_5_budget_200_2038358_5.out
│   ├── batch_ref_5_budget_200_2038358_50.err
│   ├── batch_ref_5_budget_200_2038358_50.out
│   ├── batch_ref_5_budget_200_2038358_51.err
│   ├── batch_ref_5_budget_200_2038358_51.out
│   ├── batch_ref_5_budget_200_2038358_52.err
│   ├── batch_ref_5_budget_200_2038358_52.out
│   ├── batch_ref_5_budget_200_2038358_53.err
│   ├── batch_ref_5_budget_200_2038358_53.out
│   ├── batch_ref_5_budget_200_2038358_54.err
│   ├── batch_ref_5_budget_200_2038358_54.out
│   ├── batch_ref_5_budget_200_2038358_55.err
│   ├── batch_ref_5_budget_200_2038358_55.out
│   ├── batch_ref_5_budget_200_2038358_56.err
│   ├── batch_ref_5_budget_200_2038358_56.out
│   ├── batch_ref_5_budget_200_2038358_57.err
│   ├── batch_ref_5_budget_200_2038358_57.out
│   ├── batch_ref_5_budget_200_2038358_58.err
│   ├── batch_ref_5_budget_200_2038358_58.out
│   ├── batch_ref_5_budget_200_2038358_59.err
│   ├── batch_ref_5_budget_200_2038358_59.out
│   ├── batch_ref_5_budget_200_2038358_6.err
│   ├── batch_ref_5_budget_200_2038358_6.out
│   ├── batch_ref_5_budget_200_2038358_60.err
│   ├── batch_ref_5_budget_200_2038358_60.out
│   ├── batch_ref_5_budget_200_2038358_61.err
│   ├── batch_ref_5_budget_200_2038358_61.out
│   ├── batch_ref_5_budget_200_2038358_62.err
│   ├── batch_ref_5_budget_200_2038358_62.out
│   ├── batch_ref_5_budget_200_2038358_63.err
│   ├── batch_ref_5_budget_200_2038358_63.out
│   ├── batch_ref_5_budget_200_2038358_64.err
│   ├── batch_ref_5_budget_200_2038358_64.out
│   ├── batch_ref_5_budget_200_2038358_65.err
│   ├── batch_ref_5_budget_200_2038358_65.out
│   ├── batch_ref_5_budget_200_2038358_66.err
│   ├── batch_ref_5_budget_200_2038358_66.out
│   ├── batch_ref_5_budget_200_2038358_67.err
│   ├── batch_ref_5_budget_200_2038358_67.out
│   ├── batch_ref_5_budget_200_2038358_68.err
│   ├── batch_ref_5_budget_200_2038358_68.out
│   ├── batch_ref_5_budget_200_2038358_69.err
│   ├── batch_ref_5_budget_200_2038358_69.out
│   ├── batch_ref_5_budget_200_2038358_7.err
│   ├── batch_ref_5_budget_200_2038358_7.out
│   ├── batch_ref_5_budget_200_2038358_70.err
│   ├── batch_ref_5_budget_200_2038358_70.out
│   ├── batch_ref_5_budget_200_2038358_71.err
│   ├── batch_ref_5_budget_200_2038358_71.out
│   ├── batch_ref_5_budget_200_2038358_72.err
│   ├── batch_ref_5_budget_200_2038358_72.out
│   ├── batch_ref_5_budget_200_2038358_73.err
│   ├── batch_ref_5_budget_200_2038358_73.out
│   ├── batch_ref_5_budget_200_2038358_74.err
│   ├── batch_ref_5_budget_200_2038358_74.out
│   ├── batch_ref_5_budget_200_2038358_75.err
│   ├── batch_ref_5_budget_200_2038358_75.out
│   ├── batch_ref_5_budget_200_2038358_76.err
│   ├── batch_ref_5_budget_200_2038358_76.out
│   ├── batch_ref_5_budget_200_2038358_77.err
│   ├── batch_ref_5_budget_200_2038358_77.out
│   ├── batch_ref_5_budget_200_2038358_78.err
│   ├── batch_ref_5_budget_200_2038358_78.out
│   ├── batch_ref_5_budget_200_2038358_79.err
│   ├── batch_ref_5_budget_200_2038358_79.out
│   ├── batch_ref_5_budget_200_2038358_8.err
│   ├── batch_ref_5_budget_200_2038358_8.out
│   ├── batch_ref_5_budget_200_2038358_80.err
│   ├── batch_ref_5_budget_200_2038358_80.out
│   ├── batch_ref_5_budget_200_2038358_81.err
│   ├── batch_ref_5_budget_200_2038358_81.out
│   ├── batch_ref_5_budget_200_2038358_9.err
│   ├── batch_ref_5_budget_200_2038358_9.out
│   ├── batch_ref_5_budget_200_2040032_1.err
│   ├── batch_ref_5_budget_200_2040032_1.out
│   ├── batch_ref_5_budget_200_2040032_10.err
│   ├── batch_ref_5_budget_200_2040032_10.out
│   ├── batch_ref_5_budget_200_2040032_11.err
│   ├── batch_ref_5_budget_200_2040032_11.out
│   ├── batch_ref_5_budget_200_2040032_12.err
│   ├── batch_ref_5_budget_200_2040032_12.out
│   ├── batch_ref_5_budget_200_2040032_13.err
│   ├── batch_ref_5_budget_200_2040032_13.out
│   ├── batch_ref_5_budget_200_2040032_14.err
│   ├── batch_ref_5_budget_200_2040032_14.out
│   ├── batch_ref_5_budget_200_2040032_15.err
│   ├── batch_ref_5_budget_200_2040032_15.out
│   ├── batch_ref_5_budget_200_2040032_16.err
│   ├── batch_ref_5_budget_200_2040032_16.out
│   ├── batch_ref_5_budget_200_2040032_17.err
│   ├── batch_ref_5_budget_200_2040032_17.out
│   ├── batch_ref_5_budget_200_2040032_18.err
│   ├── batch_ref_5_budget_200_2040032_18.out
│   ├── batch_ref_5_budget_200_2040032_19.err
│   ├── batch_ref_5_budget_200_2040032_19.out
│   ├── batch_ref_5_budget_200_2040032_2.err
│   ├── batch_ref_5_budget_200_2040032_2.out
│   ├── batch_ref_5_budget_200_2040032_20.err
│   ├── batch_ref_5_budget_200_2040032_20.out
│   ├── batch_ref_5_budget_200_2040032_21.err
│   ├── batch_ref_5_budget_200_2040032_21.out
│   ├── batch_ref_5_budget_200_2040032_22.err
│   ├── batch_ref_5_budget_200_2040032_22.out
│   ├── batch_ref_5_budget_200_2040032_23.err
│   ├── batch_ref_5_budget_200_2040032_23.out
│   ├── batch_ref_5_budget_200_2040032_24.err
│   ├── batch_ref_5_budget_200_2040032_24.out
│   ├── batch_ref_5_budget_200_2040032_25.err
│   ├── batch_ref_5_budget_200_2040032_25.out
│   ├── batch_ref_5_budget_200_2040032_26.err
│   ├── batch_ref_5_budget_200_2040032_26.out
│   ├── batch_ref_5_budget_200_2040032_27.err
│   ├── batch_ref_5_budget_200_2040032_27.out
│   ├── batch_ref_5_budget_200_2040032_28.err
│   ├── batch_ref_5_budget_200_2040032_28.out
│   ├── batch_ref_5_budget_200_2040032_29.err
│   ├── batch_ref_5_budget_200_2040032_29.out
│   ├── batch_ref_5_budget_200_2040032_3.err
│   ├── batch_ref_5_budget_200_2040032_3.out
│   ├── batch_ref_5_budget_200_2040032_30.err
│   ├── batch_ref_5_budget_200_2040032_30.out
│   ├── batch_ref_5_budget_200_2040032_31.err
│   ├── batch_ref_5_budget_200_2040032_31.out
│   ├── batch_ref_5_budget_200_2040032_32.err
│   ├── batch_ref_5_budget_200_2040032_32.out
│   ├── batch_ref_5_budget_200_2040032_33.err
│   ├── batch_ref_5_budget_200_2040032_33.out
│   ├── batch_ref_5_budget_200_2040032_34.err
│   ├── batch_ref_5_budget_200_2040032_34.out
│   ├── batch_ref_5_budget_200_2040032_35.err
│   ├── batch_ref_5_budget_200_2040032_35.out
│   ├── batch_ref_5_budget_200_2040032_36.err
│   ├── batch_ref_5_budget_200_2040032_36.out
│   ├── batch_ref_5_budget_200_2040032_37.err
│   ├── batch_ref_5_budget_200_2040032_37.out
│   ├── batch_ref_5_budget_200_2040032_38.err
│   ├── batch_ref_5_budget_200_2040032_38.out
│   ├── batch_ref_5_budget_200_2040032_39.err
│   ├── batch_ref_5_budget_200_2040032_39.out
│   ├── batch_ref_5_budget_200_2040032_4.err
│   ├── batch_ref_5_budget_200_2040032_4.out
│   ├── batch_ref_5_budget_200_2040032_40.err
│   ├── batch_ref_5_budget_200_2040032_40.out
│   ├── batch_ref_5_budget_200_2040032_41.err
│   ├── batch_ref_5_budget_200_2040032_41.out
│   ├── batch_ref_5_budget_200_2040032_42.err
│   ├── batch_ref_5_budget_200_2040032_42.out
│   ├── batch_ref_5_budget_200_2040032_43.err
│   ├── batch_ref_5_budget_200_2040032_43.out
│   ├── batch_ref_5_budget_200_2040032_44.err
│   ├── batch_ref_5_budget_200_2040032_44.out
│   ├── batch_ref_5_budget_200_2040032_45.err
│   ├── batch_ref_5_budget_200_2040032_45.out
│   ├── batch_ref_5_budget_200_2040032_46.err
│   ├── batch_ref_5_budget_200_2040032_46.out
│   ├── batch_ref_5_budget_200_2040032_47.err
│   ├── batch_ref_5_budget_200_2040032_47.out
│   ├── batch_ref_5_budget_200_2040032_48.err
│   ├── batch_ref_5_budget_200_2040032_48.out
│   ├── batch_ref_5_budget_200_2040032_49.err
│   ├── batch_ref_5_budget_200_2040032_49.out
│   ├── batch_ref_5_budget_200_2040032_5.err
│   ├── batch_ref_5_budget_200_2040032_5.out
│   ├── batch_ref_5_budget_200_2040032_50.err
│   ├── batch_ref_5_budget_200_2040032_50.out
│   ├── batch_ref_5_budget_200_2040032_51.err
│   ├── batch_ref_5_budget_200_2040032_51.out
│   ├── batch_ref_5_budget_200_2040032_52.err
│   ├── batch_ref_5_budget_200_2040032_52.out
│   ├── batch_ref_5_budget_200_2040032_53.err
│   ├── batch_ref_5_budget_200_2040032_53.out
│   ├── batch_ref_5_budget_200_2040032_54.err
│   ├── batch_ref_5_budget_200_2040032_54.out
│   ├── batch_ref_5_budget_200_2040032_55.err
│   ├── batch_ref_5_budget_200_2040032_55.out
│   ├── batch_ref_5_budget_200_2040032_56.err
│   ├── batch_ref_5_budget_200_2040032_56.out
│   ├── batch_ref_5_budget_200_2040032_57.err
│   ├── batch_ref_5_budget_200_2040032_57.out
│   ├── batch_ref_5_budget_200_2040032_58.err
│   ├── batch_ref_5_budget_200_2040032_58.out
│   ├── batch_ref_5_budget_200_2040032_59.err
│   ├── batch_ref_5_budget_200_2040032_59.out
│   ├── batch_ref_5_budget_200_2040032_6.err
│   ├── batch_ref_5_budget_200_2040032_6.out
│   ├── batch_ref_5_budget_200_2040032_60.err
│   ├── batch_ref_5_budget_200_2040032_60.out
│   ├── batch_ref_5_budget_200_2040032_61.err
│   ├── batch_ref_5_budget_200_2040032_61.out
│   ├── batch_ref_5_budget_200_2040032_62.err
│   ├── batch_ref_5_budget_200_2040032_62.out
│   ├── batch_ref_5_budget_200_2040032_63.err
│   ├── batch_ref_5_budget_200_2040032_63.out
│   ├── batch_ref_5_budget_200_2040032_64.err
│   ├── batch_ref_5_budget_200_2040032_64.out
│   ├── batch_ref_5_budget_200_2040032_65.err
│   ├── batch_ref_5_budget_200_2040032_65.out
│   ├── batch_ref_5_budget_200_2040032_66.err
│   ├── batch_ref_5_budget_200_2040032_66.out
│   ├── batch_ref_5_budget_200_2040032_67.err
│   ├── batch_ref_5_budget_200_2040032_67.out
│   ├── batch_ref_5_budget_200_2040032_68.err
│   ├── batch_ref_5_budget_200_2040032_68.out
│   ├── batch_ref_5_budget_200_2040032_69.err
│   ├── batch_ref_5_budget_200_2040032_69.out
│   ├── batch_ref_5_budget_200_2040032_7.err
│   ├── batch_ref_5_budget_200_2040032_7.out
│   ├── batch_ref_5_budget_200_2040032_70.err
│   ├── batch_ref_5_budget_200_2040032_70.out
│   ├── batch_ref_5_budget_200_2040032_71.err
│   ├── batch_ref_5_budget_200_2040032_71.out
│   ├── batch_ref_5_budget_200_2040032_72.err
│   ├── batch_ref_5_budget_200_2040032_72.out
│   ├── batch_ref_5_budget_200_2040032_73.err
│   ├── batch_ref_5_budget_200_2040032_73.out
│   ├── batch_ref_5_budget_200_2040032_74.err
│   ├── batch_ref_5_budget_200_2040032_74.out
│   ├── batch_ref_5_budget_200_2040032_75.err
│   ├── batch_ref_5_budget_200_2040032_75.out
│   ├── batch_ref_5_budget_200_2040032_76.err
│   ├── batch_ref_5_budget_200_2040032_76.out
│   ├── batch_ref_5_budget_200_2040032_77.err
│   ├── batch_ref_5_budget_200_2040032_77.out
│   ├── batch_ref_5_budget_200_2040032_78.err
│   ├── batch_ref_5_budget_200_2040032_78.out
│   ├── batch_ref_5_budget_200_2040032_79.err
│   ├── batch_ref_5_budget_200_2040032_79.out
│   ├── batch_ref_5_budget_200_2040032_8.err
│   ├── batch_ref_5_budget_200_2040032_8.out
│   ├── batch_ref_5_budget_200_2040032_80.err
│   ├── batch_ref_5_budget_200_2040032_80.out
│   ├── batch_ref_5_budget_200_2040032_81.err
│   ├── batch_ref_5_budget_200_2040032_81.out
│   ├── batch_ref_5_budget_200_2040032_9.err
│   ├── batch_ref_5_budget_200_2040032_9.out
│   ├── batch_ref_5_budget_50_2024694_1.err
│   ├── batch_ref_5_budget_50_2024694_1.out
│   ├── batch_ref_5_budget_50_2024694_10.err
│   ├── batch_ref_5_budget_50_2024694_10.out
│   ├── batch_ref_5_budget_50_2024694_11.err
│   ├── batch_ref_5_budget_50_2024694_11.out
│   ├── batch_ref_5_budget_50_2024694_12.err
│   ├── batch_ref_5_budget_50_2024694_12.out
│   ├── batch_ref_5_budget_50_2024694_13.err
│   ├── batch_ref_5_budget_50_2024694_13.out
│   ├── batch_ref_5_budget_50_2024694_14.err
│   ├── batch_ref_5_budget_50_2024694_14.out
│   ├── batch_ref_5_budget_50_2024694_15.err
│   ├── batch_ref_5_budget_50_2024694_15.out
│   ├── batch_ref_5_budget_50_2024694_16.err
│   ├── batch_ref_5_budget_50_2024694_16.out
│   ├── batch_ref_5_budget_50_2024694_17.err
│   ├── batch_ref_5_budget_50_2024694_17.out
│   ├── batch_ref_5_budget_50_2024694_18.err
│   ├── batch_ref_5_budget_50_2024694_18.out
│   ├── batch_ref_5_budget_50_2024694_19.err
│   ├── batch_ref_5_budget_50_2024694_19.out
│   ├── batch_ref_5_budget_50_2024694_2.err
│   ├── batch_ref_5_budget_50_2024694_2.out
│   ├── batch_ref_5_budget_50_2024694_20.err
│   ├── batch_ref_5_budget_50_2024694_20.out
│   ├── batch_ref_5_budget_50_2024694_21.err
│   ├── batch_ref_5_budget_50_2024694_21.out
│   ├── batch_ref_5_budget_50_2024694_22.err
│   ├── batch_ref_5_budget_50_2024694_22.out
│   ├── batch_ref_5_budget_50_2024694_23.err
│   ├── batch_ref_5_budget_50_2024694_23.out
│   ├── batch_ref_5_budget_50_2024694_24.err
│   ├── batch_ref_5_budget_50_2024694_24.out
│   ├── batch_ref_5_budget_50_2024694_25.err
│   ├── batch_ref_5_budget_50_2024694_25.out
│   ├── batch_ref_5_budget_50_2024694_26.err
│   ├── batch_ref_5_budget_50_2024694_26.out
│   ├── batch_ref_5_budget_50_2024694_27.err
│   ├── batch_ref_5_budget_50_2024694_27.out
│   ├── batch_ref_5_budget_50_2024694_28.err
│   ├── batch_ref_5_budget_50_2024694_28.out
│   ├── batch_ref_5_budget_50_2024694_29.err
│   ├── batch_ref_5_budget_50_2024694_29.out
│   ├── batch_ref_5_budget_50_2024694_3.err
│   ├── batch_ref_5_budget_50_2024694_3.out
│   ├── batch_ref_5_budget_50_2024694_30.err
│   ├── batch_ref_5_budget_50_2024694_30.out
│   ├── batch_ref_5_budget_50_2024694_31.err
│   ├── batch_ref_5_budget_50_2024694_31.out
│   ├── batch_ref_5_budget_50_2024694_32.err
│   ├── batch_ref_5_budget_50_2024694_32.out
│   ├── batch_ref_5_budget_50_2024694_33.err
│   ├── batch_ref_5_budget_50_2024694_33.out
│   ├── batch_ref_5_budget_50_2024694_34.err
│   ├── batch_ref_5_budget_50_2024694_34.out
│   ├── batch_ref_5_budget_50_2024694_35.err
│   ├── batch_ref_5_budget_50_2024694_35.out
│   ├── batch_ref_5_budget_50_2024694_36.err
│   ├── batch_ref_5_budget_50_2024694_36.out
│   ├── batch_ref_5_budget_50_2024694_37.err
│   ├── batch_ref_5_budget_50_2024694_37.out
│   ├── batch_ref_5_budget_50_2024694_38.err
│   ├── batch_ref_5_budget_50_2024694_38.out
│   ├── batch_ref_5_budget_50_2024694_39.err
│   ├── batch_ref_5_budget_50_2024694_39.out
│   ├── batch_ref_5_budget_50_2024694_4.err
│   ├── batch_ref_5_budget_50_2024694_4.out
│   ├── batch_ref_5_budget_50_2024694_40.err
│   ├── batch_ref_5_budget_50_2024694_40.out
│   ├── batch_ref_5_budget_50_2024694_41.err
│   ├── batch_ref_5_budget_50_2024694_41.out
│   ├── batch_ref_5_budget_50_2024694_42.err
│   ├── batch_ref_5_budget_50_2024694_42.out
│   ├── batch_ref_5_budget_50_2024694_43.err
│   ├── batch_ref_5_budget_50_2024694_43.out
│   ├── batch_ref_5_budget_50_2024694_44.err
│   ├── batch_ref_5_budget_50_2024694_44.out
│   ├── batch_ref_5_budget_50_2024694_45.err
│   ├── batch_ref_5_budget_50_2024694_45.out
│   ├── batch_ref_5_budget_50_2024694_46.err
│   ├── batch_ref_5_budget_50_2024694_46.out
│   ├── batch_ref_5_budget_50_2024694_47.err
│   ├── batch_ref_5_budget_50_2024694_47.out
│   ├── batch_ref_5_budget_50_2024694_48.err
│   ├── batch_ref_5_budget_50_2024694_48.out
│   ├── batch_ref_5_budget_50_2024694_49.err
│   ├── batch_ref_5_budget_50_2024694_49.out
│   ├── batch_ref_5_budget_50_2024694_5.err
│   ├── batch_ref_5_budget_50_2024694_5.out
│   ├── batch_ref_5_budget_50_2024694_50.err
│   ├── batch_ref_5_budget_50_2024694_50.out
│   ├── batch_ref_5_budget_50_2024694_51.err
│   ├── batch_ref_5_budget_50_2024694_51.out
│   ├── batch_ref_5_budget_50_2024694_52.err
│   ├── batch_ref_5_budget_50_2024694_52.out
│   ├── batch_ref_5_budget_50_2024694_53.err
│   ├── batch_ref_5_budget_50_2024694_53.out
│   ├── batch_ref_5_budget_50_2024694_54.err
│   ├── batch_ref_5_budget_50_2024694_54.out
│   ├── batch_ref_5_budget_50_2024694_55.err
│   ├── batch_ref_5_budget_50_2024694_55.out
│   ├── batch_ref_5_budget_50_2024694_56.err
│   ├── batch_ref_5_budget_50_2024694_56.out
│   ├── batch_ref_5_budget_50_2024694_57.err
│   ├── batch_ref_5_budget_50_2024694_57.out
│   ├── batch_ref_5_budget_50_2024694_58.err
│   ├── batch_ref_5_budget_50_2024694_58.out
│   ├── batch_ref_5_budget_50_2024694_59.err
│   ├── batch_ref_5_budget_50_2024694_59.out
│   ├── batch_ref_5_budget_50_2024694_6.err
│   ├── batch_ref_5_budget_50_2024694_6.out
│   ├── batch_ref_5_budget_50_2024694_60.err
│   ├── batch_ref_5_budget_50_2024694_60.out
│   ├── batch_ref_5_budget_50_2024694_61.err
│   ├── batch_ref_5_budget_50_2024694_61.out
│   ├── batch_ref_5_budget_50_2024694_62.err
│   ├── batch_ref_5_budget_50_2024694_62.out
│   ├── batch_ref_5_budget_50_2024694_63.err
│   ├── batch_ref_5_budget_50_2024694_63.out
│   ├── batch_ref_5_budget_50_2024694_64.err
│   ├── batch_ref_5_budget_50_2024694_64.out
│   ├── batch_ref_5_budget_50_2024694_65.err
│   ├── batch_ref_5_budget_50_2024694_65.out
│   ├── batch_ref_5_budget_50_2024694_66.err
│   ├── batch_ref_5_budget_50_2024694_66.out
│   ├── batch_ref_5_budget_50_2024694_67.err
│   ├── batch_ref_5_budget_50_2024694_67.out
│   ├── batch_ref_5_budget_50_2024694_68.err
│   ├── batch_ref_5_budget_50_2024694_68.out
│   ├── batch_ref_5_budget_50_2024694_69.err
│   ├── batch_ref_5_budget_50_2024694_69.out
│   ├── batch_ref_5_budget_50_2024694_7.err
│   ├── batch_ref_5_budget_50_2024694_7.out
│   ├── batch_ref_5_budget_50_2024694_70.err
│   ├── batch_ref_5_budget_50_2024694_70.out
│   ├── batch_ref_5_budget_50_2024694_71.err
│   ├── batch_ref_5_budget_50_2024694_71.out
│   ├── batch_ref_5_budget_50_2024694_72.err
│   ├── batch_ref_5_budget_50_2024694_72.out
│   ├── batch_ref_5_budget_50_2024694_73.err
│   ├── batch_ref_5_budget_50_2024694_73.out
│   ├── batch_ref_5_budget_50_2024694_74.err
│   ├── batch_ref_5_budget_50_2024694_74.out
│   ├── batch_ref_5_budget_50_2024694_75.err
│   ├── batch_ref_5_budget_50_2024694_75.out
│   ├── batch_ref_5_budget_50_2024694_76.err
│   ├── batch_ref_5_budget_50_2024694_76.out
│   ├── batch_ref_5_budget_50_2024694_77.err
│   ├── batch_ref_5_budget_50_2024694_77.out
│   ├── batch_ref_5_budget_50_2024694_78.err
│   ├── batch_ref_5_budget_50_2024694_78.out
│   ├── batch_ref_5_budget_50_2024694_79.err
│   ├── batch_ref_5_budget_50_2024694_79.out
│   ├── batch_ref_5_budget_50_2024694_8.err
│   ├── batch_ref_5_budget_50_2024694_8.out
│   ├── batch_ref_5_budget_50_2024694_80.err
│   ├── batch_ref_5_budget_50_2024694_80.out
│   ├── batch_ref_5_budget_50_2024694_81.err
│   ├── batch_ref_5_budget_50_2024694_81.out
│   ├── batch_ref_5_budget_50_2024694_9.err
│   ├── batch_ref_5_budget_50_2024694_9.out
│   ├── batch_ref_5_budget_50_2040033_1.err
│   ├── batch_ref_5_budget_50_2040033_1.out
│   ├── batch_ref_5_budget_50_2040033_10.err
│   ├── batch_ref_5_budget_50_2040033_10.out
│   ├── batch_ref_5_budget_50_2040033_11.err
│   ├── batch_ref_5_budget_50_2040033_11.out
│   ├── batch_ref_5_budget_50_2040033_12.err
│   ├── batch_ref_5_budget_50_2040033_12.out
│   ├── batch_ref_5_budget_50_2040033_13.err
│   ├── batch_ref_5_budget_50_2040033_13.out
│   ├── batch_ref_5_budget_50_2040033_14.err
│   ├── batch_ref_5_budget_50_2040033_14.out
│   ├── batch_ref_5_budget_50_2040033_15.err
│   ├── batch_ref_5_budget_50_2040033_15.out
│   ├── batch_ref_5_budget_50_2040033_16.err
│   ├── batch_ref_5_budget_50_2040033_16.out
│   ├── batch_ref_5_budget_50_2040033_17.err
│   ├── batch_ref_5_budget_50_2040033_17.out
│   ├── batch_ref_5_budget_50_2040033_18.err
│   ├── batch_ref_5_budget_50_2040033_18.out
│   ├── batch_ref_5_budget_50_2040033_19.err
│   ├── batch_ref_5_budget_50_2040033_19.out
│   ├── batch_ref_5_budget_50_2040033_2.err
│   ├── batch_ref_5_budget_50_2040033_2.out
│   ├── batch_ref_5_budget_50_2040033_20.err
│   ├── batch_ref_5_budget_50_2040033_20.out
│   ├── batch_ref_5_budget_50_2040033_21.err
│   ├── batch_ref_5_budget_50_2040033_21.out
│   ├── batch_ref_5_budget_50_2040033_22.err
│   ├── batch_ref_5_budget_50_2040033_22.out
│   ├── batch_ref_5_budget_50_2040033_23.err
│   ├── batch_ref_5_budget_50_2040033_23.out
│   ├── batch_ref_5_budget_50_2040033_24.err
│   ├── batch_ref_5_budget_50_2040033_24.out
│   ├── batch_ref_5_budget_50_2040033_25.err
│   ├── batch_ref_5_budget_50_2040033_25.out
│   ├── batch_ref_5_budget_50_2040033_26.err
│   ├── batch_ref_5_budget_50_2040033_26.out
│   ├── batch_ref_5_budget_50_2040033_27.err
│   ├── batch_ref_5_budget_50_2040033_27.out
│   ├── batch_ref_5_budget_50_2040033_28.err
│   ├── batch_ref_5_budget_50_2040033_28.out
│   ├── batch_ref_5_budget_50_2040033_29.err
│   ├── batch_ref_5_budget_50_2040033_29.out
│   ├── batch_ref_5_budget_50_2040033_3.err
│   ├── batch_ref_5_budget_50_2040033_3.out
│   ├── batch_ref_5_budget_50_2040033_30.err
│   ├── batch_ref_5_budget_50_2040033_30.out
│   ├── batch_ref_5_budget_50_2040033_31.err
│   ├── batch_ref_5_budget_50_2040033_31.out
│   ├── batch_ref_5_budget_50_2040033_32.err
│   ├── batch_ref_5_budget_50_2040033_32.out
│   ├── batch_ref_5_budget_50_2040033_33.err
│   ├── batch_ref_5_budget_50_2040033_33.out
│   ├── batch_ref_5_budget_50_2040033_34.err
│   ├── batch_ref_5_budget_50_2040033_34.out
│   ├── batch_ref_5_budget_50_2040033_35.err
│   ├── batch_ref_5_budget_50_2040033_35.out
│   ├── batch_ref_5_budget_50_2040033_36.err
│   ├── batch_ref_5_budget_50_2040033_36.out
│   ├── batch_ref_5_budget_50_2040033_37.err
│   ├── batch_ref_5_budget_50_2040033_37.out
│   ├── batch_ref_5_budget_50_2040033_38.err
│   ├── batch_ref_5_budget_50_2040033_38.out
│   ├── batch_ref_5_budget_50_2040033_39.err
│   ├── batch_ref_5_budget_50_2040033_39.out
│   ├── batch_ref_5_budget_50_2040033_4.err
│   ├── batch_ref_5_budget_50_2040033_4.out
│   ├── batch_ref_5_budget_50_2040033_40.err
│   ├── batch_ref_5_budget_50_2040033_40.out
│   ├── batch_ref_5_budget_50_2040033_41.err
│   ├── batch_ref_5_budget_50_2040033_41.out
│   ├── batch_ref_5_budget_50_2040033_42.err
│   ├── batch_ref_5_budget_50_2040033_42.out
│   ├── batch_ref_5_budget_50_2040033_43.err
│   ├── batch_ref_5_budget_50_2040033_43.out
│   ├── batch_ref_5_budget_50_2040033_44.err
│   ├── batch_ref_5_budget_50_2040033_44.out
│   ├── batch_ref_5_budget_50_2040033_45.err
│   ├── batch_ref_5_budget_50_2040033_45.out
│   ├── batch_ref_5_budget_50_2040033_46.err
│   ├── batch_ref_5_budget_50_2040033_46.out
│   ├── batch_ref_5_budget_50_2040033_47.err
│   ├── batch_ref_5_budget_50_2040033_47.out
│   ├── batch_ref_5_budget_50_2040033_48.err
│   ├── batch_ref_5_budget_50_2040033_48.out
│   ├── batch_ref_5_budget_50_2040033_49.err
│   ├── batch_ref_5_budget_50_2040033_49.out
│   ├── batch_ref_5_budget_50_2040033_5.err
│   ├── batch_ref_5_budget_50_2040033_5.out
│   ├── batch_ref_5_budget_50_2040033_50.err
│   ├── batch_ref_5_budget_50_2040033_50.out
│   ├── batch_ref_5_budget_50_2040033_51.err
│   ├── batch_ref_5_budget_50_2040033_51.out
│   ├── batch_ref_5_budget_50_2040033_52.err
│   ├── batch_ref_5_budget_50_2040033_52.out
│   ├── batch_ref_5_budget_50_2040033_53.err
│   ├── batch_ref_5_budget_50_2040033_53.out
│   ├── batch_ref_5_budget_50_2040033_54.err
│   ├── batch_ref_5_budget_50_2040033_54.out
│   ├── batch_ref_5_budget_50_2040033_55.err
│   ├── batch_ref_5_budget_50_2040033_55.out
│   ├── batch_ref_5_budget_50_2040033_56.err
│   ├── batch_ref_5_budget_50_2040033_56.out
│   ├── batch_ref_5_budget_50_2040033_57.err
│   ├── batch_ref_5_budget_50_2040033_57.out
│   ├── batch_ref_5_budget_50_2040033_58.err
│   ├── batch_ref_5_budget_50_2040033_58.out
│   ├── batch_ref_5_budget_50_2040033_59.err
│   ├── batch_ref_5_budget_50_2040033_59.out
│   ├── batch_ref_5_budget_50_2040033_6.err
│   ├── batch_ref_5_budget_50_2040033_6.out
│   ├── batch_ref_5_budget_50_2040033_60.err
│   ├── batch_ref_5_budget_50_2040033_60.out
│   ├── batch_ref_5_budget_50_2040033_61.err
│   ├── batch_ref_5_budget_50_2040033_61.out
│   ├── batch_ref_5_budget_50_2040033_62.err
│   ├── batch_ref_5_budget_50_2040033_62.out
│   ├── batch_ref_5_budget_50_2040033_63.err
│   ├── batch_ref_5_budget_50_2040033_63.out
│   ├── batch_ref_5_budget_50_2040033_64.err
│   ├── batch_ref_5_budget_50_2040033_64.out
│   ├── batch_ref_5_budget_50_2040033_65.err
│   ├── batch_ref_5_budget_50_2040033_65.out
│   ├── batch_ref_5_budget_50_2040033_66.err
│   ├── batch_ref_5_budget_50_2040033_66.out
│   ├── batch_ref_5_budget_50_2040033_67.err
│   ├── batch_ref_5_budget_50_2040033_67.out
│   ├── batch_ref_5_budget_50_2040033_68.err
│   ├── batch_ref_5_budget_50_2040033_68.out
│   ├── batch_ref_5_budget_50_2040033_69.err
│   ├── batch_ref_5_budget_50_2040033_69.out
│   ├── batch_ref_5_budget_50_2040033_7.err
│   ├── batch_ref_5_budget_50_2040033_7.out
│   ├── batch_ref_5_budget_50_2040033_70.err
│   ├── batch_ref_5_budget_50_2040033_70.out
│   ├── batch_ref_5_budget_50_2040033_71.err
│   ├── batch_ref_5_budget_50_2040033_71.out
│   ├── batch_ref_5_budget_50_2040033_72.err
│   ├── batch_ref_5_budget_50_2040033_72.out
│   ├── batch_ref_5_budget_50_2040033_73.err
│   ├── batch_ref_5_budget_50_2040033_73.out
│   ├── batch_ref_5_budget_50_2040033_74.err
│   ├── batch_ref_5_budget_50_2040033_74.out
│   ├── batch_ref_5_budget_50_2040033_75.err
│   ├── batch_ref_5_budget_50_2040033_75.out
│   ├── batch_ref_5_budget_50_2040033_76.err
│   ├── batch_ref_5_budget_50_2040033_76.out
│   ├── batch_ref_5_budget_50_2040033_77.err
│   ├── batch_ref_5_budget_50_2040033_77.out
│   ├── batch_ref_5_budget_50_2040033_78.err
│   ├── batch_ref_5_budget_50_2040033_78.out
│   ├── batch_ref_5_budget_50_2040033_79.err
│   ├── batch_ref_5_budget_50_2040033_79.out
│   ├── batch_ref_5_budget_50_2040033_8.err
│   ├── batch_ref_5_budget_50_2040033_8.out
│   ├── batch_ref_5_budget_50_2040033_80.err
│   ├── batch_ref_5_budget_50_2040033_80.out
│   ├── batch_ref_5_budget_50_2040033_81.err
│   ├── batch_ref_5_budget_50_2040033_81.out
│   ├── batch_ref_5_budget_50_2040033_9.err
│   ├── batch_ref_5_budget_50_2040033_9.out
│   ├── batch_ref_5_budget_50_max_5_2067290_1.err
│   ├── batch_ref_5_budget_50_max_5_2067290_1.out
│   ├── batch_ref_5_budget_50_max_5_2067290_10.err
│   ├── batch_ref_5_budget_50_max_5_2067290_10.out
│   ├── batch_ref_5_budget_50_max_5_2067290_11.err
│   ├── batch_ref_5_budget_50_max_5_2067290_11.out
│   ├── batch_ref_5_budget_50_max_5_2067290_12.err
│   ├── batch_ref_5_budget_50_max_5_2067290_12.out
│   ├── batch_ref_5_budget_50_max_5_2067290_13.err
│   ├── batch_ref_5_budget_50_max_5_2067290_13.out
│   ├── batch_ref_5_budget_50_max_5_2067290_14.err
│   ├── batch_ref_5_budget_50_max_5_2067290_14.out
│   ├── batch_ref_5_budget_50_max_5_2067290_15.err
│   ├── batch_ref_5_budget_50_max_5_2067290_15.out
│   ├── batch_ref_5_budget_50_max_5_2067290_16.err
│   ├── batch_ref_5_budget_50_max_5_2067290_16.out
│   ├── batch_ref_5_budget_50_max_5_2067290_17.err
│   ├── batch_ref_5_budget_50_max_5_2067290_17.out
│   ├── batch_ref_5_budget_50_max_5_2067290_18.err
│   ├── batch_ref_5_budget_50_max_5_2067290_18.out
│   ├── batch_ref_5_budget_50_max_5_2067290_19.err
│   ├── batch_ref_5_budget_50_max_5_2067290_19.out
│   ├── batch_ref_5_budget_50_max_5_2067290_2.err
│   ├── batch_ref_5_budget_50_max_5_2067290_2.out
│   ├── batch_ref_5_budget_50_max_5_2067290_20.err
│   ├── batch_ref_5_budget_50_max_5_2067290_20.out
│   ├── batch_ref_5_budget_50_max_5_2067290_21.err
│   ├── batch_ref_5_budget_50_max_5_2067290_21.out
│   ├── batch_ref_5_budget_50_max_5_2067290_22.err
│   ├── batch_ref_5_budget_50_max_5_2067290_22.out
│   ├── batch_ref_5_budget_50_max_5_2067290_23.err
│   ├── batch_ref_5_budget_50_max_5_2067290_23.out
│   ├── batch_ref_5_budget_50_max_5_2067290_24.err
│   ├── batch_ref_5_budget_50_max_5_2067290_24.out
│   ├── batch_ref_5_budget_50_max_5_2067290_25.err
│   ├── batch_ref_5_budget_50_max_5_2067290_25.out
│   ├── batch_ref_5_budget_50_max_5_2067290_26.err
│   ├── batch_ref_5_budget_50_max_5_2067290_26.out
│   ├── batch_ref_5_budget_50_max_5_2067290_27.err
│   ├── batch_ref_5_budget_50_max_5_2067290_27.out
│   ├── batch_ref_5_budget_50_max_5_2067290_28.err
│   ├── batch_ref_5_budget_50_max_5_2067290_28.out
│   ├── batch_ref_5_budget_50_max_5_2067290_29.err
│   ├── batch_ref_5_budget_50_max_5_2067290_29.out
│   ├── batch_ref_5_budget_50_max_5_2067290_3.err
│   ├── batch_ref_5_budget_50_max_5_2067290_3.out
│   ├── batch_ref_5_budget_50_max_5_2067290_30.err
│   ├── batch_ref_5_budget_50_max_5_2067290_30.out
│   ├── batch_ref_5_budget_50_max_5_2067290_31.err
│   ├── batch_ref_5_budget_50_max_5_2067290_31.out
│   ├── batch_ref_5_budget_50_max_5_2067290_32.err
│   ├── batch_ref_5_budget_50_max_5_2067290_32.out
│   ├── batch_ref_5_budget_50_max_5_2067290_33.err
│   ├── batch_ref_5_budget_50_max_5_2067290_33.out
│   ├── batch_ref_5_budget_50_max_5_2067290_34.err
│   ├── batch_ref_5_budget_50_max_5_2067290_34.out
│   ├── batch_ref_5_budget_50_max_5_2067290_35.err
│   ├── batch_ref_5_budget_50_max_5_2067290_35.out
│   ├── batch_ref_5_budget_50_max_5_2067290_36.err
│   ├── batch_ref_5_budget_50_max_5_2067290_36.out
│   ├── batch_ref_5_budget_50_max_5_2067290_37.err
│   ├── batch_ref_5_budget_50_max_5_2067290_37.out
│   ├── batch_ref_5_budget_50_max_5_2067290_38.err
│   ├── batch_ref_5_budget_50_max_5_2067290_38.out
│   ├── batch_ref_5_budget_50_max_5_2067290_39.err
│   ├── batch_ref_5_budget_50_max_5_2067290_39.out
│   ├── batch_ref_5_budget_50_max_5_2067290_4.err
│   ├── batch_ref_5_budget_50_max_5_2067290_4.out
│   ├── batch_ref_5_budget_50_max_5_2067290_40.err
│   ├── batch_ref_5_budget_50_max_5_2067290_40.out
│   ├── batch_ref_5_budget_50_max_5_2067290_41.err
│   ├── batch_ref_5_budget_50_max_5_2067290_41.out
│   ├── batch_ref_5_budget_50_max_5_2067290_42.err
│   ├── batch_ref_5_budget_50_max_5_2067290_42.out
│   ├── batch_ref_5_budget_50_max_5_2067290_43.err
│   ├── batch_ref_5_budget_50_max_5_2067290_43.out
│   ├── batch_ref_5_budget_50_max_5_2067290_44.err
│   ├── batch_ref_5_budget_50_max_5_2067290_44.out
│   ├── batch_ref_5_budget_50_max_5_2067290_45.err
│   ├── batch_ref_5_budget_50_max_5_2067290_45.out
│   ├── batch_ref_5_budget_50_max_5_2067290_46.err
│   ├── batch_ref_5_budget_50_max_5_2067290_46.out
│   ├── batch_ref_5_budget_50_max_5_2067290_47.err
│   ├── batch_ref_5_budget_50_max_5_2067290_47.out
│   ├── batch_ref_5_budget_50_max_5_2067290_48.err
│   ├── batch_ref_5_budget_50_max_5_2067290_48.out
│   ├── batch_ref_5_budget_50_max_5_2067290_49.err
│   ├── batch_ref_5_budget_50_max_5_2067290_49.out
│   ├── batch_ref_5_budget_50_max_5_2067290_5.err
│   ├── batch_ref_5_budget_50_max_5_2067290_5.out
│   ├── batch_ref_5_budget_50_max_5_2067290_50.err
│   ├── batch_ref_5_budget_50_max_5_2067290_50.out
│   ├── batch_ref_5_budget_50_max_5_2067290_51.err
│   ├── batch_ref_5_budget_50_max_5_2067290_51.out
│   ├── batch_ref_5_budget_50_max_5_2067290_52.err
│   ├── batch_ref_5_budget_50_max_5_2067290_52.out
│   ├── batch_ref_5_budget_50_max_5_2067290_53.err
│   ├── batch_ref_5_budget_50_max_5_2067290_53.out
│   ├── batch_ref_5_budget_50_max_5_2067290_54.err
│   ├── batch_ref_5_budget_50_max_5_2067290_54.out
│   ├── batch_ref_5_budget_50_max_5_2067290_55.err
│   ├── batch_ref_5_budget_50_max_5_2067290_55.out
│   ├── batch_ref_5_budget_50_max_5_2067290_56.err
│   ├── batch_ref_5_budget_50_max_5_2067290_56.out
│   ├── batch_ref_5_budget_50_max_5_2067290_57.err
│   ├── batch_ref_5_budget_50_max_5_2067290_57.out
│   ├── batch_ref_5_budget_50_max_5_2067290_58.err
│   ├── batch_ref_5_budget_50_max_5_2067290_58.out
│   ├── batch_ref_5_budget_50_max_5_2067290_59.err
│   ├── batch_ref_5_budget_50_max_5_2067290_59.out
│   ├── batch_ref_5_budget_50_max_5_2067290_6.err
│   ├── batch_ref_5_budget_50_max_5_2067290_6.out
│   ├── batch_ref_5_budget_50_max_5_2067290_60.err
│   ├── batch_ref_5_budget_50_max_5_2067290_60.out
│   ├── batch_ref_5_budget_50_max_5_2067290_61.err
│   ├── batch_ref_5_budget_50_max_5_2067290_61.out
│   ├── batch_ref_5_budget_50_max_5_2067290_62.err
│   ├── batch_ref_5_budget_50_max_5_2067290_62.out
│   ├── batch_ref_5_budget_50_max_5_2067290_63.err
│   ├── batch_ref_5_budget_50_max_5_2067290_63.out
│   ├── batch_ref_5_budget_50_max_5_2067290_64.err
│   ├── batch_ref_5_budget_50_max_5_2067290_64.out
│   ├── batch_ref_5_budget_50_max_5_2067290_65.err
│   ├── batch_ref_5_budget_50_max_5_2067290_65.out
│   ├── batch_ref_5_budget_50_max_5_2067290_66.err
│   ├── batch_ref_5_budget_50_max_5_2067290_66.out
│   ├── batch_ref_5_budget_50_max_5_2067290_67.err
│   ├── batch_ref_5_budget_50_max_5_2067290_67.out
│   ├── batch_ref_5_budget_50_max_5_2067290_68.err
│   ├── batch_ref_5_budget_50_max_5_2067290_68.out
│   ├── batch_ref_5_budget_50_max_5_2067290_69.err
│   ├── batch_ref_5_budget_50_max_5_2067290_69.out
│   ├── batch_ref_5_budget_50_max_5_2067290_7.err
│   ├── batch_ref_5_budget_50_max_5_2067290_7.out
│   ├── batch_ref_5_budget_50_max_5_2067290_70.err
│   ├── batch_ref_5_budget_50_max_5_2067290_70.out
│   ├── batch_ref_5_budget_50_max_5_2067290_71.err
│   ├── batch_ref_5_budget_50_max_5_2067290_71.out
│   ├── batch_ref_5_budget_50_max_5_2067290_72.err
│   ├── batch_ref_5_budget_50_max_5_2067290_72.out
│   ├── batch_ref_5_budget_50_max_5_2067290_73.err
│   ├── batch_ref_5_budget_50_max_5_2067290_73.out
│   ├── batch_ref_5_budget_50_max_5_2067290_74.err
│   ├── batch_ref_5_budget_50_max_5_2067290_74.out
│   ├── batch_ref_5_budget_50_max_5_2067290_75.err
│   ├── batch_ref_5_budget_50_max_5_2067290_75.out
│   ├── batch_ref_5_budget_50_max_5_2067290_76.err
│   ├── batch_ref_5_budget_50_max_5_2067290_76.out
│   ├── batch_ref_5_budget_50_max_5_2067290_77.err
│   ├── batch_ref_5_budget_50_max_5_2067290_77.out
│   ├── batch_ref_5_budget_50_max_5_2067290_78.err
│   ├── batch_ref_5_budget_50_max_5_2067290_78.out
│   ├── batch_ref_5_budget_50_max_5_2067290_79.err
│   ├── batch_ref_5_budget_50_max_5_2067290_79.out
│   ├── batch_ref_5_budget_50_max_5_2067290_8.err
│   ├── batch_ref_5_budget_50_max_5_2067290_8.out
│   ├── batch_ref_5_budget_50_max_5_2067290_80.err
│   ├── batch_ref_5_budget_50_max_5_2067290_80.out
│   ├── batch_ref_5_budget_50_max_5_2067290_81.err
│   ├── batch_ref_5_budget_50_max_5_2067290_81.out
│   ├── batch_ref_5_budget_50_max_5_2067290_9.err
│   ├── batch_ref_5_budget_50_max_5_2067290_9.out
│   ├── batch_ref_5_budget_60_2040034_1.err
│   ├── batch_ref_5_budget_60_2040034_1.out
│   ├── batch_ref_5_budget_60_2040034_10.err
│   ├── batch_ref_5_budget_60_2040034_10.out
│   ├── batch_ref_5_budget_60_2040034_11.err
│   ├── batch_ref_5_budget_60_2040034_11.out
│   ├── batch_ref_5_budget_60_2040034_12.err
│   ├── batch_ref_5_budget_60_2040034_12.out
│   ├── batch_ref_5_budget_60_2040034_13.err
│   ├── batch_ref_5_budget_60_2040034_13.out
│   ├── batch_ref_5_budget_60_2040034_14.err
│   ├── batch_ref_5_budget_60_2040034_14.out
│   ├── batch_ref_5_budget_60_2040034_15.err
│   ├── batch_ref_5_budget_60_2040034_15.out
│   ├── batch_ref_5_budget_60_2040034_16.err
│   ├── batch_ref_5_budget_60_2040034_16.out
│   ├── batch_ref_5_budget_60_2040034_17.err
│   ├── batch_ref_5_budget_60_2040034_17.out
│   ├── batch_ref_5_budget_60_2040034_18.err
│   ├── batch_ref_5_budget_60_2040034_18.out
│   ├── batch_ref_5_budget_60_2040034_19.err
│   ├── batch_ref_5_budget_60_2040034_19.out
│   ├── batch_ref_5_budget_60_2040034_2.err
│   ├── batch_ref_5_budget_60_2040034_2.out
│   ├── batch_ref_5_budget_60_2040034_20.err
│   ├── batch_ref_5_budget_60_2040034_20.out
│   ├── batch_ref_5_budget_60_2040034_21.err
│   ├── batch_ref_5_budget_60_2040034_21.out
│   ├── batch_ref_5_budget_60_2040034_22.err
│   ├── batch_ref_5_budget_60_2040034_22.out
│   ├── batch_ref_5_budget_60_2040034_23.err
│   ├── batch_ref_5_budget_60_2040034_23.out
│   ├── batch_ref_5_budget_60_2040034_24.err
│   ├── batch_ref_5_budget_60_2040034_24.out
│   ├── batch_ref_5_budget_60_2040034_25.err
│   ├── batch_ref_5_budget_60_2040034_25.out
│   ├── batch_ref_5_budget_60_2040034_26.err
│   ├── batch_ref_5_budget_60_2040034_26.out
│   ├── batch_ref_5_budget_60_2040034_27.err
│   ├── batch_ref_5_budget_60_2040034_27.out
│   ├── batch_ref_5_budget_60_2040034_28.err
│   ├── batch_ref_5_budget_60_2040034_28.out
│   ├── batch_ref_5_budget_60_2040034_29.err
│   ├── batch_ref_5_budget_60_2040034_29.out
│   ├── batch_ref_5_budget_60_2040034_3.err
│   ├── batch_ref_5_budget_60_2040034_3.out
│   ├── batch_ref_5_budget_60_2040034_30.err
│   ├── batch_ref_5_budget_60_2040034_30.out
│   ├── batch_ref_5_budget_60_2040034_31.err
│   ├── batch_ref_5_budget_60_2040034_31.out
│   ├── batch_ref_5_budget_60_2040034_32.err
│   ├── batch_ref_5_budget_60_2040034_32.out
│   ├── batch_ref_5_budget_60_2040034_33.err
│   ├── batch_ref_5_budget_60_2040034_33.out
│   ├── batch_ref_5_budget_60_2040034_34.err
│   ├── batch_ref_5_budget_60_2040034_34.out
│   ├── batch_ref_5_budget_60_2040034_35.err
│   ├── batch_ref_5_budget_60_2040034_35.out
│   ├── batch_ref_5_budget_60_2040034_36.err
│   ├── batch_ref_5_budget_60_2040034_36.out
│   ├── batch_ref_5_budget_60_2040034_37.err
│   ├── batch_ref_5_budget_60_2040034_37.out
│   ├── batch_ref_5_budget_60_2040034_38.err
│   ├── batch_ref_5_budget_60_2040034_38.out
│   ├── batch_ref_5_budget_60_2040034_39.err
│   ├── batch_ref_5_budget_60_2040034_39.out
│   ├── batch_ref_5_budget_60_2040034_4.err
│   ├── batch_ref_5_budget_60_2040034_4.out
│   ├── batch_ref_5_budget_60_2040034_40.err
│   ├── batch_ref_5_budget_60_2040034_40.out
│   ├── batch_ref_5_budget_60_2040034_41.err
│   ├── batch_ref_5_budget_60_2040034_41.out
│   ├── batch_ref_5_budget_60_2040034_42.err
│   ├── batch_ref_5_budget_60_2040034_42.out
│   ├── batch_ref_5_budget_60_2040034_43.err
│   ├── batch_ref_5_budget_60_2040034_43.out
│   ├── batch_ref_5_budget_60_2040034_44.err
│   ├── batch_ref_5_budget_60_2040034_44.out
│   ├── batch_ref_5_budget_60_2040034_45.err
│   ├── batch_ref_5_budget_60_2040034_45.out
│   ├── batch_ref_5_budget_60_2040034_46.err
│   ├── batch_ref_5_budget_60_2040034_46.out
│   ├── batch_ref_5_budget_60_2040034_47.err
│   ├── batch_ref_5_budget_60_2040034_47.out
│   ├── batch_ref_5_budget_60_2040034_48.err
│   ├── batch_ref_5_budget_60_2040034_48.out
│   ├── batch_ref_5_budget_60_2040034_49.err
│   ├── batch_ref_5_budget_60_2040034_49.out
│   ├── batch_ref_5_budget_60_2040034_5.err
│   ├── batch_ref_5_budget_60_2040034_5.out
│   ├── batch_ref_5_budget_60_2040034_50.err
│   ├── batch_ref_5_budget_60_2040034_50.out
│   ├── batch_ref_5_budget_60_2040034_51.err
│   ├── batch_ref_5_budget_60_2040034_51.out
│   ├── batch_ref_5_budget_60_2040034_52.err
│   ├── batch_ref_5_budget_60_2040034_52.out
│   ├── batch_ref_5_budget_60_2040034_53.err
│   ├── batch_ref_5_budget_60_2040034_53.out
│   ├── batch_ref_5_budget_60_2040034_54.err
│   ├── batch_ref_5_budget_60_2040034_54.out
│   ├── batch_ref_5_budget_60_2040034_55.err
│   ├── batch_ref_5_budget_60_2040034_55.out
│   ├── batch_ref_5_budget_60_2040034_56.err
│   ├── batch_ref_5_budget_60_2040034_56.out
│   ├── batch_ref_5_budget_60_2040034_57.err
│   ├── batch_ref_5_budget_60_2040034_57.out
│   ├── batch_ref_5_budget_60_2040034_58.err
│   ├── batch_ref_5_budget_60_2040034_58.out
│   ├── batch_ref_5_budget_60_2040034_59.err
│   ├── batch_ref_5_budget_60_2040034_59.out
│   ├── batch_ref_5_budget_60_2040034_6.err
│   ├── batch_ref_5_budget_60_2040034_6.out
│   ├── batch_ref_5_budget_60_2040034_60.err
│   ├── batch_ref_5_budget_60_2040034_60.out
│   ├── batch_ref_5_budget_60_2040034_61.err
│   ├── batch_ref_5_budget_60_2040034_61.out
│   ├── batch_ref_5_budget_60_2040034_62.err
│   ├── batch_ref_5_budget_60_2040034_62.out
│   ├── batch_ref_5_budget_60_2040034_63.err
│   ├── batch_ref_5_budget_60_2040034_63.out
│   ├── batch_ref_5_budget_60_2040034_64.err
│   ├── batch_ref_5_budget_60_2040034_64.out
│   ├── batch_ref_5_budget_60_2040034_65.err
│   ├── batch_ref_5_budget_60_2040034_65.out
│   ├── batch_ref_5_budget_60_2040034_66.err
│   ├── batch_ref_5_budget_60_2040034_66.out
│   ├── batch_ref_5_budget_60_2040034_67.err
│   ├── batch_ref_5_budget_60_2040034_67.out
│   ├── batch_ref_5_budget_60_2040034_68.err
│   ├── batch_ref_5_budget_60_2040034_68.out
│   ├── batch_ref_5_budget_60_2040034_69.err
│   ├── batch_ref_5_budget_60_2040034_69.out
│   ├── batch_ref_5_budget_60_2040034_7.err
│   ├── batch_ref_5_budget_60_2040034_7.out
│   ├── batch_ref_5_budget_60_2040034_70.err
│   ├── batch_ref_5_budget_60_2040034_70.out
│   ├── batch_ref_5_budget_60_2040034_71.err
│   ├── batch_ref_5_budget_60_2040034_71.out
│   ├── batch_ref_5_budget_60_2040034_72.err
│   ├── batch_ref_5_budget_60_2040034_72.out
│   ├── batch_ref_5_budget_60_2040034_73.err
│   ├── batch_ref_5_budget_60_2040034_73.out
│   ├── batch_ref_5_budget_60_2040034_74.err
│   ├── batch_ref_5_budget_60_2040034_74.out
│   ├── batch_ref_5_budget_60_2040034_75.err
│   ├── batch_ref_5_budget_60_2040034_75.out
│   ├── batch_ref_5_budget_60_2040034_76.err
│   ├── batch_ref_5_budget_60_2040034_76.out
│   ├── batch_ref_5_budget_60_2040034_77.err
│   ├── batch_ref_5_budget_60_2040034_77.out
│   ├── batch_ref_5_budget_60_2040034_78.err
│   ├── batch_ref_5_budget_60_2040034_78.out
│   ├── batch_ref_5_budget_60_2040034_79.err
│   ├── batch_ref_5_budget_60_2040034_79.out
│   ├── batch_ref_5_budget_60_2040034_8.err
│   ├── batch_ref_5_budget_60_2040034_8.out
│   ├── batch_ref_5_budget_60_2040034_80.err
│   ├── batch_ref_5_budget_60_2040034_80.out
│   ├── batch_ref_5_budget_60_2040034_81.err
│   ├── batch_ref_5_budget_60_2040034_81.out
│   ├── batch_ref_5_budget_60_2040034_9.err
│   ├── batch_ref_5_budget_60_2040034_9.out
│   ├── batch_ref_5_budget_70_2040035_1.err
│   ├── batch_ref_5_budget_70_2040035_1.out
│   ├── batch_ref_5_budget_70_2040035_10.err
│   ├── batch_ref_5_budget_70_2040035_10.out
│   ├── batch_ref_5_budget_70_2040035_11.err
│   ├── batch_ref_5_budget_70_2040035_11.out
│   ├── batch_ref_5_budget_70_2040035_12.err
│   ├── batch_ref_5_budget_70_2040035_12.out
│   ├── batch_ref_5_budget_70_2040035_13.err
│   ├── batch_ref_5_budget_70_2040035_13.out
│   ├── batch_ref_5_budget_70_2040035_14.err
│   ├── batch_ref_5_budget_70_2040035_14.out
│   ├── batch_ref_5_budget_70_2040035_15.err
│   ├── batch_ref_5_budget_70_2040035_15.out
│   ├── batch_ref_5_budget_70_2040035_16.err
│   ├── batch_ref_5_budget_70_2040035_16.out
│   ├── batch_ref_5_budget_70_2040035_17.err
│   ├── batch_ref_5_budget_70_2040035_17.out
│   ├── batch_ref_5_budget_70_2040035_18.err
│   ├── batch_ref_5_budget_70_2040035_18.out
│   ├── batch_ref_5_budget_70_2040035_19.err
│   ├── batch_ref_5_budget_70_2040035_19.out
│   ├── batch_ref_5_budget_70_2040035_2.err
│   ├── batch_ref_5_budget_70_2040035_2.out
│   ├── batch_ref_5_budget_70_2040035_20.err
│   ├── batch_ref_5_budget_70_2040035_20.out
│   ├── batch_ref_5_budget_70_2040035_21.err
│   ├── batch_ref_5_budget_70_2040035_21.out
│   ├── batch_ref_5_budget_70_2040035_22.err
│   ├── batch_ref_5_budget_70_2040035_22.out
│   ├── batch_ref_5_budget_70_2040035_23.err
│   ├── batch_ref_5_budget_70_2040035_23.out
│   ├── batch_ref_5_budget_70_2040035_24.err
│   ├── batch_ref_5_budget_70_2040035_24.out
│   ├── batch_ref_5_budget_70_2040035_25.err
│   ├── batch_ref_5_budget_70_2040035_25.out
│   ├── batch_ref_5_budget_70_2040035_26.err
│   ├── batch_ref_5_budget_70_2040035_26.out
│   ├── batch_ref_5_budget_70_2040035_27.err
│   ├── batch_ref_5_budget_70_2040035_27.out
│   ├── batch_ref_5_budget_70_2040035_28.err
│   ├── batch_ref_5_budget_70_2040035_28.out
│   ├── batch_ref_5_budget_70_2040035_29.err
│   ├── batch_ref_5_budget_70_2040035_29.out
│   ├── batch_ref_5_budget_70_2040035_3.err
│   ├── batch_ref_5_budget_70_2040035_3.out
│   ├── batch_ref_5_budget_70_2040035_30.err
│   ├── batch_ref_5_budget_70_2040035_30.out
│   ├── batch_ref_5_budget_70_2040035_31.err
│   ├── batch_ref_5_budget_70_2040035_31.out
│   ├── batch_ref_5_budget_70_2040035_32.err
│   ├── batch_ref_5_budget_70_2040035_32.out
│   ├── batch_ref_5_budget_70_2040035_33.err
│   ├── batch_ref_5_budget_70_2040035_33.out
│   ├── batch_ref_5_budget_70_2040035_34.err
│   ├── batch_ref_5_budget_70_2040035_34.out
│   ├── batch_ref_5_budget_70_2040035_35.err
│   ├── batch_ref_5_budget_70_2040035_35.out
│   ├── batch_ref_5_budget_70_2040035_36.err
│   ├── batch_ref_5_budget_70_2040035_36.out
│   ├── batch_ref_5_budget_70_2040035_37.err
│   ├── batch_ref_5_budget_70_2040035_37.out
│   ├── batch_ref_5_budget_70_2040035_38.err
│   ├── batch_ref_5_budget_70_2040035_38.out
│   ├── batch_ref_5_budget_70_2040035_39.err
│   ├── batch_ref_5_budget_70_2040035_39.out
│   ├── batch_ref_5_budget_70_2040035_4.err
│   ├── batch_ref_5_budget_70_2040035_4.out
│   ├── batch_ref_5_budget_70_2040035_40.err
│   ├── batch_ref_5_budget_70_2040035_40.out
│   ├── batch_ref_5_budget_70_2040035_41.err
│   ├── batch_ref_5_budget_70_2040035_41.out
│   ├── batch_ref_5_budget_70_2040035_42.err
│   ├── batch_ref_5_budget_70_2040035_42.out
│   ├── batch_ref_5_budget_70_2040035_43.err
│   ├── batch_ref_5_budget_70_2040035_43.out
│   ├── batch_ref_5_budget_70_2040035_44.err
│   ├── batch_ref_5_budget_70_2040035_44.out
│   ├── batch_ref_5_budget_70_2040035_45.err
│   ├── batch_ref_5_budget_70_2040035_45.out
│   ├── batch_ref_5_budget_70_2040035_46.err
│   ├── batch_ref_5_budget_70_2040035_46.out
│   ├── batch_ref_5_budget_70_2040035_47.err
│   ├── batch_ref_5_budget_70_2040035_47.out
│   ├── batch_ref_5_budget_70_2040035_48.err
│   ├── batch_ref_5_budget_70_2040035_48.out
│   ├── batch_ref_5_budget_70_2040035_49.err
│   ├── batch_ref_5_budget_70_2040035_49.out
│   ├── batch_ref_5_budget_70_2040035_5.err
│   ├── batch_ref_5_budget_70_2040035_5.out
│   ├── batch_ref_5_budget_70_2040035_50.err
│   ├── batch_ref_5_budget_70_2040035_50.out
│   ├── batch_ref_5_budget_70_2040035_51.err
│   ├── batch_ref_5_budget_70_2040035_51.out
│   ├── batch_ref_5_budget_70_2040035_52.err
│   ├── batch_ref_5_budget_70_2040035_52.out
│   ├── batch_ref_5_budget_70_2040035_53.err
│   ├── batch_ref_5_budget_70_2040035_53.out
│   ├── batch_ref_5_budget_70_2040035_54.err
│   ├── batch_ref_5_budget_70_2040035_54.out
│   ├── batch_ref_5_budget_70_2040035_55.err
│   ├── batch_ref_5_budget_70_2040035_55.out
│   ├── batch_ref_5_budget_70_2040035_56.err
│   ├── batch_ref_5_budget_70_2040035_56.out
│   ├── batch_ref_5_budget_70_2040035_57.err
│   ├── batch_ref_5_budget_70_2040035_57.out
│   ├── batch_ref_5_budget_70_2040035_58.err
│   ├── batch_ref_5_budget_70_2040035_58.out
│   ├── batch_ref_5_budget_70_2040035_59.err
│   ├── batch_ref_5_budget_70_2040035_59.out
│   ├── batch_ref_5_budget_70_2040035_6.err
│   ├── batch_ref_5_budget_70_2040035_6.out
│   ├── batch_ref_5_budget_70_2040035_60.err
│   ├── batch_ref_5_budget_70_2040035_60.out
│   ├── batch_ref_5_budget_70_2040035_61.err
│   ├── batch_ref_5_budget_70_2040035_61.out
│   ├── batch_ref_5_budget_70_2040035_62.err
│   ├── batch_ref_5_budget_70_2040035_62.out
│   ├── batch_ref_5_budget_70_2040035_63.err
│   ├── batch_ref_5_budget_70_2040035_63.out
│   ├── batch_ref_5_budget_70_2040035_64.err
│   ├── batch_ref_5_budget_70_2040035_64.out
│   ├── batch_ref_5_budget_70_2040035_65.err
│   ├── batch_ref_5_budget_70_2040035_65.out
│   ├── batch_ref_5_budget_70_2040035_66.err
│   ├── batch_ref_5_budget_70_2040035_66.out
│   ├── batch_ref_5_budget_70_2040035_67.err
│   ├── batch_ref_5_budget_70_2040035_67.out
│   ├── batch_ref_5_budget_70_2040035_68.err
│   ├── batch_ref_5_budget_70_2040035_68.out
│   ├── batch_ref_5_budget_70_2040035_69.err
│   ├── batch_ref_5_budget_70_2040035_69.out
│   ├── batch_ref_5_budget_70_2040035_7.err
│   ├── batch_ref_5_budget_70_2040035_7.out
│   ├── batch_ref_5_budget_70_2040035_70.err
│   ├── batch_ref_5_budget_70_2040035_70.out
│   ├── batch_ref_5_budget_70_2040035_71.err
│   ├── batch_ref_5_budget_70_2040035_71.out
│   ├── batch_ref_5_budget_70_2040035_72.err
│   ├── batch_ref_5_budget_70_2040035_72.out
│   ├── batch_ref_5_budget_70_2040035_73.err
│   ├── batch_ref_5_budget_70_2040035_73.out
│   ├── batch_ref_5_budget_70_2040035_74.err
│   ├── batch_ref_5_budget_70_2040035_74.out
│   ├── batch_ref_5_budget_70_2040035_75.err
│   ├── batch_ref_5_budget_70_2040035_75.out
│   ├── batch_ref_5_budget_70_2040035_76.err
│   ├── batch_ref_5_budget_70_2040035_76.out
│   ├── batch_ref_5_budget_70_2040035_77.err
│   ├── batch_ref_5_budget_70_2040035_77.out
│   ├── batch_ref_5_budget_70_2040035_78.err
│   ├── batch_ref_5_budget_70_2040035_78.out
│   ├── batch_ref_5_budget_70_2040035_79.err
│   ├── batch_ref_5_budget_70_2040035_79.out
│   ├── batch_ref_5_budget_70_2040035_8.err
│   ├── batch_ref_5_budget_70_2040035_8.out
│   ├── batch_ref_5_budget_70_2040035_80.err
│   ├── batch_ref_5_budget_70_2040035_80.out
│   ├── batch_ref_5_budget_70_2040035_81.err
│   ├── batch_ref_5_budget_70_2040035_81.out
│   ├── batch_ref_5_budget_70_2040035_9.err
│   ├── batch_ref_5_budget_70_2040035_9.out
│   ├── batch_ref_5_budget_80_2038357_1.err
│   ├── batch_ref_5_budget_80_2038357_1.out
│   ├── batch_ref_5_budget_80_2038357_10.err
│   ├── batch_ref_5_budget_80_2038357_10.out
│   ├── batch_ref_5_budget_80_2038357_11.err
│   ├── batch_ref_5_budget_80_2038357_11.out
│   ├── batch_ref_5_budget_80_2038357_12.err
│   ├── batch_ref_5_budget_80_2038357_12.out
│   ├── batch_ref_5_budget_80_2038357_13.err
│   ├── batch_ref_5_budget_80_2038357_13.out
│   ├── batch_ref_5_budget_80_2038357_14.err
│   ├── batch_ref_5_budget_80_2038357_14.out
│   ├── batch_ref_5_budget_80_2038357_15.err
│   ├── batch_ref_5_budget_80_2038357_15.out
│   ├── batch_ref_5_budget_80_2038357_16.err
│   ├── batch_ref_5_budget_80_2038357_16.out
│   ├── batch_ref_5_budget_80_2038357_17.err
│   ├── batch_ref_5_budget_80_2038357_17.out
│   ├── batch_ref_5_budget_80_2038357_18.err
│   ├── batch_ref_5_budget_80_2038357_18.out
│   ├── batch_ref_5_budget_80_2038357_19.err
│   ├── batch_ref_5_budget_80_2038357_19.out
│   ├── batch_ref_5_budget_80_2038357_2.err
│   ├── batch_ref_5_budget_80_2038357_2.out
│   ├── batch_ref_5_budget_80_2038357_20.err
│   ├── batch_ref_5_budget_80_2038357_20.out
│   ├── batch_ref_5_budget_80_2038357_21.err
│   ├── batch_ref_5_budget_80_2038357_21.out
│   ├── batch_ref_5_budget_80_2038357_22.err
│   ├── batch_ref_5_budget_80_2038357_22.out
│   ├── batch_ref_5_budget_80_2038357_23.err
│   ├── batch_ref_5_budget_80_2038357_23.out
│   ├── batch_ref_5_budget_80_2038357_24.err
│   ├── batch_ref_5_budget_80_2038357_24.out
│   ├── batch_ref_5_budget_80_2038357_25.err
│   ├── batch_ref_5_budget_80_2038357_25.out
│   ├── batch_ref_5_budget_80_2038357_26.err
│   ├── batch_ref_5_budget_80_2038357_26.out
│   ├── batch_ref_5_budget_80_2038357_27.err
│   ├── batch_ref_5_budget_80_2038357_27.out
│   ├── batch_ref_5_budget_80_2038357_28.err
│   ├── batch_ref_5_budget_80_2038357_28.out
│   ├── batch_ref_5_budget_80_2038357_29.err
│   ├── batch_ref_5_budget_80_2038357_29.out
│   ├── batch_ref_5_budget_80_2038357_3.err
│   ├── batch_ref_5_budget_80_2038357_3.out
│   ├── batch_ref_5_budget_80_2038357_30.err
│   ├── batch_ref_5_budget_80_2038357_30.out
│   ├── batch_ref_5_budget_80_2038357_31.err
│   ├── batch_ref_5_budget_80_2038357_31.out
│   ├── batch_ref_5_budget_80_2038357_32.err
│   ├── batch_ref_5_budget_80_2038357_32.out
│   ├── batch_ref_5_budget_80_2038357_33.err
│   ├── batch_ref_5_budget_80_2038357_33.out
│   ├── batch_ref_5_budget_80_2038357_34.err
│   ├── batch_ref_5_budget_80_2038357_34.out
│   ├── batch_ref_5_budget_80_2038357_35.err
│   ├── batch_ref_5_budget_80_2038357_35.out
│   ├── batch_ref_5_budget_80_2038357_36.err
│   ├── batch_ref_5_budget_80_2038357_36.out
│   ├── batch_ref_5_budget_80_2038357_37.err
│   ├── batch_ref_5_budget_80_2038357_37.out
│   ├── batch_ref_5_budget_80_2038357_38.err
│   ├── batch_ref_5_budget_80_2038357_38.out
│   ├── batch_ref_5_budget_80_2038357_39.err
│   ├── batch_ref_5_budget_80_2038357_39.out
│   ├── batch_ref_5_budget_80_2038357_4.err
│   ├── batch_ref_5_budget_80_2038357_4.out
│   ├── batch_ref_5_budget_80_2038357_40.err
│   ├── batch_ref_5_budget_80_2038357_40.out
│   ├── batch_ref_5_budget_80_2038357_41.err
│   ├── batch_ref_5_budget_80_2038357_41.out
│   ├── batch_ref_5_budget_80_2038357_42.err
│   ├── batch_ref_5_budget_80_2038357_42.out
│   ├── batch_ref_5_budget_80_2038357_43.err
│   ├── batch_ref_5_budget_80_2038357_43.out
│   ├── batch_ref_5_budget_80_2038357_44.err
│   ├── batch_ref_5_budget_80_2038357_44.out
│   ├── batch_ref_5_budget_80_2038357_45.err
│   ├── batch_ref_5_budget_80_2038357_45.out
│   ├── batch_ref_5_budget_80_2038357_46.err
│   ├── batch_ref_5_budget_80_2038357_46.out
│   ├── batch_ref_5_budget_80_2038357_47.err
│   ├── batch_ref_5_budget_80_2038357_47.out
│   ├── batch_ref_5_budget_80_2038357_48.err
│   ├── batch_ref_5_budget_80_2038357_48.out
│   ├── batch_ref_5_budget_80_2038357_49.err
│   ├── batch_ref_5_budget_80_2038357_49.out
│   ├── batch_ref_5_budget_80_2038357_5.err
│   ├── batch_ref_5_budget_80_2038357_5.out
│   ├── batch_ref_5_budget_80_2038357_50.err
│   ├── batch_ref_5_budget_80_2038357_50.out
│   ├── batch_ref_5_budget_80_2038357_51.err
│   ├── batch_ref_5_budget_80_2038357_51.out
│   ├── batch_ref_5_budget_80_2038357_52.err
│   ├── batch_ref_5_budget_80_2038357_52.out
│   ├── batch_ref_5_budget_80_2038357_53.err
│   ├── batch_ref_5_budget_80_2038357_53.out
│   ├── batch_ref_5_budget_80_2038357_54.err
│   ├── batch_ref_5_budget_80_2038357_54.out
│   ├── batch_ref_5_budget_80_2038357_55.err
│   ├── batch_ref_5_budget_80_2038357_55.out
│   ├── batch_ref_5_budget_80_2038357_56.err
│   ├── batch_ref_5_budget_80_2038357_56.out
│   ├── batch_ref_5_budget_80_2038357_57.err
│   ├── batch_ref_5_budget_80_2038357_57.out
│   ├── batch_ref_5_budget_80_2038357_58.err
│   ├── batch_ref_5_budget_80_2038357_58.out
│   ├── batch_ref_5_budget_80_2038357_59.err
│   ├── batch_ref_5_budget_80_2038357_59.out
│   ├── batch_ref_5_budget_80_2038357_6.err
│   ├── batch_ref_5_budget_80_2038357_6.out
│   ├── batch_ref_5_budget_80_2038357_60.err
│   ├── batch_ref_5_budget_80_2038357_60.out
│   ├── batch_ref_5_budget_80_2038357_61.err
│   ├── batch_ref_5_budget_80_2038357_61.out
│   ├── batch_ref_5_budget_80_2038357_62.err
│   ├── batch_ref_5_budget_80_2038357_62.out
│   ├── batch_ref_5_budget_80_2038357_63.err
│   ├── batch_ref_5_budget_80_2038357_63.out
│   ├── batch_ref_5_budget_80_2038357_64.err
│   ├── batch_ref_5_budget_80_2038357_64.out
│   ├── batch_ref_5_budget_80_2038357_65.err
│   ├── batch_ref_5_budget_80_2038357_65.out
│   ├── batch_ref_5_budget_80_2038357_66.err
│   ├── batch_ref_5_budget_80_2038357_66.out
│   ├── batch_ref_5_budget_80_2038357_67.err
│   ├── batch_ref_5_budget_80_2038357_67.out
│   ├── batch_ref_5_budget_80_2038357_68.err
│   ├── batch_ref_5_budget_80_2038357_68.out
│   ├── batch_ref_5_budget_80_2038357_69.err
│   ├── batch_ref_5_budget_80_2038357_69.out
│   ├── batch_ref_5_budget_80_2038357_7.err
│   ├── batch_ref_5_budget_80_2038357_7.out
│   ├── batch_ref_5_budget_80_2038357_70.err
│   ├── batch_ref_5_budget_80_2038357_70.out
│   ├── batch_ref_5_budget_80_2038357_71.err
│   ├── batch_ref_5_budget_80_2038357_71.out
│   ├── batch_ref_5_budget_80_2038357_72.err
│   ├── batch_ref_5_budget_80_2038357_72.out
│   ├── batch_ref_5_budget_80_2038357_73.err
│   ├── batch_ref_5_budget_80_2038357_73.out
│   ├── batch_ref_5_budget_80_2038357_74.err
│   ├── batch_ref_5_budget_80_2038357_74.out
│   ├── batch_ref_5_budget_80_2038357_75.err
│   ├── batch_ref_5_budget_80_2038357_75.out
│   ├── batch_ref_5_budget_80_2038357_76.err
│   ├── batch_ref_5_budget_80_2038357_76.out
│   ├── batch_ref_5_budget_80_2038357_77.err
│   ├── batch_ref_5_budget_80_2038357_77.out
│   ├── batch_ref_5_budget_80_2038357_78.err
│   ├── batch_ref_5_budget_80_2038357_78.out
│   ├── batch_ref_5_budget_80_2038357_79.err
│   ├── batch_ref_5_budget_80_2038357_79.out
│   ├── batch_ref_5_budget_80_2038357_8.err
│   ├── batch_ref_5_budget_80_2038357_8.out
│   ├── batch_ref_5_budget_80_2038357_80.err
│   ├── batch_ref_5_budget_80_2038357_80.out
│   ├── batch_ref_5_budget_80_2038357_81.err
│   ├── batch_ref_5_budget_80_2038357_81.out
│   ├── batch_ref_5_budget_80_2038357_9.err
│   ├── batch_ref_5_budget_80_2038357_9.out
│   ├── batch_ref_5_budget_80_2040036_1.err
│   ├── batch_ref_5_budget_80_2040036_1.out
│   ├── batch_ref_5_budget_80_2040036_10.err
│   ├── batch_ref_5_budget_80_2040036_10.out
│   ├── batch_ref_5_budget_80_2040036_11.err
│   ├── batch_ref_5_budget_80_2040036_11.out
│   ├── batch_ref_5_budget_80_2040036_12.err
│   ├── batch_ref_5_budget_80_2040036_12.out
│   ├── batch_ref_5_budget_80_2040036_13.err
│   ├── batch_ref_5_budget_80_2040036_13.out
│   ├── batch_ref_5_budget_80_2040036_14.err
│   ├── batch_ref_5_budget_80_2040036_14.out
│   ├── batch_ref_5_budget_80_2040036_15.err
│   ├── batch_ref_5_budget_80_2040036_15.out
│   ├── batch_ref_5_budget_80_2040036_16.err
│   ├── batch_ref_5_budget_80_2040036_16.out
│   ├── batch_ref_5_budget_80_2040036_17.err
│   ├── batch_ref_5_budget_80_2040036_17.out
│   ├── batch_ref_5_budget_80_2040036_18.err
│   ├── batch_ref_5_budget_80_2040036_18.out
│   ├── batch_ref_5_budget_80_2040036_19.err
│   ├── batch_ref_5_budget_80_2040036_19.out
│   ├── batch_ref_5_budget_80_2040036_2.err
│   ├── batch_ref_5_budget_80_2040036_2.out
│   ├── batch_ref_5_budget_80_2040036_20.err
│   ├── batch_ref_5_budget_80_2040036_20.out
│   ├── batch_ref_5_budget_80_2040036_21.err
│   ├── batch_ref_5_budget_80_2040036_21.out
│   ├── batch_ref_5_budget_80_2040036_22.err
│   ├── batch_ref_5_budget_80_2040036_22.out
│   ├── batch_ref_5_budget_80_2040036_23.err
│   ├── batch_ref_5_budget_80_2040036_23.out
│   ├── batch_ref_5_budget_80_2040036_24.err
│   ├── batch_ref_5_budget_80_2040036_24.out
│   ├── batch_ref_5_budget_80_2040036_25.err
│   ├── batch_ref_5_budget_80_2040036_25.out
│   ├── batch_ref_5_budget_80_2040036_26.err
│   ├── batch_ref_5_budget_80_2040036_26.out
│   ├── batch_ref_5_budget_80_2040036_27.err
│   ├── batch_ref_5_budget_80_2040036_27.out
│   ├── batch_ref_5_budget_80_2040036_28.err
│   ├── batch_ref_5_budget_80_2040036_28.out
│   ├── batch_ref_5_budget_80_2040036_29.err
│   ├── batch_ref_5_budget_80_2040036_29.out
│   ├── batch_ref_5_budget_80_2040036_3.err
│   ├── batch_ref_5_budget_80_2040036_3.out
│   ├── batch_ref_5_budget_80_2040036_30.err
│   ├── batch_ref_5_budget_80_2040036_30.out
│   ├── batch_ref_5_budget_80_2040036_31.err
│   ├── batch_ref_5_budget_80_2040036_31.out
│   ├── batch_ref_5_budget_80_2040036_32.err
│   ├── batch_ref_5_budget_80_2040036_32.out
│   ├── batch_ref_5_budget_80_2040036_33.err
│   ├── batch_ref_5_budget_80_2040036_33.out
│   ├── batch_ref_5_budget_80_2040036_34.err
│   ├── batch_ref_5_budget_80_2040036_34.out
│   ├── batch_ref_5_budget_80_2040036_35.err
│   ├── batch_ref_5_budget_80_2040036_35.out
│   ├── batch_ref_5_budget_80_2040036_36.err
│   ├── batch_ref_5_budget_80_2040036_36.out
│   ├── batch_ref_5_budget_80_2040036_37.err
│   ├── batch_ref_5_budget_80_2040036_37.out
│   ├── batch_ref_5_budget_80_2040036_38.err
│   ├── batch_ref_5_budget_80_2040036_38.out
│   ├── batch_ref_5_budget_80_2040036_39.err
│   ├── batch_ref_5_budget_80_2040036_39.out
│   ├── batch_ref_5_budget_80_2040036_4.err
│   ├── batch_ref_5_budget_80_2040036_4.out
│   ├── batch_ref_5_budget_80_2040036_40.err
│   ├── batch_ref_5_budget_80_2040036_40.out
│   ├── batch_ref_5_budget_80_2040036_41.err
│   ├── batch_ref_5_budget_80_2040036_41.out
│   ├── batch_ref_5_budget_80_2040036_42.err
│   ├── batch_ref_5_budget_80_2040036_42.out
│   ├── batch_ref_5_budget_80_2040036_43.err
│   ├── batch_ref_5_budget_80_2040036_43.out
│   ├── batch_ref_5_budget_80_2040036_44.err
│   ├── batch_ref_5_budget_80_2040036_44.out
│   ├── batch_ref_5_budget_80_2040036_45.err
│   ├── batch_ref_5_budget_80_2040036_45.out
│   ├── batch_ref_5_budget_80_2040036_46.err
│   ├── batch_ref_5_budget_80_2040036_46.out
│   ├── batch_ref_5_budget_80_2040036_47.err
│   ├── batch_ref_5_budget_80_2040036_47.out
│   ├── batch_ref_5_budget_80_2040036_48.err
│   ├── batch_ref_5_budget_80_2040036_48.out
│   ├── batch_ref_5_budget_80_2040036_49.err
│   ├── batch_ref_5_budget_80_2040036_49.out
│   ├── batch_ref_5_budget_80_2040036_5.err
│   ├── batch_ref_5_budget_80_2040036_5.out
│   ├── batch_ref_5_budget_80_2040036_50.err
│   ├── batch_ref_5_budget_80_2040036_50.out
│   ├── batch_ref_5_budget_80_2040036_51.err
│   ├── batch_ref_5_budget_80_2040036_51.out
│   ├── batch_ref_5_budget_80_2040036_52.err
│   ├── batch_ref_5_budget_80_2040036_52.out
│   ├── batch_ref_5_budget_80_2040036_53.err
│   ├── batch_ref_5_budget_80_2040036_53.out
│   ├── batch_ref_5_budget_80_2040036_54.err
│   ├── batch_ref_5_budget_80_2040036_54.out
│   ├── batch_ref_5_budget_80_2040036_55.err
│   ├── batch_ref_5_budget_80_2040036_55.out
│   ├── batch_ref_5_budget_80_2040036_56.err
│   ├── batch_ref_5_budget_80_2040036_56.out
│   ├── batch_ref_5_budget_80_2040036_57.err
│   ├── batch_ref_5_budget_80_2040036_57.out
│   ├── batch_ref_5_budget_80_2040036_58.err
│   ├── batch_ref_5_budget_80_2040036_58.out
│   ├── batch_ref_5_budget_80_2040036_59.err
│   ├── batch_ref_5_budget_80_2040036_59.out
│   ├── batch_ref_5_budget_80_2040036_6.err
│   ├── batch_ref_5_budget_80_2040036_6.out
│   ├── batch_ref_5_budget_80_2040036_60.err
│   ├── batch_ref_5_budget_80_2040036_60.out
│   ├── batch_ref_5_budget_80_2040036_61.err
│   ├── batch_ref_5_budget_80_2040036_61.out
│   ├── batch_ref_5_budget_80_2040036_62.err
│   ├── batch_ref_5_budget_80_2040036_62.out
│   ├── batch_ref_5_budget_80_2040036_63.err
│   ├── batch_ref_5_budget_80_2040036_63.out
│   ├── batch_ref_5_budget_80_2040036_64.err
│   ├── batch_ref_5_budget_80_2040036_64.out
│   ├── batch_ref_5_budget_80_2040036_65.err
│   ├── batch_ref_5_budget_80_2040036_65.out
│   ├── batch_ref_5_budget_80_2040036_66.err
│   ├── batch_ref_5_budget_80_2040036_66.out
│   ├── batch_ref_5_budget_80_2040036_67.err
│   ├── batch_ref_5_budget_80_2040036_67.out
│   ├── batch_ref_5_budget_80_2040036_68.err
│   ├── batch_ref_5_budget_80_2040036_68.out
│   ├── batch_ref_5_budget_80_2040036_69.err
│   ├── batch_ref_5_budget_80_2040036_69.out
│   ├── batch_ref_5_budget_80_2040036_7.err
│   ├── batch_ref_5_budget_80_2040036_7.out
│   ├── batch_ref_5_budget_80_2040036_70.err
│   ├── batch_ref_5_budget_80_2040036_70.out
│   ├── batch_ref_5_budget_80_2040036_71.err
│   ├── batch_ref_5_budget_80_2040036_71.out
│   ├── batch_ref_5_budget_80_2040036_72.err
│   ├── batch_ref_5_budget_80_2040036_72.out
│   ├── batch_ref_5_budget_80_2040036_73.err
│   ├── batch_ref_5_budget_80_2040036_73.out
│   ├── batch_ref_5_budget_80_2040036_74.err
│   ├── batch_ref_5_budget_80_2040036_74.out
│   ├── batch_ref_5_budget_80_2040036_75.err
│   ├── batch_ref_5_budget_80_2040036_75.out
│   ├── batch_ref_5_budget_80_2040036_76.err
│   ├── batch_ref_5_budget_80_2040036_76.out
│   ├── batch_ref_5_budget_80_2040036_77.err
│   ├── batch_ref_5_budget_80_2040036_77.out
│   ├── batch_ref_5_budget_80_2040036_78.err
│   ├── batch_ref_5_budget_80_2040036_78.out
│   ├── batch_ref_5_budget_80_2040036_79.err
│   ├── batch_ref_5_budget_80_2040036_79.out
│   ├── batch_ref_5_budget_80_2040036_8.err
│   ├── batch_ref_5_budget_80_2040036_8.out
│   ├── batch_ref_5_budget_80_2040036_80.err
│   ├── batch_ref_5_budget_80_2040036_80.out
│   ├── batch_ref_5_budget_80_2040036_81.err
│   ├── batch_ref_5_budget_80_2040036_81.out
│   ├── batch_ref_5_budget_80_2040036_9.err
│   ├── batch_ref_5_budget_80_2040036_9.out
│   ├── batch_ref_5_budget_80_max_5_2067309_1.err
│   ├── batch_ref_5_budget_80_max_5_2067309_1.out
│   ├── batch_ref_5_budget_80_max_5_2067309_10.err
│   ├── batch_ref_5_budget_80_max_5_2067309_10.out
│   ├── batch_ref_5_budget_80_max_5_2067309_11.err
│   ├── batch_ref_5_budget_80_max_5_2067309_11.out
│   ├── batch_ref_5_budget_80_max_5_2067309_12.err
│   ├── batch_ref_5_budget_80_max_5_2067309_12.out
│   ├── batch_ref_5_budget_80_max_5_2067309_13.err
│   ├── batch_ref_5_budget_80_max_5_2067309_13.out
│   ├── batch_ref_5_budget_80_max_5_2067309_14.err
│   ├── batch_ref_5_budget_80_max_5_2067309_14.out
│   ├── batch_ref_5_budget_80_max_5_2067309_15.err
│   ├── batch_ref_5_budget_80_max_5_2067309_15.out
│   ├── batch_ref_5_budget_80_max_5_2067309_16.err
│   ├── batch_ref_5_budget_80_max_5_2067309_16.out
│   ├── batch_ref_5_budget_80_max_5_2067309_17.err
│   ├── batch_ref_5_budget_80_max_5_2067309_17.out
│   ├── batch_ref_5_budget_80_max_5_2067309_18.err
│   ├── batch_ref_5_budget_80_max_5_2067309_18.out
│   ├── batch_ref_5_budget_80_max_5_2067309_19.err
│   ├── batch_ref_5_budget_80_max_5_2067309_19.out
│   ├── batch_ref_5_budget_80_max_5_2067309_2.err
│   ├── batch_ref_5_budget_80_max_5_2067309_2.out
│   ├── batch_ref_5_budget_80_max_5_2067309_20.err
│   ├── batch_ref_5_budget_80_max_5_2067309_20.out
│   ├── batch_ref_5_budget_80_max_5_2067309_21.err
│   ├── batch_ref_5_budget_80_max_5_2067309_21.out
│   ├── batch_ref_5_budget_80_max_5_2067309_22.err
│   ├── batch_ref_5_budget_80_max_5_2067309_22.out
│   ├── batch_ref_5_budget_80_max_5_2067309_23.err
│   ├── batch_ref_5_budget_80_max_5_2067309_23.out
│   ├── batch_ref_5_budget_80_max_5_2067309_24.err
│   ├── batch_ref_5_budget_80_max_5_2067309_24.out
│   ├── batch_ref_5_budget_80_max_5_2067309_25.err
│   ├── batch_ref_5_budget_80_max_5_2067309_25.out
│   ├── batch_ref_5_budget_80_max_5_2067309_26.err
│   ├── batch_ref_5_budget_80_max_5_2067309_26.out
│   ├── batch_ref_5_budget_80_max_5_2067309_27.err
│   ├── batch_ref_5_budget_80_max_5_2067309_27.out
│   ├── batch_ref_5_budget_80_max_5_2067309_28.err
│   ├── batch_ref_5_budget_80_max_5_2067309_28.out
│   ├── batch_ref_5_budget_80_max_5_2067309_29.err
│   ├── batch_ref_5_budget_80_max_5_2067309_29.out
│   ├── batch_ref_5_budget_80_max_5_2067309_3.err
│   ├── batch_ref_5_budget_80_max_5_2067309_3.out
│   ├── batch_ref_5_budget_80_max_5_2067309_30.err
│   ├── batch_ref_5_budget_80_max_5_2067309_30.out
│   ├── batch_ref_5_budget_80_max_5_2067309_31.err
│   ├── batch_ref_5_budget_80_max_5_2067309_31.out
│   ├── batch_ref_5_budget_80_max_5_2067309_32.err
│   ├── batch_ref_5_budget_80_max_5_2067309_32.out
│   ├── batch_ref_5_budget_80_max_5_2067309_33.err
│   ├── batch_ref_5_budget_80_max_5_2067309_33.out
│   ├── batch_ref_5_budget_80_max_5_2067309_34.err
│   ├── batch_ref_5_budget_80_max_5_2067309_34.out
│   ├── batch_ref_5_budget_80_max_5_2067309_35.err
│   ├── batch_ref_5_budget_80_max_5_2067309_35.out
│   ├── batch_ref_5_budget_80_max_5_2067309_36.err
│   ├── batch_ref_5_budget_80_max_5_2067309_36.out
│   ├── batch_ref_5_budget_80_max_5_2067309_37.err
│   ├── batch_ref_5_budget_80_max_5_2067309_37.out
│   ├── batch_ref_5_budget_80_max_5_2067309_38.err
│   ├── batch_ref_5_budget_80_max_5_2067309_38.out
│   ├── batch_ref_5_budget_80_max_5_2067309_39.err
│   ├── batch_ref_5_budget_80_max_5_2067309_39.out
│   ├── batch_ref_5_budget_80_max_5_2067309_4.err
│   ├── batch_ref_5_budget_80_max_5_2067309_4.out
│   ├── batch_ref_5_budget_80_max_5_2067309_40.err
│   ├── batch_ref_5_budget_80_max_5_2067309_40.out
│   ├── batch_ref_5_budget_80_max_5_2067309_41.err
│   ├── batch_ref_5_budget_80_max_5_2067309_41.out
│   ├── batch_ref_5_budget_80_max_5_2067309_42.err
│   ├── batch_ref_5_budget_80_max_5_2067309_42.out
│   ├── batch_ref_5_budget_80_max_5_2067309_43.err
│   ├── batch_ref_5_budget_80_max_5_2067309_43.out
│   ├── batch_ref_5_budget_80_max_5_2067309_44.err
│   ├── batch_ref_5_budget_80_max_5_2067309_44.out
│   ├── batch_ref_5_budget_80_max_5_2067309_45.err
│   ├── batch_ref_5_budget_80_max_5_2067309_45.out
│   ├── batch_ref_5_budget_80_max_5_2067309_46.err
│   ├── batch_ref_5_budget_80_max_5_2067309_46.out
│   ├── batch_ref_5_budget_80_max_5_2067309_47.err
│   ├── batch_ref_5_budget_80_max_5_2067309_47.out
│   ├── batch_ref_5_budget_80_max_5_2067309_48.err
│   ├── batch_ref_5_budget_80_max_5_2067309_48.out
│   ├── batch_ref_5_budget_80_max_5_2067309_49.err
│   ├── batch_ref_5_budget_80_max_5_2067309_49.out
│   ├── batch_ref_5_budget_80_max_5_2067309_5.err
│   ├── batch_ref_5_budget_80_max_5_2067309_5.out
│   ├── batch_ref_5_budget_80_max_5_2067309_50.err
│   ├── batch_ref_5_budget_80_max_5_2067309_50.out
│   ├── batch_ref_5_budget_80_max_5_2067309_51.err
│   ├── batch_ref_5_budget_80_max_5_2067309_51.out
│   ├── batch_ref_5_budget_80_max_5_2067309_52.err
│   ├── batch_ref_5_budget_80_max_5_2067309_52.out
│   ├── batch_ref_5_budget_80_max_5_2067309_53.err
│   ├── batch_ref_5_budget_80_max_5_2067309_53.out
│   ├── batch_ref_5_budget_80_max_5_2067309_54.err
│   ├── batch_ref_5_budget_80_max_5_2067309_54.out
│   ├── batch_ref_5_budget_80_max_5_2067309_55.err
│   ├── batch_ref_5_budget_80_max_5_2067309_55.out
│   ├── batch_ref_5_budget_80_max_5_2067309_56.err
│   ├── batch_ref_5_budget_80_max_5_2067309_56.out
│   ├── batch_ref_5_budget_80_max_5_2067309_57.err
│   ├── batch_ref_5_budget_80_max_5_2067309_57.out
│   ├── batch_ref_5_budget_80_max_5_2067309_58.err
│   ├── batch_ref_5_budget_80_max_5_2067309_58.out
│   ├── batch_ref_5_budget_80_max_5_2067309_59.err
│   ├── batch_ref_5_budget_80_max_5_2067309_59.out
│   ├── batch_ref_5_budget_80_max_5_2067309_6.err
│   ├── batch_ref_5_budget_80_max_5_2067309_6.out
│   ├── batch_ref_5_budget_80_max_5_2067309_60.err
│   ├── batch_ref_5_budget_80_max_5_2067309_60.out
│   ├── batch_ref_5_budget_80_max_5_2067309_61.err
│   ├── batch_ref_5_budget_80_max_5_2067309_61.out
│   ├── batch_ref_5_budget_80_max_5_2067309_62.err
│   ├── batch_ref_5_budget_80_max_5_2067309_62.out
│   ├── batch_ref_5_budget_80_max_5_2067309_63.err
│   ├── batch_ref_5_budget_80_max_5_2067309_63.out
│   ├── batch_ref_5_budget_80_max_5_2067309_64.err
│   ├── batch_ref_5_budget_80_max_5_2067309_64.out
│   ├── batch_ref_5_budget_80_max_5_2067309_65.err
│   ├── batch_ref_5_budget_80_max_5_2067309_65.out
│   ├── batch_ref_5_budget_80_max_5_2067309_66.err
│   ├── batch_ref_5_budget_80_max_5_2067309_66.out
│   ├── batch_ref_5_budget_80_max_5_2067309_67.err
│   ├── batch_ref_5_budget_80_max_5_2067309_67.out
│   ├── batch_ref_5_budget_80_max_5_2067309_68.err
│   ├── batch_ref_5_budget_80_max_5_2067309_68.out
│   ├── batch_ref_5_budget_80_max_5_2067309_69.err
│   ├── batch_ref_5_budget_80_max_5_2067309_69.out
│   ├── batch_ref_5_budget_80_max_5_2067309_7.err
│   ├── batch_ref_5_budget_80_max_5_2067309_7.out
│   ├── batch_ref_5_budget_80_max_5_2067309_70.err
│   ├── batch_ref_5_budget_80_max_5_2067309_70.out
│   ├── batch_ref_5_budget_80_max_5_2067309_71.err
│   ├── batch_ref_5_budget_80_max_5_2067309_71.out
│   ├── batch_ref_5_budget_80_max_5_2067309_72.err
│   ├── batch_ref_5_budget_80_max_5_2067309_72.out
│   ├── batch_ref_5_budget_80_max_5_2067309_73.err
│   ├── batch_ref_5_budget_80_max_5_2067309_73.out
│   ├── batch_ref_5_budget_80_max_5_2067309_74.err
│   ├── batch_ref_5_budget_80_max_5_2067309_74.out
│   ├── batch_ref_5_budget_80_max_5_2067309_75.err
│   ├── batch_ref_5_budget_80_max_5_2067309_75.out
│   ├── batch_ref_5_budget_80_max_5_2067309_76.err
│   ├── batch_ref_5_budget_80_max_5_2067309_76.out
│   ├── batch_ref_5_budget_80_max_5_2067309_77.err
│   ├── batch_ref_5_budget_80_max_5_2067309_77.out
│   ├── batch_ref_5_budget_80_max_5_2067309_78.err
│   ├── batch_ref_5_budget_80_max_5_2067309_78.out
│   ├── batch_ref_5_budget_80_max_5_2067309_79.err
│   ├── batch_ref_5_budget_80_max_5_2067309_79.out
│   ├── batch_ref_5_budget_80_max_5_2067309_8.err
│   ├── batch_ref_5_budget_80_max_5_2067309_8.out
│   ├── batch_ref_5_budget_80_max_5_2067309_80.err
│   ├── batch_ref_5_budget_80_max_5_2067309_80.out
│   ├── batch_ref_5_budget_80_max_5_2067309_81.err
│   ├── batch_ref_5_budget_80_max_5_2067309_81.out
│   ├── batch_ref_5_budget_80_max_5_2067309_9.err
│   ├── batch_ref_5_budget_80_max_5_2067309_9.out
│   ├── batch_ref_5_budget_90_2040037_1.err
│   ├── batch_ref_5_budget_90_2040037_1.out
│   ├── batch_ref_5_budget_90_2040037_10.err
│   ├── batch_ref_5_budget_90_2040037_10.out
│   ├── batch_ref_5_budget_90_2040037_11.err
│   ├── batch_ref_5_budget_90_2040037_11.out
│   ├── batch_ref_5_budget_90_2040037_12.err
│   ├── batch_ref_5_budget_90_2040037_12.out
│   ├── batch_ref_5_budget_90_2040037_13.err
│   ├── batch_ref_5_budget_90_2040037_13.out
│   ├── batch_ref_5_budget_90_2040037_14.err
│   ├── batch_ref_5_budget_90_2040037_14.out
│   ├── batch_ref_5_budget_90_2040037_15.err
│   ├── batch_ref_5_budget_90_2040037_15.out
│   ├── batch_ref_5_budget_90_2040037_16.err
│   ├── batch_ref_5_budget_90_2040037_16.out
│   ├── batch_ref_5_budget_90_2040037_17.err
│   ├── batch_ref_5_budget_90_2040037_17.out
│   ├── batch_ref_5_budget_90_2040037_18.err
│   ├── batch_ref_5_budget_90_2040037_18.out
│   ├── batch_ref_5_budget_90_2040037_19.err
│   ├── batch_ref_5_budget_90_2040037_19.out
│   ├── batch_ref_5_budget_90_2040037_2.err
│   ├── batch_ref_5_budget_90_2040037_2.out
│   ├── batch_ref_5_budget_90_2040037_20.err
│   ├── batch_ref_5_budget_90_2040037_20.out
│   ├── batch_ref_5_budget_90_2040037_21.err
│   ├── batch_ref_5_budget_90_2040037_21.out
│   ├── batch_ref_5_budget_90_2040037_22.err
│   ├── batch_ref_5_budget_90_2040037_22.out
│   ├── batch_ref_5_budget_90_2040037_23.err
│   ├── batch_ref_5_budget_90_2040037_23.out
│   ├── batch_ref_5_budget_90_2040037_24.err
│   ├── batch_ref_5_budget_90_2040037_24.out
│   ├── batch_ref_5_budget_90_2040037_25.err
│   ├── batch_ref_5_budget_90_2040037_25.out
│   ├── batch_ref_5_budget_90_2040037_26.err
│   ├── batch_ref_5_budget_90_2040037_26.out
│   ├── batch_ref_5_budget_90_2040037_27.err
│   ├── batch_ref_5_budget_90_2040037_27.out
│   ├── batch_ref_5_budget_90_2040037_28.err
│   ├── batch_ref_5_budget_90_2040037_28.out
│   ├── batch_ref_5_budget_90_2040037_29.err
│   ├── batch_ref_5_budget_90_2040037_29.out
│   ├── batch_ref_5_budget_90_2040037_3.err
│   ├── batch_ref_5_budget_90_2040037_3.out
│   ├── batch_ref_5_budget_90_2040037_30.err
│   ├── batch_ref_5_budget_90_2040037_30.out
│   ├── batch_ref_5_budget_90_2040037_31.err
│   ├── batch_ref_5_budget_90_2040037_31.out
│   ├── batch_ref_5_budget_90_2040037_32.err
│   ├── batch_ref_5_budget_90_2040037_32.out
│   ├── batch_ref_5_budget_90_2040037_33.err
│   ├── batch_ref_5_budget_90_2040037_33.out
│   ├── batch_ref_5_budget_90_2040037_34.err
│   ├── batch_ref_5_budget_90_2040037_34.out
│   ├── batch_ref_5_budget_90_2040037_35.err
│   ├── batch_ref_5_budget_90_2040037_35.out
│   ├── batch_ref_5_budget_90_2040037_36.err
│   ├── batch_ref_5_budget_90_2040037_36.out
│   ├── batch_ref_5_budget_90_2040037_37.err
│   ├── batch_ref_5_budget_90_2040037_37.out
│   ├── batch_ref_5_budget_90_2040037_38.err
│   ├── batch_ref_5_budget_90_2040037_38.out
│   ├── batch_ref_5_budget_90_2040037_39.err
│   ├── batch_ref_5_budget_90_2040037_39.out
│   ├── batch_ref_5_budget_90_2040037_4.err
│   ├── batch_ref_5_budget_90_2040037_4.out
│   ├── batch_ref_5_budget_90_2040037_40.err
│   ├── batch_ref_5_budget_90_2040037_40.out
│   ├── batch_ref_5_budget_90_2040037_41.err
│   ├── batch_ref_5_budget_90_2040037_41.out
│   ├── batch_ref_5_budget_90_2040037_42.err
│   ├── batch_ref_5_budget_90_2040037_42.out
│   ├── batch_ref_5_budget_90_2040037_43.err
│   ├── batch_ref_5_budget_90_2040037_43.out
│   ├── batch_ref_5_budget_90_2040037_44.err
│   ├── batch_ref_5_budget_90_2040037_44.out
│   ├── batch_ref_5_budget_90_2040037_45.err
│   ├── batch_ref_5_budget_90_2040037_45.out
│   ├── batch_ref_5_budget_90_2040037_46.err
│   ├── batch_ref_5_budget_90_2040037_46.out
│   ├── batch_ref_5_budget_90_2040037_47.err
│   ├── batch_ref_5_budget_90_2040037_47.out
│   ├── batch_ref_5_budget_90_2040037_48.err
│   ├── batch_ref_5_budget_90_2040037_48.out
│   ├── batch_ref_5_budget_90_2040037_49.err
│   ├── batch_ref_5_budget_90_2040037_49.out
│   ├── batch_ref_5_budget_90_2040037_5.err
│   ├── batch_ref_5_budget_90_2040037_5.out
│   ├── batch_ref_5_budget_90_2040037_50.err
│   ├── batch_ref_5_budget_90_2040037_50.out
│   ├── batch_ref_5_budget_90_2040037_51.err
│   ├── batch_ref_5_budget_90_2040037_51.out
│   ├── batch_ref_5_budget_90_2040037_52.err
│   ├── batch_ref_5_budget_90_2040037_52.out
│   ├── batch_ref_5_budget_90_2040037_53.err
│   ├── batch_ref_5_budget_90_2040037_53.out
│   ├── batch_ref_5_budget_90_2040037_54.err
│   ├── batch_ref_5_budget_90_2040037_54.out
│   ├── batch_ref_5_budget_90_2040037_55.err
│   ├── batch_ref_5_budget_90_2040037_55.out
│   ├── batch_ref_5_budget_90_2040037_56.err
│   ├── batch_ref_5_budget_90_2040037_56.out
│   ├── batch_ref_5_budget_90_2040037_57.err
│   ├── batch_ref_5_budget_90_2040037_57.out
│   ├── batch_ref_5_budget_90_2040037_58.err
│   ├── batch_ref_5_budget_90_2040037_58.out
│   ├── batch_ref_5_budget_90_2040037_59.err
│   ├── batch_ref_5_budget_90_2040037_59.out
│   ├── batch_ref_5_budget_90_2040037_6.err
│   ├── batch_ref_5_budget_90_2040037_6.out
│   ├── batch_ref_5_budget_90_2040037_60.err
│   ├── batch_ref_5_budget_90_2040037_60.out
│   ├── batch_ref_5_budget_90_2040037_61.err
│   ├── batch_ref_5_budget_90_2040037_61.out
│   ├── batch_ref_5_budget_90_2040037_62.err
│   ├── batch_ref_5_budget_90_2040037_62.out
│   ├── batch_ref_5_budget_90_2040037_63.err
│   ├── batch_ref_5_budget_90_2040037_63.out
│   ├── batch_ref_5_budget_90_2040037_64.err
│   ├── batch_ref_5_budget_90_2040037_64.out
│   ├── batch_ref_5_budget_90_2040037_65.err
│   ├── batch_ref_5_budget_90_2040037_65.out
│   ├── batch_ref_5_budget_90_2040037_66.err
│   ├── batch_ref_5_budget_90_2040037_66.out
│   ├── batch_ref_5_budget_90_2040037_67.err
│   ├── batch_ref_5_budget_90_2040037_67.out
│   ├── batch_ref_5_budget_90_2040037_68.err
│   ├── batch_ref_5_budget_90_2040037_68.out
│   ├── batch_ref_5_budget_90_2040037_69.err
│   ├── batch_ref_5_budget_90_2040037_69.out
│   ├── batch_ref_5_budget_90_2040037_7.err
│   ├── batch_ref_5_budget_90_2040037_7.out
│   ├── batch_ref_5_budget_90_2040037_70.err
│   ├── batch_ref_5_budget_90_2040037_70.out
│   ├── batch_ref_5_budget_90_2040037_71.err
│   ├── batch_ref_5_budget_90_2040037_71.out
│   ├── batch_ref_5_budget_90_2040037_72.err
│   ├── batch_ref_5_budget_90_2040037_72.out
│   ├── batch_ref_5_budget_90_2040037_73.err
│   ├── batch_ref_5_budget_90_2040037_73.out
│   ├── batch_ref_5_budget_90_2040037_74.err
│   ├── batch_ref_5_budget_90_2040037_74.out
│   ├── batch_ref_5_budget_90_2040037_75.err
│   ├── batch_ref_5_budget_90_2040037_75.out
│   ├── batch_ref_5_budget_90_2040037_76.err
│   ├── batch_ref_5_budget_90_2040037_76.out
│   ├── batch_ref_5_budget_90_2040037_77.err
│   ├── batch_ref_5_budget_90_2040037_77.out
│   ├── batch_ref_5_budget_90_2040037_78.err
│   ├── batch_ref_5_budget_90_2040037_78.out
│   ├── batch_ref_5_budget_90_2040037_79.err
│   ├── batch_ref_5_budget_90_2040037_79.out
│   ├── batch_ref_5_budget_90_2040037_8.err
│   ├── batch_ref_5_budget_90_2040037_8.out
│   ├── batch_ref_5_budget_90_2040037_80.err
│   ├── batch_ref_5_budget_90_2040037_80.out
│   ├── batch_ref_5_budget_90_2040037_81.err
│   ├── batch_ref_5_budget_90_2040037_81.out
│   ├── batch_ref_5_budget_90_2040037_9.err
│   ├── batch_ref_5_budget_90_2040037_9.out
│   ├── batch_ref_6_budget_100_2025120_1.err
│   ├── batch_ref_6_budget_100_2025120_1.out
│   ├── batch_ref_6_budget_100_2025120_10.err
│   ├── batch_ref_6_budget_100_2025120_10.out
│   ├── batch_ref_6_budget_100_2025120_11.err
│   ├── batch_ref_6_budget_100_2025120_11.out
│   ├── batch_ref_6_budget_100_2025120_12.err
│   ├── batch_ref_6_budget_100_2025120_12.out
│   ├── batch_ref_6_budget_100_2025120_13.err
│   ├── batch_ref_6_budget_100_2025120_13.out
│   ├── batch_ref_6_budget_100_2025120_14.err
│   ├── batch_ref_6_budget_100_2025120_14.out
│   ├── batch_ref_6_budget_100_2025120_15.err
│   ├── batch_ref_6_budget_100_2025120_15.out
│   ├── batch_ref_6_budget_100_2025120_16.err
│   ├── batch_ref_6_budget_100_2025120_16.out
│   ├── batch_ref_6_budget_100_2025120_17.err
│   ├── batch_ref_6_budget_100_2025120_17.out
│   ├── batch_ref_6_budget_100_2025120_18.err
│   ├── batch_ref_6_budget_100_2025120_18.out
│   ├── batch_ref_6_budget_100_2025120_19.err
│   ├── batch_ref_6_budget_100_2025120_19.out
│   ├── batch_ref_6_budget_100_2025120_2.err
│   ├── batch_ref_6_budget_100_2025120_2.out
│   ├── batch_ref_6_budget_100_2025120_20.err
│   ├── batch_ref_6_budget_100_2025120_20.out
│   ├── batch_ref_6_budget_100_2025120_21.err
│   ├── batch_ref_6_budget_100_2025120_21.out
│   ├── batch_ref_6_budget_100_2025120_22.err
│   ├── batch_ref_6_budget_100_2025120_22.out
│   ├── batch_ref_6_budget_100_2025120_23.err
│   ├── batch_ref_6_budget_100_2025120_23.out
│   ├── batch_ref_6_budget_100_2025120_24.err
│   ├── batch_ref_6_budget_100_2025120_24.out
│   ├── batch_ref_6_budget_100_2025120_25.err
│   ├── batch_ref_6_budget_100_2025120_25.out
│   ├── batch_ref_6_budget_100_2025120_26.err
│   ├── batch_ref_6_budget_100_2025120_26.out
│   ├── batch_ref_6_budget_100_2025120_27.err
│   ├── batch_ref_6_budget_100_2025120_27.out
│   ├── batch_ref_6_budget_100_2025120_28.err
│   ├── batch_ref_6_budget_100_2025120_28.out
│   ├── batch_ref_6_budget_100_2025120_29.err
│   ├── batch_ref_6_budget_100_2025120_29.out
│   ├── batch_ref_6_budget_100_2025120_3.err
│   ├── batch_ref_6_budget_100_2025120_3.out
│   ├── batch_ref_6_budget_100_2025120_30.err
│   ├── batch_ref_6_budget_100_2025120_30.out
│   ├── batch_ref_6_budget_100_2025120_31.err
│   ├── batch_ref_6_budget_100_2025120_31.out
│   ├── batch_ref_6_budget_100_2025120_32.err
│   ├── batch_ref_6_budget_100_2025120_32.out
│   ├── batch_ref_6_budget_100_2025120_33.err
│   ├── batch_ref_6_budget_100_2025120_33.out
│   ├── batch_ref_6_budget_100_2025120_34.err
│   ├── batch_ref_6_budget_100_2025120_34.out
│   ├── batch_ref_6_budget_100_2025120_35.err
│   ├── batch_ref_6_budget_100_2025120_35.out
│   ├── batch_ref_6_budget_100_2025120_36.err
│   ├── batch_ref_6_budget_100_2025120_36.out
│   ├── batch_ref_6_budget_100_2025120_37.err
│   ├── batch_ref_6_budget_100_2025120_37.out
│   ├── batch_ref_6_budget_100_2025120_38.err
│   ├── batch_ref_6_budget_100_2025120_38.out
│   ├── batch_ref_6_budget_100_2025120_39.err
│   ├── batch_ref_6_budget_100_2025120_39.out
│   ├── batch_ref_6_budget_100_2025120_4.err
│   ├── batch_ref_6_budget_100_2025120_4.out
│   ├── batch_ref_6_budget_100_2025120_40.err
│   ├── batch_ref_6_budget_100_2025120_40.out
│   ├── batch_ref_6_budget_100_2025120_41.err
│   ├── batch_ref_6_budget_100_2025120_41.out
│   ├── batch_ref_6_budget_100_2025120_42.err
│   ├── batch_ref_6_budget_100_2025120_42.out
│   ├── batch_ref_6_budget_100_2025120_43.err
│   ├── batch_ref_6_budget_100_2025120_43.out
│   ├── batch_ref_6_budget_100_2025120_44.err
│   ├── batch_ref_6_budget_100_2025120_44.out
│   ├── batch_ref_6_budget_100_2025120_45.err
│   ├── batch_ref_6_budget_100_2025120_45.out
│   ├── batch_ref_6_budget_100_2025120_46.err
│   ├── batch_ref_6_budget_100_2025120_46.out
│   ├── batch_ref_6_budget_100_2025120_47.err
│   ├── batch_ref_6_budget_100_2025120_47.out
│   ├── batch_ref_6_budget_100_2025120_48.err
│   ├── batch_ref_6_budget_100_2025120_48.out
│   ├── batch_ref_6_budget_100_2025120_49.err
│   ├── batch_ref_6_budget_100_2025120_49.out
│   ├── batch_ref_6_budget_100_2025120_5.err
│   ├── batch_ref_6_budget_100_2025120_5.out
│   ├── batch_ref_6_budget_100_2025120_50.err
│   ├── batch_ref_6_budget_100_2025120_50.out
│   ├── batch_ref_6_budget_100_2025120_51.err
│   ├── batch_ref_6_budget_100_2025120_51.out
│   ├── batch_ref_6_budget_100_2025120_52.err
│   ├── batch_ref_6_budget_100_2025120_52.out
│   ├── batch_ref_6_budget_100_2025120_53.err
│   ├── batch_ref_6_budget_100_2025120_53.out
│   ├── batch_ref_6_budget_100_2025120_54.err
│   ├── batch_ref_6_budget_100_2025120_54.out
│   ├── batch_ref_6_budget_100_2025120_55.err
│   ├── batch_ref_6_budget_100_2025120_55.out
│   ├── batch_ref_6_budget_100_2025120_56.err
│   ├── batch_ref_6_budget_100_2025120_56.out
│   ├── batch_ref_6_budget_100_2025120_57.err
│   ├── batch_ref_6_budget_100_2025120_57.out
│   ├── batch_ref_6_budget_100_2025120_58.err
│   ├── batch_ref_6_budget_100_2025120_58.out
│   ├── batch_ref_6_budget_100_2025120_59.err
│   ├── batch_ref_6_budget_100_2025120_59.out
│   ├── batch_ref_6_budget_100_2025120_6.err
│   ├── batch_ref_6_budget_100_2025120_6.out
│   ├── batch_ref_6_budget_100_2025120_60.err
│   ├── batch_ref_6_budget_100_2025120_60.out
│   ├── batch_ref_6_budget_100_2025120_61.err
│   ├── batch_ref_6_budget_100_2025120_61.out
│   ├── batch_ref_6_budget_100_2025120_62.err
│   ├── batch_ref_6_budget_100_2025120_62.out
│   ├── batch_ref_6_budget_100_2025120_63.err
│   ├── batch_ref_6_budget_100_2025120_63.out
│   ├── batch_ref_6_budget_100_2025120_64.err
│   ├── batch_ref_6_budget_100_2025120_64.out
│   ├── batch_ref_6_budget_100_2025120_65.err
│   ├── batch_ref_6_budget_100_2025120_65.out
│   ├── batch_ref_6_budget_100_2025120_66.err
│   ├── batch_ref_6_budget_100_2025120_66.out
│   ├── batch_ref_6_budget_100_2025120_67.err
│   ├── batch_ref_6_budget_100_2025120_67.out
│   ├── batch_ref_6_budget_100_2025120_68.err
│   ├── batch_ref_6_budget_100_2025120_68.out
│   ├── batch_ref_6_budget_100_2025120_69.err
│   ├── batch_ref_6_budget_100_2025120_69.out
│   ├── batch_ref_6_budget_100_2025120_7.err
│   ├── batch_ref_6_budget_100_2025120_7.out
│   ├── batch_ref_6_budget_100_2025120_70.err
│   ├── batch_ref_6_budget_100_2025120_70.out
│   ├── batch_ref_6_budget_100_2025120_71.err
│   ├── batch_ref_6_budget_100_2025120_71.out
│   ├── batch_ref_6_budget_100_2025120_72.err
│   ├── batch_ref_6_budget_100_2025120_72.out
│   ├── batch_ref_6_budget_100_2025120_73.err
│   ├── batch_ref_6_budget_100_2025120_73.out
│   ├── batch_ref_6_budget_100_2025120_74.err
│   ├── batch_ref_6_budget_100_2025120_74.out
│   ├── batch_ref_6_budget_100_2025120_75.err
│   ├── batch_ref_6_budget_100_2025120_75.out
│   ├── batch_ref_6_budget_100_2025120_76.err
│   ├── batch_ref_6_budget_100_2025120_76.out
│   ├── batch_ref_6_budget_100_2025120_77.err
│   ├── batch_ref_6_budget_100_2025120_77.out
│   ├── batch_ref_6_budget_100_2025120_78.err
│   ├── batch_ref_6_budget_100_2025120_78.out
│   ├── batch_ref_6_budget_100_2025120_79.err
│   ├── batch_ref_6_budget_100_2025120_79.out
│   ├── batch_ref_6_budget_100_2025120_8.err
│   ├── batch_ref_6_budget_100_2025120_8.out
│   ├── batch_ref_6_budget_100_2025120_80.err
│   ├── batch_ref_6_budget_100_2025120_80.out
│   ├── batch_ref_6_budget_100_2025120_81.err
│   ├── batch_ref_6_budget_100_2025120_81.out
│   ├── batch_ref_6_budget_100_2025120_9.err
│   ├── batch_ref_6_budget_100_2025120_9.out
│   ├── batch_ref_6_budget_100_2040038_1.err
│   ├── batch_ref_6_budget_100_2040038_1.out
│   ├── batch_ref_6_budget_100_2040038_10.err
│   ├── batch_ref_6_budget_100_2040038_10.out
│   ├── batch_ref_6_budget_100_2040038_11.err
│   ├── batch_ref_6_budget_100_2040038_11.out
│   ├── batch_ref_6_budget_100_2040038_12.err
│   ├── batch_ref_6_budget_100_2040038_12.out
│   ├── batch_ref_6_budget_100_2040038_13.err
│   ├── batch_ref_6_budget_100_2040038_13.out
│   ├── batch_ref_6_budget_100_2040038_14.err
│   ├── batch_ref_6_budget_100_2040038_14.out
│   ├── batch_ref_6_budget_100_2040038_15.err
│   ├── batch_ref_6_budget_100_2040038_15.out
│   ├── batch_ref_6_budget_100_2040038_16.err
│   ├── batch_ref_6_budget_100_2040038_16.out
│   ├── batch_ref_6_budget_100_2040038_17.err
│   ├── batch_ref_6_budget_100_2040038_17.out
│   ├── batch_ref_6_budget_100_2040038_18.err
│   ├── batch_ref_6_budget_100_2040038_18.out
│   ├── batch_ref_6_budget_100_2040038_19.err
│   ├── batch_ref_6_budget_100_2040038_19.out
│   ├── batch_ref_6_budget_100_2040038_2.err
│   ├── batch_ref_6_budget_100_2040038_2.out
│   ├── batch_ref_6_budget_100_2040038_20.err
│   ├── batch_ref_6_budget_100_2040038_20.out
│   ├── batch_ref_6_budget_100_2040038_21.err
│   ├── batch_ref_6_budget_100_2040038_21.out
│   ├── batch_ref_6_budget_100_2040038_22.err
│   ├── batch_ref_6_budget_100_2040038_22.out
│   ├── batch_ref_6_budget_100_2040038_23.err
│   ├── batch_ref_6_budget_100_2040038_23.out
│   ├── batch_ref_6_budget_100_2040038_24.err
│   ├── batch_ref_6_budget_100_2040038_24.out
│   ├── batch_ref_6_budget_100_2040038_25.err
│   ├── batch_ref_6_budget_100_2040038_25.out
│   ├── batch_ref_6_budget_100_2040038_26.err
│   ├── batch_ref_6_budget_100_2040038_26.out
│   ├── batch_ref_6_budget_100_2040038_27.err
│   ├── batch_ref_6_budget_100_2040038_27.out
│   ├── batch_ref_6_budget_100_2040038_28.err
│   ├── batch_ref_6_budget_100_2040038_28.out
│   ├── batch_ref_6_budget_100_2040038_29.err
│   ├── batch_ref_6_budget_100_2040038_29.out
│   ├── batch_ref_6_budget_100_2040038_3.err
│   ├── batch_ref_6_budget_100_2040038_3.out
│   ├── batch_ref_6_budget_100_2040038_30.err
│   ├── batch_ref_6_budget_100_2040038_30.out
│   ├── batch_ref_6_budget_100_2040038_31.err
│   ├── batch_ref_6_budget_100_2040038_31.out
│   ├── batch_ref_6_budget_100_2040038_32.err
│   ├── batch_ref_6_budget_100_2040038_32.out
│   ├── batch_ref_6_budget_100_2040038_33.err
│   ├── batch_ref_6_budget_100_2040038_33.out
│   ├── batch_ref_6_budget_100_2040038_34.err
│   ├── batch_ref_6_budget_100_2040038_34.out
│   ├── batch_ref_6_budget_100_2040038_35.err
│   ├── batch_ref_6_budget_100_2040038_35.out
│   ├── batch_ref_6_budget_100_2040038_36.err
│   ├── batch_ref_6_budget_100_2040038_36.out
│   ├── batch_ref_6_budget_100_2040038_37.err
│   ├── batch_ref_6_budget_100_2040038_37.out
│   ├── batch_ref_6_budget_100_2040038_38.err
│   ├── batch_ref_6_budget_100_2040038_38.out
│   ├── batch_ref_6_budget_100_2040038_39.err
│   ├── batch_ref_6_budget_100_2040038_39.out
│   ├── batch_ref_6_budget_100_2040038_4.err
│   ├── batch_ref_6_budget_100_2040038_4.out
│   ├── batch_ref_6_budget_100_2040038_40.err
│   ├── batch_ref_6_budget_100_2040038_40.out
│   ├── batch_ref_6_budget_100_2040038_41.err
│   ├── batch_ref_6_budget_100_2040038_41.out
│   ├── batch_ref_6_budget_100_2040038_42.err
│   ├── batch_ref_6_budget_100_2040038_42.out
│   ├── batch_ref_6_budget_100_2040038_43.err
│   ├── batch_ref_6_budget_100_2040038_43.out
│   ├── batch_ref_6_budget_100_2040038_44.err
│   ├── batch_ref_6_budget_100_2040038_44.out
│   ├── batch_ref_6_budget_100_2040038_45.err
│   ├── batch_ref_6_budget_100_2040038_45.out
│   ├── batch_ref_6_budget_100_2040038_46.err
│   ├── batch_ref_6_budget_100_2040038_46.out
│   ├── batch_ref_6_budget_100_2040038_47.err
│   ├── batch_ref_6_budget_100_2040038_47.out
│   ├── batch_ref_6_budget_100_2040038_48.err
│   ├── batch_ref_6_budget_100_2040038_48.out
│   ├── batch_ref_6_budget_100_2040038_49.err
│   ├── batch_ref_6_budget_100_2040038_49.out
│   ├── batch_ref_6_budget_100_2040038_5.err
│   ├── batch_ref_6_budget_100_2040038_5.out
│   ├── batch_ref_6_budget_100_2040038_50.err
│   ├── batch_ref_6_budget_100_2040038_50.out
│   ├── batch_ref_6_budget_100_2040038_51.err
│   ├── batch_ref_6_budget_100_2040038_51.out
│   ├── batch_ref_6_budget_100_2040038_52.err
│   ├── batch_ref_6_budget_100_2040038_52.out
│   ├── batch_ref_6_budget_100_2040038_53.err
│   ├── batch_ref_6_budget_100_2040038_53.out
│   ├── batch_ref_6_budget_100_2040038_54.err
│   ├── batch_ref_6_budget_100_2040038_54.out
│   ├── batch_ref_6_budget_100_2040038_55.err
│   ├── batch_ref_6_budget_100_2040038_55.out
│   ├── batch_ref_6_budget_100_2040038_56.err
│   ├── batch_ref_6_budget_100_2040038_56.out
│   ├── batch_ref_6_budget_100_2040038_57.err
│   ├── batch_ref_6_budget_100_2040038_57.out
│   ├── batch_ref_6_budget_100_2040038_58.err
│   ├── batch_ref_6_budget_100_2040038_58.out
│   ├── batch_ref_6_budget_100_2040038_59.err
│   ├── batch_ref_6_budget_100_2040038_59.out
│   ├── batch_ref_6_budget_100_2040038_6.err
│   ├── batch_ref_6_budget_100_2040038_6.out
│   ├── batch_ref_6_budget_100_2040038_60.err
│   ├── batch_ref_6_budget_100_2040038_60.out
│   ├── batch_ref_6_budget_100_2040038_61.err
│   ├── batch_ref_6_budget_100_2040038_61.out
│   ├── batch_ref_6_budget_100_2040038_62.err
│   ├── batch_ref_6_budget_100_2040038_62.out
│   ├── batch_ref_6_budget_100_2040038_63.err
│   ├── batch_ref_6_budget_100_2040038_63.out
│   ├── batch_ref_6_budget_100_2040038_64.err
│   ├── batch_ref_6_budget_100_2040038_64.out
│   ├── batch_ref_6_budget_100_2040038_65.err
│   ├── batch_ref_6_budget_100_2040038_65.out
│   ├── batch_ref_6_budget_100_2040038_66.err
│   ├── batch_ref_6_budget_100_2040038_66.out
│   ├── batch_ref_6_budget_100_2040038_67.err
│   ├── batch_ref_6_budget_100_2040038_67.out
│   ├── batch_ref_6_budget_100_2040038_68.err
│   ├── batch_ref_6_budget_100_2040038_68.out
│   ├── batch_ref_6_budget_100_2040038_69.err
│   ├── batch_ref_6_budget_100_2040038_69.out
│   ├── batch_ref_6_budget_100_2040038_7.err
│   ├── batch_ref_6_budget_100_2040038_7.out
│   ├── batch_ref_6_budget_100_2040038_70.err
│   ├── batch_ref_6_budget_100_2040038_70.out
│   ├── batch_ref_6_budget_100_2040038_71.err
│   ├── batch_ref_6_budget_100_2040038_71.out
│   ├── batch_ref_6_budget_100_2040038_72.err
│   ├── batch_ref_6_budget_100_2040038_72.out
│   ├── batch_ref_6_budget_100_2040038_73.err
│   ├── batch_ref_6_budget_100_2040038_73.out
│   ├── batch_ref_6_budget_100_2040038_74.err
│   ├── batch_ref_6_budget_100_2040038_74.out
│   ├── batch_ref_6_budget_100_2040038_75.err
│   ├── batch_ref_6_budget_100_2040038_75.out
│   ├── batch_ref_6_budget_100_2040038_76.err
│   ├── batch_ref_6_budget_100_2040038_76.out
│   ├── batch_ref_6_budget_100_2040038_77.err
│   ├── batch_ref_6_budget_100_2040038_77.out
│   ├── batch_ref_6_budget_100_2040038_78.err
│   ├── batch_ref_6_budget_100_2040038_78.out
│   ├── batch_ref_6_budget_100_2040038_79.err
│   ├── batch_ref_6_budget_100_2040038_79.out
│   ├── batch_ref_6_budget_100_2040038_8.err
│   ├── batch_ref_6_budget_100_2040038_8.out
│   ├── batch_ref_6_budget_100_2040038_80.err
│   ├── batch_ref_6_budget_100_2040038_80.out
│   ├── batch_ref_6_budget_100_2040038_81.err
│   ├── batch_ref_6_budget_100_2040038_81.out
│   ├── batch_ref_6_budget_100_2040038_9.err
│   ├── batch_ref_6_budget_100_2040038_9.out
│   ├── batch_ref_6_budget_100_max_6_2067314_1.err
│   ├── batch_ref_6_budget_100_max_6_2067314_1.out
│   ├── batch_ref_6_budget_100_max_6_2067314_10.err
│   ├── batch_ref_6_budget_100_max_6_2067314_10.out
│   ├── batch_ref_6_budget_100_max_6_2067314_11.err
│   ├── batch_ref_6_budget_100_max_6_2067314_11.out
│   ├── batch_ref_6_budget_100_max_6_2067314_12.err
│   ├── batch_ref_6_budget_100_max_6_2067314_12.out
│   ├── batch_ref_6_budget_100_max_6_2067314_13.err
│   ├── batch_ref_6_budget_100_max_6_2067314_13.out
│   ├── batch_ref_6_budget_100_max_6_2067314_14.err
│   ├── batch_ref_6_budget_100_max_6_2067314_14.out
│   ├── batch_ref_6_budget_100_max_6_2067314_15.err
│   ├── batch_ref_6_budget_100_max_6_2067314_15.out
│   ├── batch_ref_6_budget_100_max_6_2067314_16.err
│   ├── batch_ref_6_budget_100_max_6_2067314_16.out
│   ├── batch_ref_6_budget_100_max_6_2067314_17.err
│   ├── batch_ref_6_budget_100_max_6_2067314_17.out
│   ├── batch_ref_6_budget_100_max_6_2067314_18.err
│   ├── batch_ref_6_budget_100_max_6_2067314_18.out
│   ├── batch_ref_6_budget_100_max_6_2067314_19.err
│   ├── batch_ref_6_budget_100_max_6_2067314_19.out
│   ├── batch_ref_6_budget_100_max_6_2067314_2.err
│   ├── batch_ref_6_budget_100_max_6_2067314_2.out
│   ├── batch_ref_6_budget_100_max_6_2067314_20.err
│   ├── batch_ref_6_budget_100_max_6_2067314_20.out
│   ├── batch_ref_6_budget_100_max_6_2067314_21.err
│   ├── batch_ref_6_budget_100_max_6_2067314_21.out
│   ├── batch_ref_6_budget_100_max_6_2067314_22.err
│   ├── batch_ref_6_budget_100_max_6_2067314_22.out
│   ├── batch_ref_6_budget_100_max_6_2067314_23.err
│   ├── batch_ref_6_budget_100_max_6_2067314_23.out
│   ├── batch_ref_6_budget_100_max_6_2067314_24.err
│   ├── batch_ref_6_budget_100_max_6_2067314_24.out
│   ├── batch_ref_6_budget_100_max_6_2067314_25.err
│   ├── batch_ref_6_budget_100_max_6_2067314_25.out
│   ├── batch_ref_6_budget_100_max_6_2067314_26.err
│   ├── batch_ref_6_budget_100_max_6_2067314_26.out
│   ├── batch_ref_6_budget_100_max_6_2067314_27.err
│   ├── batch_ref_6_budget_100_max_6_2067314_27.out
│   ├── batch_ref_6_budget_100_max_6_2067314_28.err
│   ├── batch_ref_6_budget_100_max_6_2067314_28.out
│   ├── batch_ref_6_budget_100_max_6_2067314_29.err
│   ├── batch_ref_6_budget_100_max_6_2067314_29.out
│   ├── batch_ref_6_budget_100_max_6_2067314_3.err
│   ├── batch_ref_6_budget_100_max_6_2067314_3.out
│   ├── batch_ref_6_budget_100_max_6_2067314_30.err
│   ├── batch_ref_6_budget_100_max_6_2067314_30.out
│   ├── batch_ref_6_budget_100_max_6_2067314_31.err
│   ├── batch_ref_6_budget_100_max_6_2067314_31.out
│   ├── batch_ref_6_budget_100_max_6_2067314_32.err
│   ├── batch_ref_6_budget_100_max_6_2067314_32.out
│   ├── batch_ref_6_budget_100_max_6_2067314_33.err
│   ├── batch_ref_6_budget_100_max_6_2067314_33.out
│   ├── batch_ref_6_budget_100_max_6_2067314_34.err
│   ├── batch_ref_6_budget_100_max_6_2067314_34.out
│   ├── batch_ref_6_budget_100_max_6_2067314_35.err
│   ├── batch_ref_6_budget_100_max_6_2067314_35.out
│   ├── batch_ref_6_budget_100_max_6_2067314_36.err
│   ├── batch_ref_6_budget_100_max_6_2067314_36.out
│   ├── batch_ref_6_budget_100_max_6_2067314_37.err
│   ├── batch_ref_6_budget_100_max_6_2067314_37.out
│   ├── batch_ref_6_budget_100_max_6_2067314_38.err
│   ├── batch_ref_6_budget_100_max_6_2067314_38.out
│   ├── batch_ref_6_budget_100_max_6_2067314_39.err
│   ├── batch_ref_6_budget_100_max_6_2067314_39.out
│   ├── batch_ref_6_budget_100_max_6_2067314_4.err
│   ├── batch_ref_6_budget_100_max_6_2067314_4.out
│   ├── batch_ref_6_budget_100_max_6_2067314_40.err
│   ├── batch_ref_6_budget_100_max_6_2067314_40.out
│   ├── batch_ref_6_budget_100_max_6_2067314_41.err
│   ├── batch_ref_6_budget_100_max_6_2067314_41.out
│   ├── batch_ref_6_budget_100_max_6_2067314_42.err
│   ├── batch_ref_6_budget_100_max_6_2067314_42.out
│   ├── batch_ref_6_budget_100_max_6_2067314_43.err
│   ├── batch_ref_6_budget_100_max_6_2067314_43.out
│   ├── batch_ref_6_budget_100_max_6_2067314_44.err
│   ├── batch_ref_6_budget_100_max_6_2067314_44.out
│   ├── batch_ref_6_budget_100_max_6_2067314_45.err
│   ├── batch_ref_6_budget_100_max_6_2067314_45.out
│   ├── batch_ref_6_budget_100_max_6_2067314_46.err
│   ├── batch_ref_6_budget_100_max_6_2067314_46.out
│   ├── batch_ref_6_budget_100_max_6_2067314_47.err
│   ├── batch_ref_6_budget_100_max_6_2067314_47.out
│   ├── batch_ref_6_budget_100_max_6_2067314_48.err
│   ├── batch_ref_6_budget_100_max_6_2067314_48.out
│   ├── batch_ref_6_budget_100_max_6_2067314_49.err
│   ├── batch_ref_6_budget_100_max_6_2067314_49.out
│   ├── batch_ref_6_budget_100_max_6_2067314_5.err
│   ├── batch_ref_6_budget_100_max_6_2067314_5.out
│   ├── batch_ref_6_budget_100_max_6_2067314_50.err
│   ├── batch_ref_6_budget_100_max_6_2067314_50.out
│   ├── batch_ref_6_budget_100_max_6_2067314_51.err
│   ├── batch_ref_6_budget_100_max_6_2067314_51.out
│   ├── batch_ref_6_budget_100_max_6_2067314_52.err
│   ├── batch_ref_6_budget_100_max_6_2067314_52.out
│   ├── batch_ref_6_budget_100_max_6_2067314_53.err
│   ├── batch_ref_6_budget_100_max_6_2067314_53.out
│   ├── batch_ref_6_budget_100_max_6_2067314_54.err
│   ├── batch_ref_6_budget_100_max_6_2067314_54.out
│   ├── batch_ref_6_budget_100_max_6_2067314_55.err
│   ├── batch_ref_6_budget_100_max_6_2067314_55.out
│   ├── batch_ref_6_budget_100_max_6_2067314_56.err
│   ├── batch_ref_6_budget_100_max_6_2067314_56.out
│   ├── batch_ref_6_budget_100_max_6_2067314_57.err
│   ├── batch_ref_6_budget_100_max_6_2067314_57.out
│   ├── batch_ref_6_budget_100_max_6_2067314_58.err
│   ├── batch_ref_6_budget_100_max_6_2067314_58.out
│   ├── batch_ref_6_budget_100_max_6_2067314_59.err
│   ├── batch_ref_6_budget_100_max_6_2067314_59.out
│   ├── batch_ref_6_budget_100_max_6_2067314_6.err
│   ├── batch_ref_6_budget_100_max_6_2067314_6.out
│   ├── batch_ref_6_budget_100_max_6_2067314_60.err
│   ├── batch_ref_6_budget_100_max_6_2067314_60.out
│   ├── batch_ref_6_budget_100_max_6_2067314_61.err
│   ├── batch_ref_6_budget_100_max_6_2067314_61.out
│   ├── batch_ref_6_budget_100_max_6_2067314_62.err
│   ├── batch_ref_6_budget_100_max_6_2067314_62.out
│   ├── batch_ref_6_budget_100_max_6_2067314_63.err
│   ├── batch_ref_6_budget_100_max_6_2067314_63.out
│   ├── batch_ref_6_budget_100_max_6_2067314_64.err
│   ├── batch_ref_6_budget_100_max_6_2067314_64.out
│   ├── batch_ref_6_budget_100_max_6_2067314_65.err
│   ├── batch_ref_6_budget_100_max_6_2067314_65.out
│   ├── batch_ref_6_budget_100_max_6_2067314_66.err
│   ├── batch_ref_6_budget_100_max_6_2067314_66.out
│   ├── batch_ref_6_budget_100_max_6_2067314_67.err
│   ├── batch_ref_6_budget_100_max_6_2067314_67.out
│   ├── batch_ref_6_budget_100_max_6_2067314_68.err
│   ├── batch_ref_6_budget_100_max_6_2067314_68.out
│   ├── batch_ref_6_budget_100_max_6_2067314_69.err
│   ├── batch_ref_6_budget_100_max_6_2067314_69.out
│   ├── batch_ref_6_budget_100_max_6_2067314_7.err
│   ├── batch_ref_6_budget_100_max_6_2067314_7.out
│   ├── batch_ref_6_budget_100_max_6_2067314_70.err
│   ├── batch_ref_6_budget_100_max_6_2067314_70.out
│   ├── batch_ref_6_budget_100_max_6_2067314_71.err
│   ├── batch_ref_6_budget_100_max_6_2067314_71.out
│   ├── batch_ref_6_budget_100_max_6_2067314_72.err
│   ├── batch_ref_6_budget_100_max_6_2067314_72.out
│   ├── batch_ref_6_budget_100_max_6_2067314_73.err
│   ├── batch_ref_6_budget_100_max_6_2067314_73.out
│   ├── batch_ref_6_budget_100_max_6_2067314_74.err
│   ├── batch_ref_6_budget_100_max_6_2067314_74.out
│   ├── batch_ref_6_budget_100_max_6_2067314_75.err
│   ├── batch_ref_6_budget_100_max_6_2067314_75.out
│   ├── batch_ref_6_budget_100_max_6_2067314_76.err
│   ├── batch_ref_6_budget_100_max_6_2067314_76.out
│   ├── batch_ref_6_budget_100_max_6_2067314_77.err
│   ├── batch_ref_6_budget_100_max_6_2067314_77.out
│   ├── batch_ref_6_budget_100_max_6_2067314_78.err
│   ├── batch_ref_6_budget_100_max_6_2067314_78.out
│   ├── batch_ref_6_budget_100_max_6_2067314_79.err
│   ├── batch_ref_6_budget_100_max_6_2067314_79.out
│   ├── batch_ref_6_budget_100_max_6_2067314_8.err
│   ├── batch_ref_6_budget_100_max_6_2067314_8.out
│   ├── batch_ref_6_budget_100_max_6_2067314_80.err
│   ├── batch_ref_6_budget_100_max_6_2067314_80.out
│   ├── batch_ref_6_budget_100_max_6_2067314_81.err
│   ├── batch_ref_6_budget_100_max_6_2067314_81.out
│   ├── batch_ref_6_budget_100_max_6_2067314_9.err
│   ├── batch_ref_6_budget_100_max_6_2067314_9.out
│   ├── batch_ref_6_budget_150_2038360_1.err
│   ├── batch_ref_6_budget_150_2038360_1.out
│   ├── batch_ref_6_budget_150_2038360_10.err
│   ├── batch_ref_6_budget_150_2038360_10.out
│   ├── batch_ref_6_budget_150_2038360_11.err
│   ├── batch_ref_6_budget_150_2038360_11.out
│   ├── batch_ref_6_budget_150_2038360_12.err
│   ├── batch_ref_6_budget_150_2038360_12.out
│   ├── batch_ref_6_budget_150_2038360_13.err
│   ├── batch_ref_6_budget_150_2038360_13.out
│   ├── batch_ref_6_budget_150_2038360_14.err
│   ├── batch_ref_6_budget_150_2038360_14.out
│   ├── batch_ref_6_budget_150_2038360_15.err
│   ├── batch_ref_6_budget_150_2038360_15.out
│   ├── batch_ref_6_budget_150_2038360_16.err
│   ├── batch_ref_6_budget_150_2038360_16.out
│   ├── batch_ref_6_budget_150_2038360_17.err
│   ├── batch_ref_6_budget_150_2038360_17.out
│   ├── batch_ref_6_budget_150_2038360_18.err
│   ├── batch_ref_6_budget_150_2038360_18.out
│   ├── batch_ref_6_budget_150_2038360_19.err
│   ├── batch_ref_6_budget_150_2038360_19.out
│   ├── batch_ref_6_budget_150_2038360_2.err
│   ├── batch_ref_6_budget_150_2038360_2.out
│   ├── batch_ref_6_budget_150_2038360_20.err
│   ├── batch_ref_6_budget_150_2038360_20.out
│   ├── batch_ref_6_budget_150_2038360_21.err
│   ├── batch_ref_6_budget_150_2038360_21.out
│   ├── batch_ref_6_budget_150_2038360_22.err
│   ├── batch_ref_6_budget_150_2038360_22.out
│   ├── batch_ref_6_budget_150_2038360_23.err
│   ├── batch_ref_6_budget_150_2038360_23.out
│   ├── batch_ref_6_budget_150_2038360_24.err
│   ├── batch_ref_6_budget_150_2038360_24.out
│   ├── batch_ref_6_budget_150_2038360_25.err
│   ├── batch_ref_6_budget_150_2038360_25.out
│   ├── batch_ref_6_budget_150_2038360_26.err
│   ├── batch_ref_6_budget_150_2038360_26.out
│   ├── batch_ref_6_budget_150_2038360_27.err
│   ├── batch_ref_6_budget_150_2038360_27.out
│   ├── batch_ref_6_budget_150_2038360_28.err
│   ├── batch_ref_6_budget_150_2038360_28.out
│   ├── batch_ref_6_budget_150_2038360_29.err
│   ├── batch_ref_6_budget_150_2038360_29.out
│   ├── batch_ref_6_budget_150_2038360_3.err
│   ├── batch_ref_6_budget_150_2038360_3.out
│   ├── batch_ref_6_budget_150_2038360_30.err
│   ├── batch_ref_6_budget_150_2038360_30.out
│   ├── batch_ref_6_budget_150_2038360_31.err
│   ├── batch_ref_6_budget_150_2038360_31.out
│   ├── batch_ref_6_budget_150_2038360_32.err
│   ├── batch_ref_6_budget_150_2038360_32.out
│   ├── batch_ref_6_budget_150_2038360_33.err
│   ├── batch_ref_6_budget_150_2038360_33.out
│   ├── batch_ref_6_budget_150_2038360_34.err
│   ├── batch_ref_6_budget_150_2038360_34.out
│   ├── batch_ref_6_budget_150_2038360_35.err
│   ├── batch_ref_6_budget_150_2038360_35.out
│   ├── batch_ref_6_budget_150_2038360_36.err
│   ├── batch_ref_6_budget_150_2038360_36.out
│   ├── batch_ref_6_budget_150_2038360_37.err
│   ├── batch_ref_6_budget_150_2038360_37.out
│   ├── batch_ref_6_budget_150_2038360_38.err
│   ├── batch_ref_6_budget_150_2038360_38.out
│   ├── batch_ref_6_budget_150_2038360_39.err
│   ├── batch_ref_6_budget_150_2038360_39.out
│   ├── batch_ref_6_budget_150_2038360_4.err
│   ├── batch_ref_6_budget_150_2038360_4.out
│   ├── batch_ref_6_budget_150_2038360_40.err
│   ├── batch_ref_6_budget_150_2038360_40.out
│   ├── batch_ref_6_budget_150_2038360_41.err
│   ├── batch_ref_6_budget_150_2038360_41.out
│   ├── batch_ref_6_budget_150_2038360_42.err
│   ├── batch_ref_6_budget_150_2038360_42.out
│   ├── batch_ref_6_budget_150_2038360_43.err
│   ├── batch_ref_6_budget_150_2038360_43.out
│   ├── batch_ref_6_budget_150_2038360_44.err
│   ├── batch_ref_6_budget_150_2038360_44.out
│   ├── batch_ref_6_budget_150_2038360_45.err
│   ├── batch_ref_6_budget_150_2038360_45.out
│   ├── batch_ref_6_budget_150_2038360_46.err
│   ├── batch_ref_6_budget_150_2038360_46.out
│   ├── batch_ref_6_budget_150_2038360_47.err
│   ├── batch_ref_6_budget_150_2038360_47.out
│   ├── batch_ref_6_budget_150_2038360_48.err
│   ├── batch_ref_6_budget_150_2038360_48.out
│   ├── batch_ref_6_budget_150_2038360_49.err
│   ├── batch_ref_6_budget_150_2038360_49.out
│   ├── batch_ref_6_budget_150_2038360_5.err
│   ├── batch_ref_6_budget_150_2038360_5.out
│   ├── batch_ref_6_budget_150_2038360_50.err
│   ├── batch_ref_6_budget_150_2038360_50.out
│   ├── batch_ref_6_budget_150_2038360_51.err
│   ├── batch_ref_6_budget_150_2038360_51.out
│   ├── batch_ref_6_budget_150_2038360_52.err
│   ├── batch_ref_6_budget_150_2038360_52.out
│   ├── batch_ref_6_budget_150_2038360_53.err
│   ├── batch_ref_6_budget_150_2038360_53.out
│   ├── batch_ref_6_budget_150_2038360_54.err
│   ├── batch_ref_6_budget_150_2038360_54.out
│   ├── batch_ref_6_budget_150_2038360_55.err
│   ├── batch_ref_6_budget_150_2038360_55.out
│   ├── batch_ref_6_budget_150_2038360_56.err
│   ├── batch_ref_6_budget_150_2038360_56.out
│   ├── batch_ref_6_budget_150_2038360_57.err
│   ├── batch_ref_6_budget_150_2038360_57.out
│   ├── batch_ref_6_budget_150_2038360_58.err
│   ├── batch_ref_6_budget_150_2038360_58.out
│   ├── batch_ref_6_budget_150_2038360_59.err
│   ├── batch_ref_6_budget_150_2038360_59.out
│   ├── batch_ref_6_budget_150_2038360_6.err
│   ├── batch_ref_6_budget_150_2038360_6.out
│   ├── batch_ref_6_budget_150_2038360_60.err
│   ├── batch_ref_6_budget_150_2038360_60.out
│   ├── batch_ref_6_budget_150_2038360_61.err
│   ├── batch_ref_6_budget_150_2038360_61.out
│   ├── batch_ref_6_budget_150_2038360_62.err
│   ├── batch_ref_6_budget_150_2038360_62.out
│   ├── batch_ref_6_budget_150_2038360_63.err
│   ├── batch_ref_6_budget_150_2038360_63.out
│   ├── batch_ref_6_budget_150_2038360_64.err
│   ├── batch_ref_6_budget_150_2038360_64.out
│   ├── batch_ref_6_budget_150_2038360_65.err
│   ├── batch_ref_6_budget_150_2038360_65.out
│   ├── batch_ref_6_budget_150_2038360_66.err
│   ├── batch_ref_6_budget_150_2038360_66.out
│   ├── batch_ref_6_budget_150_2038360_67.err
│   ├── batch_ref_6_budget_150_2038360_67.out
│   ├── batch_ref_6_budget_150_2038360_68.err
│   ├── batch_ref_6_budget_150_2038360_68.out
│   ├── batch_ref_6_budget_150_2038360_69.err
│   ├── batch_ref_6_budget_150_2038360_69.out
│   ├── batch_ref_6_budget_150_2038360_7.err
│   ├── batch_ref_6_budget_150_2038360_7.out
│   ├── batch_ref_6_budget_150_2038360_70.err
│   ├── batch_ref_6_budget_150_2038360_70.out
│   ├── batch_ref_6_budget_150_2038360_71.err
│   ├── batch_ref_6_budget_150_2038360_71.out
│   ├── batch_ref_6_budget_150_2038360_72.err
│   ├── batch_ref_6_budget_150_2038360_72.out
│   ├── batch_ref_6_budget_150_2038360_73.err
│   ├── batch_ref_6_budget_150_2038360_73.out
│   ├── batch_ref_6_budget_150_2038360_74.err
│   ├── batch_ref_6_budget_150_2038360_74.out
│   ├── batch_ref_6_budget_150_2038360_75.err
│   ├── batch_ref_6_budget_150_2038360_75.out
│   ├── batch_ref_6_budget_150_2038360_76.err
│   ├── batch_ref_6_budget_150_2038360_76.out
│   ├── batch_ref_6_budget_150_2038360_77.err
│   ├── batch_ref_6_budget_150_2038360_77.out
│   ├── batch_ref_6_budget_150_2038360_78.err
│   ├── batch_ref_6_budget_150_2038360_78.out
│   ├── batch_ref_6_budget_150_2038360_79.err
│   ├── batch_ref_6_budget_150_2038360_79.out
│   ├── batch_ref_6_budget_150_2038360_8.err
│   ├── batch_ref_6_budget_150_2038360_8.out
│   ├── batch_ref_6_budget_150_2038360_80.err
│   ├── batch_ref_6_budget_150_2038360_80.out
│   ├── batch_ref_6_budget_150_2038360_81.err
│   ├── batch_ref_6_budget_150_2038360_81.out
│   ├── batch_ref_6_budget_150_2038360_9.err
│   ├── batch_ref_6_budget_150_2038360_9.out
│   ├── batch_ref_6_budget_150_2040039_1.err
│   ├── batch_ref_6_budget_150_2040039_1.out
│   ├── batch_ref_6_budget_150_2040039_10.err
│   ├── batch_ref_6_budget_150_2040039_10.out
│   ├── batch_ref_6_budget_150_2040039_11.err
│   ├── batch_ref_6_budget_150_2040039_11.out
│   ├── batch_ref_6_budget_150_2040039_12.err
│   ├── batch_ref_6_budget_150_2040039_12.out
│   ├── batch_ref_6_budget_150_2040039_13.err
│   ├── batch_ref_6_budget_150_2040039_13.out
│   ├── batch_ref_6_budget_150_2040039_14.err
│   ├── batch_ref_6_budget_150_2040039_14.out
│   ├── batch_ref_6_budget_150_2040039_15.err
│   ├── batch_ref_6_budget_150_2040039_15.out
│   ├── batch_ref_6_budget_150_2040039_16.err
│   ├── batch_ref_6_budget_150_2040039_16.out
│   ├── batch_ref_6_budget_150_2040039_17.err
│   ├── batch_ref_6_budget_150_2040039_17.out
│   ├── batch_ref_6_budget_150_2040039_18.err
│   ├── batch_ref_6_budget_150_2040039_18.out
│   ├── batch_ref_6_budget_150_2040039_19.err
│   ├── batch_ref_6_budget_150_2040039_19.out
│   ├── batch_ref_6_budget_150_2040039_2.err
│   ├── batch_ref_6_budget_150_2040039_2.out
│   ├── batch_ref_6_budget_150_2040039_20.err
│   ├── batch_ref_6_budget_150_2040039_20.out
│   ├── batch_ref_6_budget_150_2040039_21.err
│   ├── batch_ref_6_budget_150_2040039_21.out
│   ├── batch_ref_6_budget_150_2040039_22.err
│   ├── batch_ref_6_budget_150_2040039_22.out
│   ├── batch_ref_6_budget_150_2040039_23.err
│   ├── batch_ref_6_budget_150_2040039_23.out
│   ├── batch_ref_6_budget_150_2040039_24.err
│   ├── batch_ref_6_budget_150_2040039_24.out
│   ├── batch_ref_6_budget_150_2040039_25.err
│   ├── batch_ref_6_budget_150_2040039_25.out
│   ├── batch_ref_6_budget_150_2040039_26.err
│   ├── batch_ref_6_budget_150_2040039_26.out
│   ├── batch_ref_6_budget_150_2040039_27.err
│   ├── batch_ref_6_budget_150_2040039_27.out
│   ├── batch_ref_6_budget_150_2040039_28.err
│   ├── batch_ref_6_budget_150_2040039_28.out
│   ├── batch_ref_6_budget_150_2040039_29.err
│   ├── batch_ref_6_budget_150_2040039_29.out
│   ├── batch_ref_6_budget_150_2040039_3.err
│   ├── batch_ref_6_budget_150_2040039_3.out
│   ├── batch_ref_6_budget_150_2040039_30.err
│   ├── batch_ref_6_budget_150_2040039_30.out
│   ├── batch_ref_6_budget_150_2040039_31.err
│   ├── batch_ref_6_budget_150_2040039_31.out
│   ├── batch_ref_6_budget_150_2040039_32.err
│   ├── batch_ref_6_budget_150_2040039_32.out
│   ├── batch_ref_6_budget_150_2040039_33.err
│   ├── batch_ref_6_budget_150_2040039_33.out
│   ├── batch_ref_6_budget_150_2040039_34.err
│   ├── batch_ref_6_budget_150_2040039_34.out
│   ├── batch_ref_6_budget_150_2040039_35.err
│   ├── batch_ref_6_budget_150_2040039_35.out
│   ├── batch_ref_6_budget_150_2040039_36.err
│   ├── batch_ref_6_budget_150_2040039_36.out
│   ├── batch_ref_6_budget_150_2040039_37.err
│   ├── batch_ref_6_budget_150_2040039_37.out
│   ├── batch_ref_6_budget_150_2040039_38.err
│   ├── batch_ref_6_budget_150_2040039_38.out
│   ├── batch_ref_6_budget_150_2040039_39.err
│   ├── batch_ref_6_budget_150_2040039_39.out
│   ├── batch_ref_6_budget_150_2040039_4.err
│   ├── batch_ref_6_budget_150_2040039_4.out
│   ├── batch_ref_6_budget_150_2040039_40.err
│   ├── batch_ref_6_budget_150_2040039_40.out
│   ├── batch_ref_6_budget_150_2040039_41.err
│   ├── batch_ref_6_budget_150_2040039_41.out
│   ├── batch_ref_6_budget_150_2040039_42.err
│   ├── batch_ref_6_budget_150_2040039_42.out
│   ├── batch_ref_6_budget_150_2040039_43.err
│   ├── batch_ref_6_budget_150_2040039_43.out
│   ├── batch_ref_6_budget_150_2040039_44.err
│   ├── batch_ref_6_budget_150_2040039_44.out
│   ├── batch_ref_6_budget_150_2040039_45.err
│   ├── batch_ref_6_budget_150_2040039_45.out
│   ├── batch_ref_6_budget_150_2040039_46.err
│   ├── batch_ref_6_budget_150_2040039_46.out
│   ├── batch_ref_6_budget_150_2040039_47.err
│   ├── batch_ref_6_budget_150_2040039_47.out
│   ├── batch_ref_6_budget_150_2040039_48.err
│   ├── batch_ref_6_budget_150_2040039_48.out
│   ├── batch_ref_6_budget_150_2040039_49.err
│   ├── batch_ref_6_budget_150_2040039_49.out
│   ├── batch_ref_6_budget_150_2040039_5.err
│   ├── batch_ref_6_budget_150_2040039_5.out
│   ├── batch_ref_6_budget_150_2040039_50.err
│   ├── batch_ref_6_budget_150_2040039_50.out
│   ├── batch_ref_6_budget_150_2040039_51.err
│   ├── batch_ref_6_budget_150_2040039_51.out
│   ├── batch_ref_6_budget_150_2040039_52.err
│   ├── batch_ref_6_budget_150_2040039_52.out
│   ├── batch_ref_6_budget_150_2040039_53.err
│   ├── batch_ref_6_budget_150_2040039_53.out
│   ├── batch_ref_6_budget_150_2040039_54.err
│   ├── batch_ref_6_budget_150_2040039_54.out
│   ├── batch_ref_6_budget_150_2040039_55.err
│   ├── batch_ref_6_budget_150_2040039_55.out
│   ├── batch_ref_6_budget_150_2040039_56.err
│   ├── batch_ref_6_budget_150_2040039_56.out
│   ├── batch_ref_6_budget_150_2040039_57.err
│   ├── batch_ref_6_budget_150_2040039_57.out
│   ├── batch_ref_6_budget_150_2040039_58.err
│   ├── batch_ref_6_budget_150_2040039_58.out
│   ├── batch_ref_6_budget_150_2040039_59.err
│   ├── batch_ref_6_budget_150_2040039_59.out
│   ├── batch_ref_6_budget_150_2040039_6.err
│   ├── batch_ref_6_budget_150_2040039_6.out
│   ├── batch_ref_6_budget_150_2040039_60.err
│   ├── batch_ref_6_budget_150_2040039_60.out
│   ├── batch_ref_6_budget_150_2040039_61.err
│   ├── batch_ref_6_budget_150_2040039_61.out
│   ├── batch_ref_6_budget_150_2040039_62.err
│   ├── batch_ref_6_budget_150_2040039_62.out
│   ├── batch_ref_6_budget_150_2040039_63.err
│   ├── batch_ref_6_budget_150_2040039_63.out
│   ├── batch_ref_6_budget_150_2040039_64.err
│   ├── batch_ref_6_budget_150_2040039_64.out
│   ├── batch_ref_6_budget_150_2040039_65.err
│   ├── batch_ref_6_budget_150_2040039_65.out
│   ├── batch_ref_6_budget_150_2040039_66.err
│   ├── batch_ref_6_budget_150_2040039_66.out
│   ├── batch_ref_6_budget_150_2040039_67.err
│   ├── batch_ref_6_budget_150_2040039_67.out
│   ├── batch_ref_6_budget_150_2040039_68.err
│   ├── batch_ref_6_budget_150_2040039_68.out
│   ├── batch_ref_6_budget_150_2040039_69.err
│   ├── batch_ref_6_budget_150_2040039_69.out
│   ├── batch_ref_6_budget_150_2040039_7.err
│   ├── batch_ref_6_budget_150_2040039_7.out
│   ├── batch_ref_6_budget_150_2040039_70.err
│   ├── batch_ref_6_budget_150_2040039_70.out
│   ├── batch_ref_6_budget_150_2040039_71.err
│   ├── batch_ref_6_budget_150_2040039_71.out
│   ├── batch_ref_6_budget_150_2040039_72.err
│   ├── batch_ref_6_budget_150_2040039_72.out
│   ├── batch_ref_6_budget_150_2040039_73.err
│   ├── batch_ref_6_budget_150_2040039_73.out
│   ├── batch_ref_6_budget_150_2040039_74.err
│   ├── batch_ref_6_budget_150_2040039_74.out
│   ├── batch_ref_6_budget_150_2040039_75.err
│   ├── batch_ref_6_budget_150_2040039_75.out
│   ├── batch_ref_6_budget_150_2040039_76.err
│   ├── batch_ref_6_budget_150_2040039_76.out
│   ├── batch_ref_6_budget_150_2040039_77.err
│   ├── batch_ref_6_budget_150_2040039_77.out
│   ├── batch_ref_6_budget_150_2040039_78.err
│   ├── batch_ref_6_budget_150_2040039_78.out
│   ├── batch_ref_6_budget_150_2040039_79.err
│   ├── batch_ref_6_budget_150_2040039_79.out
│   ├── batch_ref_6_budget_150_2040039_8.err
│   ├── batch_ref_6_budget_150_2040039_8.out
│   ├── batch_ref_6_budget_150_2040039_80.err
│   ├── batch_ref_6_budget_150_2040039_80.out
│   ├── batch_ref_6_budget_150_2040039_81.err
│   ├── batch_ref_6_budget_150_2040039_81.out
│   ├── batch_ref_6_budget_150_2040039_9.err
│   ├── batch_ref_6_budget_150_2040039_9.out
│   ├── batch_ref_6_budget_200_2038459_1.err
│   ├── batch_ref_6_budget_200_2038459_1.out
│   ├── batch_ref_6_budget_200_2038459_10.err
│   ├── batch_ref_6_budget_200_2038459_10.out
│   ├── batch_ref_6_budget_200_2038459_11.err
│   ├── batch_ref_6_budget_200_2038459_11.out
│   ├── batch_ref_6_budget_200_2038459_12.err
│   ├── batch_ref_6_budget_200_2038459_12.out
│   ├── batch_ref_6_budget_200_2038459_13.err
│   ├── batch_ref_6_budget_200_2038459_13.out
│   ├── batch_ref_6_budget_200_2038459_14.err
│   ├── batch_ref_6_budget_200_2038459_14.out
│   ├── batch_ref_6_budget_200_2038459_15.err
│   ├── batch_ref_6_budget_200_2038459_15.out
│   ├── batch_ref_6_budget_200_2038459_16.err
│   ├── batch_ref_6_budget_200_2038459_16.out
│   ├── batch_ref_6_budget_200_2038459_17.err
│   ├── batch_ref_6_budget_200_2038459_17.out
│   ├── batch_ref_6_budget_200_2038459_18.err
│   ├── batch_ref_6_budget_200_2038459_18.out
│   ├── batch_ref_6_budget_200_2038459_19.err
│   ├── batch_ref_6_budget_200_2038459_19.out
│   ├── batch_ref_6_budget_200_2038459_2.err
│   ├── batch_ref_6_budget_200_2038459_2.out
│   ├── batch_ref_6_budget_200_2038459_20.err
│   ├── batch_ref_6_budget_200_2038459_20.out
│   ├── batch_ref_6_budget_200_2038459_21.err
│   ├── batch_ref_6_budget_200_2038459_21.out
│   ├── batch_ref_6_budget_200_2038459_22.err
│   ├── batch_ref_6_budget_200_2038459_22.out
│   ├── batch_ref_6_budget_200_2038459_23.err
│   ├── batch_ref_6_budget_200_2038459_23.out
│   ├── batch_ref_6_budget_200_2038459_24.err
│   ├── batch_ref_6_budget_200_2038459_24.out
│   ├── batch_ref_6_budget_200_2038459_25.err
│   ├── batch_ref_6_budget_200_2038459_25.out
│   ├── batch_ref_6_budget_200_2038459_26.err
│   ├── batch_ref_6_budget_200_2038459_26.out
│   ├── batch_ref_6_budget_200_2038459_27.err
│   ├── batch_ref_6_budget_200_2038459_27.out
│   ├── batch_ref_6_budget_200_2038459_28.err
│   ├── batch_ref_6_budget_200_2038459_28.out
│   ├── batch_ref_6_budget_200_2038459_29.err
│   ├── batch_ref_6_budget_200_2038459_29.out
│   ├── batch_ref_6_budget_200_2038459_3.err
│   ├── batch_ref_6_budget_200_2038459_3.out
│   ├── batch_ref_6_budget_200_2038459_30.err
│   ├── batch_ref_6_budget_200_2038459_30.out
│   ├── batch_ref_6_budget_200_2038459_31.err
│   ├── batch_ref_6_budget_200_2038459_31.out
│   ├── batch_ref_6_budget_200_2038459_32.err
│   ├── batch_ref_6_budget_200_2038459_32.out
│   ├── batch_ref_6_budget_200_2038459_33.err
│   ├── batch_ref_6_budget_200_2038459_33.out
│   ├── batch_ref_6_budget_200_2038459_34.err
│   ├── batch_ref_6_budget_200_2038459_34.out
│   ├── batch_ref_6_budget_200_2038459_35.err
│   ├── batch_ref_6_budget_200_2038459_35.out
│   ├── batch_ref_6_budget_200_2038459_36.err
│   ├── batch_ref_6_budget_200_2038459_36.out
│   ├── batch_ref_6_budget_200_2038459_37.err
│   ├── batch_ref_6_budget_200_2038459_37.out
│   ├── batch_ref_6_budget_200_2038459_38.err
│   ├── batch_ref_6_budget_200_2038459_38.out
│   ├── batch_ref_6_budget_200_2038459_39.err
│   ├── batch_ref_6_budget_200_2038459_39.out
│   ├── batch_ref_6_budget_200_2038459_4.err
│   ├── batch_ref_6_budget_200_2038459_4.out
│   ├── batch_ref_6_budget_200_2038459_40.err
│   ├── batch_ref_6_budget_200_2038459_40.out
│   ├── batch_ref_6_budget_200_2038459_41.err
│   ├── batch_ref_6_budget_200_2038459_41.out
│   ├── batch_ref_6_budget_200_2038459_42.err
│   ├── batch_ref_6_budget_200_2038459_42.out
│   ├── batch_ref_6_budget_200_2038459_43.err
│   ├── batch_ref_6_budget_200_2038459_43.out
│   ├── batch_ref_6_budget_200_2038459_44.err
│   ├── batch_ref_6_budget_200_2038459_44.out
│   ├── batch_ref_6_budget_200_2038459_45.err
│   ├── batch_ref_6_budget_200_2038459_45.out
│   ├── batch_ref_6_budget_200_2038459_46.err
│   ├── batch_ref_6_budget_200_2038459_46.out
│   ├── batch_ref_6_budget_200_2038459_47.err
│   ├── batch_ref_6_budget_200_2038459_47.out
│   ├── batch_ref_6_budget_200_2038459_48.err
│   ├── batch_ref_6_budget_200_2038459_48.out
│   ├── batch_ref_6_budget_200_2038459_49.err
│   ├── batch_ref_6_budget_200_2038459_49.out
│   ├── batch_ref_6_budget_200_2038459_5.err
│   ├── batch_ref_6_budget_200_2038459_5.out
│   ├── batch_ref_6_budget_200_2038459_50.err
│   ├── batch_ref_6_budget_200_2038459_50.out
│   ├── batch_ref_6_budget_200_2038459_51.err
│   ├── batch_ref_6_budget_200_2038459_51.out
│   ├── batch_ref_6_budget_200_2038459_52.err
│   ├── batch_ref_6_budget_200_2038459_52.out
│   ├── batch_ref_6_budget_200_2038459_53.err
│   ├── batch_ref_6_budget_200_2038459_53.out
│   ├── batch_ref_6_budget_200_2038459_54.err
│   ├── batch_ref_6_budget_200_2038459_54.out
│   ├── batch_ref_6_budget_200_2038459_55.err
│   ├── batch_ref_6_budget_200_2038459_55.out
│   ├── batch_ref_6_budget_200_2038459_56.err
│   ├── batch_ref_6_budget_200_2038459_56.out
│   ├── batch_ref_6_budget_200_2038459_57.err
│   ├── batch_ref_6_budget_200_2038459_57.out
│   ├── batch_ref_6_budget_200_2038459_58.err
│   ├── batch_ref_6_budget_200_2038459_58.out
│   ├── batch_ref_6_budget_200_2038459_59.err
│   ├── batch_ref_6_budget_200_2038459_59.out
│   ├── batch_ref_6_budget_200_2038459_6.err
│   ├── batch_ref_6_budget_200_2038459_6.out
│   ├── batch_ref_6_budget_200_2038459_60.err
│   ├── batch_ref_6_budget_200_2038459_60.out
│   ├── batch_ref_6_budget_200_2038459_61.err
│   ├── batch_ref_6_budget_200_2038459_61.out
│   ├── batch_ref_6_budget_200_2038459_62.err
│   ├── batch_ref_6_budget_200_2038459_62.out
│   ├── batch_ref_6_budget_200_2038459_63.err
│   ├── batch_ref_6_budget_200_2038459_63.out
│   ├── batch_ref_6_budget_200_2038459_64.err
│   ├── batch_ref_6_budget_200_2038459_64.out
│   ├── batch_ref_6_budget_200_2038459_65.err
│   ├── batch_ref_6_budget_200_2038459_65.out
│   ├── batch_ref_6_budget_200_2038459_66.err
│   ├── batch_ref_6_budget_200_2038459_66.out
│   ├── batch_ref_6_budget_200_2038459_67.err
│   ├── batch_ref_6_budget_200_2038459_67.out
│   ├── batch_ref_6_budget_200_2038459_68.err
│   ├── batch_ref_6_budget_200_2038459_68.out
│   ├── batch_ref_6_budget_200_2038459_69.err
│   ├── batch_ref_6_budget_200_2038459_69.out
│   ├── batch_ref_6_budget_200_2038459_7.err
│   ├── batch_ref_6_budget_200_2038459_7.out
│   ├── batch_ref_6_budget_200_2038459_70.err
│   ├── batch_ref_6_budget_200_2038459_70.out
│   ├── batch_ref_6_budget_200_2038459_71.err
│   ├── batch_ref_6_budget_200_2038459_71.out
│   ├── batch_ref_6_budget_200_2038459_72.err
│   ├── batch_ref_6_budget_200_2038459_72.out
│   ├── batch_ref_6_budget_200_2038459_73.err
│   ├── batch_ref_6_budget_200_2038459_73.out
│   ├── batch_ref_6_budget_200_2038459_74.err
│   ├── batch_ref_6_budget_200_2038459_74.out
│   ├── batch_ref_6_budget_200_2038459_75.err
│   ├── batch_ref_6_budget_200_2038459_75.out
│   ├── batch_ref_6_budget_200_2038459_76.err
│   ├── batch_ref_6_budget_200_2038459_76.out
│   ├── batch_ref_6_budget_200_2038459_77.err
│   ├── batch_ref_6_budget_200_2038459_77.out
│   ├── batch_ref_6_budget_200_2038459_78.err
│   ├── batch_ref_6_budget_200_2038459_78.out
│   ├── batch_ref_6_budget_200_2038459_79.err
│   ├── batch_ref_6_budget_200_2038459_79.out
│   ├── batch_ref_6_budget_200_2038459_8.err
│   ├── batch_ref_6_budget_200_2038459_8.out
│   ├── batch_ref_6_budget_200_2038459_80.err
│   ├── batch_ref_6_budget_200_2038459_80.out
│   ├── batch_ref_6_budget_200_2038459_81.err
│   ├── batch_ref_6_budget_200_2038459_81.out
│   ├── batch_ref_6_budget_200_2038459_9.err
│   ├── batch_ref_6_budget_200_2038459_9.out
│   ├── batch_ref_6_budget_200_2040040_1.err
│   ├── batch_ref_6_budget_200_2040040_1.out
│   ├── batch_ref_6_budget_200_2040040_10.err
│   ├── batch_ref_6_budget_200_2040040_10.out
│   ├── batch_ref_6_budget_200_2040040_11.err
│   ├── batch_ref_6_budget_200_2040040_11.out
│   ├── batch_ref_6_budget_200_2040040_12.err
│   ├── batch_ref_6_budget_200_2040040_12.out
│   ├── batch_ref_6_budget_200_2040040_13.err
│   ├── batch_ref_6_budget_200_2040040_13.out
│   ├── batch_ref_6_budget_200_2040040_14.err
│   ├── batch_ref_6_budget_200_2040040_14.out
│   ├── batch_ref_6_budget_200_2040040_15.err
│   ├── batch_ref_6_budget_200_2040040_15.out
│   ├── batch_ref_6_budget_200_2040040_16.err
│   ├── batch_ref_6_budget_200_2040040_16.out
│   ├── batch_ref_6_budget_200_2040040_17.err
│   ├── batch_ref_6_budget_200_2040040_17.out
│   ├── batch_ref_6_budget_200_2040040_18.err
│   ├── batch_ref_6_budget_200_2040040_18.out
│   ├── batch_ref_6_budget_200_2040040_19.err
│   ├── batch_ref_6_budget_200_2040040_19.out
│   ├── batch_ref_6_budget_200_2040040_2.err
│   ├── batch_ref_6_budget_200_2040040_2.out
│   ├── batch_ref_6_budget_200_2040040_20.err
│   ├── batch_ref_6_budget_200_2040040_20.out
│   ├── batch_ref_6_budget_200_2040040_21.err
│   ├── batch_ref_6_budget_200_2040040_21.out
│   ├── batch_ref_6_budget_200_2040040_22.err
│   ├── batch_ref_6_budget_200_2040040_22.out
│   ├── batch_ref_6_budget_200_2040040_23.err
│   ├── batch_ref_6_budget_200_2040040_23.out
│   ├── batch_ref_6_budget_200_2040040_24.err
│   ├── batch_ref_6_budget_200_2040040_24.out
│   ├── batch_ref_6_budget_200_2040040_25.err
│   ├── batch_ref_6_budget_200_2040040_25.out
│   ├── batch_ref_6_budget_200_2040040_26.err
│   ├── batch_ref_6_budget_200_2040040_26.out
│   ├── batch_ref_6_budget_200_2040040_27.err
│   ├── batch_ref_6_budget_200_2040040_27.out
│   ├── batch_ref_6_budget_200_2040040_28.err
│   ├── batch_ref_6_budget_200_2040040_28.out
│   ├── batch_ref_6_budget_200_2040040_29.err
│   ├── batch_ref_6_budget_200_2040040_29.out
│   ├── batch_ref_6_budget_200_2040040_3.err
│   ├── batch_ref_6_budget_200_2040040_3.out
│   ├── batch_ref_6_budget_200_2040040_30.err
│   ├── batch_ref_6_budget_200_2040040_30.out
│   ├── batch_ref_6_budget_200_2040040_31.err
│   ├── batch_ref_6_budget_200_2040040_31.out
│   ├── batch_ref_6_budget_200_2040040_32.err
│   ├── batch_ref_6_budget_200_2040040_32.out
│   ├── batch_ref_6_budget_200_2040040_33.err
│   ├── batch_ref_6_budget_200_2040040_33.out
│   ├── batch_ref_6_budget_200_2040040_34.err
│   ├── batch_ref_6_budget_200_2040040_34.out
│   ├── batch_ref_6_budget_200_2040040_35.err
│   ├── batch_ref_6_budget_200_2040040_35.out
│   ├── batch_ref_6_budget_200_2040040_36.err
│   ├── batch_ref_6_budget_200_2040040_36.out
│   ├── batch_ref_6_budget_200_2040040_37.err
│   ├── batch_ref_6_budget_200_2040040_37.out
│   ├── batch_ref_6_budget_200_2040040_38.err
│   ├── batch_ref_6_budget_200_2040040_38.out
│   ├── batch_ref_6_budget_200_2040040_39.err
│   ├── batch_ref_6_budget_200_2040040_39.out
│   ├── batch_ref_6_budget_200_2040040_4.err
│   ├── batch_ref_6_budget_200_2040040_4.out
│   ├── batch_ref_6_budget_200_2040040_40.err
│   ├── batch_ref_6_budget_200_2040040_40.out
│   ├── batch_ref_6_budget_200_2040040_41.err
│   ├── batch_ref_6_budget_200_2040040_41.out
│   ├── batch_ref_6_budget_200_2040040_42.err
│   ├── batch_ref_6_budget_200_2040040_42.out
│   ├── batch_ref_6_budget_200_2040040_43.err
│   ├── batch_ref_6_budget_200_2040040_43.out
│   ├── batch_ref_6_budget_200_2040040_44.err
│   ├── batch_ref_6_budget_200_2040040_44.out
│   ├── batch_ref_6_budget_200_2040040_45.err
│   ├── batch_ref_6_budget_200_2040040_45.out
│   ├── batch_ref_6_budget_200_2040040_46.err
│   ├── batch_ref_6_budget_200_2040040_46.out
│   ├── batch_ref_6_budget_200_2040040_47.err
│   ├── batch_ref_6_budget_200_2040040_47.out
│   ├── batch_ref_6_budget_200_2040040_48.err
│   ├── batch_ref_6_budget_200_2040040_48.out
│   ├── batch_ref_6_budget_200_2040040_49.err
│   ├── batch_ref_6_budget_200_2040040_49.out
│   ├── batch_ref_6_budget_200_2040040_5.err
│   ├── batch_ref_6_budget_200_2040040_5.out
│   ├── batch_ref_6_budget_200_2040040_50.err
│   ├── batch_ref_6_budget_200_2040040_50.out
│   ├── batch_ref_6_budget_200_2040040_51.err
│   ├── batch_ref_6_budget_200_2040040_51.out
│   ├── batch_ref_6_budget_200_2040040_52.err
│   ├── batch_ref_6_budget_200_2040040_52.out
│   ├── batch_ref_6_budget_200_2040040_53.err
│   ├── batch_ref_6_budget_200_2040040_53.out
│   ├── batch_ref_6_budget_200_2040040_54.err
│   ├── batch_ref_6_budget_200_2040040_54.out
│   ├── batch_ref_6_budget_200_2040040_55.err
│   ├── batch_ref_6_budget_200_2040040_55.out
│   ├── batch_ref_6_budget_200_2040040_56.err
│   ├── batch_ref_6_budget_200_2040040_56.out
│   ├── batch_ref_6_budget_200_2040040_57.err
│   ├── batch_ref_6_budget_200_2040040_57.out
│   ├── batch_ref_6_budget_200_2040040_58.err
│   ├── batch_ref_6_budget_200_2040040_58.out
│   ├── batch_ref_6_budget_200_2040040_59.err
│   ├── batch_ref_6_budget_200_2040040_59.out
│   ├── batch_ref_6_budget_200_2040040_6.err
│   ├── batch_ref_6_budget_200_2040040_6.out
│   ├── batch_ref_6_budget_200_2040040_60.err
│   ├── batch_ref_6_budget_200_2040040_60.out
│   ├── batch_ref_6_budget_200_2040040_61.err
│   ├── batch_ref_6_budget_200_2040040_61.out
│   ├── batch_ref_6_budget_200_2040040_62.err
│   ├── batch_ref_6_budget_200_2040040_62.out
│   ├── batch_ref_6_budget_200_2040040_63.err
│   ├── batch_ref_6_budget_200_2040040_63.out
│   ├── batch_ref_6_budget_200_2040040_64.err
│   ├── batch_ref_6_budget_200_2040040_64.out
│   ├── batch_ref_6_budget_200_2040040_65.err
│   ├── batch_ref_6_budget_200_2040040_65.out
│   ├── batch_ref_6_budget_200_2040040_66.err
│   ├── batch_ref_6_budget_200_2040040_66.out
│   ├── batch_ref_6_budget_200_2040040_67.err
│   ├── batch_ref_6_budget_200_2040040_67.out
│   ├── batch_ref_6_budget_200_2040040_68.err
│   ├── batch_ref_6_budget_200_2040040_68.out
│   ├── batch_ref_6_budget_200_2040040_69.err
│   ├── batch_ref_6_budget_200_2040040_69.out
│   ├── batch_ref_6_budget_200_2040040_7.err
│   ├── batch_ref_6_budget_200_2040040_7.out
│   ├── batch_ref_6_budget_200_2040040_70.err
│   ├── batch_ref_6_budget_200_2040040_70.out
│   ├── batch_ref_6_budget_200_2040040_71.err
│   ├── batch_ref_6_budget_200_2040040_71.out
│   ├── batch_ref_6_budget_200_2040040_72.err
│   ├── batch_ref_6_budget_200_2040040_72.out
│   ├── batch_ref_6_budget_200_2040040_73.err
│   ├── batch_ref_6_budget_200_2040040_73.out
│   ├── batch_ref_6_budget_200_2040040_74.err
│   ├── batch_ref_6_budget_200_2040040_74.out
│   ├── batch_ref_6_budget_200_2040040_75.err
│   ├── batch_ref_6_budget_200_2040040_75.out
│   ├── batch_ref_6_budget_200_2040040_76.err
│   ├── batch_ref_6_budget_200_2040040_76.out
│   ├── batch_ref_6_budget_200_2040040_77.err
│   ├── batch_ref_6_budget_200_2040040_77.out
│   ├── batch_ref_6_budget_200_2040040_78.err
│   ├── batch_ref_6_budget_200_2040040_78.out
│   ├── batch_ref_6_budget_200_2040040_79.err
│   ├── batch_ref_6_budget_200_2040040_79.out
│   ├── batch_ref_6_budget_200_2040040_8.err
│   ├── batch_ref_6_budget_200_2040040_8.out
│   ├── batch_ref_6_budget_200_2040040_80.err
│   ├── batch_ref_6_budget_200_2040040_80.out
│   ├── batch_ref_6_budget_200_2040040_81.err
│   ├── batch_ref_6_budget_200_2040040_81.out
│   ├── batch_ref_6_budget_200_2040040_9.err
│   ├── batch_ref_6_budget_200_2040040_9.out
│   ├── batch_ref_6_budget_300_2019672_1.err
│   ├── batch_ref_6_budget_300_2019672_1.out
│   ├── batch_ref_6_budget_300_2019672_10.err
│   ├── batch_ref_6_budget_300_2019672_10.out
│   ├── batch_ref_6_budget_300_2019672_11.err
│   ├── batch_ref_6_budget_300_2019672_11.out
│   ├── batch_ref_6_budget_300_2019672_12.err
│   ├── batch_ref_6_budget_300_2019672_12.out
│   ├── batch_ref_6_budget_300_2019672_13.err
│   ├── batch_ref_6_budget_300_2019672_13.out
│   ├── batch_ref_6_budget_300_2019672_14.err
│   ├── batch_ref_6_budget_300_2019672_14.out
│   ├── batch_ref_6_budget_300_2019672_15.err
│   ├── batch_ref_6_budget_300_2019672_15.out
│   ├── batch_ref_6_budget_300_2019672_16.err
│   ├── batch_ref_6_budget_300_2019672_16.out
│   ├── batch_ref_6_budget_300_2019672_17.err
│   ├── batch_ref_6_budget_300_2019672_17.out
│   ├── batch_ref_6_budget_300_2019672_18.err
│   ├── batch_ref_6_budget_300_2019672_18.out
│   ├── batch_ref_6_budget_300_2019672_19.err
│   ├── batch_ref_6_budget_300_2019672_19.out
│   ├── batch_ref_6_budget_300_2019672_2.err
│   ├── batch_ref_6_budget_300_2019672_2.out
│   ├── batch_ref_6_budget_300_2019672_20.err
│   ├── batch_ref_6_budget_300_2019672_20.out
│   ├── batch_ref_6_budget_300_2019672_21.err
│   ├── batch_ref_6_budget_300_2019672_21.out
│   ├── batch_ref_6_budget_300_2019672_22.err
│   ├── batch_ref_6_budget_300_2019672_22.out
│   ├── batch_ref_6_budget_300_2019672_23.err
│   ├── batch_ref_6_budget_300_2019672_23.out
│   ├── batch_ref_6_budget_300_2019672_24.err
│   ├── batch_ref_6_budget_300_2019672_24.out
│   ├── batch_ref_6_budget_300_2019672_25.err
│   ├── batch_ref_6_budget_300_2019672_25.out
│   ├── batch_ref_6_budget_300_2019672_26.err
│   ├── batch_ref_6_budget_300_2019672_26.out
│   ├── batch_ref_6_budget_300_2019672_27.err
│   ├── batch_ref_6_budget_300_2019672_27.out
│   ├── batch_ref_6_budget_300_2019672_28.err
│   ├── batch_ref_6_budget_300_2019672_28.out
│   ├── batch_ref_6_budget_300_2019672_29.err
│   ├── batch_ref_6_budget_300_2019672_29.out
│   ├── batch_ref_6_budget_300_2019672_3.err
│   ├── batch_ref_6_budget_300_2019672_3.out
│   ├── batch_ref_6_budget_300_2019672_30.err
│   ├── batch_ref_6_budget_300_2019672_30.out
│   ├── batch_ref_6_budget_300_2019672_31.err
│   ├── batch_ref_6_budget_300_2019672_31.out
│   ├── batch_ref_6_budget_300_2019672_32.err
│   ├── batch_ref_6_budget_300_2019672_32.out
│   ├── batch_ref_6_budget_300_2019672_33.err
│   ├── batch_ref_6_budget_300_2019672_33.out
│   ├── batch_ref_6_budget_300_2019672_34.err
│   ├── batch_ref_6_budget_300_2019672_34.out
│   ├── batch_ref_6_budget_300_2019672_35.err
│   ├── batch_ref_6_budget_300_2019672_35.out
│   ├── batch_ref_6_budget_300_2019672_36.err
│   ├── batch_ref_6_budget_300_2019672_36.out
│   ├── batch_ref_6_budget_300_2019672_37.err
│   ├── batch_ref_6_budget_300_2019672_37.out
│   ├── batch_ref_6_budget_300_2019672_38.err
│   ├── batch_ref_6_budget_300_2019672_38.out
│   ├── batch_ref_6_budget_300_2019672_39.err
│   ├── batch_ref_6_budget_300_2019672_39.out
│   ├── batch_ref_6_budget_300_2019672_4.err
│   ├── batch_ref_6_budget_300_2019672_4.out
│   ├── batch_ref_6_budget_300_2019672_40.err
│   ├── batch_ref_6_budget_300_2019672_40.out
│   ├── batch_ref_6_budget_300_2019672_41.err
│   ├── batch_ref_6_budget_300_2019672_41.out
│   ├── batch_ref_6_budget_300_2019672_42.err
│   ├── batch_ref_6_budget_300_2019672_42.out
│   ├── batch_ref_6_budget_300_2019672_43.err
│   ├── batch_ref_6_budget_300_2019672_43.out
│   ├── batch_ref_6_budget_300_2019672_44.err
│   ├── batch_ref_6_budget_300_2019672_44.out
│   ├── batch_ref_6_budget_300_2019672_45.err
│   ├── batch_ref_6_budget_300_2019672_45.out
│   ├── batch_ref_6_budget_300_2019672_46.err
│   ├── batch_ref_6_budget_300_2019672_46.out
│   ├── batch_ref_6_budget_300_2019672_47.err
│   ├── batch_ref_6_budget_300_2019672_47.out
│   ├── batch_ref_6_budget_300_2019672_48.err
│   ├── batch_ref_6_budget_300_2019672_48.out
│   ├── batch_ref_6_budget_300_2019672_49.err
│   ├── batch_ref_6_budget_300_2019672_49.out
│   ├── batch_ref_6_budget_300_2019672_5.err
│   ├── batch_ref_6_budget_300_2019672_5.out
│   ├── batch_ref_6_budget_300_2019672_50.err
│   ├── batch_ref_6_budget_300_2019672_50.out
│   ├── batch_ref_6_budget_300_2019672_51.err
│   ├── batch_ref_6_budget_300_2019672_51.out
│   ├── batch_ref_6_budget_300_2019672_52.err
│   ├── batch_ref_6_budget_300_2019672_52.out
│   ├── batch_ref_6_budget_300_2019672_53.err
│   ├── batch_ref_6_budget_300_2019672_53.out
│   ├── batch_ref_6_budget_300_2019672_54.err
│   ├── batch_ref_6_budget_300_2019672_54.out
│   ├── batch_ref_6_budget_300_2019672_55.err
│   ├── batch_ref_6_budget_300_2019672_55.out
│   ├── batch_ref_6_budget_300_2019672_56.err
│   ├── batch_ref_6_budget_300_2019672_56.out
│   ├── batch_ref_6_budget_300_2019672_57.err
│   ├── batch_ref_6_budget_300_2019672_57.out
│   ├── batch_ref_6_budget_300_2019672_58.err
│   ├── batch_ref_6_budget_300_2019672_58.out
│   ├── batch_ref_6_budget_300_2019672_59.err
│   ├── batch_ref_6_budget_300_2019672_59.out
│   ├── batch_ref_6_budget_300_2019672_6.err
│   ├── batch_ref_6_budget_300_2019672_6.out
│   ├── batch_ref_6_budget_300_2019672_60.err
│   ├── batch_ref_6_budget_300_2019672_60.out
│   ├── batch_ref_6_budget_300_2019672_61.err
│   ├── batch_ref_6_budget_300_2019672_61.out
│   ├── batch_ref_6_budget_300_2019672_62.err
│   ├── batch_ref_6_budget_300_2019672_62.out
│   ├── batch_ref_6_budget_300_2019672_63.err
│   ├── batch_ref_6_budget_300_2019672_63.out
│   ├── batch_ref_6_budget_300_2019672_64.err
│   ├── batch_ref_6_budget_300_2019672_64.out
│   ├── batch_ref_6_budget_300_2019672_65.err
│   ├── batch_ref_6_budget_300_2019672_65.out
│   ├── batch_ref_6_budget_300_2019672_66.err
│   ├── batch_ref_6_budget_300_2019672_66.out
│   ├── batch_ref_6_budget_300_2019672_67.err
│   ├── batch_ref_6_budget_300_2019672_67.out
│   ├── batch_ref_6_budget_300_2019672_68.err
│   ├── batch_ref_6_budget_300_2019672_68.out
│   ├── batch_ref_6_budget_300_2019672_69.err
│   ├── batch_ref_6_budget_300_2019672_69.out
│   ├── batch_ref_6_budget_300_2019672_7.err
│   ├── batch_ref_6_budget_300_2019672_7.out
│   ├── batch_ref_6_budget_300_2019672_70.err
│   ├── batch_ref_6_budget_300_2019672_70.out
│   ├── batch_ref_6_budget_300_2019672_71.err
│   ├── batch_ref_6_budget_300_2019672_71.out
│   ├── batch_ref_6_budget_300_2019672_72.err
│   ├── batch_ref_6_budget_300_2019672_72.out
│   ├── batch_ref_6_budget_300_2019672_73.err
│   ├── batch_ref_6_budget_300_2019672_73.out
│   ├── batch_ref_6_budget_300_2019672_74.err
│   ├── batch_ref_6_budget_300_2019672_74.out
│   ├── batch_ref_6_budget_300_2019672_75.err
│   ├── batch_ref_6_budget_300_2019672_75.out
│   ├── batch_ref_6_budget_300_2019672_76.err
│   ├── batch_ref_6_budget_300_2019672_76.out
│   ├── batch_ref_6_budget_300_2019672_77.err
│   ├── batch_ref_6_budget_300_2019672_77.out
│   ├── batch_ref_6_budget_300_2019672_78.err
│   ├── batch_ref_6_budget_300_2019672_78.out
│   ├── batch_ref_6_budget_300_2019672_79.err
│   ├── batch_ref_6_budget_300_2019672_79.out
│   ├── batch_ref_6_budget_300_2019672_8.err
│   ├── batch_ref_6_budget_300_2019672_8.out
│   ├── batch_ref_6_budget_300_2019672_80.err
│   ├── batch_ref_6_budget_300_2019672_80.out
│   ├── batch_ref_6_budget_300_2019672_81.err
│   ├── batch_ref_6_budget_300_2019672_81.out
│   ├── batch_ref_6_budget_300_2019672_9.err
│   ├── batch_ref_6_budget_300_2019672_9.out
│   ├── batch_ref_6_budget_300_2040041_1.err
│   ├── batch_ref_6_budget_300_2040041_1.out
│   ├── batch_ref_6_budget_300_2040041_10.err
│   ├── batch_ref_6_budget_300_2040041_10.out
│   ├── batch_ref_6_budget_300_2040041_11.err
│   ├── batch_ref_6_budget_300_2040041_11.out
│   ├── batch_ref_6_budget_300_2040041_12.err
│   ├── batch_ref_6_budget_300_2040041_12.out
│   ├── batch_ref_6_budget_300_2040041_13.err
│   ├── batch_ref_6_budget_300_2040041_13.out
│   ├── batch_ref_6_budget_300_2040041_14.err
│   ├── batch_ref_6_budget_300_2040041_14.out
│   ├── batch_ref_6_budget_300_2040041_15.err
│   ├── batch_ref_6_budget_300_2040041_15.out
│   ├── batch_ref_6_budget_300_2040041_16.err
│   ├── batch_ref_6_budget_300_2040041_16.out
│   ├── batch_ref_6_budget_300_2040041_17.err
│   ├── batch_ref_6_budget_300_2040041_17.out
│   ├── batch_ref_6_budget_300_2040041_18.err
│   ├── batch_ref_6_budget_300_2040041_18.out
│   ├── batch_ref_6_budget_300_2040041_19.err
│   ├── batch_ref_6_budget_300_2040041_19.out
│   ├── batch_ref_6_budget_300_2040041_2.err
│   ├── batch_ref_6_budget_300_2040041_2.out
│   ├── batch_ref_6_budget_300_2040041_20.err
│   ├── batch_ref_6_budget_300_2040041_20.out
│   ├── batch_ref_6_budget_300_2040041_21.err
│   ├── batch_ref_6_budget_300_2040041_21.out
│   ├── batch_ref_6_budget_300_2040041_22.err
│   ├── batch_ref_6_budget_300_2040041_22.out
│   ├── batch_ref_6_budget_300_2040041_23.err
│   ├── batch_ref_6_budget_300_2040041_23.out
│   ├── batch_ref_6_budget_300_2040041_24.err
│   ├── batch_ref_6_budget_300_2040041_24.out
│   ├── batch_ref_6_budget_300_2040041_25.err
│   ├── batch_ref_6_budget_300_2040041_25.out
│   ├── batch_ref_6_budget_300_2040041_26.err
│   ├── batch_ref_6_budget_300_2040041_26.out
│   ├── batch_ref_6_budget_300_2040041_27.err
│   ├── batch_ref_6_budget_300_2040041_27.out
│   ├── batch_ref_6_budget_300_2040041_28.err
│   ├── batch_ref_6_budget_300_2040041_28.out
│   ├── batch_ref_6_budget_300_2040041_29.err
│   ├── batch_ref_6_budget_300_2040041_29.out
│   ├── batch_ref_6_budget_300_2040041_3.err
│   ├── batch_ref_6_budget_300_2040041_3.out
│   ├── batch_ref_6_budget_300_2040041_30.err
│   ├── batch_ref_6_budget_300_2040041_30.out
│   ├── batch_ref_6_budget_300_2040041_31.err
│   ├── batch_ref_6_budget_300_2040041_31.out
│   ├── batch_ref_6_budget_300_2040041_32.err
│   ├── batch_ref_6_budget_300_2040041_32.out
│   ├── batch_ref_6_budget_300_2040041_33.err
│   ├── batch_ref_6_budget_300_2040041_33.out
│   ├── batch_ref_6_budget_300_2040041_34.err
│   ├── batch_ref_6_budget_300_2040041_34.out
│   ├── batch_ref_6_budget_300_2040041_35.err
│   ├── batch_ref_6_budget_300_2040041_35.out
│   ├── batch_ref_6_budget_300_2040041_36.err
│   ├── batch_ref_6_budget_300_2040041_36.out
│   ├── batch_ref_6_budget_300_2040041_37.err
│   ├── batch_ref_6_budget_300_2040041_37.out
│   ├── batch_ref_6_budget_300_2040041_38.err
│   ├── batch_ref_6_budget_300_2040041_38.out
│   ├── batch_ref_6_budget_300_2040041_39.err
│   ├── batch_ref_6_budget_300_2040041_39.out
│   ├── batch_ref_6_budget_300_2040041_4.err
│   ├── batch_ref_6_budget_300_2040041_4.out
│   ├── batch_ref_6_budget_300_2040041_40.err
│   ├── batch_ref_6_budget_300_2040041_40.out
│   ├── batch_ref_6_budget_300_2040041_41.err
│   ├── batch_ref_6_budget_300_2040041_41.out
│   ├── batch_ref_6_budget_300_2040041_42.err
│   ├── batch_ref_6_budget_300_2040041_42.out
│   ├── batch_ref_6_budget_300_2040041_43.err
│   ├── batch_ref_6_budget_300_2040041_43.out
│   ├── batch_ref_6_budget_300_2040041_44.err
│   ├── batch_ref_6_budget_300_2040041_44.out
│   ├── batch_ref_6_budget_300_2040041_45.err
│   ├── batch_ref_6_budget_300_2040041_45.out
│   ├── batch_ref_6_budget_300_2040041_46.err
│   ├── batch_ref_6_budget_300_2040041_46.out
│   ├── batch_ref_6_budget_300_2040041_47.err
│   ├── batch_ref_6_budget_300_2040041_47.out
│   ├── batch_ref_6_budget_300_2040041_48.err
│   ├── batch_ref_6_budget_300_2040041_48.out
│   ├── batch_ref_6_budget_300_2040041_49.err
│   ├── batch_ref_6_budget_300_2040041_49.out
│   ├── batch_ref_6_budget_300_2040041_5.err
│   ├── batch_ref_6_budget_300_2040041_5.out
│   ├── batch_ref_6_budget_300_2040041_50.err
│   ├── batch_ref_6_budget_300_2040041_50.out
│   ├── batch_ref_6_budget_300_2040041_51.err
│   ├── batch_ref_6_budget_300_2040041_51.out
│   ├── batch_ref_6_budget_300_2040041_52.err
│   ├── batch_ref_6_budget_300_2040041_52.out
│   ├── batch_ref_6_budget_300_2040041_53.err
│   ├── batch_ref_6_budget_300_2040041_53.out
│   ├── batch_ref_6_budget_300_2040041_54.err
│   ├── batch_ref_6_budget_300_2040041_54.out
│   ├── batch_ref_6_budget_300_2040041_55.err
│   ├── batch_ref_6_budget_300_2040041_55.out
│   ├── batch_ref_6_budget_300_2040041_56.err
│   ├── batch_ref_6_budget_300_2040041_56.out
│   ├── batch_ref_6_budget_300_2040041_57.err
│   ├── batch_ref_6_budget_300_2040041_57.out
│   ├── batch_ref_6_budget_300_2040041_58.err
│   ├── batch_ref_6_budget_300_2040041_58.out
│   ├── batch_ref_6_budget_300_2040041_59.err
│   ├── batch_ref_6_budget_300_2040041_59.out
│   ├── batch_ref_6_budget_300_2040041_6.err
│   ├── batch_ref_6_budget_300_2040041_6.out
│   ├── batch_ref_6_budget_300_2040041_60.err
│   ├── batch_ref_6_budget_300_2040041_60.out
│   ├── batch_ref_6_budget_300_2040041_61.err
│   ├── batch_ref_6_budget_300_2040041_61.out
│   ├── batch_ref_6_budget_300_2040041_62.err
│   ├── batch_ref_6_budget_300_2040041_62.out
│   ├── batch_ref_6_budget_300_2040041_63.err
│   ├── batch_ref_6_budget_300_2040041_63.out
│   ├── batch_ref_6_budget_300_2040041_64.err
│   ├── batch_ref_6_budget_300_2040041_64.out
│   ├── batch_ref_6_budget_300_2040041_65.err
│   ├── batch_ref_6_budget_300_2040041_65.out
│   ├── batch_ref_6_budget_300_2040041_66.err
│   ├── batch_ref_6_budget_300_2040041_66.out
│   ├── batch_ref_6_budget_300_2040041_67.err
│   ├── batch_ref_6_budget_300_2040041_67.out
│   ├── batch_ref_6_budget_300_2040041_68.err
│   ├── batch_ref_6_budget_300_2040041_68.out
│   ├── batch_ref_6_budget_300_2040041_69.err
│   ├── batch_ref_6_budget_300_2040041_69.out
│   ├── batch_ref_6_budget_300_2040041_7.err
│   ├── batch_ref_6_budget_300_2040041_7.out
│   ├── batch_ref_6_budget_300_2040041_70.err
│   ├── batch_ref_6_budget_300_2040041_70.out
│   ├── batch_ref_6_budget_300_2040041_71.err
│   ├── batch_ref_6_budget_300_2040041_71.out
│   ├── batch_ref_6_budget_300_2040041_72.err
│   ├── batch_ref_6_budget_300_2040041_72.out
│   ├── batch_ref_6_budget_300_2040041_73.err
│   ├── batch_ref_6_budget_300_2040041_73.out
│   ├── batch_ref_6_budget_300_2040041_74.err
│   ├── batch_ref_6_budget_300_2040041_74.out
│   ├── batch_ref_6_budget_300_2040041_75.err
│   ├── batch_ref_6_budget_300_2040041_75.out
│   ├── batch_ref_6_budget_300_2040041_76.err
│   ├── batch_ref_6_budget_300_2040041_76.out
│   ├── batch_ref_6_budget_300_2040041_77.err
│   ├── batch_ref_6_budget_300_2040041_77.out
│   ├── batch_ref_6_budget_300_2040041_78.err
│   ├── batch_ref_6_budget_300_2040041_78.out
│   ├── batch_ref_6_budget_300_2040041_79.err
│   ├── batch_ref_6_budget_300_2040041_79.out
│   ├── batch_ref_6_budget_300_2040041_8.err
│   ├── batch_ref_6_budget_300_2040041_8.out
│   ├── batch_ref_6_budget_300_2040041_80.err
│   ├── batch_ref_6_budget_300_2040041_80.out
│   ├── batch_ref_6_budget_300_2040041_81.err
│   ├── batch_ref_6_budget_300_2040041_81.out
│   ├── batch_ref_6_budget_300_2040041_9.err
│   ├── batch_ref_6_budget_300_2040041_9.out
│   ├── batch_ref_6_budget_50_2024775_1.err
│   ├── batch_ref_6_budget_50_2024775_1.out
│   ├── batch_ref_6_budget_50_2024775_10.err
│   ├── batch_ref_6_budget_50_2024775_10.out
│   ├── batch_ref_6_budget_50_2024775_11.err
│   ├── batch_ref_6_budget_50_2024775_11.out
│   ├── batch_ref_6_budget_50_2024775_12.err
│   ├── batch_ref_6_budget_50_2024775_12.out
│   ├── batch_ref_6_budget_50_2024775_13.err
│   ├── batch_ref_6_budget_50_2024775_13.out
│   ├── batch_ref_6_budget_50_2024775_14.err
│   ├── batch_ref_6_budget_50_2024775_14.out
│   ├── batch_ref_6_budget_50_2024775_15.err
│   ├── batch_ref_6_budget_50_2024775_15.out
│   ├── batch_ref_6_budget_50_2024775_16.err
│   ├── batch_ref_6_budget_50_2024775_16.out
│   ├── batch_ref_6_budget_50_2024775_17.err
│   ├── batch_ref_6_budget_50_2024775_17.out
│   ├── batch_ref_6_budget_50_2024775_18.err
│   ├── batch_ref_6_budget_50_2024775_18.out
│   ├── batch_ref_6_budget_50_2024775_19.err
│   ├── batch_ref_6_budget_50_2024775_19.out
│   ├── batch_ref_6_budget_50_2024775_2.err
│   ├── batch_ref_6_budget_50_2024775_2.out
│   ├── batch_ref_6_budget_50_2024775_20.err
│   ├── batch_ref_6_budget_50_2024775_20.out
│   ├── batch_ref_6_budget_50_2024775_21.err
│   ├── batch_ref_6_budget_50_2024775_21.out
│   ├── batch_ref_6_budget_50_2024775_22.err
│   ├── batch_ref_6_budget_50_2024775_22.out
│   ├── batch_ref_6_budget_50_2024775_23.err
│   ├── batch_ref_6_budget_50_2024775_23.out
│   ├── batch_ref_6_budget_50_2024775_24.err
│   ├── batch_ref_6_budget_50_2024775_24.out
│   ├── batch_ref_6_budget_50_2024775_25.err
│   ├── batch_ref_6_budget_50_2024775_25.out
│   ├── batch_ref_6_budget_50_2024775_26.err
│   ├── batch_ref_6_budget_50_2024775_26.out
│   ├── batch_ref_6_budget_50_2024775_27.err
│   ├── batch_ref_6_budget_50_2024775_27.out
│   ├── batch_ref_6_budget_50_2024775_28.err
│   ├── batch_ref_6_budget_50_2024775_28.out
│   ├── batch_ref_6_budget_50_2024775_29.err
│   ├── batch_ref_6_budget_50_2024775_29.out
│   ├── batch_ref_6_budget_50_2024775_3.err
│   ├── batch_ref_6_budget_50_2024775_3.out
│   ├── batch_ref_6_budget_50_2024775_30.err
│   ├── batch_ref_6_budget_50_2024775_30.out
│   ├── batch_ref_6_budget_50_2024775_31.err
│   ├── batch_ref_6_budget_50_2024775_31.out
│   ├── batch_ref_6_budget_50_2024775_32.err
│   ├── batch_ref_6_budget_50_2024775_32.out
│   ├── batch_ref_6_budget_50_2024775_33.err
│   ├── batch_ref_6_budget_50_2024775_33.out
│   ├── batch_ref_6_budget_50_2024775_34.err
│   ├── batch_ref_6_budget_50_2024775_34.out
│   ├── batch_ref_6_budget_50_2024775_35.err
│   ├── batch_ref_6_budget_50_2024775_35.out
│   ├── batch_ref_6_budget_50_2024775_36.err
│   ├── batch_ref_6_budget_50_2024775_36.out
│   ├── batch_ref_6_budget_50_2024775_37.err
│   ├── batch_ref_6_budget_50_2024775_37.out
│   ├── batch_ref_6_budget_50_2024775_38.err
│   ├── batch_ref_6_budget_50_2024775_38.out
│   ├── batch_ref_6_budget_50_2024775_39.err
│   ├── batch_ref_6_budget_50_2024775_39.out
│   ├── batch_ref_6_budget_50_2024775_4.err
│   ├── batch_ref_6_budget_50_2024775_4.out
│   ├── batch_ref_6_budget_50_2024775_40.err
│   ├── batch_ref_6_budget_50_2024775_40.out
│   ├── batch_ref_6_budget_50_2024775_41.err
│   ├── batch_ref_6_budget_50_2024775_41.out
│   ├── batch_ref_6_budget_50_2024775_42.err
│   ├── batch_ref_6_budget_50_2024775_42.out
│   ├── batch_ref_6_budget_50_2024775_43.err
│   ├── batch_ref_6_budget_50_2024775_43.out
│   ├── batch_ref_6_budget_50_2024775_44.err
│   ├── batch_ref_6_budget_50_2024775_44.out
│   ├── batch_ref_6_budget_50_2024775_45.err
│   ├── batch_ref_6_budget_50_2024775_45.out
│   ├── batch_ref_6_budget_50_2024775_46.err
│   ├── batch_ref_6_budget_50_2024775_46.out
│   ├── batch_ref_6_budget_50_2024775_47.err
│   ├── batch_ref_6_budget_50_2024775_47.out
│   ├── batch_ref_6_budget_50_2024775_48.err
│   ├── batch_ref_6_budget_50_2024775_48.out
│   ├── batch_ref_6_budget_50_2024775_49.err
│   ├── batch_ref_6_budget_50_2024775_49.out
│   ├── batch_ref_6_budget_50_2024775_5.err
│   ├── batch_ref_6_budget_50_2024775_5.out
│   ├── batch_ref_6_budget_50_2024775_50.err
│   ├── batch_ref_6_budget_50_2024775_50.out
│   ├── batch_ref_6_budget_50_2024775_51.err
│   ├── batch_ref_6_budget_50_2024775_51.out
│   ├── batch_ref_6_budget_50_2024775_52.err
│   ├── batch_ref_6_budget_50_2024775_52.out
│   ├── batch_ref_6_budget_50_2024775_53.err
│   ├── batch_ref_6_budget_50_2024775_53.out
│   ├── batch_ref_6_budget_50_2024775_54.err
│   ├── batch_ref_6_budget_50_2024775_54.out
│   ├── batch_ref_6_budget_50_2024775_55.err
│   ├── batch_ref_6_budget_50_2024775_55.out
│   ├── batch_ref_6_budget_50_2024775_56.err
│   ├── batch_ref_6_budget_50_2024775_56.out
│   ├── batch_ref_6_budget_50_2024775_57.err
│   ├── batch_ref_6_budget_50_2024775_57.out
│   ├── batch_ref_6_budget_50_2024775_58.err
│   ├── batch_ref_6_budget_50_2024775_58.out
│   ├── batch_ref_6_budget_50_2024775_59.err
│   ├── batch_ref_6_budget_50_2024775_59.out
│   ├── batch_ref_6_budget_50_2024775_6.err
│   ├── batch_ref_6_budget_50_2024775_6.out
│   ├── batch_ref_6_budget_50_2024775_60.err
│   ├── batch_ref_6_budget_50_2024775_60.out
│   ├── batch_ref_6_budget_50_2024775_61.err
│   ├── batch_ref_6_budget_50_2024775_61.out
│   ├── batch_ref_6_budget_50_2024775_62.err
│   ├── batch_ref_6_budget_50_2024775_62.out
│   ├── batch_ref_6_budget_50_2024775_63.err
│   ├── batch_ref_6_budget_50_2024775_63.out
│   ├── batch_ref_6_budget_50_2024775_64.err
│   ├── batch_ref_6_budget_50_2024775_64.out
│   ├── batch_ref_6_budget_50_2024775_65.err
│   ├── batch_ref_6_budget_50_2024775_65.out
│   ├── batch_ref_6_budget_50_2024775_66.err
│   ├── batch_ref_6_budget_50_2024775_66.out
│   ├── batch_ref_6_budget_50_2024775_67.err
│   ├── batch_ref_6_budget_50_2024775_67.out
│   ├── batch_ref_6_budget_50_2024775_68.err
│   ├── batch_ref_6_budget_50_2024775_68.out
│   ├── batch_ref_6_budget_50_2024775_69.err
│   ├── batch_ref_6_budget_50_2024775_69.out
│   ├── batch_ref_6_budget_50_2024775_7.err
│   ├── batch_ref_6_budget_50_2024775_7.out
│   ├── batch_ref_6_budget_50_2024775_70.err
│   ├── batch_ref_6_budget_50_2024775_70.out
│   ├── batch_ref_6_budget_50_2024775_71.err
│   ├── batch_ref_6_budget_50_2024775_71.out
│   ├── batch_ref_6_budget_50_2024775_72.err
│   ├── batch_ref_6_budget_50_2024775_72.out
│   ├── batch_ref_6_budget_50_2024775_73.err
│   ├── batch_ref_6_budget_50_2024775_73.out
│   ├── batch_ref_6_budget_50_2024775_74.err
│   ├── batch_ref_6_budget_50_2024775_74.out
│   ├── batch_ref_6_budget_50_2024775_75.err
│   ├── batch_ref_6_budget_50_2024775_75.out
│   ├── batch_ref_6_budget_50_2024775_76.err
│   ├── batch_ref_6_budget_50_2024775_76.out
│   ├── batch_ref_6_budget_50_2024775_77.err
│   ├── batch_ref_6_budget_50_2024775_77.out
│   ├── batch_ref_6_budget_50_2024775_78.err
│   ├── batch_ref_6_budget_50_2024775_78.out
│   ├── batch_ref_6_budget_50_2024775_79.err
│   ├── batch_ref_6_budget_50_2024775_79.out
│   ├── batch_ref_6_budget_50_2024775_8.err
│   ├── batch_ref_6_budget_50_2024775_8.out
│   ├── batch_ref_6_budget_50_2024775_80.err
│   ├── batch_ref_6_budget_50_2024775_80.out
│   ├── batch_ref_6_budget_50_2024775_81.err
│   ├── batch_ref_6_budget_50_2024775_81.out
│   ├── batch_ref_6_budget_50_2024775_9.err
│   ├── batch_ref_6_budget_50_2024775_9.out
│   ├── batch_ref_6_budget_50_2040042_1.err
│   ├── batch_ref_6_budget_50_2040042_1.out
│   ├── batch_ref_6_budget_50_2040042_10.err
│   ├── batch_ref_6_budget_50_2040042_10.out
│   ├── batch_ref_6_budget_50_2040042_11.err
│   ├── batch_ref_6_budget_50_2040042_11.out
│   ├── batch_ref_6_budget_50_2040042_12.err
│   ├── batch_ref_6_budget_50_2040042_12.out
│   ├── batch_ref_6_budget_50_2040042_13.err
│   ├── batch_ref_6_budget_50_2040042_13.out
│   ├── batch_ref_6_budget_50_2040042_14.err
│   ├── batch_ref_6_budget_50_2040042_14.out
│   ├── batch_ref_6_budget_50_2040042_15.err
│   ├── batch_ref_6_budget_50_2040042_15.out
│   ├── batch_ref_6_budget_50_2040042_16.err
│   ├── batch_ref_6_budget_50_2040042_16.out
│   ├── batch_ref_6_budget_50_2040042_17.err
│   ├── batch_ref_6_budget_50_2040042_17.out
│   ├── batch_ref_6_budget_50_2040042_18.err
│   ├── batch_ref_6_budget_50_2040042_18.out
│   ├── batch_ref_6_budget_50_2040042_19.err
│   ├── batch_ref_6_budget_50_2040042_19.out
│   ├── batch_ref_6_budget_50_2040042_2.err
│   ├── batch_ref_6_budget_50_2040042_2.out
│   ├── batch_ref_6_budget_50_2040042_20.err
│   ├── batch_ref_6_budget_50_2040042_20.out
│   ├── batch_ref_6_budget_50_2040042_21.err
│   ├── batch_ref_6_budget_50_2040042_21.out
│   ├── batch_ref_6_budget_50_2040042_22.err
│   ├── batch_ref_6_budget_50_2040042_22.out
│   ├── batch_ref_6_budget_50_2040042_23.err
│   ├── batch_ref_6_budget_50_2040042_23.out
│   ├── batch_ref_6_budget_50_2040042_24.err
│   ├── batch_ref_6_budget_50_2040042_24.out
│   ├── batch_ref_6_budget_50_2040042_25.err
│   ├── batch_ref_6_budget_50_2040042_25.out
│   ├── batch_ref_6_budget_50_2040042_26.err
│   ├── batch_ref_6_budget_50_2040042_26.out
│   ├── batch_ref_6_budget_50_2040042_27.err
│   ├── batch_ref_6_budget_50_2040042_27.out
│   ├── batch_ref_6_budget_50_2040042_28.err
│   ├── batch_ref_6_budget_50_2040042_28.out
│   ├── batch_ref_6_budget_50_2040042_29.err
│   ├── batch_ref_6_budget_50_2040042_29.out
│   ├── batch_ref_6_budget_50_2040042_3.err
│   ├── batch_ref_6_budget_50_2040042_3.out
│   ├── batch_ref_6_budget_50_2040042_30.err
│   ├── batch_ref_6_budget_50_2040042_30.out
│   ├── batch_ref_6_budget_50_2040042_31.err
│   ├── batch_ref_6_budget_50_2040042_31.out
│   ├── batch_ref_6_budget_50_2040042_32.err
│   ├── batch_ref_6_budget_50_2040042_32.out
│   ├── batch_ref_6_budget_50_2040042_33.err
│   ├── batch_ref_6_budget_50_2040042_33.out
│   ├── batch_ref_6_budget_50_2040042_34.err
│   ├── batch_ref_6_budget_50_2040042_34.out
│   ├── batch_ref_6_budget_50_2040042_35.err
│   ├── batch_ref_6_budget_50_2040042_35.out
│   ├── batch_ref_6_budget_50_2040042_36.err
│   ├── batch_ref_6_budget_50_2040042_36.out
│   ├── batch_ref_6_budget_50_2040042_37.err
│   ├── batch_ref_6_budget_50_2040042_37.out
│   ├── batch_ref_6_budget_50_2040042_38.err
│   ├── batch_ref_6_budget_50_2040042_38.out
│   ├── batch_ref_6_budget_50_2040042_39.err
│   ├── batch_ref_6_budget_50_2040042_39.out
│   ├── batch_ref_6_budget_50_2040042_4.err
│   ├── batch_ref_6_budget_50_2040042_4.out
│   ├── batch_ref_6_budget_50_2040042_40.err
│   ├── batch_ref_6_budget_50_2040042_40.out
│   ├── batch_ref_6_budget_50_2040042_41.err
│   ├── batch_ref_6_budget_50_2040042_41.out
│   ├── batch_ref_6_budget_50_2040042_42.err
│   ├── batch_ref_6_budget_50_2040042_42.out
│   ├── batch_ref_6_budget_50_2040042_43.err
│   ├── batch_ref_6_budget_50_2040042_43.out
│   ├── batch_ref_6_budget_50_2040042_44.err
│   ├── batch_ref_6_budget_50_2040042_44.out
│   ├── batch_ref_6_budget_50_2040042_45.err
│   ├── batch_ref_6_budget_50_2040042_45.out
│   ├── batch_ref_6_budget_50_2040042_46.err
│   ├── batch_ref_6_budget_50_2040042_46.out
│   ├── batch_ref_6_budget_50_2040042_47.err
│   ├── batch_ref_6_budget_50_2040042_47.out
│   ├── batch_ref_6_budget_50_2040042_48.err
│   ├── batch_ref_6_budget_50_2040042_48.out
│   ├── batch_ref_6_budget_50_2040042_49.err
│   ├── batch_ref_6_budget_50_2040042_49.out
│   ├── batch_ref_6_budget_50_2040042_5.err
│   ├── batch_ref_6_budget_50_2040042_5.out
│   ├── batch_ref_6_budget_50_2040042_50.err
│   ├── batch_ref_6_budget_50_2040042_50.out
│   ├── batch_ref_6_budget_50_2040042_51.err
│   ├── batch_ref_6_budget_50_2040042_51.out
│   ├── batch_ref_6_budget_50_2040042_52.err
│   ├── batch_ref_6_budget_50_2040042_52.out
│   ├── batch_ref_6_budget_50_2040042_53.err
│   ├── batch_ref_6_budget_50_2040042_53.out
│   ├── batch_ref_6_budget_50_2040042_54.err
│   ├── batch_ref_6_budget_50_2040042_54.out
│   ├── batch_ref_6_budget_50_2040042_55.err
│   ├── batch_ref_6_budget_50_2040042_55.out
│   ├── batch_ref_6_budget_50_2040042_56.err
│   ├── batch_ref_6_budget_50_2040042_56.out
│   ├── batch_ref_6_budget_50_2040042_57.err
│   ├── batch_ref_6_budget_50_2040042_57.out
│   ├── batch_ref_6_budget_50_2040042_58.err
│   ├── batch_ref_6_budget_50_2040042_58.out
│   ├── batch_ref_6_budget_50_2040042_59.err
│   ├── batch_ref_6_budget_50_2040042_59.out
│   ├── batch_ref_6_budget_50_2040042_6.err
│   ├── batch_ref_6_budget_50_2040042_6.out
│   ├── batch_ref_6_budget_50_2040042_60.err
│   ├── batch_ref_6_budget_50_2040042_60.out
│   ├── batch_ref_6_budget_50_2040042_61.err
│   ├── batch_ref_6_budget_50_2040042_61.out
│   ├── batch_ref_6_budget_50_2040042_62.err
│   ├── batch_ref_6_budget_50_2040042_62.out
│   ├── batch_ref_6_budget_50_2040042_63.err
│   ├── batch_ref_6_budget_50_2040042_63.out
│   ├── batch_ref_6_budget_50_2040042_64.err
│   ├── batch_ref_6_budget_50_2040042_64.out
│   ├── batch_ref_6_budget_50_2040042_65.err
│   ├── batch_ref_6_budget_50_2040042_65.out
│   ├── batch_ref_6_budget_50_2040042_66.err
│   ├── batch_ref_6_budget_50_2040042_66.out
│   ├── batch_ref_6_budget_50_2040042_67.err
│   ├── batch_ref_6_budget_50_2040042_67.out
│   ├── batch_ref_6_budget_50_2040042_68.err
│   ├── batch_ref_6_budget_50_2040042_68.out
│   ├── batch_ref_6_budget_50_2040042_69.err
│   ├── batch_ref_6_budget_50_2040042_69.out
│   ├── batch_ref_6_budget_50_2040042_7.err
│   ├── batch_ref_6_budget_50_2040042_7.out
│   ├── batch_ref_6_budget_50_2040042_70.err
│   ├── batch_ref_6_budget_50_2040042_70.out
│   ├── batch_ref_6_budget_50_2040042_71.err
│   ├── batch_ref_6_budget_50_2040042_71.out
│   ├── batch_ref_6_budget_50_2040042_72.err
│   ├── batch_ref_6_budget_50_2040042_72.out
│   ├── batch_ref_6_budget_50_2040042_73.err
│   ├── batch_ref_6_budget_50_2040042_73.out
│   ├── batch_ref_6_budget_50_2040042_74.err
│   ├── batch_ref_6_budget_50_2040042_74.out
│   ├── batch_ref_6_budget_50_2040042_75.err
│   ├── batch_ref_6_budget_50_2040042_75.out
│   ├── batch_ref_6_budget_50_2040042_76.err
│   ├── batch_ref_6_budget_50_2040042_76.out
│   ├── batch_ref_6_budget_50_2040042_77.err
│   ├── batch_ref_6_budget_50_2040042_77.out
│   ├── batch_ref_6_budget_50_2040042_78.err
│   ├── batch_ref_6_budget_50_2040042_78.out
│   ├── batch_ref_6_budget_50_2040042_79.err
│   ├── batch_ref_6_budget_50_2040042_79.out
│   ├── batch_ref_6_budget_50_2040042_8.err
│   ├── batch_ref_6_budget_50_2040042_8.out
│   ├── batch_ref_6_budget_50_2040042_80.err
│   ├── batch_ref_6_budget_50_2040042_80.out
│   ├── batch_ref_6_budget_50_2040042_81.err
│   ├── batch_ref_6_budget_50_2040042_81.out
│   ├── batch_ref_6_budget_50_2040042_9.err
│   ├── batch_ref_6_budget_50_2040042_9.out
│   ├── batch_ref_6_budget_50_max_6_2067312_1.err
│   ├── batch_ref_6_budget_50_max_6_2067312_1.out
│   ├── batch_ref_6_budget_50_max_6_2067312_10.err
│   ├── batch_ref_6_budget_50_max_6_2067312_10.out
│   ├── batch_ref_6_budget_50_max_6_2067312_11.err
│   ├── batch_ref_6_budget_50_max_6_2067312_11.out
│   ├── batch_ref_6_budget_50_max_6_2067312_12.err
│   ├── batch_ref_6_budget_50_max_6_2067312_12.out
│   ├── batch_ref_6_budget_50_max_6_2067312_13.err
│   ├── batch_ref_6_budget_50_max_6_2067312_13.out
│   ├── batch_ref_6_budget_50_max_6_2067312_14.err
│   ├── batch_ref_6_budget_50_max_6_2067312_14.out
│   ├── batch_ref_6_budget_50_max_6_2067312_15.err
│   ├── batch_ref_6_budget_50_max_6_2067312_15.out
│   ├── batch_ref_6_budget_50_max_6_2067312_16.err
│   ├── batch_ref_6_budget_50_max_6_2067312_16.out
│   ├── batch_ref_6_budget_50_max_6_2067312_17.err
│   ├── batch_ref_6_budget_50_max_6_2067312_17.out
│   ├── batch_ref_6_budget_50_max_6_2067312_18.err
│   ├── batch_ref_6_budget_50_max_6_2067312_18.out
│   ├── batch_ref_6_budget_50_max_6_2067312_19.err
│   ├── batch_ref_6_budget_50_max_6_2067312_19.out
│   ├── batch_ref_6_budget_50_max_6_2067312_2.err
│   ├── batch_ref_6_budget_50_max_6_2067312_2.out
│   ├── batch_ref_6_budget_50_max_6_2067312_20.err
│   ├── batch_ref_6_budget_50_max_6_2067312_20.out
│   ├── batch_ref_6_budget_50_max_6_2067312_21.err
│   ├── batch_ref_6_budget_50_max_6_2067312_21.out
│   ├── batch_ref_6_budget_50_max_6_2067312_22.err
│   ├── batch_ref_6_budget_50_max_6_2067312_22.out
│   ├── batch_ref_6_budget_50_max_6_2067312_23.err
│   ├── batch_ref_6_budget_50_max_6_2067312_23.out
│   ├── batch_ref_6_budget_50_max_6_2067312_24.err
│   ├── batch_ref_6_budget_50_max_6_2067312_24.out
│   ├── batch_ref_6_budget_50_max_6_2067312_25.err
│   ├── batch_ref_6_budget_50_max_6_2067312_25.out
│   ├── batch_ref_6_budget_50_max_6_2067312_26.err
│   ├── batch_ref_6_budget_50_max_6_2067312_26.out
│   ├── batch_ref_6_budget_50_max_6_2067312_27.err
│   ├── batch_ref_6_budget_50_max_6_2067312_27.out
│   ├── batch_ref_6_budget_50_max_6_2067312_28.err
│   ├── batch_ref_6_budget_50_max_6_2067312_28.out
│   ├── batch_ref_6_budget_50_max_6_2067312_29.err
│   ├── batch_ref_6_budget_50_max_6_2067312_29.out
│   ├── batch_ref_6_budget_50_max_6_2067312_3.err
│   ├── batch_ref_6_budget_50_max_6_2067312_3.out
│   ├── batch_ref_6_budget_50_max_6_2067312_30.err
│   ├── batch_ref_6_budget_50_max_6_2067312_30.out
│   ├── batch_ref_6_budget_50_max_6_2067312_31.err
│   ├── batch_ref_6_budget_50_max_6_2067312_31.out
│   ├── batch_ref_6_budget_50_max_6_2067312_32.err
│   ├── batch_ref_6_budget_50_max_6_2067312_32.out
│   ├── batch_ref_6_budget_50_max_6_2067312_33.err
│   ├── batch_ref_6_budget_50_max_6_2067312_33.out
│   ├── batch_ref_6_budget_50_max_6_2067312_34.err
│   ├── batch_ref_6_budget_50_max_6_2067312_34.out
│   ├── batch_ref_6_budget_50_max_6_2067312_35.err
│   ├── batch_ref_6_budget_50_max_6_2067312_35.out
│   ├── batch_ref_6_budget_50_max_6_2067312_36.err
│   ├── batch_ref_6_budget_50_max_6_2067312_36.out
│   ├── batch_ref_6_budget_50_max_6_2067312_37.err
│   ├── batch_ref_6_budget_50_max_6_2067312_37.out
│   ├── batch_ref_6_budget_50_max_6_2067312_38.err
│   ├── batch_ref_6_budget_50_max_6_2067312_38.out
│   ├── batch_ref_6_budget_50_max_6_2067312_39.err
│   ├── batch_ref_6_budget_50_max_6_2067312_39.out
│   ├── batch_ref_6_budget_50_max_6_2067312_4.err
│   ├── batch_ref_6_budget_50_max_6_2067312_4.out
│   ├── batch_ref_6_budget_50_max_6_2067312_40.err
│   ├── batch_ref_6_budget_50_max_6_2067312_40.out
│   ├── batch_ref_6_budget_50_max_6_2067312_41.err
│   ├── batch_ref_6_budget_50_max_6_2067312_41.out
│   ├── batch_ref_6_budget_50_max_6_2067312_42.err
│   ├── batch_ref_6_budget_50_max_6_2067312_42.out
│   ├── batch_ref_6_budget_50_max_6_2067312_43.err
│   ├── batch_ref_6_budget_50_max_6_2067312_43.out
│   ├── batch_ref_6_budget_50_max_6_2067312_44.err
│   ├── batch_ref_6_budget_50_max_6_2067312_44.out
│   ├── batch_ref_6_budget_50_max_6_2067312_45.err
│   ├── batch_ref_6_budget_50_max_6_2067312_45.out
│   ├── batch_ref_6_budget_50_max_6_2067312_46.err
│   ├── batch_ref_6_budget_50_max_6_2067312_46.out
│   ├── batch_ref_6_budget_50_max_6_2067312_47.err
│   ├── batch_ref_6_budget_50_max_6_2067312_47.out
│   ├── batch_ref_6_budget_50_max_6_2067312_48.err
│   ├── batch_ref_6_budget_50_max_6_2067312_48.out
│   ├── batch_ref_6_budget_50_max_6_2067312_49.err
│   ├── batch_ref_6_budget_50_max_6_2067312_49.out
│   ├── batch_ref_6_budget_50_max_6_2067312_5.err
│   ├── batch_ref_6_budget_50_max_6_2067312_5.out
│   ├── batch_ref_6_budget_50_max_6_2067312_50.err
│   ├── batch_ref_6_budget_50_max_6_2067312_50.out
│   ├── batch_ref_6_budget_50_max_6_2067312_51.err
│   ├── batch_ref_6_budget_50_max_6_2067312_51.out
│   ├── batch_ref_6_budget_50_max_6_2067312_52.err
│   ├── batch_ref_6_budget_50_max_6_2067312_52.out
│   ├── batch_ref_6_budget_50_max_6_2067312_53.err
│   ├── batch_ref_6_budget_50_max_6_2067312_53.out
│   ├── batch_ref_6_budget_50_max_6_2067312_54.err
│   ├── batch_ref_6_budget_50_max_6_2067312_54.out
│   ├── batch_ref_6_budget_50_max_6_2067312_55.err
│   ├── batch_ref_6_budget_50_max_6_2067312_55.out
│   ├── batch_ref_6_budget_50_max_6_2067312_56.err
│   ├── batch_ref_6_budget_50_max_6_2067312_56.out
│   ├── batch_ref_6_budget_50_max_6_2067312_57.err
│   ├── batch_ref_6_budget_50_max_6_2067312_57.out
│   ├── batch_ref_6_budget_50_max_6_2067312_58.err
│   ├── batch_ref_6_budget_50_max_6_2067312_58.out
│   ├── batch_ref_6_budget_50_max_6_2067312_59.err
│   ├── batch_ref_6_budget_50_max_6_2067312_59.out
│   ├── batch_ref_6_budget_50_max_6_2067312_6.err
│   ├── batch_ref_6_budget_50_max_6_2067312_6.out
│   ├── batch_ref_6_budget_50_max_6_2067312_60.err
│   ├── batch_ref_6_budget_50_max_6_2067312_60.out
│   ├── batch_ref_6_budget_50_max_6_2067312_61.err
│   ├── batch_ref_6_budget_50_max_6_2067312_61.out
│   ├── batch_ref_6_budget_50_max_6_2067312_62.err
│   ├── batch_ref_6_budget_50_max_6_2067312_62.out
│   ├── batch_ref_6_budget_50_max_6_2067312_63.err
│   ├── batch_ref_6_budget_50_max_6_2067312_63.out
│   ├── batch_ref_6_budget_50_max_6_2067312_64.err
│   ├── batch_ref_6_budget_50_max_6_2067312_64.out
│   ├── batch_ref_6_budget_50_max_6_2067312_65.err
│   ├── batch_ref_6_budget_50_max_6_2067312_65.out
│   ├── batch_ref_6_budget_50_max_6_2067312_66.err
│   ├── batch_ref_6_budget_50_max_6_2067312_66.out
│   ├── batch_ref_6_budget_50_max_6_2067312_67.err
│   ├── batch_ref_6_budget_50_max_6_2067312_67.out
│   ├── batch_ref_6_budget_50_max_6_2067312_68.err
│   ├── batch_ref_6_budget_50_max_6_2067312_68.out
│   ├── batch_ref_6_budget_50_max_6_2067312_69.err
│   ├── batch_ref_6_budget_50_max_6_2067312_69.out
│   ├── batch_ref_6_budget_50_max_6_2067312_7.err
│   ├── batch_ref_6_budget_50_max_6_2067312_7.out
│   ├── batch_ref_6_budget_50_max_6_2067312_70.err
│   ├── batch_ref_6_budget_50_max_6_2067312_70.out
│   ├── batch_ref_6_budget_50_max_6_2067312_71.err
│   ├── batch_ref_6_budget_50_max_6_2067312_71.out
│   ├── batch_ref_6_budget_50_max_6_2067312_72.err
│   ├── batch_ref_6_budget_50_max_6_2067312_72.out
│   ├── batch_ref_6_budget_50_max_6_2067312_73.err
│   ├── batch_ref_6_budget_50_max_6_2067312_73.out
│   ├── batch_ref_6_budget_50_max_6_2067312_74.err
│   ├── batch_ref_6_budget_50_max_6_2067312_74.out
│   ├── batch_ref_6_budget_50_max_6_2067312_75.err
│   ├── batch_ref_6_budget_50_max_6_2067312_75.out
│   ├── batch_ref_6_budget_50_max_6_2067312_76.err
│   ├── batch_ref_6_budget_50_max_6_2067312_76.out
│   ├── batch_ref_6_budget_50_max_6_2067312_77.err
│   ├── batch_ref_6_budget_50_max_6_2067312_77.out
│   ├── batch_ref_6_budget_50_max_6_2067312_78.err
│   ├── batch_ref_6_budget_50_max_6_2067312_78.out
│   ├── batch_ref_6_budget_50_max_6_2067312_79.err
│   ├── batch_ref_6_budget_50_max_6_2067312_79.out
│   ├── batch_ref_6_budget_50_max_6_2067312_8.err
│   ├── batch_ref_6_budget_50_max_6_2067312_8.out
│   ├── batch_ref_6_budget_50_max_6_2067312_80.err
│   ├── batch_ref_6_budget_50_max_6_2067312_80.out
│   ├── batch_ref_6_budget_50_max_6_2067312_81.err
│   ├── batch_ref_6_budget_50_max_6_2067312_81.out
│   ├── batch_ref_6_budget_50_max_6_2067312_9.err
│   ├── batch_ref_6_budget_50_max_6_2067312_9.out
│   ├── batch_ref_6_budget_80_2038359_1.err
│   ├── batch_ref_6_budget_80_2038359_1.out
│   ├── batch_ref_6_budget_80_2038359_10.err
│   ├── batch_ref_6_budget_80_2038359_10.out
│   ├── batch_ref_6_budget_80_2038359_11.err
│   ├── batch_ref_6_budget_80_2038359_11.out
│   ├── batch_ref_6_budget_80_2038359_12.err
│   ├── batch_ref_6_budget_80_2038359_12.out
│   ├── batch_ref_6_budget_80_2038359_13.err
│   ├── batch_ref_6_budget_80_2038359_13.out
│   ├── batch_ref_6_budget_80_2038359_14.err
│   ├── batch_ref_6_budget_80_2038359_14.out
│   ├── batch_ref_6_budget_80_2038359_15.err
│   ├── batch_ref_6_budget_80_2038359_15.out
│   ├── batch_ref_6_budget_80_2038359_16.err
│   ├── batch_ref_6_budget_80_2038359_16.out
│   ├── batch_ref_6_budget_80_2038359_17.err
│   ├── batch_ref_6_budget_80_2038359_17.out
│   ├── batch_ref_6_budget_80_2038359_18.err
│   ├── batch_ref_6_budget_80_2038359_18.out
│   ├── batch_ref_6_budget_80_2038359_19.err
│   ├── batch_ref_6_budget_80_2038359_19.out
│   ├── batch_ref_6_budget_80_2038359_2.err
│   ├── batch_ref_6_budget_80_2038359_2.out
│   ├── batch_ref_6_budget_80_2038359_20.err
│   ├── batch_ref_6_budget_80_2038359_20.out
│   ├── batch_ref_6_budget_80_2038359_21.err
│   ├── batch_ref_6_budget_80_2038359_21.out
│   ├── batch_ref_6_budget_80_2038359_22.err
│   ├── batch_ref_6_budget_80_2038359_22.out
│   ├── batch_ref_6_budget_80_2038359_23.err
│   ├── batch_ref_6_budget_80_2038359_23.out
│   ├── batch_ref_6_budget_80_2038359_24.err
│   ├── batch_ref_6_budget_80_2038359_24.out
│   ├── batch_ref_6_budget_80_2038359_25.err
│   ├── batch_ref_6_budget_80_2038359_25.out
│   ├── batch_ref_6_budget_80_2038359_26.err
│   ├── batch_ref_6_budget_80_2038359_26.out
│   ├── batch_ref_6_budget_80_2038359_27.err
│   ├── batch_ref_6_budget_80_2038359_27.out
│   ├── batch_ref_6_budget_80_2038359_28.err
│   ├── batch_ref_6_budget_80_2038359_28.out
│   ├── batch_ref_6_budget_80_2038359_29.err
│   ├── batch_ref_6_budget_80_2038359_29.out
│   ├── batch_ref_6_budget_80_2038359_3.err
│   ├── batch_ref_6_budget_80_2038359_3.out
│   ├── batch_ref_6_budget_80_2038359_30.err
│   ├── batch_ref_6_budget_80_2038359_30.out
│   ├── batch_ref_6_budget_80_2038359_31.err
│   ├── batch_ref_6_budget_80_2038359_31.out
│   ├── batch_ref_6_budget_80_2038359_32.err
│   ├── batch_ref_6_budget_80_2038359_32.out
│   ├── batch_ref_6_budget_80_2038359_33.err
│   ├── batch_ref_6_budget_80_2038359_33.out
│   ├── batch_ref_6_budget_80_2038359_34.err
│   ├── batch_ref_6_budget_80_2038359_34.out
│   ├── batch_ref_6_budget_80_2038359_35.err
│   ├── batch_ref_6_budget_80_2038359_35.out
│   ├── batch_ref_6_budget_80_2038359_36.err
│   ├── batch_ref_6_budget_80_2038359_36.out
│   ├── batch_ref_6_budget_80_2038359_37.err
│   ├── batch_ref_6_budget_80_2038359_37.out
│   ├── batch_ref_6_budget_80_2038359_38.err
│   ├── batch_ref_6_budget_80_2038359_38.out
│   ├── batch_ref_6_budget_80_2038359_39.err
│   ├── batch_ref_6_budget_80_2038359_39.out
│   ├── batch_ref_6_budget_80_2038359_4.err
│   ├── batch_ref_6_budget_80_2038359_4.out
│   ├── batch_ref_6_budget_80_2038359_40.err
│   ├── batch_ref_6_budget_80_2038359_40.out
│   ├── batch_ref_6_budget_80_2038359_41.err
│   ├── batch_ref_6_budget_80_2038359_41.out
│   ├── batch_ref_6_budget_80_2038359_42.err
│   ├── batch_ref_6_budget_80_2038359_42.out
│   ├── batch_ref_6_budget_80_2038359_43.err
│   ├── batch_ref_6_budget_80_2038359_43.out
│   ├── batch_ref_6_budget_80_2038359_44.err
│   ├── batch_ref_6_budget_80_2038359_44.out
│   ├── batch_ref_6_budget_80_2038359_45.err
│   ├── batch_ref_6_budget_80_2038359_45.out
│   ├── batch_ref_6_budget_80_2038359_46.err
│   ├── batch_ref_6_budget_80_2038359_46.out
│   ├── batch_ref_6_budget_80_2038359_47.err
│   ├── batch_ref_6_budget_80_2038359_47.out
│   ├── batch_ref_6_budget_80_2038359_48.err
│   ├── batch_ref_6_budget_80_2038359_48.out
│   ├── batch_ref_6_budget_80_2038359_49.err
│   ├── batch_ref_6_budget_80_2038359_49.out
│   ├── batch_ref_6_budget_80_2038359_5.err
│   ├── batch_ref_6_budget_80_2038359_5.out
│   ├── batch_ref_6_budget_80_2038359_50.err
│   ├── batch_ref_6_budget_80_2038359_50.out
│   ├── batch_ref_6_budget_80_2038359_51.err
│   ├── batch_ref_6_budget_80_2038359_51.out
│   ├── batch_ref_6_budget_80_2038359_52.err
│   ├── batch_ref_6_budget_80_2038359_52.out
│   ├── batch_ref_6_budget_80_2038359_53.err
│   ├── batch_ref_6_budget_80_2038359_53.out
│   ├── batch_ref_6_budget_80_2038359_54.err
│   ├── batch_ref_6_budget_80_2038359_54.out
│   ├── batch_ref_6_budget_80_2038359_55.err
│   ├── batch_ref_6_budget_80_2038359_55.out
│   ├── batch_ref_6_budget_80_2038359_56.err
│   ├── batch_ref_6_budget_80_2038359_56.out
│   ├── batch_ref_6_budget_80_2038359_57.err
│   ├── batch_ref_6_budget_80_2038359_57.out
│   ├── batch_ref_6_budget_80_2038359_58.err
│   ├── batch_ref_6_budget_80_2038359_58.out
│   ├── batch_ref_6_budget_80_2038359_59.err
│   ├── batch_ref_6_budget_80_2038359_59.out
│   ├── batch_ref_6_budget_80_2038359_6.err
│   ├── batch_ref_6_budget_80_2038359_6.out
│   ├── batch_ref_6_budget_80_2038359_60.err
│   ├── batch_ref_6_budget_80_2038359_60.out
│   ├── batch_ref_6_budget_80_2038359_61.err
│   ├── batch_ref_6_budget_80_2038359_61.out
│   ├── batch_ref_6_budget_80_2038359_62.err
│   ├── batch_ref_6_budget_80_2038359_62.out
│   ├── batch_ref_6_budget_80_2038359_63.err
│   ├── batch_ref_6_budget_80_2038359_63.out
│   ├── batch_ref_6_budget_80_2038359_64.err
│   ├── batch_ref_6_budget_80_2038359_64.out
│   ├── batch_ref_6_budget_80_2038359_65.err
│   ├── batch_ref_6_budget_80_2038359_65.out
│   ├── batch_ref_6_budget_80_2038359_66.err
│   ├── batch_ref_6_budget_80_2038359_66.out
│   ├── batch_ref_6_budget_80_2038359_67.err
│   ├── batch_ref_6_budget_80_2038359_67.out
│   ├── batch_ref_6_budget_80_2038359_68.err
│   ├── batch_ref_6_budget_80_2038359_68.out
│   ├── batch_ref_6_budget_80_2038359_69.err
│   ├── batch_ref_6_budget_80_2038359_69.out
│   ├── batch_ref_6_budget_80_2038359_7.err
│   ├── batch_ref_6_budget_80_2038359_7.out
│   ├── batch_ref_6_budget_80_2038359_70.err
│   ├── batch_ref_6_budget_80_2038359_70.out
│   ├── batch_ref_6_budget_80_2038359_71.err
│   ├── batch_ref_6_budget_80_2038359_71.out
│   ├── batch_ref_6_budget_80_2038359_72.err
│   ├── batch_ref_6_budget_80_2038359_72.out
│   ├── batch_ref_6_budget_80_2038359_73.err
│   ├── batch_ref_6_budget_80_2038359_73.out
│   ├── batch_ref_6_budget_80_2038359_74.err
│   ├── batch_ref_6_budget_80_2038359_74.out
│   ├── batch_ref_6_budget_80_2038359_75.err
│   ├── batch_ref_6_budget_80_2038359_75.out
│   ├── batch_ref_6_budget_80_2038359_76.err
│   ├── batch_ref_6_budget_80_2038359_76.out
│   ├── batch_ref_6_budget_80_2038359_77.err
│   ├── batch_ref_6_budget_80_2038359_77.out
│   ├── batch_ref_6_budget_80_2038359_78.err
│   ├── batch_ref_6_budget_80_2038359_78.out
│   ├── batch_ref_6_budget_80_2038359_79.err
│   ├── batch_ref_6_budget_80_2038359_79.out
│   ├── batch_ref_6_budget_80_2038359_8.err
│   ├── batch_ref_6_budget_80_2038359_8.out
│   ├── batch_ref_6_budget_80_2038359_80.err
│   ├── batch_ref_6_budget_80_2038359_80.out
│   ├── batch_ref_6_budget_80_2038359_81.err
│   ├── batch_ref_6_budget_80_2038359_81.out
│   ├── batch_ref_6_budget_80_2038359_9.err
│   ├── batch_ref_6_budget_80_2038359_9.out
│   ├── batch_ref_6_budget_80_2039592_1.err
│   ├── batch_ref_6_budget_80_2039592_1.out
│   ├── batch_ref_6_budget_80_2039592_10.err
│   ├── batch_ref_6_budget_80_2039592_10.out
│   ├── batch_ref_6_budget_80_2039592_11.err
│   ├── batch_ref_6_budget_80_2039592_11.out
│   ├── batch_ref_6_budget_80_2039592_12.err
│   ├── batch_ref_6_budget_80_2039592_12.out
│   ├── batch_ref_6_budget_80_2039592_13.err
│   ├── batch_ref_6_budget_80_2039592_13.out
│   ├── batch_ref_6_budget_80_2039592_14.err
│   ├── batch_ref_6_budget_80_2039592_14.out
│   ├── batch_ref_6_budget_80_2039592_15.err
│   ├── batch_ref_6_budget_80_2039592_15.out
│   ├── batch_ref_6_budget_80_2039592_16.err
│   ├── batch_ref_6_budget_80_2039592_16.out
│   ├── batch_ref_6_budget_80_2039592_17.err
│   ├── batch_ref_6_budget_80_2039592_17.out
│   ├── batch_ref_6_budget_80_2039592_18.err
│   ├── batch_ref_6_budget_80_2039592_18.out
│   ├── batch_ref_6_budget_80_2039592_19.err
│   ├── batch_ref_6_budget_80_2039592_19.out
│   ├── batch_ref_6_budget_80_2039592_2.err
│   ├── batch_ref_6_budget_80_2039592_2.out
│   ├── batch_ref_6_budget_80_2039592_20.err
│   ├── batch_ref_6_budget_80_2039592_20.out
│   ├── batch_ref_6_budget_80_2039592_21.err
│   ├── batch_ref_6_budget_80_2039592_21.out
│   ├── batch_ref_6_budget_80_2039592_22.err
│   ├── batch_ref_6_budget_80_2039592_22.out
│   ├── batch_ref_6_budget_80_2039592_23.err
│   ├── batch_ref_6_budget_80_2039592_23.out
│   ├── batch_ref_6_budget_80_2039592_24.err
│   ├── batch_ref_6_budget_80_2039592_24.out
│   ├── batch_ref_6_budget_80_2039592_25.err
│   ├── batch_ref_6_budget_80_2039592_25.out
│   ├── batch_ref_6_budget_80_2039592_26.err
│   ├── batch_ref_6_budget_80_2039592_26.out
│   ├── batch_ref_6_budget_80_2039592_27.err
│   ├── batch_ref_6_budget_80_2039592_27.out
│   ├── batch_ref_6_budget_80_2039592_28.err
│   ├── batch_ref_6_budget_80_2039592_28.out
│   ├── batch_ref_6_budget_80_2039592_29.err
│   ├── batch_ref_6_budget_80_2039592_29.out
│   ├── batch_ref_6_budget_80_2039592_3.err
│   ├── batch_ref_6_budget_80_2039592_3.out
│   ├── batch_ref_6_budget_80_2039592_30.err
│   ├── batch_ref_6_budget_80_2039592_30.out
│   ├── batch_ref_6_budget_80_2039592_31.err
│   ├── batch_ref_6_budget_80_2039592_31.out
│   ├── batch_ref_6_budget_80_2039592_32.err
│   ├── batch_ref_6_budget_80_2039592_32.out
│   ├── batch_ref_6_budget_80_2039592_33.err
│   ├── batch_ref_6_budget_80_2039592_33.out
│   ├── batch_ref_6_budget_80_2039592_34.err
│   ├── batch_ref_6_budget_80_2039592_34.out
│   ├── batch_ref_6_budget_80_2039592_35.err
│   ├── batch_ref_6_budget_80_2039592_35.out
│   ├── batch_ref_6_budget_80_2039592_36.err
│   ├── batch_ref_6_budget_80_2039592_36.out
│   ├── batch_ref_6_budget_80_2039592_37.err
│   ├── batch_ref_6_budget_80_2039592_37.out
│   ├── batch_ref_6_budget_80_2039592_38.err
│   ├── batch_ref_6_budget_80_2039592_38.out
│   ├── batch_ref_6_budget_80_2039592_39.err
│   ├── batch_ref_6_budget_80_2039592_39.out
│   ├── batch_ref_6_budget_80_2039592_4.err
│   ├── batch_ref_6_budget_80_2039592_4.out
│   ├── batch_ref_6_budget_80_2039592_40.err
│   ├── batch_ref_6_budget_80_2039592_40.out
│   ├── batch_ref_6_budget_80_2039592_41.err
│   ├── batch_ref_6_budget_80_2039592_41.out
│   ├── batch_ref_6_budget_80_2039592_42.err
│   ├── batch_ref_6_budget_80_2039592_42.out
│   ├── batch_ref_6_budget_80_2039592_43.err
│   ├── batch_ref_6_budget_80_2039592_43.out
│   ├── batch_ref_6_budget_80_2039592_44.err
│   ├── batch_ref_6_budget_80_2039592_44.out
│   ├── batch_ref_6_budget_80_2039592_45.err
│   ├── batch_ref_6_budget_80_2039592_45.out
│   ├── batch_ref_6_budget_80_2039592_46.err
│   ├── batch_ref_6_budget_80_2039592_46.out
│   ├── batch_ref_6_budget_80_2039592_47.err
│   ├── batch_ref_6_budget_80_2039592_47.out
│   ├── batch_ref_6_budget_80_2039592_48.err
│   ├── batch_ref_6_budget_80_2039592_48.out
│   ├── batch_ref_6_budget_80_2039592_49.err
│   ├── batch_ref_6_budget_80_2039592_49.out
│   ├── batch_ref_6_budget_80_2039592_5.err
│   ├── batch_ref_6_budget_80_2039592_5.out
│   ├── batch_ref_6_budget_80_2039592_50.err
│   ├── batch_ref_6_budget_80_2039592_50.out
│   ├── batch_ref_6_budget_80_2039592_51.err
│   ├── batch_ref_6_budget_80_2039592_51.out
│   ├── batch_ref_6_budget_80_2039592_52.err
│   ├── batch_ref_6_budget_80_2039592_52.out
│   ├── batch_ref_6_budget_80_2039592_53.err
│   ├── batch_ref_6_budget_80_2039592_53.out
│   ├── batch_ref_6_budget_80_2039592_54.err
│   ├── batch_ref_6_budget_80_2039592_54.out
│   ├── batch_ref_6_budget_80_2039592_55.err
│   ├── batch_ref_6_budget_80_2039592_55.out
│   ├── batch_ref_6_budget_80_2039592_56.err
│   ├── batch_ref_6_budget_80_2039592_56.out
│   ├── batch_ref_6_budget_80_2039592_57.err
│   ├── batch_ref_6_budget_80_2039592_57.out
│   ├── batch_ref_6_budget_80_2039592_58.err
│   ├── batch_ref_6_budget_80_2039592_58.out
│   ├── batch_ref_6_budget_80_2039592_59.err
│   ├── batch_ref_6_budget_80_2039592_59.out
│   ├── batch_ref_6_budget_80_2039592_6.err
│   ├── batch_ref_6_budget_80_2039592_6.out
│   ├── batch_ref_6_budget_80_2039592_60.err
│   ├── batch_ref_6_budget_80_2039592_60.out
│   ├── batch_ref_6_budget_80_2039592_61.err
│   ├── batch_ref_6_budget_80_2039592_61.out
│   ├── batch_ref_6_budget_80_2039592_62.err
│   ├── batch_ref_6_budget_80_2039592_62.out
│   ├── batch_ref_6_budget_80_2039592_63.err
│   ├── batch_ref_6_budget_80_2039592_63.out
│   ├── batch_ref_6_budget_80_2039592_64.err
│   ├── batch_ref_6_budget_80_2039592_64.out
│   ├── batch_ref_6_budget_80_2039592_65.err
│   ├── batch_ref_6_budget_80_2039592_65.out
│   ├── batch_ref_6_budget_80_2039592_66.err
│   ├── batch_ref_6_budget_80_2039592_66.out
│   ├── batch_ref_6_budget_80_2039592_67.err
│   ├── batch_ref_6_budget_80_2039592_67.out
│   ├── batch_ref_6_budget_80_2039592_68.err
│   ├── batch_ref_6_budget_80_2039592_68.out
│   ├── batch_ref_6_budget_80_2039592_69.err
│   ├── batch_ref_6_budget_80_2039592_69.out
│   ├── batch_ref_6_budget_80_2039592_7.err
│   ├── batch_ref_6_budget_80_2039592_7.out
│   ├── batch_ref_6_budget_80_2039592_70.err
│   ├── batch_ref_6_budget_80_2039592_70.out
│   ├── batch_ref_6_budget_80_2039592_71.err
│   ├── batch_ref_6_budget_80_2039592_71.out
│   ├── batch_ref_6_budget_80_2039592_72.err
│   ├── batch_ref_6_budget_80_2039592_72.out
│   ├── batch_ref_6_budget_80_2039592_73.err
│   ├── batch_ref_6_budget_80_2039592_73.out
│   ├── batch_ref_6_budget_80_2039592_74.err
│   ├── batch_ref_6_budget_80_2039592_74.out
│   ├── batch_ref_6_budget_80_2039592_75.err
│   ├── batch_ref_6_budget_80_2039592_75.out
│   ├── batch_ref_6_budget_80_2039592_76.err
│   ├── batch_ref_6_budget_80_2039592_76.out
│   ├── batch_ref_6_budget_80_2039592_77.err
│   ├── batch_ref_6_budget_80_2039592_77.out
│   ├── batch_ref_6_budget_80_2039592_78.err
│   ├── batch_ref_6_budget_80_2039592_78.out
│   ├── batch_ref_6_budget_80_2039592_79.err
│   ├── batch_ref_6_budget_80_2039592_79.out
│   ├── batch_ref_6_budget_80_2039592_8.err
│   ├── batch_ref_6_budget_80_2039592_8.out
│   ├── batch_ref_6_budget_80_2039592_80.err
│   ├── batch_ref_6_budget_80_2039592_80.out
│   ├── batch_ref_6_budget_80_2039592_81.err
│   ├── batch_ref_6_budget_80_2039592_81.out
│   ├── batch_ref_6_budget_80_2039592_9.err
│   ├── batch_ref_6_budget_80_2039592_9.out
│   ├── batch_ref_6_budget_80_2039693_1.err
│   ├── batch_ref_6_budget_80_2039693_1.out
│   ├── batch_ref_6_budget_80_2039693_10.err
│   ├── batch_ref_6_budget_80_2039693_10.out
│   ├── batch_ref_6_budget_80_2039693_11.err
│   ├── batch_ref_6_budget_80_2039693_11.out
│   ├── batch_ref_6_budget_80_2039693_12.err
│   ├── batch_ref_6_budget_80_2039693_12.out
│   ├── batch_ref_6_budget_80_2039693_13.err
│   ├── batch_ref_6_budget_80_2039693_13.out
│   ├── batch_ref_6_budget_80_2039693_14.err
│   ├── batch_ref_6_budget_80_2039693_14.out
│   ├── batch_ref_6_budget_80_2039693_15.err
│   ├── batch_ref_6_budget_80_2039693_15.out
│   ├── batch_ref_6_budget_80_2039693_16.err
│   ├── batch_ref_6_budget_80_2039693_16.out
│   ├── batch_ref_6_budget_80_2039693_17.err
│   ├── batch_ref_6_budget_80_2039693_17.out
│   ├── batch_ref_6_budget_80_2039693_18.err
│   ├── batch_ref_6_budget_80_2039693_18.out
│   ├── batch_ref_6_budget_80_2039693_19.err
│   ├── batch_ref_6_budget_80_2039693_19.out
│   ├── batch_ref_6_budget_80_2039693_2.err
│   ├── batch_ref_6_budget_80_2039693_2.out
│   ├── batch_ref_6_budget_80_2039693_20.err
│   ├── batch_ref_6_budget_80_2039693_20.out
│   ├── batch_ref_6_budget_80_2039693_21.err
│   ├── batch_ref_6_budget_80_2039693_21.out
│   ├── batch_ref_6_budget_80_2039693_22.err
│   ├── batch_ref_6_budget_80_2039693_22.out
│   ├── batch_ref_6_budget_80_2039693_23.err
│   ├── batch_ref_6_budget_80_2039693_23.out
│   ├── batch_ref_6_budget_80_2039693_24.err
│   ├── batch_ref_6_budget_80_2039693_24.out
│   ├── batch_ref_6_budget_80_2039693_25.err
│   ├── batch_ref_6_budget_80_2039693_25.out
│   ├── batch_ref_6_budget_80_2039693_26.err
│   ├── batch_ref_6_budget_80_2039693_26.out
│   ├── batch_ref_6_budget_80_2039693_27.err
│   ├── batch_ref_6_budget_80_2039693_27.out
│   ├── batch_ref_6_budget_80_2039693_28.err
│   ├── batch_ref_6_budget_80_2039693_28.out
│   ├── batch_ref_6_budget_80_2039693_29.err
│   ├── batch_ref_6_budget_80_2039693_29.out
│   ├── batch_ref_6_budget_80_2039693_3.err
│   ├── batch_ref_6_budget_80_2039693_3.out
│   ├── batch_ref_6_budget_80_2039693_30.err
│   ├── batch_ref_6_budget_80_2039693_30.out
│   ├── batch_ref_6_budget_80_2039693_31.err
│   ├── batch_ref_6_budget_80_2039693_31.out
│   ├── batch_ref_6_budget_80_2039693_32.err
│   ├── batch_ref_6_budget_80_2039693_32.out
│   ├── batch_ref_6_budget_80_2039693_33.err
│   ├── batch_ref_6_budget_80_2039693_33.out
│   ├── batch_ref_6_budget_80_2039693_34.err
│   ├── batch_ref_6_budget_80_2039693_34.out
│   ├── batch_ref_6_budget_80_2039693_35.err
│   ├── batch_ref_6_budget_80_2039693_35.out
│   ├── batch_ref_6_budget_80_2039693_36.err
│   ├── batch_ref_6_budget_80_2039693_36.out
│   ├── batch_ref_6_budget_80_2039693_37.err
│   ├── batch_ref_6_budget_80_2039693_37.out
│   ├── batch_ref_6_budget_80_2039693_38.err
│   ├── batch_ref_6_budget_80_2039693_38.out
│   ├── batch_ref_6_budget_80_2039693_39.err
│   ├── batch_ref_6_budget_80_2039693_39.out
│   ├── batch_ref_6_budget_80_2039693_4.err
│   ├── batch_ref_6_budget_80_2039693_4.out
│   ├── batch_ref_6_budget_80_2039693_40.err
│   ├── batch_ref_6_budget_80_2039693_40.out
│   ├── batch_ref_6_budget_80_2039693_41.err
│   ├── batch_ref_6_budget_80_2039693_41.out
│   ├── batch_ref_6_budget_80_2039693_42.err
│   ├── batch_ref_6_budget_80_2039693_42.out
│   ├── batch_ref_6_budget_80_2039693_43.err
│   ├── batch_ref_6_budget_80_2039693_43.out
│   ├── batch_ref_6_budget_80_2039693_44.err
│   ├── batch_ref_6_budget_80_2039693_44.out
│   ├── batch_ref_6_budget_80_2039693_45.err
│   ├── batch_ref_6_budget_80_2039693_45.out
│   ├── batch_ref_6_budget_80_2039693_46.err
│   ├── batch_ref_6_budget_80_2039693_46.out
│   ├── batch_ref_6_budget_80_2039693_47.err
│   ├── batch_ref_6_budget_80_2039693_47.out
│   ├── batch_ref_6_budget_80_2039693_48.err
│   ├── batch_ref_6_budget_80_2039693_48.out
│   ├── batch_ref_6_budget_80_2039693_49.err
│   ├── batch_ref_6_budget_80_2039693_49.out
│   ├── batch_ref_6_budget_80_2039693_5.err
│   ├── batch_ref_6_budget_80_2039693_5.out
│   ├── batch_ref_6_budget_80_2039693_50.err
│   ├── batch_ref_6_budget_80_2039693_50.out
│   ├── batch_ref_6_budget_80_2039693_51.err
│   ├── batch_ref_6_budget_80_2039693_51.out
│   ├── batch_ref_6_budget_80_2039693_52.err
│   ├── batch_ref_6_budget_80_2039693_52.out
│   ├── batch_ref_6_budget_80_2039693_53.err
│   ├── batch_ref_6_budget_80_2039693_53.out
│   ├── batch_ref_6_budget_80_2039693_54.err
│   ├── batch_ref_6_budget_80_2039693_54.out
│   ├── batch_ref_6_budget_80_2039693_55.err
│   ├── batch_ref_6_budget_80_2039693_55.out
│   ├── batch_ref_6_budget_80_2039693_56.err
│   ├── batch_ref_6_budget_80_2039693_56.out
│   ├── batch_ref_6_budget_80_2039693_57.err
│   ├── batch_ref_6_budget_80_2039693_57.out
│   ├── batch_ref_6_budget_80_2039693_58.err
│   ├── batch_ref_6_budget_80_2039693_58.out
│   ├── batch_ref_6_budget_80_2039693_59.err
│   ├── batch_ref_6_budget_80_2039693_59.out
│   ├── batch_ref_6_budget_80_2039693_6.err
│   ├── batch_ref_6_budget_80_2039693_6.out
│   ├── batch_ref_6_budget_80_2039693_60.err
│   ├── batch_ref_6_budget_80_2039693_60.out
│   ├── batch_ref_6_budget_80_2039693_61.err
│   ├── batch_ref_6_budget_80_2039693_61.out
│   ├── batch_ref_6_budget_80_2039693_62.err
│   ├── batch_ref_6_budget_80_2039693_62.out
│   ├── batch_ref_6_budget_80_2039693_63.err
│   ├── batch_ref_6_budget_80_2039693_63.out
│   ├── batch_ref_6_budget_80_2039693_64.err
│   ├── batch_ref_6_budget_80_2039693_64.out
│   ├── batch_ref_6_budget_80_2039693_65.err
│   ├── batch_ref_6_budget_80_2039693_65.out
│   ├── batch_ref_6_budget_80_2039693_66.err
│   ├── batch_ref_6_budget_80_2039693_66.out
│   ├── batch_ref_6_budget_80_2039693_67.err
│   ├── batch_ref_6_budget_80_2039693_67.out
│   ├── batch_ref_6_budget_80_2039693_68.err
│   ├── batch_ref_6_budget_80_2039693_68.out
│   ├── batch_ref_6_budget_80_2039693_69.err
│   ├── batch_ref_6_budget_80_2039693_69.out
│   ├── batch_ref_6_budget_80_2039693_7.err
│   ├── batch_ref_6_budget_80_2039693_7.out
│   ├── batch_ref_6_budget_80_2039693_70.err
│   ├── batch_ref_6_budget_80_2039693_70.out
│   ├── batch_ref_6_budget_80_2039693_71.err
│   ├── batch_ref_6_budget_80_2039693_71.out
│   ├── batch_ref_6_budget_80_2039693_72.err
│   ├── batch_ref_6_budget_80_2039693_72.out
│   ├── batch_ref_6_budget_80_2039693_73.err
│   ├── batch_ref_6_budget_80_2039693_73.out
│   ├── batch_ref_6_budget_80_2039693_74.err
│   ├── batch_ref_6_budget_80_2039693_74.out
│   ├── batch_ref_6_budget_80_2039693_75.err
│   ├── batch_ref_6_budget_80_2039693_75.out
│   ├── batch_ref_6_budget_80_2039693_76.err
│   ├── batch_ref_6_budget_80_2039693_76.out
│   ├── batch_ref_6_budget_80_2039693_77.err
│   ├── batch_ref_6_budget_80_2039693_77.out
│   ├── batch_ref_6_budget_80_2039693_78.err
│   ├── batch_ref_6_budget_80_2039693_78.out
│   ├── batch_ref_6_budget_80_2039693_79.err
│   ├── batch_ref_6_budget_80_2039693_79.out
│   ├── batch_ref_6_budget_80_2039693_8.err
│   ├── batch_ref_6_budget_80_2039693_8.out
│   ├── batch_ref_6_budget_80_2039693_80.err
│   ├── batch_ref_6_budget_80_2039693_80.out
│   ├── batch_ref_6_budget_80_2039693_81.err
│   ├── batch_ref_6_budget_80_2039693_81.out
│   ├── batch_ref_6_budget_80_2039693_9.err
│   ├── batch_ref_6_budget_80_2039693_9.out
│   ├── batch_ref_6_budget_80_2040043_1.err
│   ├── batch_ref_6_budget_80_2040043_1.out
│   ├── batch_ref_6_budget_80_2040043_10.err
│   ├── batch_ref_6_budget_80_2040043_10.out
│   ├── batch_ref_6_budget_80_2040043_11.err
│   ├── batch_ref_6_budget_80_2040043_11.out
│   ├── batch_ref_6_budget_80_2040043_12.err
│   ├── batch_ref_6_budget_80_2040043_12.out
│   ├── batch_ref_6_budget_80_2040043_13.err
│   ├── batch_ref_6_budget_80_2040043_13.out
│   ├── batch_ref_6_budget_80_2040043_14.err
│   ├── batch_ref_6_budget_80_2040043_14.out
│   ├── batch_ref_6_budget_80_2040043_15.err
│   ├── batch_ref_6_budget_80_2040043_15.out
│   ├── batch_ref_6_budget_80_2040043_16.err
│   ├── batch_ref_6_budget_80_2040043_16.out
│   ├── batch_ref_6_budget_80_2040043_17.err
│   ├── batch_ref_6_budget_80_2040043_17.out
│   ├── batch_ref_6_budget_80_2040043_18.err
│   ├── batch_ref_6_budget_80_2040043_18.out
│   ├── batch_ref_6_budget_80_2040043_19.err
│   ├── batch_ref_6_budget_80_2040043_19.out
│   ├── batch_ref_6_budget_80_2040043_2.err
│   ├── batch_ref_6_budget_80_2040043_2.out
│   ├── batch_ref_6_budget_80_2040043_20.err
│   ├── batch_ref_6_budget_80_2040043_20.out
│   ├── batch_ref_6_budget_80_2040043_21.err
│   ├── batch_ref_6_budget_80_2040043_21.out
│   ├── batch_ref_6_budget_80_2040043_22.err
│   ├── batch_ref_6_budget_80_2040043_22.out
│   ├── batch_ref_6_budget_80_2040043_23.err
│   ├── batch_ref_6_budget_80_2040043_23.out
│   ├── batch_ref_6_budget_80_2040043_24.err
│   ├── batch_ref_6_budget_80_2040043_24.out
│   ├── batch_ref_6_budget_80_2040043_25.err
│   ├── batch_ref_6_budget_80_2040043_25.out
│   ├── batch_ref_6_budget_80_2040043_26.err
│   ├── batch_ref_6_budget_80_2040043_26.out
│   ├── batch_ref_6_budget_80_2040043_27.err
│   ├── batch_ref_6_budget_80_2040043_27.out
│   ├── batch_ref_6_budget_80_2040043_28.err
│   ├── batch_ref_6_budget_80_2040043_28.out
│   ├── batch_ref_6_budget_80_2040043_29.err
│   ├── batch_ref_6_budget_80_2040043_29.out
│   ├── batch_ref_6_budget_80_2040043_3.err
│   ├── batch_ref_6_budget_80_2040043_3.out
│   ├── batch_ref_6_budget_80_2040043_30.err
│   ├── batch_ref_6_budget_80_2040043_30.out
│   ├── batch_ref_6_budget_80_2040043_31.err
│   ├── batch_ref_6_budget_80_2040043_31.out
│   ├── batch_ref_6_budget_80_2040043_32.err
│   ├── batch_ref_6_budget_80_2040043_32.out
│   ├── batch_ref_6_budget_80_2040043_33.err
│   ├── batch_ref_6_budget_80_2040043_33.out
│   ├── batch_ref_6_budget_80_2040043_34.err
│   ├── batch_ref_6_budget_80_2040043_34.out
│   ├── batch_ref_6_budget_80_2040043_35.err
│   ├── batch_ref_6_budget_80_2040043_35.out
│   ├── batch_ref_6_budget_80_2040043_36.err
│   ├── batch_ref_6_budget_80_2040043_36.out
│   ├── batch_ref_6_budget_80_2040043_37.err
│   ├── batch_ref_6_budget_80_2040043_37.out
│   ├── batch_ref_6_budget_80_2040043_38.err
│   ├── batch_ref_6_budget_80_2040043_38.out
│   ├── batch_ref_6_budget_80_2040043_39.err
│   ├── batch_ref_6_budget_80_2040043_39.out
│   ├── batch_ref_6_budget_80_2040043_4.err
│   ├── batch_ref_6_budget_80_2040043_4.out
│   ├── batch_ref_6_budget_80_2040043_40.err
│   ├── batch_ref_6_budget_80_2040043_40.out
│   ├── batch_ref_6_budget_80_2040043_41.err
│   ├── batch_ref_6_budget_80_2040043_41.out
│   ├── batch_ref_6_budget_80_2040043_42.err
│   ├── batch_ref_6_budget_80_2040043_42.out
│   ├── batch_ref_6_budget_80_2040043_43.err
│   ├── batch_ref_6_budget_80_2040043_43.out
│   ├── batch_ref_6_budget_80_2040043_44.err
│   ├── batch_ref_6_budget_80_2040043_44.out
│   ├── batch_ref_6_budget_80_2040043_45.err
│   ├── batch_ref_6_budget_80_2040043_45.out
│   ├── batch_ref_6_budget_80_2040043_46.err
│   ├── batch_ref_6_budget_80_2040043_46.out
│   ├── batch_ref_6_budget_80_2040043_47.err
│   ├── batch_ref_6_budget_80_2040043_47.out
│   ├── batch_ref_6_budget_80_2040043_48.err
│   ├── batch_ref_6_budget_80_2040043_48.out
│   ├── batch_ref_6_budget_80_2040043_49.err
│   ├── batch_ref_6_budget_80_2040043_49.out
│   ├── batch_ref_6_budget_80_2040043_5.err
│   ├── batch_ref_6_budget_80_2040043_5.out
│   ├── batch_ref_6_budget_80_2040043_50.err
│   ├── batch_ref_6_budget_80_2040043_50.out
│   ├── batch_ref_6_budget_80_2040043_51.err
│   ├── batch_ref_6_budget_80_2040043_51.out
│   ├── batch_ref_6_budget_80_2040043_52.err
│   ├── batch_ref_6_budget_80_2040043_52.out
│   ├── batch_ref_6_budget_80_2040043_53.err
│   ├── batch_ref_6_budget_80_2040043_53.out
│   ├── batch_ref_6_budget_80_2040043_54.err
│   ├── batch_ref_6_budget_80_2040043_54.out
│   ├── batch_ref_6_budget_80_2040043_55.err
│   ├── batch_ref_6_budget_80_2040043_55.out
│   ├── batch_ref_6_budget_80_2040043_56.err
│   ├── batch_ref_6_budget_80_2040043_56.out
│   ├── batch_ref_6_budget_80_2040043_57.err
│   ├── batch_ref_6_budget_80_2040043_57.out
│   ├── batch_ref_6_budget_80_2040043_58.err
│   ├── batch_ref_6_budget_80_2040043_58.out
│   ├── batch_ref_6_budget_80_2040043_59.err
│   ├── batch_ref_6_budget_80_2040043_59.out
│   ├── batch_ref_6_budget_80_2040043_6.err
│   ├── batch_ref_6_budget_80_2040043_6.out
│   ├── batch_ref_6_budget_80_2040043_60.err
│   ├── batch_ref_6_budget_80_2040043_60.out
│   ├── batch_ref_6_budget_80_2040043_61.err
│   ├── batch_ref_6_budget_80_2040043_61.out
│   ├── batch_ref_6_budget_80_2040043_62.err
│   ├── batch_ref_6_budget_80_2040043_62.out
│   ├── batch_ref_6_budget_80_2040043_63.err
│   ├── batch_ref_6_budget_80_2040043_63.out
│   ├── batch_ref_6_budget_80_2040043_64.err
│   ├── batch_ref_6_budget_80_2040043_64.out
│   ├── batch_ref_6_budget_80_2040043_65.err
│   ├── batch_ref_6_budget_80_2040043_65.out
│   ├── batch_ref_6_budget_80_2040043_66.err
│   ├── batch_ref_6_budget_80_2040043_66.out
│   ├── batch_ref_6_budget_80_2040043_67.err
│   ├── batch_ref_6_budget_80_2040043_67.out
│   ├── batch_ref_6_budget_80_2040043_68.err
│   ├── batch_ref_6_budget_80_2040043_68.out
│   ├── batch_ref_6_budget_80_2040043_69.err
│   ├── batch_ref_6_budget_80_2040043_69.out
│   ├── batch_ref_6_budget_80_2040043_7.err
│   ├── batch_ref_6_budget_80_2040043_7.out
│   ├── batch_ref_6_budget_80_2040043_70.err
│   ├── batch_ref_6_budget_80_2040043_70.out
│   ├── batch_ref_6_budget_80_2040043_71.err
│   ├── batch_ref_6_budget_80_2040043_71.out
│   ├── batch_ref_6_budget_80_2040043_72.err
│   ├── batch_ref_6_budget_80_2040043_72.out
│   ├── batch_ref_6_budget_80_2040043_73.err
│   ├── batch_ref_6_budget_80_2040043_73.out
│   ├── batch_ref_6_budget_80_2040043_74.err
│   ├── batch_ref_6_budget_80_2040043_74.out
│   ├── batch_ref_6_budget_80_2040043_75.err
│   ├── batch_ref_6_budget_80_2040043_75.out
│   ├── batch_ref_6_budget_80_2040043_76.err
│   ├── batch_ref_6_budget_80_2040043_76.out
│   ├── batch_ref_6_budget_80_2040043_77.err
│   ├── batch_ref_6_budget_80_2040043_77.out
│   ├── batch_ref_6_budget_80_2040043_78.err
│   ├── batch_ref_6_budget_80_2040043_78.out
│   ├── batch_ref_6_budget_80_2040043_79.err
│   ├── batch_ref_6_budget_80_2040043_79.out
│   ├── batch_ref_6_budget_80_2040043_8.err
│   ├── batch_ref_6_budget_80_2040043_8.out
│   ├── batch_ref_6_budget_80_2040043_80.err
│   ├── batch_ref_6_budget_80_2040043_80.out
│   ├── batch_ref_6_budget_80_2040043_81.err
│   ├── batch_ref_6_budget_80_2040043_81.out
│   ├── batch_ref_6_budget_80_2040043_9.err
│   ├── batch_ref_6_budget_80_2040043_9.out
│   ├── batch_ref_6_budget_80_max_6_2067313_1.err
│   ├── batch_ref_6_budget_80_max_6_2067313_1.out
│   ├── batch_ref_6_budget_80_max_6_2067313_10.err
│   ├── batch_ref_6_budget_80_max_6_2067313_10.out
│   ├── batch_ref_6_budget_80_max_6_2067313_11.err
│   ├── batch_ref_6_budget_80_max_6_2067313_11.out
│   ├── batch_ref_6_budget_80_max_6_2067313_12.err
│   ├── batch_ref_6_budget_80_max_6_2067313_12.out
│   ├── batch_ref_6_budget_80_max_6_2067313_13.err
│   ├── batch_ref_6_budget_80_max_6_2067313_13.out
│   ├── batch_ref_6_budget_80_max_6_2067313_14.err
│   ├── batch_ref_6_budget_80_max_6_2067313_14.out
│   ├── batch_ref_6_budget_80_max_6_2067313_15.err
│   ├── batch_ref_6_budget_80_max_6_2067313_15.out
│   ├── batch_ref_6_budget_80_max_6_2067313_16.err
│   ├── batch_ref_6_budget_80_max_6_2067313_16.out
│   ├── batch_ref_6_budget_80_max_6_2067313_17.err
│   ├── batch_ref_6_budget_80_max_6_2067313_17.out
│   ├── batch_ref_6_budget_80_max_6_2067313_18.err
│   ├── batch_ref_6_budget_80_max_6_2067313_18.out
│   ├── batch_ref_6_budget_80_max_6_2067313_19.err
│   ├── batch_ref_6_budget_80_max_6_2067313_19.out
│   ├── batch_ref_6_budget_80_max_6_2067313_2.err
│   ├── batch_ref_6_budget_80_max_6_2067313_2.out
│   ├── batch_ref_6_budget_80_max_6_2067313_20.err
│   ├── batch_ref_6_budget_80_max_6_2067313_20.out
│   ├── batch_ref_6_budget_80_max_6_2067313_21.err
│   ├── batch_ref_6_budget_80_max_6_2067313_21.out
│   ├── batch_ref_6_budget_80_max_6_2067313_22.err
│   ├── batch_ref_6_budget_80_max_6_2067313_22.out
│   ├── batch_ref_6_budget_80_max_6_2067313_23.err
│   ├── batch_ref_6_budget_80_max_6_2067313_23.out
│   ├── batch_ref_6_budget_80_max_6_2067313_24.err
│   ├── batch_ref_6_budget_80_max_6_2067313_24.out
│   ├── batch_ref_6_budget_80_max_6_2067313_25.err
│   ├── batch_ref_6_budget_80_max_6_2067313_25.out
│   ├── batch_ref_6_budget_80_max_6_2067313_26.err
│   ├── batch_ref_6_budget_80_max_6_2067313_26.out
│   ├── batch_ref_6_budget_80_max_6_2067313_27.err
│   ├── batch_ref_6_budget_80_max_6_2067313_27.out
│   ├── batch_ref_6_budget_80_max_6_2067313_28.err
│   ├── batch_ref_6_budget_80_max_6_2067313_28.out
│   ├── batch_ref_6_budget_80_max_6_2067313_29.err
│   ├── batch_ref_6_budget_80_max_6_2067313_29.out
│   ├── batch_ref_6_budget_80_max_6_2067313_3.err
│   ├── batch_ref_6_budget_80_max_6_2067313_3.out
│   ├── batch_ref_6_budget_80_max_6_2067313_30.err
│   ├── batch_ref_6_budget_80_max_6_2067313_30.out
│   ├── batch_ref_6_budget_80_max_6_2067313_31.err
│   ├── batch_ref_6_budget_80_max_6_2067313_31.out
│   ├── batch_ref_6_budget_80_max_6_2067313_32.err
│   ├── batch_ref_6_budget_80_max_6_2067313_32.out
│   ├── batch_ref_6_budget_80_max_6_2067313_33.err
│   ├── batch_ref_6_budget_80_max_6_2067313_33.out
│   ├── batch_ref_6_budget_80_max_6_2067313_34.err
│   ├── batch_ref_6_budget_80_max_6_2067313_34.out
│   ├── batch_ref_6_budget_80_max_6_2067313_35.err
│   ├── batch_ref_6_budget_80_max_6_2067313_35.out
│   ├── batch_ref_6_budget_80_max_6_2067313_36.err
│   ├── batch_ref_6_budget_80_max_6_2067313_36.out
│   ├── batch_ref_6_budget_80_max_6_2067313_37.err
│   ├── batch_ref_6_budget_80_max_6_2067313_37.out
│   ├── batch_ref_6_budget_80_max_6_2067313_38.err
│   ├── batch_ref_6_budget_80_max_6_2067313_38.out
│   ├── batch_ref_6_budget_80_max_6_2067313_39.err
│   ├── batch_ref_6_budget_80_max_6_2067313_39.out
│   ├── batch_ref_6_budget_80_max_6_2067313_4.err
│   ├── batch_ref_6_budget_80_max_6_2067313_4.out
│   ├── batch_ref_6_budget_80_max_6_2067313_40.err
│   ├── batch_ref_6_budget_80_max_6_2067313_40.out
│   ├── batch_ref_6_budget_80_max_6_2067313_41.err
│   ├── batch_ref_6_budget_80_max_6_2067313_41.out
│   ├── batch_ref_6_budget_80_max_6_2067313_42.err
│   ├── batch_ref_6_budget_80_max_6_2067313_42.out
│   ├── batch_ref_6_budget_80_max_6_2067313_43.err
│   ├── batch_ref_6_budget_80_max_6_2067313_43.out
│   ├── batch_ref_6_budget_80_max_6_2067313_44.err
│   ├── batch_ref_6_budget_80_max_6_2067313_44.out
│   ├── batch_ref_6_budget_80_max_6_2067313_45.err
│   ├── batch_ref_6_budget_80_max_6_2067313_45.out
│   ├── batch_ref_6_budget_80_max_6_2067313_46.err
│   ├── batch_ref_6_budget_80_max_6_2067313_46.out
│   ├── batch_ref_6_budget_80_max_6_2067313_47.err
│   ├── batch_ref_6_budget_80_max_6_2067313_47.out
│   ├── batch_ref_6_budget_80_max_6_2067313_48.err
│   ├── batch_ref_6_budget_80_max_6_2067313_48.out
│   ├── batch_ref_6_budget_80_max_6_2067313_49.err
│   ├── batch_ref_6_budget_80_max_6_2067313_49.out
│   ├── batch_ref_6_budget_80_max_6_2067313_5.err
│   ├── batch_ref_6_budget_80_max_6_2067313_5.out
│   ├── batch_ref_6_budget_80_max_6_2067313_50.err
│   ├── batch_ref_6_budget_80_max_6_2067313_50.out
│   ├── batch_ref_6_budget_80_max_6_2067313_51.err
│   ├── batch_ref_6_budget_80_max_6_2067313_51.out
│   ├── batch_ref_6_budget_80_max_6_2067313_52.err
│   ├── batch_ref_6_budget_80_max_6_2067313_52.out
│   ├── batch_ref_6_budget_80_max_6_2067313_53.err
│   ├── batch_ref_6_budget_80_max_6_2067313_53.out
│   ├── batch_ref_6_budget_80_max_6_2067313_54.err
│   ├── batch_ref_6_budget_80_max_6_2067313_54.out
│   ├── batch_ref_6_budget_80_max_6_2067313_55.err
│   ├── batch_ref_6_budget_80_max_6_2067313_55.out
│   ├── batch_ref_6_budget_80_max_6_2067313_56.err
│   ├── batch_ref_6_budget_80_max_6_2067313_56.out
│   ├── batch_ref_6_budget_80_max_6_2067313_57.err
│   ├── batch_ref_6_budget_80_max_6_2067313_57.out
│   ├── batch_ref_6_budget_80_max_6_2067313_58.err
│   ├── batch_ref_6_budget_80_max_6_2067313_58.out
│   ├── batch_ref_6_budget_80_max_6_2067313_59.err
│   ├── batch_ref_6_budget_80_max_6_2067313_59.out
│   ├── batch_ref_6_budget_80_max_6_2067313_6.err
│   ├── batch_ref_6_budget_80_max_6_2067313_6.out
│   ├── batch_ref_6_budget_80_max_6_2067313_60.err
│   ├── batch_ref_6_budget_80_max_6_2067313_60.out
│   ├── batch_ref_6_budget_80_max_6_2067313_61.err
│   ├── batch_ref_6_budget_80_max_6_2067313_61.out
│   ├── batch_ref_6_budget_80_max_6_2067313_62.err
│   ├── batch_ref_6_budget_80_max_6_2067313_62.out
│   ├── batch_ref_6_budget_80_max_6_2067313_63.err
│   ├── batch_ref_6_budget_80_max_6_2067313_63.out
│   ├── batch_ref_6_budget_80_max_6_2067313_64.err
│   ├── batch_ref_6_budget_80_max_6_2067313_64.out
│   ├── batch_ref_6_budget_80_max_6_2067313_65.err
│   ├── batch_ref_6_budget_80_max_6_2067313_65.out
│   ├── batch_ref_6_budget_80_max_6_2067313_66.err
│   ├── batch_ref_6_budget_80_max_6_2067313_66.out
│   ├── batch_ref_6_budget_80_max_6_2067313_67.err
│   ├── batch_ref_6_budget_80_max_6_2067313_67.out
│   ├── batch_ref_6_budget_80_max_6_2067313_68.err
│   ├── batch_ref_6_budget_80_max_6_2067313_68.out
│   ├── batch_ref_6_budget_80_max_6_2067313_69.err
│   ├── batch_ref_6_budget_80_max_6_2067313_69.out
│   ├── batch_ref_6_budget_80_max_6_2067313_7.err
│   ├── batch_ref_6_budget_80_max_6_2067313_7.out
│   ├── batch_ref_6_budget_80_max_6_2067313_70.err
│   ├── batch_ref_6_budget_80_max_6_2067313_70.out
│   ├── batch_ref_6_budget_80_max_6_2067313_71.err
│   ├── batch_ref_6_budget_80_max_6_2067313_71.out
│   ├── batch_ref_6_budget_80_max_6_2067313_72.err
│   ├── batch_ref_6_budget_80_max_6_2067313_72.out
│   ├── batch_ref_6_budget_80_max_6_2067313_73.err
│   ├── batch_ref_6_budget_80_max_6_2067313_73.out
│   ├── batch_ref_6_budget_80_max_6_2067313_74.err
│   ├── batch_ref_6_budget_80_max_6_2067313_74.out
│   ├── batch_ref_6_budget_80_max_6_2067313_75.err
│   ├── batch_ref_6_budget_80_max_6_2067313_75.out
│   ├── batch_ref_6_budget_80_max_6_2067313_76.err
│   ├── batch_ref_6_budget_80_max_6_2067313_76.out
│   ├── batch_ref_6_budget_80_max_6_2067313_77.err
│   ├── batch_ref_6_budget_80_max_6_2067313_77.out
│   ├── batch_ref_6_budget_80_max_6_2067313_78.err
│   ├── batch_ref_6_budget_80_max_6_2067313_78.out
│   ├── batch_ref_6_budget_80_max_6_2067313_79.err
│   ├── batch_ref_6_budget_80_max_6_2067313_79.out
│   ├── batch_ref_6_budget_80_max_6_2067313_8.err
│   ├── batch_ref_6_budget_80_max_6_2067313_8.out
│   ├── batch_ref_6_budget_80_max_6_2067313_80.err
│   ├── batch_ref_6_budget_80_max_6_2067313_80.out
│   ├── batch_ref_6_budget_80_max_6_2067313_81.err
│   ├── batch_ref_6_budget_80_max_6_2067313_81.out
│   ├── batch_ref_6_budget_80_max_6_2067313_9.err
│   ├── batch_ref_6_budget_80_max_6_2067313_9.out
│   ├── batch_ref_7_budget_100_2038461_1.err
│   ├── batch_ref_7_budget_100_2038461_1.out
│   ├── batch_ref_7_budget_100_2038461_10.err
│   ├── batch_ref_7_budget_100_2038461_10.out
│   ├── batch_ref_7_budget_100_2038461_11.err
│   ├── batch_ref_7_budget_100_2038461_11.out
│   ├── batch_ref_7_budget_100_2038461_12.err
│   ├── batch_ref_7_budget_100_2038461_12.out
│   ├── batch_ref_7_budget_100_2038461_13.err
│   ├── batch_ref_7_budget_100_2038461_13.out
│   ├── batch_ref_7_budget_100_2038461_14.err
│   ├── batch_ref_7_budget_100_2038461_14.out
│   ├── batch_ref_7_budget_100_2038461_15.err
│   ├── batch_ref_7_budget_100_2038461_15.out
│   ├── batch_ref_7_budget_100_2038461_16.err
│   ├── batch_ref_7_budget_100_2038461_16.out
│   ├── batch_ref_7_budget_100_2038461_17.err
│   ├── batch_ref_7_budget_100_2038461_17.out
│   ├── batch_ref_7_budget_100_2038461_18.err
│   ├── batch_ref_7_budget_100_2038461_18.out
│   ├── batch_ref_7_budget_100_2038461_19.err
│   ├── batch_ref_7_budget_100_2038461_19.out
│   ├── batch_ref_7_budget_100_2038461_2.err
│   ├── batch_ref_7_budget_100_2038461_2.out
│   ├── batch_ref_7_budget_100_2038461_20.err
│   ├── batch_ref_7_budget_100_2038461_20.out
│   ├── batch_ref_7_budget_100_2038461_21.err
│   ├── batch_ref_7_budget_100_2038461_21.out
│   ├── batch_ref_7_budget_100_2038461_22.err
│   ├── batch_ref_7_budget_100_2038461_22.out
│   ├── batch_ref_7_budget_100_2038461_23.err
│   ├── batch_ref_7_budget_100_2038461_23.out
│   ├── batch_ref_7_budget_100_2038461_24.err
│   ├── batch_ref_7_budget_100_2038461_24.out
│   ├── batch_ref_7_budget_100_2038461_25.err
│   ├── batch_ref_7_budget_100_2038461_25.out
│   ├── batch_ref_7_budget_100_2038461_26.err
│   ├── batch_ref_7_budget_100_2038461_26.out
│   ├── batch_ref_7_budget_100_2038461_27.err
│   ├── batch_ref_7_budget_100_2038461_27.out
│   ├── batch_ref_7_budget_100_2038461_28.err
│   ├── batch_ref_7_budget_100_2038461_28.out
│   ├── batch_ref_7_budget_100_2038461_29.err
│   ├── batch_ref_7_budget_100_2038461_29.out
│   ├── batch_ref_7_budget_100_2038461_3.err
│   ├── batch_ref_7_budget_100_2038461_3.out
│   ├── batch_ref_7_budget_100_2038461_30.err
│   ├── batch_ref_7_budget_100_2038461_30.out
│   ├── batch_ref_7_budget_100_2038461_31.err
│   ├── batch_ref_7_budget_100_2038461_31.out
│   ├── batch_ref_7_budget_100_2038461_32.err
│   ├── batch_ref_7_budget_100_2038461_32.out
│   ├── batch_ref_7_budget_100_2038461_33.err
│   ├── batch_ref_7_budget_100_2038461_33.out
│   ├── batch_ref_7_budget_100_2038461_34.err
│   ├── batch_ref_7_budget_100_2038461_34.out
│   ├── batch_ref_7_budget_100_2038461_35.err
│   ├── batch_ref_7_budget_100_2038461_35.out
│   ├── batch_ref_7_budget_100_2038461_36.err
│   ├── batch_ref_7_budget_100_2038461_36.out
│   ├── batch_ref_7_budget_100_2038461_37.err
│   ├── batch_ref_7_budget_100_2038461_37.out
│   ├── batch_ref_7_budget_100_2038461_38.err
│   ├── batch_ref_7_budget_100_2038461_38.out
│   ├── batch_ref_7_budget_100_2038461_39.err
│   ├── batch_ref_7_budget_100_2038461_39.out
│   ├── batch_ref_7_budget_100_2038461_4.err
│   ├── batch_ref_7_budget_100_2038461_4.out
│   ├── batch_ref_7_budget_100_2038461_40.err
│   ├── batch_ref_7_budget_100_2038461_40.out
│   ├── batch_ref_7_budget_100_2038461_41.err
│   ├── batch_ref_7_budget_100_2038461_41.out
│   ├── batch_ref_7_budget_100_2038461_42.err
│   ├── batch_ref_7_budget_100_2038461_42.out
│   ├── batch_ref_7_budget_100_2038461_43.err
│   ├── batch_ref_7_budget_100_2038461_43.out
│   ├── batch_ref_7_budget_100_2038461_44.err
│   ├── batch_ref_7_budget_100_2038461_44.out
│   ├── batch_ref_7_budget_100_2038461_45.err
│   ├── batch_ref_7_budget_100_2038461_45.out
│   ├── batch_ref_7_budget_100_2038461_46.err
│   ├── batch_ref_7_budget_100_2038461_46.out
│   ├── batch_ref_7_budget_100_2038461_47.err
│   ├── batch_ref_7_budget_100_2038461_47.out
│   ├── batch_ref_7_budget_100_2038461_48.err
│   ├── batch_ref_7_budget_100_2038461_48.out
│   ├── batch_ref_7_budget_100_2038461_49.err
│   ├── batch_ref_7_budget_100_2038461_49.out
│   ├── batch_ref_7_budget_100_2038461_5.err
│   ├── batch_ref_7_budget_100_2038461_5.out
│   ├── batch_ref_7_budget_100_2038461_50.err
│   ├── batch_ref_7_budget_100_2038461_50.out
│   ├── batch_ref_7_budget_100_2038461_51.err
│   ├── batch_ref_7_budget_100_2038461_51.out
│   ├── batch_ref_7_budget_100_2038461_52.err
│   ├── batch_ref_7_budget_100_2038461_52.out
│   ├── batch_ref_7_budget_100_2038461_53.err
│   ├── batch_ref_7_budget_100_2038461_53.out
│   ├── batch_ref_7_budget_100_2038461_54.err
│   ├── batch_ref_7_budget_100_2038461_54.out
│   ├── batch_ref_7_budget_100_2038461_55.err
│   ├── batch_ref_7_budget_100_2038461_55.out
│   ├── batch_ref_7_budget_100_2038461_56.err
│   ├── batch_ref_7_budget_100_2038461_56.out
│   ├── batch_ref_7_budget_100_2038461_57.err
│   ├── batch_ref_7_budget_100_2038461_57.out
│   ├── batch_ref_7_budget_100_2038461_58.err
│   ├── batch_ref_7_budget_100_2038461_58.out
│   ├── batch_ref_7_budget_100_2038461_59.err
│   ├── batch_ref_7_budget_100_2038461_59.out
│   ├── batch_ref_7_budget_100_2038461_6.err
│   ├── batch_ref_7_budget_100_2038461_6.out
│   ├── batch_ref_7_budget_100_2038461_60.err
│   ├── batch_ref_7_budget_100_2038461_60.out
│   ├── batch_ref_7_budget_100_2038461_61.err
│   ├── batch_ref_7_budget_100_2038461_61.out
│   ├── batch_ref_7_budget_100_2038461_62.err
│   ├── batch_ref_7_budget_100_2038461_62.out
│   ├── batch_ref_7_budget_100_2038461_63.err
│   ├── batch_ref_7_budget_100_2038461_63.out
│   ├── batch_ref_7_budget_100_2038461_64.err
│   ├── batch_ref_7_budget_100_2038461_64.out
│   ├── batch_ref_7_budget_100_2038461_65.err
│   ├── batch_ref_7_budget_100_2038461_65.out
│   ├── batch_ref_7_budget_100_2038461_66.err
│   ├── batch_ref_7_budget_100_2038461_66.out
│   ├── batch_ref_7_budget_100_2038461_67.err
│   ├── batch_ref_7_budget_100_2038461_67.out
│   ├── batch_ref_7_budget_100_2038461_68.err
│   ├── batch_ref_7_budget_100_2038461_68.out
│   ├── batch_ref_7_budget_100_2038461_69.err
│   ├── batch_ref_7_budget_100_2038461_69.out
│   ├── batch_ref_7_budget_100_2038461_7.err
│   ├── batch_ref_7_budget_100_2038461_7.out
│   ├── batch_ref_7_budget_100_2038461_70.err
│   ├── batch_ref_7_budget_100_2038461_70.out
│   ├── batch_ref_7_budget_100_2038461_71.err
│   ├── batch_ref_7_budget_100_2038461_71.out
│   ├── batch_ref_7_budget_100_2038461_72.err
│   ├── batch_ref_7_budget_100_2038461_72.out
│   ├── batch_ref_7_budget_100_2038461_73.err
│   ├── batch_ref_7_budget_100_2038461_73.out
│   ├── batch_ref_7_budget_100_2038461_74.err
│   ├── batch_ref_7_budget_100_2038461_74.out
│   ├── batch_ref_7_budget_100_2038461_75.err
│   ├── batch_ref_7_budget_100_2038461_75.out
│   ├── batch_ref_7_budget_100_2038461_76.err
│   ├── batch_ref_7_budget_100_2038461_76.out
│   ├── batch_ref_7_budget_100_2038461_77.err
│   ├── batch_ref_7_budget_100_2038461_77.out
│   ├── batch_ref_7_budget_100_2038461_78.err
│   ├── batch_ref_7_budget_100_2038461_78.out
│   ├── batch_ref_7_budget_100_2038461_79.err
│   ├── batch_ref_7_budget_100_2038461_79.out
│   ├── batch_ref_7_budget_100_2038461_8.err
│   ├── batch_ref_7_budget_100_2038461_8.out
│   ├── batch_ref_7_budget_100_2038461_80.err
│   ├── batch_ref_7_budget_100_2038461_80.out
│   ├── batch_ref_7_budget_100_2038461_81.err
│   ├── batch_ref_7_budget_100_2038461_81.out
│   ├── batch_ref_7_budget_100_2038461_9.err
│   ├── batch_ref_7_budget_100_2038461_9.out
│   ├── batch_ref_7_budget_100_2040044_1.err
│   ├── batch_ref_7_budget_100_2040044_1.out
│   ├── batch_ref_7_budget_100_2040044_10.err
│   ├── batch_ref_7_budget_100_2040044_10.out
│   ├── batch_ref_7_budget_100_2040044_11.err
│   ├── batch_ref_7_budget_100_2040044_11.out
│   ├── batch_ref_7_budget_100_2040044_12.err
│   ├── batch_ref_7_budget_100_2040044_12.out
│   ├── batch_ref_7_budget_100_2040044_13.err
│   ├── batch_ref_7_budget_100_2040044_13.out
│   ├── batch_ref_7_budget_100_2040044_14.err
│   ├── batch_ref_7_budget_100_2040044_14.out
│   ├── batch_ref_7_budget_100_2040044_15.err
│   ├── batch_ref_7_budget_100_2040044_15.out
│   ├── batch_ref_7_budget_100_2040044_16.err
│   ├── batch_ref_7_budget_100_2040044_16.out
│   ├── batch_ref_7_budget_100_2040044_17.err
│   ├── batch_ref_7_budget_100_2040044_17.out
│   ├── batch_ref_7_budget_100_2040044_18.err
│   ├── batch_ref_7_budget_100_2040044_18.out
│   ├── batch_ref_7_budget_100_2040044_19.err
│   ├── batch_ref_7_budget_100_2040044_19.out
│   ├── batch_ref_7_budget_100_2040044_2.err
│   ├── batch_ref_7_budget_100_2040044_2.out
│   ├── batch_ref_7_budget_100_2040044_20.err
│   ├── batch_ref_7_budget_100_2040044_20.out
│   ├── batch_ref_7_budget_100_2040044_21.err
│   ├── batch_ref_7_budget_100_2040044_21.out
│   ├── batch_ref_7_budget_100_2040044_22.err
│   ├── batch_ref_7_budget_100_2040044_22.out
│   ├── batch_ref_7_budget_100_2040044_23.err
│   ├── batch_ref_7_budget_100_2040044_23.out
│   ├── batch_ref_7_budget_100_2040044_24.err
│   ├── batch_ref_7_budget_100_2040044_24.out
│   ├── batch_ref_7_budget_100_2040044_25.err
│   ├── batch_ref_7_budget_100_2040044_25.out
│   ├── batch_ref_7_budget_100_2040044_26.err
│   ├── batch_ref_7_budget_100_2040044_26.out
│   ├── batch_ref_7_budget_100_2040044_27.err
│   ├── batch_ref_7_budget_100_2040044_27.out
│   ├── batch_ref_7_budget_100_2040044_28.err
│   ├── batch_ref_7_budget_100_2040044_28.out
│   ├── batch_ref_7_budget_100_2040044_29.err
│   ├── batch_ref_7_budget_100_2040044_29.out
│   ├── batch_ref_7_budget_100_2040044_3.err
│   ├── batch_ref_7_budget_100_2040044_3.out
│   ├── batch_ref_7_budget_100_2040044_30.err
│   ├── batch_ref_7_budget_100_2040044_30.out
│   ├── batch_ref_7_budget_100_2040044_31.err
│   ├── batch_ref_7_budget_100_2040044_31.out
│   ├── batch_ref_7_budget_100_2040044_32.err
│   ├── batch_ref_7_budget_100_2040044_32.out
│   ├── batch_ref_7_budget_100_2040044_33.err
│   ├── batch_ref_7_budget_100_2040044_33.out
│   ├── batch_ref_7_budget_100_2040044_34.err
│   ├── batch_ref_7_budget_100_2040044_34.out
│   ├── batch_ref_7_budget_100_2040044_35.err
│   ├── batch_ref_7_budget_100_2040044_35.out
│   ├── batch_ref_7_budget_100_2040044_36.err
│   ├── batch_ref_7_budget_100_2040044_36.out
│   ├── batch_ref_7_budget_100_2040044_37.err
│   ├── batch_ref_7_budget_100_2040044_37.out
│   ├── batch_ref_7_budget_100_2040044_38.err
│   ├── batch_ref_7_budget_100_2040044_38.out
│   ├── batch_ref_7_budget_100_2040044_39.err
│   ├── batch_ref_7_budget_100_2040044_39.out
│   ├── batch_ref_7_budget_100_2040044_4.err
│   ├── batch_ref_7_budget_100_2040044_4.out
│   ├── batch_ref_7_budget_100_2040044_40.err
│   ├── batch_ref_7_budget_100_2040044_40.out
│   ├── batch_ref_7_budget_100_2040044_41.err
│   ├── batch_ref_7_budget_100_2040044_41.out
│   ├── batch_ref_7_budget_100_2040044_42.err
│   ├── batch_ref_7_budget_100_2040044_42.out
│   ├── batch_ref_7_budget_100_2040044_43.err
│   ├── batch_ref_7_budget_100_2040044_43.out
│   ├── batch_ref_7_budget_100_2040044_44.err
│   ├── batch_ref_7_budget_100_2040044_44.out
│   ├── batch_ref_7_budget_100_2040044_45.err
│   ├── batch_ref_7_budget_100_2040044_45.out
│   ├── batch_ref_7_budget_100_2040044_46.err
│   ├── batch_ref_7_budget_100_2040044_46.out
│   ├── batch_ref_7_budget_100_2040044_47.err
│   ├── batch_ref_7_budget_100_2040044_47.out
│   ├── batch_ref_7_budget_100_2040044_48.err
│   ├── batch_ref_7_budget_100_2040044_48.out
│   ├── batch_ref_7_budget_100_2040044_49.err
│   ├── batch_ref_7_budget_100_2040044_49.out
│   ├── batch_ref_7_budget_100_2040044_5.err
│   ├── batch_ref_7_budget_100_2040044_5.out
│   ├── batch_ref_7_budget_100_2040044_50.err
│   ├── batch_ref_7_budget_100_2040044_50.out
│   ├── batch_ref_7_budget_100_2040044_51.err
│   ├── batch_ref_7_budget_100_2040044_51.out
│   ├── batch_ref_7_budget_100_2040044_52.err
│   ├── batch_ref_7_budget_100_2040044_52.out
│   ├── batch_ref_7_budget_100_2040044_53.err
│   ├── batch_ref_7_budget_100_2040044_53.out
│   ├── batch_ref_7_budget_100_2040044_54.err
│   ├── batch_ref_7_budget_100_2040044_54.out
│   ├── batch_ref_7_budget_100_2040044_55.err
│   ├── batch_ref_7_budget_100_2040044_55.out
│   ├── batch_ref_7_budget_100_2040044_56.err
│   ├── batch_ref_7_budget_100_2040044_56.out
│   ├── batch_ref_7_budget_100_2040044_57.err
│   ├── batch_ref_7_budget_100_2040044_57.out
│   ├── batch_ref_7_budget_100_2040044_58.err
│   ├── batch_ref_7_budget_100_2040044_58.out
│   ├── batch_ref_7_budget_100_2040044_59.err
│   ├── batch_ref_7_budget_100_2040044_59.out
│   ├── batch_ref_7_budget_100_2040044_6.err
│   ├── batch_ref_7_budget_100_2040044_6.out
│   ├── batch_ref_7_budget_100_2040044_60.err
│   ├── batch_ref_7_budget_100_2040044_60.out
│   ├── batch_ref_7_budget_100_2040044_61.err
│   ├── batch_ref_7_budget_100_2040044_61.out
│   ├── batch_ref_7_budget_100_2040044_62.err
│   ├── batch_ref_7_budget_100_2040044_62.out
│   ├── batch_ref_7_budget_100_2040044_63.err
│   ├── batch_ref_7_budget_100_2040044_63.out
│   ├── batch_ref_7_budget_100_2040044_64.err
│   ├── batch_ref_7_budget_100_2040044_64.out
│   ├── batch_ref_7_budget_100_2040044_65.err
│   ├── batch_ref_7_budget_100_2040044_65.out
│   ├── batch_ref_7_budget_100_2040044_66.err
│   ├── batch_ref_7_budget_100_2040044_66.out
│   ├── batch_ref_7_budget_100_2040044_67.err
│   ├── batch_ref_7_budget_100_2040044_67.out
│   ├── batch_ref_7_budget_100_2040044_68.err
│   ├── batch_ref_7_budget_100_2040044_68.out
│   ├── batch_ref_7_budget_100_2040044_69.err
│   ├── batch_ref_7_budget_100_2040044_69.out
│   ├── batch_ref_7_budget_100_2040044_7.err
│   ├── batch_ref_7_budget_100_2040044_7.out
│   ├── batch_ref_7_budget_100_2040044_70.err
│   ├── batch_ref_7_budget_100_2040044_70.out
│   ├── batch_ref_7_budget_100_2040044_71.err
│   ├── batch_ref_7_budget_100_2040044_71.out
│   ├── batch_ref_7_budget_100_2040044_72.err
│   ├── batch_ref_7_budget_100_2040044_72.out
│   ├── batch_ref_7_budget_100_2040044_73.err
│   ├── batch_ref_7_budget_100_2040044_73.out
│   ├── batch_ref_7_budget_100_2040044_74.err
│   ├── batch_ref_7_budget_100_2040044_74.out
│   ├── batch_ref_7_budget_100_2040044_75.err
│   ├── batch_ref_7_budget_100_2040044_75.out
│   ├── batch_ref_7_budget_100_2040044_76.err
│   ├── batch_ref_7_budget_100_2040044_76.out
│   ├── batch_ref_7_budget_100_2040044_77.err
│   ├── batch_ref_7_budget_100_2040044_77.out
│   ├── batch_ref_7_budget_100_2040044_78.err
│   ├── batch_ref_7_budget_100_2040044_78.out
│   ├── batch_ref_7_budget_100_2040044_79.err
│   ├── batch_ref_7_budget_100_2040044_79.out
│   ├── batch_ref_7_budget_100_2040044_8.err
│   ├── batch_ref_7_budget_100_2040044_8.out
│   ├── batch_ref_7_budget_100_2040044_80.err
│   ├── batch_ref_7_budget_100_2040044_80.out
│   ├── batch_ref_7_budget_100_2040044_81.err
│   ├── batch_ref_7_budget_100_2040044_81.out
│   ├── batch_ref_7_budget_100_2040044_9.err
│   ├── batch_ref_7_budget_100_2040044_9.out
│   ├── batch_ref_7_budget_150_2038462_1.err
│   ├── batch_ref_7_budget_150_2038462_1.out
│   ├── batch_ref_7_budget_150_2038462_10.err
│   ├── batch_ref_7_budget_150_2038462_10.out
│   ├── batch_ref_7_budget_150_2038462_11.err
│   ├── batch_ref_7_budget_150_2038462_11.out
│   ├── batch_ref_7_budget_150_2038462_12.err
│   ├── batch_ref_7_budget_150_2038462_12.out
│   ├── batch_ref_7_budget_150_2038462_13.err
│   ├── batch_ref_7_budget_150_2038462_13.out
│   ├── batch_ref_7_budget_150_2038462_14.err
│   ├── batch_ref_7_budget_150_2038462_14.out
│   ├── batch_ref_7_budget_150_2038462_15.err
│   ├── batch_ref_7_budget_150_2038462_15.out
│   ├── batch_ref_7_budget_150_2038462_16.err
│   ├── batch_ref_7_budget_150_2038462_16.out
│   ├── batch_ref_7_budget_150_2038462_17.err
│   ├── batch_ref_7_budget_150_2038462_17.out
│   ├── batch_ref_7_budget_150_2038462_18.err
│   ├── batch_ref_7_budget_150_2038462_18.out
│   ├── batch_ref_7_budget_150_2038462_19.err
│   ├── batch_ref_7_budget_150_2038462_19.out
│   ├── batch_ref_7_budget_150_2038462_2.err
│   ├── batch_ref_7_budget_150_2038462_2.out
│   ├── batch_ref_7_budget_150_2038462_20.err
│   ├── batch_ref_7_budget_150_2038462_20.out
│   ├── batch_ref_7_budget_150_2038462_21.err
│   ├── batch_ref_7_budget_150_2038462_21.out
│   ├── batch_ref_7_budget_150_2038462_22.err
│   ├── batch_ref_7_budget_150_2038462_22.out
│   ├── batch_ref_7_budget_150_2038462_23.err
│   ├── batch_ref_7_budget_150_2038462_23.out
│   ├── batch_ref_7_budget_150_2038462_24.err
│   ├── batch_ref_7_budget_150_2038462_24.out
│   ├── batch_ref_7_budget_150_2038462_25.err
│   ├── batch_ref_7_budget_150_2038462_25.out
│   ├── batch_ref_7_budget_150_2038462_26.err
│   ├── batch_ref_7_budget_150_2038462_26.out
│   ├── batch_ref_7_budget_150_2038462_27.err
│   ├── batch_ref_7_budget_150_2038462_27.out
│   ├── batch_ref_7_budget_150_2038462_28.err
│   ├── batch_ref_7_budget_150_2038462_28.out
│   ├── batch_ref_7_budget_150_2038462_29.err
│   ├── batch_ref_7_budget_150_2038462_29.out
│   ├── batch_ref_7_budget_150_2038462_3.err
│   ├── batch_ref_7_budget_150_2038462_3.out
│   ├── batch_ref_7_budget_150_2038462_30.err
│   ├── batch_ref_7_budget_150_2038462_30.out
│   ├── batch_ref_7_budget_150_2038462_31.err
│   ├── batch_ref_7_budget_150_2038462_31.out
│   ├── batch_ref_7_budget_150_2038462_32.err
│   ├── batch_ref_7_budget_150_2038462_32.out
│   ├── batch_ref_7_budget_150_2038462_33.err
│   ├── batch_ref_7_budget_150_2038462_33.out
│   ├── batch_ref_7_budget_150_2038462_34.err
│   ├── batch_ref_7_budget_150_2038462_34.out
│   ├── batch_ref_7_budget_150_2038462_35.err
│   ├── batch_ref_7_budget_150_2038462_35.out
│   ├── batch_ref_7_budget_150_2038462_36.err
│   ├── batch_ref_7_budget_150_2038462_36.out
│   ├── batch_ref_7_budget_150_2038462_37.err
│   ├── batch_ref_7_budget_150_2038462_37.out
│   ├── batch_ref_7_budget_150_2038462_38.err
│   ├── batch_ref_7_budget_150_2038462_38.out
│   ├── batch_ref_7_budget_150_2038462_39.err
│   ├── batch_ref_7_budget_150_2038462_39.out
│   ├── batch_ref_7_budget_150_2038462_4.err
│   ├── batch_ref_7_budget_150_2038462_4.out
│   ├── batch_ref_7_budget_150_2038462_40.err
│   ├── batch_ref_7_budget_150_2038462_40.out
│   ├── batch_ref_7_budget_150_2038462_41.err
│   ├── batch_ref_7_budget_150_2038462_41.out
│   ├── batch_ref_7_budget_150_2038462_42.err
│   ├── batch_ref_7_budget_150_2038462_42.out
│   ├── batch_ref_7_budget_150_2038462_43.err
│   ├── batch_ref_7_budget_150_2038462_43.out
│   ├── batch_ref_7_budget_150_2038462_44.err
│   ├── batch_ref_7_budget_150_2038462_44.out
│   ├── batch_ref_7_budget_150_2038462_45.err
│   ├── batch_ref_7_budget_150_2038462_45.out
│   ├── batch_ref_7_budget_150_2038462_46.err
│   ├── batch_ref_7_budget_150_2038462_46.out
│   ├── batch_ref_7_budget_150_2038462_47.err
│   ├── batch_ref_7_budget_150_2038462_47.out
│   ├── batch_ref_7_budget_150_2038462_48.err
│   ├── batch_ref_7_budget_150_2038462_48.out
│   ├── batch_ref_7_budget_150_2038462_49.err
│   ├── batch_ref_7_budget_150_2038462_49.out
│   ├── batch_ref_7_budget_150_2038462_5.err
│   ├── batch_ref_7_budget_150_2038462_5.out
│   ├── batch_ref_7_budget_150_2038462_50.err
│   ├── batch_ref_7_budget_150_2038462_50.out
│   ├── batch_ref_7_budget_150_2038462_51.err
│   ├── batch_ref_7_budget_150_2038462_51.out
│   ├── batch_ref_7_budget_150_2038462_52.err
│   ├── batch_ref_7_budget_150_2038462_52.out
│   ├── batch_ref_7_budget_150_2038462_53.err
│   ├── batch_ref_7_budget_150_2038462_53.out
│   ├── batch_ref_7_budget_150_2038462_54.err
│   ├── batch_ref_7_budget_150_2038462_54.out
│   ├── batch_ref_7_budget_150_2038462_55.err
│   ├── batch_ref_7_budget_150_2038462_55.out
│   ├── batch_ref_7_budget_150_2038462_56.err
│   ├── batch_ref_7_budget_150_2038462_56.out
│   ├── batch_ref_7_budget_150_2038462_57.err
│   ├── batch_ref_7_budget_150_2038462_57.out
│   ├── batch_ref_7_budget_150_2038462_58.err
│   ├── batch_ref_7_budget_150_2038462_58.out
│   ├── batch_ref_7_budget_150_2038462_59.err
│   ├── batch_ref_7_budget_150_2038462_59.out
│   ├── batch_ref_7_budget_150_2038462_6.err
│   ├── batch_ref_7_budget_150_2038462_6.out
│   ├── batch_ref_7_budget_150_2038462_60.err
│   ├── batch_ref_7_budget_150_2038462_60.out
│   ├── batch_ref_7_budget_150_2038462_61.err
│   ├── batch_ref_7_budget_150_2038462_61.out
│   ├── batch_ref_7_budget_150_2038462_62.err
│   ├── batch_ref_7_budget_150_2038462_62.out
│   ├── batch_ref_7_budget_150_2038462_63.err
│   ├── batch_ref_7_budget_150_2038462_63.out
│   ├── batch_ref_7_budget_150_2038462_64.err
│   ├── batch_ref_7_budget_150_2038462_64.out
│   ├── batch_ref_7_budget_150_2038462_65.err
│   ├── batch_ref_7_budget_150_2038462_65.out
│   ├── batch_ref_7_budget_150_2038462_66.err
│   ├── batch_ref_7_budget_150_2038462_66.out
│   ├── batch_ref_7_budget_150_2038462_67.err
│   ├── batch_ref_7_budget_150_2038462_67.out
│   ├── batch_ref_7_budget_150_2038462_68.err
│   ├── batch_ref_7_budget_150_2038462_68.out
│   ├── batch_ref_7_budget_150_2038462_69.err
│   ├── batch_ref_7_budget_150_2038462_69.out
│   ├── batch_ref_7_budget_150_2038462_7.err
│   ├── batch_ref_7_budget_150_2038462_7.out
│   ├── batch_ref_7_budget_150_2038462_70.err
│   ├── batch_ref_7_budget_150_2038462_70.out
│   ├── batch_ref_7_budget_150_2038462_71.err
│   ├── batch_ref_7_budget_150_2038462_71.out
│   ├── batch_ref_7_budget_150_2038462_72.err
│   ├── batch_ref_7_budget_150_2038462_72.out
│   ├── batch_ref_7_budget_150_2038462_73.err
│   ├── batch_ref_7_budget_150_2038462_73.out
│   ├── batch_ref_7_budget_150_2038462_74.err
│   ├── batch_ref_7_budget_150_2038462_74.out
│   ├── batch_ref_7_budget_150_2038462_75.err
│   ├── batch_ref_7_budget_150_2038462_75.out
│   ├── batch_ref_7_budget_150_2038462_76.err
│   ├── batch_ref_7_budget_150_2038462_76.out
│   ├── batch_ref_7_budget_150_2038462_77.err
│   ├── batch_ref_7_budget_150_2038462_77.out
│   ├── batch_ref_7_budget_150_2038462_78.err
│   ├── batch_ref_7_budget_150_2038462_78.out
│   ├── batch_ref_7_budget_150_2038462_79.err
│   ├── batch_ref_7_budget_150_2038462_79.out
│   ├── batch_ref_7_budget_150_2038462_8.err
│   ├── batch_ref_7_budget_150_2038462_8.out
│   ├── batch_ref_7_budget_150_2038462_80.err
│   ├── batch_ref_7_budget_150_2038462_80.out
│   ├── batch_ref_7_budget_150_2038462_81.err
│   ├── batch_ref_7_budget_150_2038462_81.out
│   ├── batch_ref_7_budget_150_2038462_9.err
│   ├── batch_ref_7_budget_150_2038462_9.out
│   ├── batch_ref_7_budget_150_2040045_1.err
│   ├── batch_ref_7_budget_150_2040045_1.out
│   ├── batch_ref_7_budget_150_2040045_10.err
│   ├── batch_ref_7_budget_150_2040045_10.out
│   ├── batch_ref_7_budget_150_2040045_11.err
│   ├── batch_ref_7_budget_150_2040045_11.out
│   ├── batch_ref_7_budget_150_2040045_12.err
│   ├── batch_ref_7_budget_150_2040045_12.out
│   ├── batch_ref_7_budget_150_2040045_13.err
│   ├── batch_ref_7_budget_150_2040045_13.out
│   ├── batch_ref_7_budget_150_2040045_14.err
│   ├── batch_ref_7_budget_150_2040045_14.out
│   ├── batch_ref_7_budget_150_2040045_15.err
│   ├── batch_ref_7_budget_150_2040045_15.out
│   ├── batch_ref_7_budget_150_2040045_16.err
│   ├── batch_ref_7_budget_150_2040045_16.out
│   ├── batch_ref_7_budget_150_2040045_17.err
│   ├── batch_ref_7_budget_150_2040045_17.out
│   ├── batch_ref_7_budget_150_2040045_18.err
│   ├── batch_ref_7_budget_150_2040045_18.out
│   ├── batch_ref_7_budget_150_2040045_19.err
│   ├── batch_ref_7_budget_150_2040045_19.out
│   ├── batch_ref_7_budget_150_2040045_2.err
│   ├── batch_ref_7_budget_150_2040045_2.out
│   ├── batch_ref_7_budget_150_2040045_20.err
│   ├── batch_ref_7_budget_150_2040045_20.out
│   ├── batch_ref_7_budget_150_2040045_21.err
│   ├── batch_ref_7_budget_150_2040045_21.out
│   ├── batch_ref_7_budget_150_2040045_22.err
│   ├── batch_ref_7_budget_150_2040045_22.out
│   ├── batch_ref_7_budget_150_2040045_23.err
│   ├── batch_ref_7_budget_150_2040045_23.out
│   ├── batch_ref_7_budget_150_2040045_24.err
│   ├── batch_ref_7_budget_150_2040045_24.out
│   ├── batch_ref_7_budget_150_2040045_25.err
│   ├── batch_ref_7_budget_150_2040045_25.out
│   ├── batch_ref_7_budget_150_2040045_26.err
│   ├── batch_ref_7_budget_150_2040045_26.out
│   ├── batch_ref_7_budget_150_2040045_27.err
│   ├── batch_ref_7_budget_150_2040045_27.out
│   ├── batch_ref_7_budget_150_2040045_28.err
│   ├── batch_ref_7_budget_150_2040045_28.out
│   ├── batch_ref_7_budget_150_2040045_29.err
│   ├── batch_ref_7_budget_150_2040045_29.out
│   ├── batch_ref_7_budget_150_2040045_3.err
│   ├── batch_ref_7_budget_150_2040045_3.out
│   ├── batch_ref_7_budget_150_2040045_30.err
│   ├── batch_ref_7_budget_150_2040045_30.out
│   ├── batch_ref_7_budget_150_2040045_31.err
│   ├── batch_ref_7_budget_150_2040045_31.out
│   ├── batch_ref_7_budget_150_2040045_32.err
│   ├── batch_ref_7_budget_150_2040045_32.out
│   ├── batch_ref_7_budget_150_2040045_33.err
│   ├── batch_ref_7_budget_150_2040045_33.out
│   ├── batch_ref_7_budget_150_2040045_34.err
│   ├── batch_ref_7_budget_150_2040045_34.out
│   ├── batch_ref_7_budget_150_2040045_35.err
│   ├── batch_ref_7_budget_150_2040045_35.out
│   ├── batch_ref_7_budget_150_2040045_36.err
│   ├── batch_ref_7_budget_150_2040045_36.out
│   ├── batch_ref_7_budget_150_2040045_37.err
│   ├── batch_ref_7_budget_150_2040045_37.out
│   ├── batch_ref_7_budget_150_2040045_38.err
│   ├── batch_ref_7_budget_150_2040045_38.out
│   ├── batch_ref_7_budget_150_2040045_39.err
│   ├── batch_ref_7_budget_150_2040045_39.out
│   ├── batch_ref_7_budget_150_2040045_4.err
│   ├── batch_ref_7_budget_150_2040045_4.out
│   ├── batch_ref_7_budget_150_2040045_40.err
│   ├── batch_ref_7_budget_150_2040045_40.out
│   ├── batch_ref_7_budget_150_2040045_41.err
│   ├── batch_ref_7_budget_150_2040045_41.out
│   ├── batch_ref_7_budget_150_2040045_42.err
│   ├── batch_ref_7_budget_150_2040045_42.out
│   ├── batch_ref_7_budget_150_2040045_43.err
│   ├── batch_ref_7_budget_150_2040045_43.out
│   ├── batch_ref_7_budget_150_2040045_44.err
│   ├── batch_ref_7_budget_150_2040045_44.out
│   ├── batch_ref_7_budget_150_2040045_45.err
│   ├── batch_ref_7_budget_150_2040045_45.out
│   ├── batch_ref_7_budget_150_2040045_46.err
│   ├── batch_ref_7_budget_150_2040045_46.out
│   ├── batch_ref_7_budget_150_2040045_47.err
│   ├── batch_ref_7_budget_150_2040045_47.out
│   ├── batch_ref_7_budget_150_2040045_48.err
│   ├── batch_ref_7_budget_150_2040045_48.out
│   ├── batch_ref_7_budget_150_2040045_49.err
│   ├── batch_ref_7_budget_150_2040045_49.out
│   ├── batch_ref_7_budget_150_2040045_5.err
│   ├── batch_ref_7_budget_150_2040045_5.out
│   ├── batch_ref_7_budget_150_2040045_50.err
│   ├── batch_ref_7_budget_150_2040045_50.out
│   ├── batch_ref_7_budget_150_2040045_51.err
│   ├── batch_ref_7_budget_150_2040045_51.out
│   ├── batch_ref_7_budget_150_2040045_52.err
│   ├── batch_ref_7_budget_150_2040045_52.out
│   ├── batch_ref_7_budget_150_2040045_53.err
│   ├── batch_ref_7_budget_150_2040045_53.out
│   ├── batch_ref_7_budget_150_2040045_54.err
│   ├── batch_ref_7_budget_150_2040045_54.out
│   ├── batch_ref_7_budget_150_2040045_55.err
│   ├── batch_ref_7_budget_150_2040045_55.out
│   ├── batch_ref_7_budget_150_2040045_56.err
│   ├── batch_ref_7_budget_150_2040045_56.out
│   ├── batch_ref_7_budget_150_2040045_57.err
│   ├── batch_ref_7_budget_150_2040045_57.out
│   ├── batch_ref_7_budget_150_2040045_58.err
│   ├── batch_ref_7_budget_150_2040045_58.out
│   ├── batch_ref_7_budget_150_2040045_59.err
│   ├── batch_ref_7_budget_150_2040045_59.out
│   ├── batch_ref_7_budget_150_2040045_6.err
│   ├── batch_ref_7_budget_150_2040045_6.out
│   ├── batch_ref_7_budget_150_2040045_60.err
│   ├── batch_ref_7_budget_150_2040045_60.out
│   ├── batch_ref_7_budget_150_2040045_61.err
│   ├── batch_ref_7_budget_150_2040045_61.out
│   ├── batch_ref_7_budget_150_2040045_62.err
│   ├── batch_ref_7_budget_150_2040045_62.out
│   ├── batch_ref_7_budget_150_2040045_63.err
│   ├── batch_ref_7_budget_150_2040045_63.out
│   ├── batch_ref_7_budget_150_2040045_64.err
│   ├── batch_ref_7_budget_150_2040045_64.out
│   ├── batch_ref_7_budget_150_2040045_65.err
│   ├── batch_ref_7_budget_150_2040045_65.out
│   ├── batch_ref_7_budget_150_2040045_66.err
│   ├── batch_ref_7_budget_150_2040045_66.out
│   ├── batch_ref_7_budget_150_2040045_67.err
│   ├── batch_ref_7_budget_150_2040045_67.out
│   ├── batch_ref_7_budget_150_2040045_68.err
│   ├── batch_ref_7_budget_150_2040045_68.out
│   ├── batch_ref_7_budget_150_2040045_69.err
│   ├── batch_ref_7_budget_150_2040045_69.out
│   ├── batch_ref_7_budget_150_2040045_7.err
│   ├── batch_ref_7_budget_150_2040045_7.out
│   ├── batch_ref_7_budget_150_2040045_70.err
│   ├── batch_ref_7_budget_150_2040045_70.out
│   ├── batch_ref_7_budget_150_2040045_71.err
│   ├── batch_ref_7_budget_150_2040045_71.out
│   ├── batch_ref_7_budget_150_2040045_72.err
│   ├── batch_ref_7_budget_150_2040045_72.out
│   ├── batch_ref_7_budget_150_2040045_73.err
│   ├── batch_ref_7_budget_150_2040045_73.out
│   ├── batch_ref_7_budget_150_2040045_74.err
│   ├── batch_ref_7_budget_150_2040045_74.out
│   ├── batch_ref_7_budget_150_2040045_75.err
│   ├── batch_ref_7_budget_150_2040045_75.out
│   ├── batch_ref_7_budget_150_2040045_76.err
│   ├── batch_ref_7_budget_150_2040045_76.out
│   ├── batch_ref_7_budget_150_2040045_77.err
│   ├── batch_ref_7_budget_150_2040045_77.out
│   ├── batch_ref_7_budget_150_2040045_78.err
│   ├── batch_ref_7_budget_150_2040045_78.out
│   ├── batch_ref_7_budget_150_2040045_79.err
│   ├── batch_ref_7_budget_150_2040045_79.out
│   ├── batch_ref_7_budget_150_2040045_8.err
│   ├── batch_ref_7_budget_150_2040045_8.out
│   ├── batch_ref_7_budget_150_2040045_80.err
│   ├── batch_ref_7_budget_150_2040045_80.out
│   ├── batch_ref_7_budget_150_2040045_81.err
│   ├── batch_ref_7_budget_150_2040045_81.out
│   ├── batch_ref_7_budget_150_2040045_9.err
│   ├── batch_ref_7_budget_150_2040045_9.out
│   ├── batch_ref_7_budget_200_2038463_1.err
│   ├── batch_ref_7_budget_200_2038463_1.out
│   ├── batch_ref_7_budget_200_2038463_10.err
│   ├── batch_ref_7_budget_200_2038463_10.out
│   ├── batch_ref_7_budget_200_2038463_11.err
│   ├── batch_ref_7_budget_200_2038463_11.out
│   ├── batch_ref_7_budget_200_2038463_12.err
│   ├── batch_ref_7_budget_200_2038463_12.out
│   ├── batch_ref_7_budget_200_2038463_13.err
│   ├── batch_ref_7_budget_200_2038463_13.out
│   ├── batch_ref_7_budget_200_2038463_14.err
│   ├── batch_ref_7_budget_200_2038463_14.out
│   ├── batch_ref_7_budget_200_2038463_15.err
│   ├── batch_ref_7_budget_200_2038463_15.out
│   ├── batch_ref_7_budget_200_2038463_16.err
│   ├── batch_ref_7_budget_200_2038463_16.out
│   ├── batch_ref_7_budget_200_2038463_17.err
│   ├── batch_ref_7_budget_200_2038463_17.out
│   ├── batch_ref_7_budget_200_2038463_18.err
│   ├── batch_ref_7_budget_200_2038463_18.out
│   ├── batch_ref_7_budget_200_2038463_19.err
│   ├── batch_ref_7_budget_200_2038463_19.out
│   ├── batch_ref_7_budget_200_2038463_2.err
│   ├── batch_ref_7_budget_200_2038463_2.out
│   ├── batch_ref_7_budget_200_2038463_20.err
│   ├── batch_ref_7_budget_200_2038463_20.out
│   ├── batch_ref_7_budget_200_2038463_21.err
│   ├── batch_ref_7_budget_200_2038463_21.out
│   ├── batch_ref_7_budget_200_2038463_22.err
│   ├── batch_ref_7_budget_200_2038463_22.out
│   ├── batch_ref_7_budget_200_2038463_23.err
│   ├── batch_ref_7_budget_200_2038463_23.out
│   ├── batch_ref_7_budget_200_2038463_24.err
│   ├── batch_ref_7_budget_200_2038463_24.out
│   ├── batch_ref_7_budget_200_2038463_25.err
│   ├── batch_ref_7_budget_200_2038463_25.out
│   ├── batch_ref_7_budget_200_2038463_26.err
│   ├── batch_ref_7_budget_200_2038463_26.out
│   ├── batch_ref_7_budget_200_2038463_27.err
│   ├── batch_ref_7_budget_200_2038463_27.out
│   ├── batch_ref_7_budget_200_2038463_28.err
│   ├── batch_ref_7_budget_200_2038463_28.out
│   ├── batch_ref_7_budget_200_2038463_29.err
│   ├── batch_ref_7_budget_200_2038463_29.out
│   ├── batch_ref_7_budget_200_2038463_3.err
│   ├── batch_ref_7_budget_200_2038463_3.out
│   ├── batch_ref_7_budget_200_2038463_30.err
│   ├── batch_ref_7_budget_200_2038463_30.out
│   ├── batch_ref_7_budget_200_2038463_31.err
│   ├── batch_ref_7_budget_200_2038463_31.out
│   ├── batch_ref_7_budget_200_2038463_32.err
│   ├── batch_ref_7_budget_200_2038463_32.out
│   ├── batch_ref_7_budget_200_2038463_33.err
│   ├── batch_ref_7_budget_200_2038463_33.out
│   ├── batch_ref_7_budget_200_2038463_34.err
│   ├── batch_ref_7_budget_200_2038463_34.out
│   ├── batch_ref_7_budget_200_2038463_35.err
│   ├── batch_ref_7_budget_200_2038463_35.out
│   ├── batch_ref_7_budget_200_2038463_36.err
│   ├── batch_ref_7_budget_200_2038463_36.out
│   ├── batch_ref_7_budget_200_2038463_37.err
│   ├── batch_ref_7_budget_200_2038463_37.out
│   ├── batch_ref_7_budget_200_2038463_38.err
│   ├── batch_ref_7_budget_200_2038463_38.out
│   ├── batch_ref_7_budget_200_2038463_39.err
│   ├── batch_ref_7_budget_200_2038463_39.out
│   ├── batch_ref_7_budget_200_2038463_4.err
│   ├── batch_ref_7_budget_200_2038463_4.out
│   ├── batch_ref_7_budget_200_2038463_40.err
│   ├── batch_ref_7_budget_200_2038463_40.out
│   ├── batch_ref_7_budget_200_2038463_41.err
│   ├── batch_ref_7_budget_200_2038463_41.out
│   ├── batch_ref_7_budget_200_2038463_42.err
│   ├── batch_ref_7_budget_200_2038463_42.out
│   ├── batch_ref_7_budget_200_2038463_43.err
│   ├── batch_ref_7_budget_200_2038463_43.out
│   ├── batch_ref_7_budget_200_2038463_44.err
│   ├── batch_ref_7_budget_200_2038463_44.out
│   ├── batch_ref_7_budget_200_2038463_45.err
│   ├── batch_ref_7_budget_200_2038463_45.out
│   ├── batch_ref_7_budget_200_2038463_46.err
│   ├── batch_ref_7_budget_200_2038463_46.out
│   ├── batch_ref_7_budget_200_2038463_47.err
│   ├── batch_ref_7_budget_200_2038463_47.out
│   ├── batch_ref_7_budget_200_2038463_48.err
│   ├── batch_ref_7_budget_200_2038463_48.out
│   ├── batch_ref_7_budget_200_2038463_49.err
│   ├── batch_ref_7_budget_200_2038463_49.out
│   ├── batch_ref_7_budget_200_2038463_5.err
│   ├── batch_ref_7_budget_200_2038463_5.out
│   ├── batch_ref_7_budget_200_2038463_50.err
│   ├── batch_ref_7_budget_200_2038463_50.out
│   ├── batch_ref_7_budget_200_2038463_51.err
│   ├── batch_ref_7_budget_200_2038463_51.out
│   ├── batch_ref_7_budget_200_2038463_52.err
│   ├── batch_ref_7_budget_200_2038463_52.out
│   ├── batch_ref_7_budget_200_2038463_53.err
│   ├── batch_ref_7_budget_200_2038463_53.out
│   ├── batch_ref_7_budget_200_2038463_54.err
│   ├── batch_ref_7_budget_200_2038463_54.out
│   ├── batch_ref_7_budget_200_2038463_55.err
│   ├── batch_ref_7_budget_200_2038463_55.out
│   ├── batch_ref_7_budget_200_2038463_56.err
│   ├── batch_ref_7_budget_200_2038463_56.out
│   ├── batch_ref_7_budget_200_2038463_57.err
│   ├── batch_ref_7_budget_200_2038463_57.out
│   ├── batch_ref_7_budget_200_2038463_58.err
│   ├── batch_ref_7_budget_200_2038463_58.out
│   ├── batch_ref_7_budget_200_2038463_59.err
│   ├── batch_ref_7_budget_200_2038463_59.out
│   ├── batch_ref_7_budget_200_2038463_6.err
│   ├── batch_ref_7_budget_200_2038463_6.out
│   ├── batch_ref_7_budget_200_2038463_60.err
│   ├── batch_ref_7_budget_200_2038463_60.out
│   ├── batch_ref_7_budget_200_2038463_61.err
│   ├── batch_ref_7_budget_200_2038463_61.out
│   ├── batch_ref_7_budget_200_2038463_62.err
│   ├── batch_ref_7_budget_200_2038463_62.out
│   ├── batch_ref_7_budget_200_2038463_63.err
│   ├── batch_ref_7_budget_200_2038463_63.out
│   ├── batch_ref_7_budget_200_2038463_64.err
│   ├── batch_ref_7_budget_200_2038463_64.out
│   ├── batch_ref_7_budget_200_2038463_65.err
│   ├── batch_ref_7_budget_200_2038463_65.out
│   ├── batch_ref_7_budget_200_2038463_66.err
│   ├── batch_ref_7_budget_200_2038463_66.out
│   ├── batch_ref_7_budget_200_2038463_67.err
│   ├── batch_ref_7_budget_200_2038463_67.out
│   ├── batch_ref_7_budget_200_2038463_68.err
│   ├── batch_ref_7_budget_200_2038463_68.out
│   ├── batch_ref_7_budget_200_2038463_69.err
│   ├── batch_ref_7_budget_200_2038463_69.out
│   ├── batch_ref_7_budget_200_2038463_7.err
│   ├── batch_ref_7_budget_200_2038463_7.out
│   ├── batch_ref_7_budget_200_2038463_70.err
│   ├── batch_ref_7_budget_200_2038463_70.out
│   ├── batch_ref_7_budget_200_2038463_71.err
│   ├── batch_ref_7_budget_200_2038463_71.out
│   ├── batch_ref_7_budget_200_2038463_72.err
│   ├── batch_ref_7_budget_200_2038463_72.out
│   ├── batch_ref_7_budget_200_2038463_73.err
│   ├── batch_ref_7_budget_200_2038463_73.out
│   ├── batch_ref_7_budget_200_2038463_74.err
│   ├── batch_ref_7_budget_200_2038463_74.out
│   ├── batch_ref_7_budget_200_2038463_75.err
│   ├── batch_ref_7_budget_200_2038463_75.out
│   ├── batch_ref_7_budget_200_2038463_76.err
│   ├── batch_ref_7_budget_200_2038463_76.out
│   ├── batch_ref_7_budget_200_2038463_77.err
│   ├── batch_ref_7_budget_200_2038463_77.out
│   ├── batch_ref_7_budget_200_2038463_78.err
│   ├── batch_ref_7_budget_200_2038463_78.out
│   ├── batch_ref_7_budget_200_2038463_79.err
│   ├── batch_ref_7_budget_200_2038463_79.out
│   ├── batch_ref_7_budget_200_2038463_8.err
│   ├── batch_ref_7_budget_200_2038463_8.out
│   ├── batch_ref_7_budget_200_2038463_80.err
│   ├── batch_ref_7_budget_200_2038463_80.out
│   ├── batch_ref_7_budget_200_2038463_81.err
│   ├── batch_ref_7_budget_200_2038463_81.out
│   ├── batch_ref_7_budget_200_2038463_9.err
│   ├── batch_ref_7_budget_200_2038463_9.out
│   ├── batch_ref_7_budget_200_2040206_1.err
│   ├── batch_ref_7_budget_200_2040206_1.out
│   ├── batch_ref_7_budget_200_2040206_10.err
│   ├── batch_ref_7_budget_200_2040206_10.out
│   ├── batch_ref_7_budget_200_2040206_11.err
│   ├── batch_ref_7_budget_200_2040206_11.out
│   ├── batch_ref_7_budget_200_2040206_12.err
│   ├── batch_ref_7_budget_200_2040206_12.out
│   ├── batch_ref_7_budget_200_2040206_13.err
│   ├── batch_ref_7_budget_200_2040206_13.out
│   ├── batch_ref_7_budget_200_2040206_14.err
│   ├── batch_ref_7_budget_200_2040206_14.out
│   ├── batch_ref_7_budget_200_2040206_15.err
│   ├── batch_ref_7_budget_200_2040206_15.out
│   ├── batch_ref_7_budget_200_2040206_16.err
│   ├── batch_ref_7_budget_200_2040206_16.out
│   ├── batch_ref_7_budget_200_2040206_17.err
│   ├── batch_ref_7_budget_200_2040206_17.out
│   ├── batch_ref_7_budget_200_2040206_18.err
│   ├── batch_ref_7_budget_200_2040206_18.out
│   ├── batch_ref_7_budget_200_2040206_19.err
│   ├── batch_ref_7_budget_200_2040206_19.out
│   ├── batch_ref_7_budget_200_2040206_2.err
│   ├── batch_ref_7_budget_200_2040206_2.out
│   ├── batch_ref_7_budget_200_2040206_20.err
│   ├── batch_ref_7_budget_200_2040206_20.out
│   ├── batch_ref_7_budget_200_2040206_21.err
│   ├── batch_ref_7_budget_200_2040206_21.out
│   ├── batch_ref_7_budget_200_2040206_22.err
│   ├── batch_ref_7_budget_200_2040206_22.out
│   ├── batch_ref_7_budget_200_2040206_23.err
│   ├── batch_ref_7_budget_200_2040206_23.out
│   ├── batch_ref_7_budget_200_2040206_24.err
│   ├── batch_ref_7_budget_200_2040206_24.out
│   ├── batch_ref_7_budget_200_2040206_25.err
│   ├── batch_ref_7_budget_200_2040206_25.out
│   ├── batch_ref_7_budget_200_2040206_26.err
│   ├── batch_ref_7_budget_200_2040206_26.out
│   ├── batch_ref_7_budget_200_2040206_27.err
│   ├── batch_ref_7_budget_200_2040206_27.out
│   ├── batch_ref_7_budget_200_2040206_28.err
│   ├── batch_ref_7_budget_200_2040206_28.out
│   ├── batch_ref_7_budget_200_2040206_29.err
│   ├── batch_ref_7_budget_200_2040206_29.out
│   ├── batch_ref_7_budget_200_2040206_3.err
│   ├── batch_ref_7_budget_200_2040206_3.out
│   ├── batch_ref_7_budget_200_2040206_30.err
│   ├── batch_ref_7_budget_200_2040206_30.out
│   ├── batch_ref_7_budget_200_2040206_31.err
│   ├── batch_ref_7_budget_200_2040206_31.out
│   ├── batch_ref_7_budget_200_2040206_32.err
│   ├── batch_ref_7_budget_200_2040206_32.out
│   ├── batch_ref_7_budget_200_2040206_33.err
│   ├── batch_ref_7_budget_200_2040206_33.out
│   ├── batch_ref_7_budget_200_2040206_34.err
│   ├── batch_ref_7_budget_200_2040206_34.out
│   ├── batch_ref_7_budget_200_2040206_35.err
│   ├── batch_ref_7_budget_200_2040206_35.out
│   ├── batch_ref_7_budget_200_2040206_36.err
│   ├── batch_ref_7_budget_200_2040206_36.out
│   ├── batch_ref_7_budget_200_2040206_37.err
│   ├── batch_ref_7_budget_200_2040206_37.out
│   ├── batch_ref_7_budget_200_2040206_38.err
│   ├── batch_ref_7_budget_200_2040206_38.out
│   ├── batch_ref_7_budget_200_2040206_39.err
│   ├── batch_ref_7_budget_200_2040206_39.out
│   ├── batch_ref_7_budget_200_2040206_4.err
│   ├── batch_ref_7_budget_200_2040206_4.out
│   ├── batch_ref_7_budget_200_2040206_40.err
│   ├── batch_ref_7_budget_200_2040206_40.out
│   ├── batch_ref_7_budget_200_2040206_41.err
│   ├── batch_ref_7_budget_200_2040206_41.out
│   ├── batch_ref_7_budget_200_2040206_42.err
│   ├── batch_ref_7_budget_200_2040206_42.out
│   ├── batch_ref_7_budget_200_2040206_43.err
│   ├── batch_ref_7_budget_200_2040206_43.out
│   ├── batch_ref_7_budget_200_2040206_44.err
│   ├── batch_ref_7_budget_200_2040206_44.out
│   ├── batch_ref_7_budget_200_2040206_45.err
│   ├── batch_ref_7_budget_200_2040206_45.out
│   ├── batch_ref_7_budget_200_2040206_46.err
│   ├── batch_ref_7_budget_200_2040206_46.out
│   ├── batch_ref_7_budget_200_2040206_47.err
│   ├── batch_ref_7_budget_200_2040206_47.out
│   ├── batch_ref_7_budget_200_2040206_48.err
│   ├── batch_ref_7_budget_200_2040206_48.out
│   ├── batch_ref_7_budget_200_2040206_49.err
│   ├── batch_ref_7_budget_200_2040206_49.out
│   ├── batch_ref_7_budget_200_2040206_5.err
│   ├── batch_ref_7_budget_200_2040206_5.out
│   ├── batch_ref_7_budget_200_2040206_50.err
│   ├── batch_ref_7_budget_200_2040206_50.out
│   ├── batch_ref_7_budget_200_2040206_51.err
│   ├── batch_ref_7_budget_200_2040206_51.out
│   ├── batch_ref_7_budget_200_2040206_52.err
│   ├── batch_ref_7_budget_200_2040206_52.out
│   ├── batch_ref_7_budget_200_2040206_53.err
│   ├── batch_ref_7_budget_200_2040206_53.out
│   ├── batch_ref_7_budget_200_2040206_54.err
│   ├── batch_ref_7_budget_200_2040206_54.out
│   ├── batch_ref_7_budget_200_2040206_55.err
│   ├── batch_ref_7_budget_200_2040206_55.out
│   ├── batch_ref_7_budget_200_2040206_56.err
│   ├── batch_ref_7_budget_200_2040206_56.out
│   ├── batch_ref_7_budget_200_2040206_57.err
│   ├── batch_ref_7_budget_200_2040206_57.out
│   ├── batch_ref_7_budget_200_2040206_58.err
│   ├── batch_ref_7_budget_200_2040206_58.out
│   ├── batch_ref_7_budget_200_2040206_59.err
│   ├── batch_ref_7_budget_200_2040206_59.out
│   ├── batch_ref_7_budget_200_2040206_6.err
│   ├── batch_ref_7_budget_200_2040206_6.out
│   ├── batch_ref_7_budget_200_2040206_60.err
│   ├── batch_ref_7_budget_200_2040206_60.out
│   ├── batch_ref_7_budget_200_2040206_61.err
│   ├── batch_ref_7_budget_200_2040206_61.out
│   ├── batch_ref_7_budget_200_2040206_62.err
│   ├── batch_ref_7_budget_200_2040206_62.out
│   ├── batch_ref_7_budget_200_2040206_63.err
│   ├── batch_ref_7_budget_200_2040206_63.out
│   ├── batch_ref_7_budget_200_2040206_64.err
│   ├── batch_ref_7_budget_200_2040206_64.out
│   ├── batch_ref_7_budget_200_2040206_65.err
│   ├── batch_ref_7_budget_200_2040206_65.out
│   ├── batch_ref_7_budget_200_2040206_66.err
│   ├── batch_ref_7_budget_200_2040206_66.out
│   ├── batch_ref_7_budget_200_2040206_67.err
│   ├── batch_ref_7_budget_200_2040206_67.out
│   ├── batch_ref_7_budget_200_2040206_68.err
│   ├── batch_ref_7_budget_200_2040206_68.out
│   ├── batch_ref_7_budget_200_2040206_69.err
│   ├── batch_ref_7_budget_200_2040206_69.out
│   ├── batch_ref_7_budget_200_2040206_7.err
│   ├── batch_ref_7_budget_200_2040206_7.out
│   ├── batch_ref_7_budget_200_2040206_70.err
│   ├── batch_ref_7_budget_200_2040206_70.out
│   ├── batch_ref_7_budget_200_2040206_71.err
│   ├── batch_ref_7_budget_200_2040206_71.out
│   ├── batch_ref_7_budget_200_2040206_72.err
│   ├── batch_ref_7_budget_200_2040206_72.out
│   ├── batch_ref_7_budget_200_2040206_73.err
│   ├── batch_ref_7_budget_200_2040206_73.out
│   ├── batch_ref_7_budget_200_2040206_74.err
│   ├── batch_ref_7_budget_200_2040206_74.out
│   ├── batch_ref_7_budget_200_2040206_75.err
│   ├── batch_ref_7_budget_200_2040206_75.out
│   ├── batch_ref_7_budget_200_2040206_76.err
│   ├── batch_ref_7_budget_200_2040206_76.out
│   ├── batch_ref_7_budget_200_2040206_77.err
│   ├── batch_ref_7_budget_200_2040206_77.out
│   ├── batch_ref_7_budget_200_2040206_78.err
│   ├── batch_ref_7_budget_200_2040206_78.out
│   ├── batch_ref_7_budget_200_2040206_79.err
│   ├── batch_ref_7_budget_200_2040206_79.out
│   ├── batch_ref_7_budget_200_2040206_8.err
│   ├── batch_ref_7_budget_200_2040206_8.out
│   ├── batch_ref_7_budget_200_2040206_80.err
│   ├── batch_ref_7_budget_200_2040206_80.out
│   ├── batch_ref_7_budget_200_2040206_81.err
│   ├── batch_ref_7_budget_200_2040206_81.out
│   ├── batch_ref_7_budget_200_2040206_9.err
│   ├── batch_ref_7_budget_200_2040206_9.out
│   ├── batch_ref_7_budget_50_2024857_1.err
│   ├── batch_ref_7_budget_50_2024857_1.out
│   ├── batch_ref_7_budget_50_2024857_10.err
│   ├── batch_ref_7_budget_50_2024857_10.out
│   ├── batch_ref_7_budget_50_2024857_11.err
│   ├── batch_ref_7_budget_50_2024857_11.out
│   ├── batch_ref_7_budget_50_2024857_12.err
│   ├── batch_ref_7_budget_50_2024857_12.out
│   ├── batch_ref_7_budget_50_2024857_13.err
│   ├── batch_ref_7_budget_50_2024857_13.out
│   ├── batch_ref_7_budget_50_2024857_14.err
│   ├── batch_ref_7_budget_50_2024857_14.out
│   ├── batch_ref_7_budget_50_2024857_15.err
│   ├── batch_ref_7_budget_50_2024857_15.out
│   ├── batch_ref_7_budget_50_2024857_16.err
│   ├── batch_ref_7_budget_50_2024857_16.out
│   ├── batch_ref_7_budget_50_2024857_17.err
│   ├── batch_ref_7_budget_50_2024857_17.out
│   ├── batch_ref_7_budget_50_2024857_18.err
│   ├── batch_ref_7_budget_50_2024857_18.out
│   ├── batch_ref_7_budget_50_2024857_19.err
│   ├── batch_ref_7_budget_50_2024857_19.out
│   ├── batch_ref_7_budget_50_2024857_2.err
│   ├── batch_ref_7_budget_50_2024857_2.out
│   ├── batch_ref_7_budget_50_2024857_20.err
│   ├── batch_ref_7_budget_50_2024857_20.out
│   ├── batch_ref_7_budget_50_2024857_21.err
│   ├── batch_ref_7_budget_50_2024857_21.out
│   ├── batch_ref_7_budget_50_2024857_22.err
│   ├── batch_ref_7_budget_50_2024857_22.out
│   ├── batch_ref_7_budget_50_2024857_23.err
│   ├── batch_ref_7_budget_50_2024857_23.out
│   ├── batch_ref_7_budget_50_2024857_24.err
│   ├── batch_ref_7_budget_50_2024857_24.out
│   ├── batch_ref_7_budget_50_2024857_25.err
│   ├── batch_ref_7_budget_50_2024857_25.out
│   ├── batch_ref_7_budget_50_2024857_26.err
│   ├── batch_ref_7_budget_50_2024857_26.out
│   ├── batch_ref_7_budget_50_2024857_27.err
│   ├── batch_ref_7_budget_50_2024857_27.out
│   ├── batch_ref_7_budget_50_2024857_28.err
│   ├── batch_ref_7_budget_50_2024857_28.out
│   ├── batch_ref_7_budget_50_2024857_29.err
│   ├── batch_ref_7_budget_50_2024857_29.out
│   ├── batch_ref_7_budget_50_2024857_3.err
│   ├── batch_ref_7_budget_50_2024857_3.out
│   ├── batch_ref_7_budget_50_2024857_30.err
│   ├── batch_ref_7_budget_50_2024857_30.out
│   ├── batch_ref_7_budget_50_2024857_31.err
│   ├── batch_ref_7_budget_50_2024857_31.out
│   ├── batch_ref_7_budget_50_2024857_32.err
│   ├── batch_ref_7_budget_50_2024857_32.out
│   ├── batch_ref_7_budget_50_2024857_33.err
│   ├── batch_ref_7_budget_50_2024857_33.out
│   ├── batch_ref_7_budget_50_2024857_34.err
│   ├── batch_ref_7_budget_50_2024857_34.out
│   ├── batch_ref_7_budget_50_2024857_35.err
│   ├── batch_ref_7_budget_50_2024857_35.out
│   ├── batch_ref_7_budget_50_2024857_36.err
│   ├── batch_ref_7_budget_50_2024857_36.out
│   ├── batch_ref_7_budget_50_2024857_37.err
│   ├── batch_ref_7_budget_50_2024857_37.out
│   ├── batch_ref_7_budget_50_2024857_38.err
│   ├── batch_ref_7_budget_50_2024857_38.out
│   ├── batch_ref_7_budget_50_2024857_39.err
│   ├── batch_ref_7_budget_50_2024857_39.out
│   ├── batch_ref_7_budget_50_2024857_4.err
│   ├── batch_ref_7_budget_50_2024857_4.out
│   ├── batch_ref_7_budget_50_2024857_40.err
│   ├── batch_ref_7_budget_50_2024857_40.out
│   ├── batch_ref_7_budget_50_2024857_41.err
│   ├── batch_ref_7_budget_50_2024857_41.out
│   ├── batch_ref_7_budget_50_2024857_42.err
│   ├── batch_ref_7_budget_50_2024857_42.out
│   ├── batch_ref_7_budget_50_2024857_43.err
│   ├── batch_ref_7_budget_50_2024857_43.out
│   ├── batch_ref_7_budget_50_2024857_44.err
│   ├── batch_ref_7_budget_50_2024857_44.out
│   ├── batch_ref_7_budget_50_2024857_45.err
│   ├── batch_ref_7_budget_50_2024857_45.out
│   ├── batch_ref_7_budget_50_2024857_46.err
│   ├── batch_ref_7_budget_50_2024857_46.out
│   ├── batch_ref_7_budget_50_2024857_47.err
│   ├── batch_ref_7_budget_50_2024857_47.out
│   ├── batch_ref_7_budget_50_2024857_48.err
│   ├── batch_ref_7_budget_50_2024857_48.out
│   ├── batch_ref_7_budget_50_2024857_49.err
│   ├── batch_ref_7_budget_50_2024857_49.out
│   ├── batch_ref_7_budget_50_2024857_5.err
│   ├── batch_ref_7_budget_50_2024857_5.out
│   ├── batch_ref_7_budget_50_2024857_50.err
│   ├── batch_ref_7_budget_50_2024857_50.out
│   ├── batch_ref_7_budget_50_2024857_51.err
│   ├── batch_ref_7_budget_50_2024857_51.out
│   ├── batch_ref_7_budget_50_2024857_52.err
│   ├── batch_ref_7_budget_50_2024857_52.out
│   ├── batch_ref_7_budget_50_2024857_53.err
│   ├── batch_ref_7_budget_50_2024857_53.out
│   ├── batch_ref_7_budget_50_2024857_54.err
│   ├── batch_ref_7_budget_50_2024857_54.out
│   ├── batch_ref_7_budget_50_2024857_55.err
│   ├── batch_ref_7_budget_50_2024857_55.out
│   ├── batch_ref_7_budget_50_2024857_56.err
│   ├── batch_ref_7_budget_50_2024857_56.out
│   ├── batch_ref_7_budget_50_2024857_57.err
│   ├── batch_ref_7_budget_50_2024857_57.out
│   ├── batch_ref_7_budget_50_2024857_58.err
│   ├── batch_ref_7_budget_50_2024857_58.out
│   ├── batch_ref_7_budget_50_2024857_59.err
│   ├── batch_ref_7_budget_50_2024857_59.out
│   ├── batch_ref_7_budget_50_2024857_6.err
│   ├── batch_ref_7_budget_50_2024857_6.out
│   ├── batch_ref_7_budget_50_2024857_60.err
│   ├── batch_ref_7_budget_50_2024857_60.out
│   ├── batch_ref_7_budget_50_2024857_61.err
│   ├── batch_ref_7_budget_50_2024857_61.out
│   ├── batch_ref_7_budget_50_2024857_62.err
│   ├── batch_ref_7_budget_50_2024857_62.out
│   ├── batch_ref_7_budget_50_2024857_63.err
│   ├── batch_ref_7_budget_50_2024857_63.out
│   ├── batch_ref_7_budget_50_2024857_64.err
│   ├── batch_ref_7_budget_50_2024857_64.out
│   ├── batch_ref_7_budget_50_2024857_65.err
│   ├── batch_ref_7_budget_50_2024857_65.out
│   ├── batch_ref_7_budget_50_2024857_66.err
│   ├── batch_ref_7_budget_50_2024857_66.out
│   ├── batch_ref_7_budget_50_2024857_67.err
│   ├── batch_ref_7_budget_50_2024857_67.out
│   ├── batch_ref_7_budget_50_2024857_68.err
│   ├── batch_ref_7_budget_50_2024857_68.out
│   ├── batch_ref_7_budget_50_2024857_69.err
│   ├── batch_ref_7_budget_50_2024857_69.out
│   ├── batch_ref_7_budget_50_2024857_7.err
│   ├── batch_ref_7_budget_50_2024857_7.out
│   ├── batch_ref_7_budget_50_2024857_70.err
│   ├── batch_ref_7_budget_50_2024857_70.out
│   ├── batch_ref_7_budget_50_2024857_71.err
│   ├── batch_ref_7_budget_50_2024857_71.out
│   ├── batch_ref_7_budget_50_2024857_72.err
│   ├── batch_ref_7_budget_50_2024857_72.out
│   ├── batch_ref_7_budget_50_2024857_73.err
│   ├── batch_ref_7_budget_50_2024857_73.out
│   ├── batch_ref_7_budget_50_2024857_74.err
│   ├── batch_ref_7_budget_50_2024857_74.out
│   ├── batch_ref_7_budget_50_2024857_75.err
│   ├── batch_ref_7_budget_50_2024857_75.out
│   ├── batch_ref_7_budget_50_2024857_76.err
│   ├── batch_ref_7_budget_50_2024857_76.out
│   ├── batch_ref_7_budget_50_2024857_77.err
│   ├── batch_ref_7_budget_50_2024857_77.out
│   ├── batch_ref_7_budget_50_2024857_78.err
│   ├── batch_ref_7_budget_50_2024857_78.out
│   ├── batch_ref_7_budget_50_2024857_79.err
│   ├── batch_ref_7_budget_50_2024857_79.out
│   ├── batch_ref_7_budget_50_2024857_8.err
│   ├── batch_ref_7_budget_50_2024857_8.out
│   ├── batch_ref_7_budget_50_2024857_80.err
│   ├── batch_ref_7_budget_50_2024857_80.out
│   ├── batch_ref_7_budget_50_2024857_81.err
│   ├── batch_ref_7_budget_50_2024857_81.out
│   ├── batch_ref_7_budget_50_2024857_9.err
│   ├── batch_ref_7_budget_50_2024857_9.out
│   ├── batch_ref_7_budget_50_2040207_1.err
│   ├── batch_ref_7_budget_50_2040207_1.out
│   ├── batch_ref_7_budget_50_2040207_10.err
│   ├── batch_ref_7_budget_50_2040207_10.out
│   ├── batch_ref_7_budget_50_2040207_11.err
│   ├── batch_ref_7_budget_50_2040207_11.out
│   ├── batch_ref_7_budget_50_2040207_12.err
│   ├── batch_ref_7_budget_50_2040207_12.out
│   ├── batch_ref_7_budget_50_2040207_13.err
│   ├── batch_ref_7_budget_50_2040207_13.out
│   ├── batch_ref_7_budget_50_2040207_14.err
│   ├── batch_ref_7_budget_50_2040207_14.out
│   ├── batch_ref_7_budget_50_2040207_15.err
│   ├── batch_ref_7_budget_50_2040207_15.out
│   ├── batch_ref_7_budget_50_2040207_16.err
│   ├── batch_ref_7_budget_50_2040207_16.out
│   ├── batch_ref_7_budget_50_2040207_17.err
│   ├── batch_ref_7_budget_50_2040207_17.out
│   ├── batch_ref_7_budget_50_2040207_18.err
│   ├── batch_ref_7_budget_50_2040207_18.out
│   ├── batch_ref_7_budget_50_2040207_19.err
│   ├── batch_ref_7_budget_50_2040207_19.out
│   ├── batch_ref_7_budget_50_2040207_2.err
│   ├── batch_ref_7_budget_50_2040207_2.out
│   ├── batch_ref_7_budget_50_2040207_20.err
│   ├── batch_ref_7_budget_50_2040207_20.out
│   ├── batch_ref_7_budget_50_2040207_21.err
│   ├── batch_ref_7_budget_50_2040207_21.out
│   ├── batch_ref_7_budget_50_2040207_22.err
│   ├── batch_ref_7_budget_50_2040207_22.out
│   ├── batch_ref_7_budget_50_2040207_23.err
│   ├── batch_ref_7_budget_50_2040207_23.out
│   ├── batch_ref_7_budget_50_2040207_24.err
│   ├── batch_ref_7_budget_50_2040207_24.out
│   ├── batch_ref_7_budget_50_2040207_25.err
│   ├── batch_ref_7_budget_50_2040207_25.out
│   ├── batch_ref_7_budget_50_2040207_26.err
│   ├── batch_ref_7_budget_50_2040207_26.out
│   ├── batch_ref_7_budget_50_2040207_27.err
│   ├── batch_ref_7_budget_50_2040207_27.out
│   ├── batch_ref_7_budget_50_2040207_28.err
│   ├── batch_ref_7_budget_50_2040207_28.out
│   ├── batch_ref_7_budget_50_2040207_29.err
│   ├── batch_ref_7_budget_50_2040207_29.out
│   ├── batch_ref_7_budget_50_2040207_3.err
│   ├── batch_ref_7_budget_50_2040207_3.out
│   ├── batch_ref_7_budget_50_2040207_30.err
│   ├── batch_ref_7_budget_50_2040207_30.out
│   ├── batch_ref_7_budget_50_2040207_31.err
│   ├── batch_ref_7_budget_50_2040207_31.out
│   ├── batch_ref_7_budget_50_2040207_32.err
│   ├── batch_ref_7_budget_50_2040207_32.out
│   ├── batch_ref_7_budget_50_2040207_33.err
│   ├── batch_ref_7_budget_50_2040207_33.out
│   ├── batch_ref_7_budget_50_2040207_34.err
│   ├── batch_ref_7_budget_50_2040207_34.out
│   ├── batch_ref_7_budget_50_2040207_35.err
│   ├── batch_ref_7_budget_50_2040207_35.out
│   ├── batch_ref_7_budget_50_2040207_36.err
│   ├── batch_ref_7_budget_50_2040207_36.out
│   ├── batch_ref_7_budget_50_2040207_37.err
│   ├── batch_ref_7_budget_50_2040207_37.out
│   ├── batch_ref_7_budget_50_2040207_38.err
│   ├── batch_ref_7_budget_50_2040207_38.out
│   ├── batch_ref_7_budget_50_2040207_39.err
│   ├── batch_ref_7_budget_50_2040207_39.out
│   ├── batch_ref_7_budget_50_2040207_4.err
│   ├── batch_ref_7_budget_50_2040207_4.out
│   ├── batch_ref_7_budget_50_2040207_40.err
│   ├── batch_ref_7_budget_50_2040207_40.out
│   ├── batch_ref_7_budget_50_2040207_41.err
│   ├── batch_ref_7_budget_50_2040207_41.out
│   ├── batch_ref_7_budget_50_2040207_42.err
│   ├── batch_ref_7_budget_50_2040207_42.out
│   ├── batch_ref_7_budget_50_2040207_43.err
│   ├── batch_ref_7_budget_50_2040207_43.out
│   ├── batch_ref_7_budget_50_2040207_44.err
│   ├── batch_ref_7_budget_50_2040207_44.out
│   ├── batch_ref_7_budget_50_2040207_45.err
│   ├── batch_ref_7_budget_50_2040207_45.out
│   ├── batch_ref_7_budget_50_2040207_46.err
│   ├── batch_ref_7_budget_50_2040207_46.out
│   ├── batch_ref_7_budget_50_2040207_47.err
│   ├── batch_ref_7_budget_50_2040207_47.out
│   ├── batch_ref_7_budget_50_2040207_48.err
│   ├── batch_ref_7_budget_50_2040207_48.out
│   ├── batch_ref_7_budget_50_2040207_49.err
│   ├── batch_ref_7_budget_50_2040207_49.out
│   ├── batch_ref_7_budget_50_2040207_5.err
│   ├── batch_ref_7_budget_50_2040207_5.out
│   ├── batch_ref_7_budget_50_2040207_50.err
│   ├── batch_ref_7_budget_50_2040207_50.out
│   ├── batch_ref_7_budget_50_2040207_51.err
│   ├── batch_ref_7_budget_50_2040207_51.out
│   ├── batch_ref_7_budget_50_2040207_52.err
│   ├── batch_ref_7_budget_50_2040207_52.out
│   ├── batch_ref_7_budget_50_2040207_53.err
│   ├── batch_ref_7_budget_50_2040207_53.out
│   ├── batch_ref_7_budget_50_2040207_54.err
│   ├── batch_ref_7_budget_50_2040207_54.out
│   ├── batch_ref_7_budget_50_2040207_55.err
│   ├── batch_ref_7_budget_50_2040207_55.out
│   ├── batch_ref_7_budget_50_2040207_56.err
│   ├── batch_ref_7_budget_50_2040207_56.out
│   ├── batch_ref_7_budget_50_2040207_57.err
│   ├── batch_ref_7_budget_50_2040207_57.out
│   ├── batch_ref_7_budget_50_2040207_58.err
│   ├── batch_ref_7_budget_50_2040207_58.out
│   ├── batch_ref_7_budget_50_2040207_59.err
│   ├── batch_ref_7_budget_50_2040207_59.out
│   ├── batch_ref_7_budget_50_2040207_6.err
│   ├── batch_ref_7_budget_50_2040207_6.out
│   ├── batch_ref_7_budget_50_2040207_60.err
│   ├── batch_ref_7_budget_50_2040207_60.out
│   ├── batch_ref_7_budget_50_2040207_61.err
│   ├── batch_ref_7_budget_50_2040207_61.out
│   ├── batch_ref_7_budget_50_2040207_62.err
│   ├── batch_ref_7_budget_50_2040207_62.out
│   ├── batch_ref_7_budget_50_2040207_63.err
│   ├── batch_ref_7_budget_50_2040207_63.out
│   ├── batch_ref_7_budget_50_2040207_64.err
│   ├── batch_ref_7_budget_50_2040207_64.out
│   ├── batch_ref_7_budget_50_2040207_65.err
│   ├── batch_ref_7_budget_50_2040207_65.out
│   ├── batch_ref_7_budget_50_2040207_66.err
│   ├── batch_ref_7_budget_50_2040207_66.out
│   ├── batch_ref_7_budget_50_2040207_67.err
│   ├── batch_ref_7_budget_50_2040207_67.out
│   ├── batch_ref_7_budget_50_2040207_68.err
│   ├── batch_ref_7_budget_50_2040207_68.out
│   ├── batch_ref_7_budget_50_2040207_69.err
│   ├── batch_ref_7_budget_50_2040207_69.out
│   ├── batch_ref_7_budget_50_2040207_7.err
│   ├── batch_ref_7_budget_50_2040207_7.out
│   ├── batch_ref_7_budget_50_2040207_70.err
│   ├── batch_ref_7_budget_50_2040207_70.out
│   ├── batch_ref_7_budget_50_2040207_71.err
│   ├── batch_ref_7_budget_50_2040207_71.out
│   ├── batch_ref_7_budget_50_2040207_72.err
│   ├── batch_ref_7_budget_50_2040207_72.out
│   ├── batch_ref_7_budget_50_2040207_73.err
│   ├── batch_ref_7_budget_50_2040207_73.out
│   ├── batch_ref_7_budget_50_2040207_74.err
│   ├── batch_ref_7_budget_50_2040207_74.out
│   ├── batch_ref_7_budget_50_2040207_75.err
│   ├── batch_ref_7_budget_50_2040207_75.out
│   ├── batch_ref_7_budget_50_2040207_76.err
│   ├── batch_ref_7_budget_50_2040207_76.out
│   ├── batch_ref_7_budget_50_2040207_77.err
│   ├── batch_ref_7_budget_50_2040207_77.out
│   ├── batch_ref_7_budget_50_2040207_78.err
│   ├── batch_ref_7_budget_50_2040207_78.out
│   ├── batch_ref_7_budget_50_2040207_79.err
│   ├── batch_ref_7_budget_50_2040207_79.out
│   ├── batch_ref_7_budget_50_2040207_8.err
│   ├── batch_ref_7_budget_50_2040207_8.out
│   ├── batch_ref_7_budget_50_2040207_80.err
│   ├── batch_ref_7_budget_50_2040207_80.out
│   ├── batch_ref_7_budget_50_2040207_81.err
│   ├── batch_ref_7_budget_50_2040207_81.out
│   ├── batch_ref_7_budget_50_2040207_9.err
│   ├── batch_ref_7_budget_50_2040207_9.out
│   ├── batch_ref_7_budget_600_2019753_1.err
│   ├── batch_ref_7_budget_600_2019753_1.out
│   ├── batch_ref_7_budget_600_2019753_10.err
│   ├── batch_ref_7_budget_600_2019753_10.out
│   ├── batch_ref_7_budget_600_2019753_11.err
│   ├── batch_ref_7_budget_600_2019753_11.out
│   ├── batch_ref_7_budget_600_2019753_12.err
│   ├── batch_ref_7_budget_600_2019753_12.out
│   ├── batch_ref_7_budget_600_2019753_13.err
│   ├── batch_ref_7_budget_600_2019753_13.out
│   ├── batch_ref_7_budget_600_2019753_14.err
│   ├── batch_ref_7_budget_600_2019753_14.out
│   ├── batch_ref_7_budget_600_2019753_15.err
│   ├── batch_ref_7_budget_600_2019753_15.out
│   ├── batch_ref_7_budget_600_2019753_16.err
│   ├── batch_ref_7_budget_600_2019753_16.out
│   ├── batch_ref_7_budget_600_2019753_17.err
│   ├── batch_ref_7_budget_600_2019753_17.out
│   ├── batch_ref_7_budget_600_2019753_18.err
│   ├── batch_ref_7_budget_600_2019753_18.out
│   ├── batch_ref_7_budget_600_2019753_19.err
│   ├── batch_ref_7_budget_600_2019753_19.out
│   ├── batch_ref_7_budget_600_2019753_2.err
│   ├── batch_ref_7_budget_600_2019753_2.out
│   ├── batch_ref_7_budget_600_2019753_20.err
│   ├── batch_ref_7_budget_600_2019753_20.out
│   ├── batch_ref_7_budget_600_2019753_21.err
│   ├── batch_ref_7_budget_600_2019753_21.out
│   ├── batch_ref_7_budget_600_2019753_22.err
│   ├── batch_ref_7_budget_600_2019753_22.out
│   ├── batch_ref_7_budget_600_2019753_23.err
│   ├── batch_ref_7_budget_600_2019753_23.out
│   ├── batch_ref_7_budget_600_2019753_24.err
│   ├── batch_ref_7_budget_600_2019753_24.out
│   ├── batch_ref_7_budget_600_2019753_25.err
│   ├── batch_ref_7_budget_600_2019753_25.out
│   ├── batch_ref_7_budget_600_2019753_26.err
│   ├── batch_ref_7_budget_600_2019753_26.out
│   ├── batch_ref_7_budget_600_2019753_27.err
│   ├── batch_ref_7_budget_600_2019753_27.out
│   ├── batch_ref_7_budget_600_2019753_28.err
│   ├── batch_ref_7_budget_600_2019753_28.out
│   ├── batch_ref_7_budget_600_2019753_29.err
│   ├── batch_ref_7_budget_600_2019753_29.out
│   ├── batch_ref_7_budget_600_2019753_3.err
│   ├── batch_ref_7_budget_600_2019753_3.out
│   ├── batch_ref_7_budget_600_2019753_30.err
│   ├── batch_ref_7_budget_600_2019753_30.out
│   ├── batch_ref_7_budget_600_2019753_31.err
│   ├── batch_ref_7_budget_600_2019753_31.out
│   ├── batch_ref_7_budget_600_2019753_32.err
│   ├── batch_ref_7_budget_600_2019753_32.out
│   ├── batch_ref_7_budget_600_2019753_33.err
│   ├── batch_ref_7_budget_600_2019753_33.out
│   ├── batch_ref_7_budget_600_2019753_34.err
│   ├── batch_ref_7_budget_600_2019753_34.out
│   ├── batch_ref_7_budget_600_2019753_35.err
│   ├── batch_ref_7_budget_600_2019753_35.out
│   ├── batch_ref_7_budget_600_2019753_36.err
│   ├── batch_ref_7_budget_600_2019753_36.out
│   ├── batch_ref_7_budget_600_2019753_37.err
│   ├── batch_ref_7_budget_600_2019753_37.out
│   ├── batch_ref_7_budget_600_2019753_38.err
│   ├── batch_ref_7_budget_600_2019753_38.out
│   ├── batch_ref_7_budget_600_2019753_39.err
│   ├── batch_ref_7_budget_600_2019753_39.out
│   ├── batch_ref_7_budget_600_2019753_4.err
│   ├── batch_ref_7_budget_600_2019753_4.out
│   ├── batch_ref_7_budget_600_2019753_40.err
│   ├── batch_ref_7_budget_600_2019753_40.out
│   ├── batch_ref_7_budget_600_2019753_41.err
│   ├── batch_ref_7_budget_600_2019753_41.out
│   ├── batch_ref_7_budget_600_2019753_42.err
│   ├── batch_ref_7_budget_600_2019753_42.out
│   ├── batch_ref_7_budget_600_2019753_43.err
│   ├── batch_ref_7_budget_600_2019753_43.out
│   ├── batch_ref_7_budget_600_2019753_44.err
│   ├── batch_ref_7_budget_600_2019753_44.out
│   ├── batch_ref_7_budget_600_2019753_45.err
│   ├── batch_ref_7_budget_600_2019753_45.out
│   ├── batch_ref_7_budget_600_2019753_46.err
│   ├── batch_ref_7_budget_600_2019753_46.out
│   ├── batch_ref_7_budget_600_2019753_47.err
│   ├── batch_ref_7_budget_600_2019753_47.out
│   ├── batch_ref_7_budget_600_2019753_48.err
│   ├── batch_ref_7_budget_600_2019753_48.out
│   ├── batch_ref_7_budget_600_2019753_49.err
│   ├── batch_ref_7_budget_600_2019753_49.out
│   ├── batch_ref_7_budget_600_2019753_5.err
│   ├── batch_ref_7_budget_600_2019753_5.out
│   ├── batch_ref_7_budget_600_2019753_50.err
│   ├── batch_ref_7_budget_600_2019753_50.out
│   ├── batch_ref_7_budget_600_2019753_51.err
│   ├── batch_ref_7_budget_600_2019753_51.out
│   ├── batch_ref_7_budget_600_2019753_52.err
│   ├── batch_ref_7_budget_600_2019753_52.out
│   ├── batch_ref_7_budget_600_2019753_53.err
│   ├── batch_ref_7_budget_600_2019753_53.out
│   ├── batch_ref_7_budget_600_2019753_54.err
│   ├── batch_ref_7_budget_600_2019753_54.out
│   ├── batch_ref_7_budget_600_2019753_55.err
│   ├── batch_ref_7_budget_600_2019753_55.out
│   ├── batch_ref_7_budget_600_2019753_56.err
│   ├── batch_ref_7_budget_600_2019753_56.out
│   ├── batch_ref_7_budget_600_2019753_57.err
│   ├── batch_ref_7_budget_600_2019753_57.out
│   ├── batch_ref_7_budget_600_2019753_58.err
│   ├── batch_ref_7_budget_600_2019753_58.out
│   ├── batch_ref_7_budget_600_2019753_59.err
│   ├── batch_ref_7_budget_600_2019753_59.out
│   ├── batch_ref_7_budget_600_2019753_6.err
│   ├── batch_ref_7_budget_600_2019753_6.out
│   ├── batch_ref_7_budget_600_2019753_60.err
│   ├── batch_ref_7_budget_600_2019753_60.out
│   ├── batch_ref_7_budget_600_2019753_61.err
│   ├── batch_ref_7_budget_600_2019753_61.out
│   ├── batch_ref_7_budget_600_2019753_62.err
│   ├── batch_ref_7_budget_600_2019753_62.out
│   ├── batch_ref_7_budget_600_2019753_63.err
│   ├── batch_ref_7_budget_600_2019753_63.out
│   ├── batch_ref_7_budget_600_2019753_64.err
│   ├── batch_ref_7_budget_600_2019753_64.out
│   ├── batch_ref_7_budget_600_2019753_65.err
│   ├── batch_ref_7_budget_600_2019753_65.out
│   ├── batch_ref_7_budget_600_2019753_66.err
│   ├── batch_ref_7_budget_600_2019753_66.out
│   ├── batch_ref_7_budget_600_2019753_67.err
│   ├── batch_ref_7_budget_600_2019753_67.out
│   ├── batch_ref_7_budget_600_2019753_68.err
│   ├── batch_ref_7_budget_600_2019753_68.out
│   ├── batch_ref_7_budget_600_2019753_69.err
│   ├── batch_ref_7_budget_600_2019753_69.out
│   ├── batch_ref_7_budget_600_2019753_7.err
│   ├── batch_ref_7_budget_600_2019753_7.out
│   ├── batch_ref_7_budget_600_2019753_70.err
│   ├── batch_ref_7_budget_600_2019753_70.out
│   ├── batch_ref_7_budget_600_2019753_71.err
│   ├── batch_ref_7_budget_600_2019753_71.out
│   ├── batch_ref_7_budget_600_2019753_72.err
│   ├── batch_ref_7_budget_600_2019753_72.out
│   ├── batch_ref_7_budget_600_2019753_73.err
│   ├── batch_ref_7_budget_600_2019753_73.out
│   ├── batch_ref_7_budget_600_2019753_74.err
│   ├── batch_ref_7_budget_600_2019753_74.out
│   ├── batch_ref_7_budget_600_2019753_75.err
│   ├── batch_ref_7_budget_600_2019753_75.out
│   ├── batch_ref_7_budget_600_2019753_76.err
│   ├── batch_ref_7_budget_600_2019753_76.out
│   ├── batch_ref_7_budget_600_2019753_77.err
│   ├── batch_ref_7_budget_600_2019753_77.out
│   ├── batch_ref_7_budget_600_2019753_78.err
│   ├── batch_ref_7_budget_600_2019753_78.out
│   ├── batch_ref_7_budget_600_2019753_79.err
│   ├── batch_ref_7_budget_600_2019753_79.out
│   ├── batch_ref_7_budget_600_2019753_8.err
│   ├── batch_ref_7_budget_600_2019753_8.out
│   ├── batch_ref_7_budget_600_2019753_80.err
│   ├── batch_ref_7_budget_600_2019753_80.out
│   ├── batch_ref_7_budget_600_2019753_81.err
│   ├── batch_ref_7_budget_600_2019753_81.out
│   ├── batch_ref_7_budget_600_2019753_9.err
│   ├── batch_ref_7_budget_600_2019753_9.out
│   ├── batch_ref_7_budget_600_2040208_1.err
│   ├── batch_ref_7_budget_600_2040208_1.out
│   ├── batch_ref_7_budget_600_2040208_10.err
│   ├── batch_ref_7_budget_600_2040208_10.out
│   ├── batch_ref_7_budget_600_2040208_11.err
│   ├── batch_ref_7_budget_600_2040208_11.out
│   ├── batch_ref_7_budget_600_2040208_12.err
│   ├── batch_ref_7_budget_600_2040208_12.out
│   ├── batch_ref_7_budget_600_2040208_13.err
│   ├── batch_ref_7_budget_600_2040208_13.out
│   ├── batch_ref_7_budget_600_2040208_14.err
│   ├── batch_ref_7_budget_600_2040208_14.out
│   ├── batch_ref_7_budget_600_2040208_15.err
│   ├── batch_ref_7_budget_600_2040208_15.out
│   ├── batch_ref_7_budget_600_2040208_16.err
│   ├── batch_ref_7_budget_600_2040208_16.out
│   ├── batch_ref_7_budget_600_2040208_17.err
│   ├── batch_ref_7_budget_600_2040208_17.out
│   ├── batch_ref_7_budget_600_2040208_18.err
│   ├── batch_ref_7_budget_600_2040208_18.out
│   ├── batch_ref_7_budget_600_2040208_19.err
│   ├── batch_ref_7_budget_600_2040208_19.out
│   ├── batch_ref_7_budget_600_2040208_2.err
│   ├── batch_ref_7_budget_600_2040208_2.out
│   ├── batch_ref_7_budget_600_2040208_20.err
│   ├── batch_ref_7_budget_600_2040208_20.out
│   ├── batch_ref_7_budget_600_2040208_21.err
│   ├── batch_ref_7_budget_600_2040208_21.out
│   ├── batch_ref_7_budget_600_2040208_22.err
│   ├── batch_ref_7_budget_600_2040208_22.out
│   ├── batch_ref_7_budget_600_2040208_23.err
│   ├── batch_ref_7_budget_600_2040208_23.out
│   ├── batch_ref_7_budget_600_2040208_24.err
│   ├── batch_ref_7_budget_600_2040208_24.out
│   ├── batch_ref_7_budget_600_2040208_25.err
│   ├── batch_ref_7_budget_600_2040208_25.out
│   ├── batch_ref_7_budget_600_2040208_26.err
│   ├── batch_ref_7_budget_600_2040208_26.out
│   ├── batch_ref_7_budget_600_2040208_27.err
│   ├── batch_ref_7_budget_600_2040208_27.out
│   ├── batch_ref_7_budget_600_2040208_28.err
│   ├── batch_ref_7_budget_600_2040208_28.out
│   ├── batch_ref_7_budget_600_2040208_29.err
│   ├── batch_ref_7_budget_600_2040208_29.out
│   ├── batch_ref_7_budget_600_2040208_3.err
│   ├── batch_ref_7_budget_600_2040208_3.out
│   ├── batch_ref_7_budget_600_2040208_30.err
│   ├── batch_ref_7_budget_600_2040208_30.out
│   ├── batch_ref_7_budget_600_2040208_31.err
│   ├── batch_ref_7_budget_600_2040208_31.out
│   ├── batch_ref_7_budget_600_2040208_32.err
│   ├── batch_ref_7_budget_600_2040208_32.out
│   ├── batch_ref_7_budget_600_2040208_33.err
│   ├── batch_ref_7_budget_600_2040208_33.out
│   ├── batch_ref_7_budget_600_2040208_34.err
│   ├── batch_ref_7_budget_600_2040208_34.out
│   ├── batch_ref_7_budget_600_2040208_35.err
│   ├── batch_ref_7_budget_600_2040208_35.out
│   ├── batch_ref_7_budget_600_2040208_36.err
│   ├── batch_ref_7_budget_600_2040208_36.out
│   ├── batch_ref_7_budget_600_2040208_37.err
│   ├── batch_ref_7_budget_600_2040208_37.out
│   ├── batch_ref_7_budget_600_2040208_38.err
│   ├── batch_ref_7_budget_600_2040208_38.out
│   ├── batch_ref_7_budget_600_2040208_39.err
│   ├── batch_ref_7_budget_600_2040208_39.out
│   ├── batch_ref_7_budget_600_2040208_4.err
│   ├── batch_ref_7_budget_600_2040208_4.out
│   ├── batch_ref_7_budget_600_2040208_40.err
│   ├── batch_ref_7_budget_600_2040208_40.out
│   ├── batch_ref_7_budget_600_2040208_41.err
│   ├── batch_ref_7_budget_600_2040208_41.out
│   ├── batch_ref_7_budget_600_2040208_42.err
│   ├── batch_ref_7_budget_600_2040208_42.out
│   ├── batch_ref_7_budget_600_2040208_43.err
│   ├── batch_ref_7_budget_600_2040208_43.out
│   ├── batch_ref_7_budget_600_2040208_44.err
│   ├── batch_ref_7_budget_600_2040208_44.out
│   ├── batch_ref_7_budget_600_2040208_45.err
│   ├── batch_ref_7_budget_600_2040208_45.out
│   ├── batch_ref_7_budget_600_2040208_46.err
│   ├── batch_ref_7_budget_600_2040208_46.out
│   ├── batch_ref_7_budget_600_2040208_47.err
│   ├── batch_ref_7_budget_600_2040208_47.out
│   ├── batch_ref_7_budget_600_2040208_48.err
│   ├── batch_ref_7_budget_600_2040208_48.out
│   ├── batch_ref_7_budget_600_2040208_49.err
│   ├── batch_ref_7_budget_600_2040208_49.out
│   ├── batch_ref_7_budget_600_2040208_5.err
│   ├── batch_ref_7_budget_600_2040208_5.out
│   ├── batch_ref_7_budget_600_2040208_50.err
│   ├── batch_ref_7_budget_600_2040208_50.out
│   ├── batch_ref_7_budget_600_2040208_51.err
│   ├── batch_ref_7_budget_600_2040208_51.out
│   ├── batch_ref_7_budget_600_2040208_52.err
│   ├── batch_ref_7_budget_600_2040208_52.out
│   ├── batch_ref_7_budget_600_2040208_53.err
│   ├── batch_ref_7_budget_600_2040208_53.out
│   ├── batch_ref_7_budget_600_2040208_54.err
│   ├── batch_ref_7_budget_600_2040208_54.out
│   ├── batch_ref_7_budget_600_2040208_55.err
│   ├── batch_ref_7_budget_600_2040208_55.out
│   ├── batch_ref_7_budget_600_2040208_56.err
│   ├── batch_ref_7_budget_600_2040208_56.out
│   ├── batch_ref_7_budget_600_2040208_57.err
│   ├── batch_ref_7_budget_600_2040208_57.out
│   ├── batch_ref_7_budget_600_2040208_58.err
│   ├── batch_ref_7_budget_600_2040208_58.out
│   ├── batch_ref_7_budget_600_2040208_59.err
│   ├── batch_ref_7_budget_600_2040208_59.out
│   ├── batch_ref_7_budget_600_2040208_6.err
│   ├── batch_ref_7_budget_600_2040208_6.out
│   ├── batch_ref_7_budget_600_2040208_60.err
│   ├── batch_ref_7_budget_600_2040208_60.out
│   ├── batch_ref_7_budget_600_2040208_61.err
│   ├── batch_ref_7_budget_600_2040208_61.out
│   ├── batch_ref_7_budget_600_2040208_62.err
│   ├── batch_ref_7_budget_600_2040208_62.out
│   ├── batch_ref_7_budget_600_2040208_63.err
│   ├── batch_ref_7_budget_600_2040208_63.out
│   ├── batch_ref_7_budget_600_2040208_64.err
│   ├── batch_ref_7_budget_600_2040208_64.out
│   ├── batch_ref_7_budget_600_2040208_65.err
│   ├── batch_ref_7_budget_600_2040208_65.out
│   ├── batch_ref_7_budget_600_2040208_66.err
│   ├── batch_ref_7_budget_600_2040208_66.out
│   ├── batch_ref_7_budget_600_2040208_67.err
│   ├── batch_ref_7_budget_600_2040208_67.out
│   ├── batch_ref_7_budget_600_2040208_68.err
│   ├── batch_ref_7_budget_600_2040208_68.out
│   ├── batch_ref_7_budget_600_2040208_69.err
│   ├── batch_ref_7_budget_600_2040208_69.out
│   ├── batch_ref_7_budget_600_2040208_7.err
│   ├── batch_ref_7_budget_600_2040208_7.out
│   ├── batch_ref_7_budget_600_2040208_70.err
│   ├── batch_ref_7_budget_600_2040208_70.out
│   ├── batch_ref_7_budget_600_2040208_71.err
│   ├── batch_ref_7_budget_600_2040208_71.out
│   ├── batch_ref_7_budget_600_2040208_72.err
│   ├── batch_ref_7_budget_600_2040208_72.out
│   ├── batch_ref_7_budget_600_2040208_73.err
│   ├── batch_ref_7_budget_600_2040208_73.out
│   ├── batch_ref_7_budget_600_2040208_74.err
│   ├── batch_ref_7_budget_600_2040208_74.out
│   ├── batch_ref_7_budget_600_2040208_75.err
│   ├── batch_ref_7_budget_600_2040208_75.out
│   ├── batch_ref_7_budget_600_2040208_76.err
│   ├── batch_ref_7_budget_600_2040208_76.out
│   ├── batch_ref_7_budget_600_2040208_77.err
│   ├── batch_ref_7_budget_600_2040208_77.out
│   ├── batch_ref_7_budget_600_2040208_78.err
│   ├── batch_ref_7_budget_600_2040208_78.out
│   ├── batch_ref_7_budget_600_2040208_79.err
│   ├── batch_ref_7_budget_600_2040208_79.out
│   ├── batch_ref_7_budget_600_2040208_8.err
│   ├── batch_ref_7_budget_600_2040208_8.out
│   ├── batch_ref_7_budget_600_2040208_80.err
│   ├── batch_ref_7_budget_600_2040208_80.out
│   ├── batch_ref_7_budget_600_2040208_81.err
│   ├── batch_ref_7_budget_600_2040208_81.out
│   ├── batch_ref_7_budget_600_2040208_9.err
│   ├── batch_ref_7_budget_600_2040208_9.out
│   ├── batch_ref_7_budget_80_2038460_1.err
│   ├── batch_ref_7_budget_80_2038460_1.out
│   ├── batch_ref_7_budget_80_2038460_10.err
│   ├── batch_ref_7_budget_80_2038460_10.out
│   ├── batch_ref_7_budget_80_2038460_11.err
│   ├── batch_ref_7_budget_80_2038460_11.out
│   ├── batch_ref_7_budget_80_2038460_12.err
│   ├── batch_ref_7_budget_80_2038460_12.out
│   ├── batch_ref_7_budget_80_2038460_13.err
│   ├── batch_ref_7_budget_80_2038460_13.out
│   ├── batch_ref_7_budget_80_2038460_14.err
│   ├── batch_ref_7_budget_80_2038460_14.out
│   ├── batch_ref_7_budget_80_2038460_15.err
│   ├── batch_ref_7_budget_80_2038460_15.out
│   ├── batch_ref_7_budget_80_2038460_16.err
│   ├── batch_ref_7_budget_80_2038460_16.out
│   ├── batch_ref_7_budget_80_2038460_17.err
│   ├── batch_ref_7_budget_80_2038460_17.out
│   ├── batch_ref_7_budget_80_2038460_18.err
│   ├── batch_ref_7_budget_80_2038460_18.out
│   ├── batch_ref_7_budget_80_2038460_19.err
│   ├── batch_ref_7_budget_80_2038460_19.out
│   ├── batch_ref_7_budget_80_2038460_2.err
│   ├── batch_ref_7_budget_80_2038460_2.out
│   ├── batch_ref_7_budget_80_2038460_20.err
│   ├── batch_ref_7_budget_80_2038460_20.out
│   ├── batch_ref_7_budget_80_2038460_21.err
│   ├── batch_ref_7_budget_80_2038460_21.out
│   ├── batch_ref_7_budget_80_2038460_22.err
│   ├── batch_ref_7_budget_80_2038460_22.out
│   ├── batch_ref_7_budget_80_2038460_23.err
│   ├── batch_ref_7_budget_80_2038460_23.out
│   ├── batch_ref_7_budget_80_2038460_24.err
│   ├── batch_ref_7_budget_80_2038460_24.out
│   ├── batch_ref_7_budget_80_2038460_25.err
│   ├── batch_ref_7_budget_80_2038460_25.out
│   ├── batch_ref_7_budget_80_2038460_26.err
│   ├── batch_ref_7_budget_80_2038460_26.out
│   ├── batch_ref_7_budget_80_2038460_27.err
│   ├── batch_ref_7_budget_80_2038460_27.out
│   ├── batch_ref_7_budget_80_2038460_28.err
│   ├── batch_ref_7_budget_80_2038460_28.out
│   ├── batch_ref_7_budget_80_2038460_29.err
│   ├── batch_ref_7_budget_80_2038460_29.out
│   ├── batch_ref_7_budget_80_2038460_3.err
│   ├── batch_ref_7_budget_80_2038460_3.out
│   ├── batch_ref_7_budget_80_2038460_30.err
│   ├── batch_ref_7_budget_80_2038460_30.out
│   ├── batch_ref_7_budget_80_2038460_31.err
│   ├── batch_ref_7_budget_80_2038460_31.out
│   ├── batch_ref_7_budget_80_2038460_32.err
│   ├── batch_ref_7_budget_80_2038460_32.out
│   ├── batch_ref_7_budget_80_2038460_33.err
│   ├── batch_ref_7_budget_80_2038460_33.out
│   ├── batch_ref_7_budget_80_2038460_34.err
│   ├── batch_ref_7_budget_80_2038460_34.out
│   ├── batch_ref_7_budget_80_2038460_35.err
│   ├── batch_ref_7_budget_80_2038460_35.out
│   ├── batch_ref_7_budget_80_2038460_36.err
│   ├── batch_ref_7_budget_80_2038460_36.out
│   ├── batch_ref_7_budget_80_2038460_37.err
│   ├── batch_ref_7_budget_80_2038460_37.out
│   ├── batch_ref_7_budget_80_2038460_38.err
│   ├── batch_ref_7_budget_80_2038460_38.out
│   ├── batch_ref_7_budget_80_2038460_39.err
│   ├── batch_ref_7_budget_80_2038460_39.out
│   ├── batch_ref_7_budget_80_2038460_4.err
│   ├── batch_ref_7_budget_80_2038460_4.out
│   ├── batch_ref_7_budget_80_2038460_40.err
│   ├── batch_ref_7_budget_80_2038460_40.out
│   ├── batch_ref_7_budget_80_2038460_41.err
│   ├── batch_ref_7_budget_80_2038460_41.out
│   ├── batch_ref_7_budget_80_2038460_42.err
│   ├── batch_ref_7_budget_80_2038460_42.out
│   ├── batch_ref_7_budget_80_2038460_43.err
│   ├── batch_ref_7_budget_80_2038460_43.out
│   ├── batch_ref_7_budget_80_2038460_44.err
│   ├── batch_ref_7_budget_80_2038460_44.out
│   ├── batch_ref_7_budget_80_2038460_45.err
│   ├── batch_ref_7_budget_80_2038460_45.out
│   ├── batch_ref_7_budget_80_2038460_46.err
│   ├── batch_ref_7_budget_80_2038460_46.out
│   ├── batch_ref_7_budget_80_2038460_47.err
│   ├── batch_ref_7_budget_80_2038460_47.out
│   ├── batch_ref_7_budget_80_2038460_48.err
│   ├── batch_ref_7_budget_80_2038460_48.out
│   ├── batch_ref_7_budget_80_2038460_49.err
│   ├── batch_ref_7_budget_80_2038460_49.out
│   ├── batch_ref_7_budget_80_2038460_5.err
│   ├── batch_ref_7_budget_80_2038460_5.out
│   ├── batch_ref_7_budget_80_2038460_50.err
│   ├── batch_ref_7_budget_80_2038460_50.out
│   ├── batch_ref_7_budget_80_2038460_51.err
│   ├── batch_ref_7_budget_80_2038460_51.out
│   ├── batch_ref_7_budget_80_2038460_52.err
│   ├── batch_ref_7_budget_80_2038460_52.out
│   ├── batch_ref_7_budget_80_2038460_53.err
│   ├── batch_ref_7_budget_80_2038460_53.out
│   ├── batch_ref_7_budget_80_2038460_54.err
│   ├── batch_ref_7_budget_80_2038460_54.out
│   ├── batch_ref_7_budget_80_2038460_55.err
│   ├── batch_ref_7_budget_80_2038460_55.out
│   ├── batch_ref_7_budget_80_2038460_56.err
│   ├── batch_ref_7_budget_80_2038460_56.out
│   ├── batch_ref_7_budget_80_2038460_57.err
│   ├── batch_ref_7_budget_80_2038460_57.out
│   ├── batch_ref_7_budget_80_2038460_58.err
│   ├── batch_ref_7_budget_80_2038460_58.out
│   ├── batch_ref_7_budget_80_2038460_59.err
│   ├── batch_ref_7_budget_80_2038460_59.out
│   ├── batch_ref_7_budget_80_2038460_6.err
│   ├── batch_ref_7_budget_80_2038460_6.out
│   ├── batch_ref_7_budget_80_2038460_60.err
│   ├── batch_ref_7_budget_80_2038460_60.out
│   ├── batch_ref_7_budget_80_2038460_61.err
│   ├── batch_ref_7_budget_80_2038460_61.out
│   ├── batch_ref_7_budget_80_2038460_62.err
│   ├── batch_ref_7_budget_80_2038460_62.out
│   ├── batch_ref_7_budget_80_2038460_63.err
│   ├── batch_ref_7_budget_80_2038460_63.out
│   ├── batch_ref_7_budget_80_2038460_64.err
│   ├── batch_ref_7_budget_80_2038460_64.out
│   ├── batch_ref_7_budget_80_2038460_65.err
│   ├── batch_ref_7_budget_80_2038460_65.out
│   ├── batch_ref_7_budget_80_2038460_66.err
│   ├── batch_ref_7_budget_80_2038460_66.out
│   ├── batch_ref_7_budget_80_2038460_67.err
│   ├── batch_ref_7_budget_80_2038460_67.out
│   ├── batch_ref_7_budget_80_2038460_68.err
│   ├── batch_ref_7_budget_80_2038460_68.out
│   ├── batch_ref_7_budget_80_2038460_69.err
│   ├── batch_ref_7_budget_80_2038460_69.out
│   ├── batch_ref_7_budget_80_2038460_7.err
│   ├── batch_ref_7_budget_80_2038460_7.out
│   ├── batch_ref_7_budget_80_2038460_70.err
│   ├── batch_ref_7_budget_80_2038460_70.out
│   ├── batch_ref_7_budget_80_2038460_71.err
│   ├── batch_ref_7_budget_80_2038460_71.out
│   ├── batch_ref_7_budget_80_2038460_72.err
│   ├── batch_ref_7_budget_80_2038460_72.out
│   ├── batch_ref_7_budget_80_2038460_73.err
│   ├── batch_ref_7_budget_80_2038460_73.out
│   ├── batch_ref_7_budget_80_2038460_74.err
│   ├── batch_ref_7_budget_80_2038460_74.out
│   ├── batch_ref_7_budget_80_2038460_75.err
│   ├── batch_ref_7_budget_80_2038460_75.out
│   ├── batch_ref_7_budget_80_2038460_76.err
│   ├── batch_ref_7_budget_80_2038460_76.out
│   ├── batch_ref_7_budget_80_2038460_77.err
│   ├── batch_ref_7_budget_80_2038460_77.out
│   ├── batch_ref_7_budget_80_2038460_78.err
│   ├── batch_ref_7_budget_80_2038460_78.out
│   ├── batch_ref_7_budget_80_2038460_79.err
│   ├── batch_ref_7_budget_80_2038460_79.out
│   ├── batch_ref_7_budget_80_2038460_8.err
│   ├── batch_ref_7_budget_80_2038460_8.out
│   ├── batch_ref_7_budget_80_2038460_80.err
│   ├── batch_ref_7_budget_80_2038460_80.out
│   ├── batch_ref_7_budget_80_2038460_81.err
│   ├── batch_ref_7_budget_80_2038460_81.out
│   ├── batch_ref_7_budget_80_2038460_9.err
│   ├── batch_ref_7_budget_80_2038460_9.out
│   ├── batch_ref_7_budget_80_2040209_1.err
│   ├── batch_ref_7_budget_80_2040209_1.out
│   ├── batch_ref_7_budget_80_2040209_10.err
│   ├── batch_ref_7_budget_80_2040209_10.out
│   ├── batch_ref_7_budget_80_2040209_11.err
│   ├── batch_ref_7_budget_80_2040209_11.out
│   ├── batch_ref_7_budget_80_2040209_12.err
│   ├── batch_ref_7_budget_80_2040209_12.out
│   ├── batch_ref_7_budget_80_2040209_13.err
│   ├── batch_ref_7_budget_80_2040209_13.out
│   ├── batch_ref_7_budget_80_2040209_14.err
│   ├── batch_ref_7_budget_80_2040209_14.out
│   ├── batch_ref_7_budget_80_2040209_15.err
│   ├── batch_ref_7_budget_80_2040209_15.out
│   ├── batch_ref_7_budget_80_2040209_16.err
│   ├── batch_ref_7_budget_80_2040209_16.out
│   ├── batch_ref_7_budget_80_2040209_17.err
│   ├── batch_ref_7_budget_80_2040209_17.out
│   ├── batch_ref_7_budget_80_2040209_18.err
│   ├── batch_ref_7_budget_80_2040209_18.out
│   ├── batch_ref_7_budget_80_2040209_19.err
│   ├── batch_ref_7_budget_80_2040209_19.out
│   ├── batch_ref_7_budget_80_2040209_2.err
│   ├── batch_ref_7_budget_80_2040209_2.out
│   ├── batch_ref_7_budget_80_2040209_20.err
│   ├── batch_ref_7_budget_80_2040209_20.out
│   ├── batch_ref_7_budget_80_2040209_21.err
│   ├── batch_ref_7_budget_80_2040209_21.out
│   ├── batch_ref_7_budget_80_2040209_22.err
│   ├── batch_ref_7_budget_80_2040209_22.out
│   ├── batch_ref_7_budget_80_2040209_23.err
│   ├── batch_ref_7_budget_80_2040209_23.out
│   ├── batch_ref_7_budget_80_2040209_24.err
│   ├── batch_ref_7_budget_80_2040209_24.out
│   ├── batch_ref_7_budget_80_2040209_25.err
│   ├── batch_ref_7_budget_80_2040209_25.out
│   ├── batch_ref_7_budget_80_2040209_26.err
│   ├── batch_ref_7_budget_80_2040209_26.out
│   ├── batch_ref_7_budget_80_2040209_27.err
│   ├── batch_ref_7_budget_80_2040209_27.out
│   ├── batch_ref_7_budget_80_2040209_28.err
│   ├── batch_ref_7_budget_80_2040209_28.out
│   ├── batch_ref_7_budget_80_2040209_29.err
│   ├── batch_ref_7_budget_80_2040209_29.out
│   ├── batch_ref_7_budget_80_2040209_3.err
│   ├── batch_ref_7_budget_80_2040209_3.out
│   ├── batch_ref_7_budget_80_2040209_30.err
│   ├── batch_ref_7_budget_80_2040209_30.out
│   ├── batch_ref_7_budget_80_2040209_31.err
│   ├── batch_ref_7_budget_80_2040209_31.out
│   ├── batch_ref_7_budget_80_2040209_32.err
│   ├── batch_ref_7_budget_80_2040209_32.out
│   ├── batch_ref_7_budget_80_2040209_33.err
│   ├── batch_ref_7_budget_80_2040209_33.out
│   ├── batch_ref_7_budget_80_2040209_34.err
│   ├── batch_ref_7_budget_80_2040209_34.out
│   ├── batch_ref_7_budget_80_2040209_35.err
│   ├── batch_ref_7_budget_80_2040209_35.out
│   ├── batch_ref_7_budget_80_2040209_36.err
│   ├── batch_ref_7_budget_80_2040209_36.out
│   ├── batch_ref_7_budget_80_2040209_37.err
│   ├── batch_ref_7_budget_80_2040209_37.out
│   ├── batch_ref_7_budget_80_2040209_38.err
│   ├── batch_ref_7_budget_80_2040209_38.out
│   ├── batch_ref_7_budget_80_2040209_39.err
│   ├── batch_ref_7_budget_80_2040209_39.out
│   ├── batch_ref_7_budget_80_2040209_4.err
│   ├── batch_ref_7_budget_80_2040209_4.out
│   ├── batch_ref_7_budget_80_2040209_40.err
│   ├── batch_ref_7_budget_80_2040209_40.out
│   ├── batch_ref_7_budget_80_2040209_41.err
│   ├── batch_ref_7_budget_80_2040209_41.out
│   ├── batch_ref_7_budget_80_2040209_42.err
│   ├── batch_ref_7_budget_80_2040209_42.out
│   ├── batch_ref_7_budget_80_2040209_43.err
│   ├── batch_ref_7_budget_80_2040209_43.out
│   ├── batch_ref_7_budget_80_2040209_44.err
│   ├── batch_ref_7_budget_80_2040209_44.out
│   ├── batch_ref_7_budget_80_2040209_45.err
│   ├── batch_ref_7_budget_80_2040209_45.out
│   ├── batch_ref_7_budget_80_2040209_46.err
│   ├── batch_ref_7_budget_80_2040209_46.out
│   ├── batch_ref_7_budget_80_2040209_47.err
│   ├── batch_ref_7_budget_80_2040209_47.out
│   ├── batch_ref_7_budget_80_2040209_48.err
│   ├── batch_ref_7_budget_80_2040209_48.out
│   ├── batch_ref_7_budget_80_2040209_49.err
│   ├── batch_ref_7_budget_80_2040209_49.out
│   ├── batch_ref_7_budget_80_2040209_5.err
│   ├── batch_ref_7_budget_80_2040209_5.out
│   ├── batch_ref_7_budget_80_2040209_50.err
│   ├── batch_ref_7_budget_80_2040209_50.out
│   ├── batch_ref_7_budget_80_2040209_51.err
│   ├── batch_ref_7_budget_80_2040209_51.out
│   ├── batch_ref_7_budget_80_2040209_52.err
│   ├── batch_ref_7_budget_80_2040209_52.out
│   ├── batch_ref_7_budget_80_2040209_53.err
│   ├── batch_ref_7_budget_80_2040209_53.out
│   ├── batch_ref_7_budget_80_2040209_54.err
│   ├── batch_ref_7_budget_80_2040209_54.out
│   ├── batch_ref_7_budget_80_2040209_55.err
│   ├── batch_ref_7_budget_80_2040209_55.out
│   ├── batch_ref_7_budget_80_2040209_56.err
│   ├── batch_ref_7_budget_80_2040209_56.out
│   ├── batch_ref_7_budget_80_2040209_57.err
│   ├── batch_ref_7_budget_80_2040209_57.out
│   ├── batch_ref_7_budget_80_2040209_58.err
│   ├── batch_ref_7_budget_80_2040209_58.out
│   ├── batch_ref_7_budget_80_2040209_59.err
│   ├── batch_ref_7_budget_80_2040209_59.out
│   ├── batch_ref_7_budget_80_2040209_6.err
│   ├── batch_ref_7_budget_80_2040209_6.out
│   ├── batch_ref_7_budget_80_2040209_60.err
│   ├── batch_ref_7_budget_80_2040209_60.out
│   ├── batch_ref_7_budget_80_2040209_61.err
│   ├── batch_ref_7_budget_80_2040209_61.out
│   ├── batch_ref_7_budget_80_2040209_62.err
│   ├── batch_ref_7_budget_80_2040209_62.out
│   ├── batch_ref_7_budget_80_2040209_63.err
│   ├── batch_ref_7_budget_80_2040209_63.out
│   ├── batch_ref_7_budget_80_2040209_64.err
│   ├── batch_ref_7_budget_80_2040209_64.out
│   ├── batch_ref_7_budget_80_2040209_65.err
│   ├── batch_ref_7_budget_80_2040209_65.out
│   ├── batch_ref_7_budget_80_2040209_66.err
│   ├── batch_ref_7_budget_80_2040209_66.out
│   ├── batch_ref_7_budget_80_2040209_67.err
│   ├── batch_ref_7_budget_80_2040209_67.out
│   ├── batch_ref_7_budget_80_2040209_68.err
│   ├── batch_ref_7_budget_80_2040209_68.out
│   ├── batch_ref_7_budget_80_2040209_69.err
│   ├── batch_ref_7_budget_80_2040209_69.out
│   ├── batch_ref_7_budget_80_2040209_7.err
│   ├── batch_ref_7_budget_80_2040209_7.out
│   ├── batch_ref_7_budget_80_2040209_70.err
│   ├── batch_ref_7_budget_80_2040209_70.out
│   ├── batch_ref_7_budget_80_2040209_71.err
│   ├── batch_ref_7_budget_80_2040209_71.out
│   ├── batch_ref_7_budget_80_2040209_72.err
│   ├── batch_ref_7_budget_80_2040209_72.out
│   ├── batch_ref_7_budget_80_2040209_73.err
│   ├── batch_ref_7_budget_80_2040209_73.out
│   ├── batch_ref_7_budget_80_2040209_74.err
│   ├── batch_ref_7_budget_80_2040209_74.out
│   ├── batch_ref_7_budget_80_2040209_75.err
│   ├── batch_ref_7_budget_80_2040209_75.out
│   ├── batch_ref_7_budget_80_2040209_76.err
│   ├── batch_ref_7_budget_80_2040209_76.out
│   ├── batch_ref_7_budget_80_2040209_77.err
│   ├── batch_ref_7_budget_80_2040209_77.out
│   ├── batch_ref_7_budget_80_2040209_78.err
│   ├── batch_ref_7_budget_80_2040209_78.out
│   ├── batch_ref_7_budget_80_2040209_79.err
│   ├── batch_ref_7_budget_80_2040209_79.out
│   ├── batch_ref_7_budget_80_2040209_8.err
│   ├── batch_ref_7_budget_80_2040209_8.out
│   ├── batch_ref_7_budget_80_2040209_80.err
│   ├── batch_ref_7_budget_80_2040209_80.out
│   ├── batch_ref_7_budget_80_2040209_81.err
│   ├── batch_ref_7_budget_80_2040209_81.out
│   ├── batch_ref_7_budget_80_2040209_9.err
│   ├── batch_ref_7_budget_80_2040209_9.out
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
│   ├── test_param_sweep_1888914_1.out
│   ├── test_param_sweep_1888918_0.err
│   ├── test_param_sweep_1888918_0.out
│   ├── test_param_sweep_1888918_1.err
│   ├── test_param_sweep_1888918_1.out
│   ├── test_param_sweep_1888920_0.err
│   ├── test_param_sweep_1888920_0.out
│   ├── test_param_sweep_1888920_1.err
│   └── test_param_sweep_1888920_1.out
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
│   │   ├── enhanced_callback_data.py
│   │   ├── enhanced_callback_mixed.py
│   │   ├── enhanced_callback_mixed_backup.py
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
├── results
│   ├── full_param_sweep_2025-05-29_105232
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── job_completed.yaml
│   │   │   ├── job_failed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   ├── performance.txt
│   │   │   └── training_report.pdf
│   │   └── gamma_50.0_step_0.1_rl_40_budget_40
│   │       ├── models
│   │       ├── tensorboard
│   │       ├── config.yaml
│   │       ├── device_info.txt
│   │       ├── evaluation.txt
│   │       ├── final_model.zip
│   │       ├── job_completed.yaml
│   │       ├── job_failed.yaml
│   │       ├── model_10000_steps.zip
│   │       ├── model_15000_steps.zip
│   │       ├── model_20000_steps.zip
│   │       ├── model_25000_steps.zip
│   │       ├── model_30000_steps.zip
│   │       ├── model_35000_steps.zip
│   │       ├── model_40000_steps.zip
│   │       ├── model_45000_steps.zip
│   │       ├── model_50000_steps.zip
│   │       ├── model_5000_steps.zip
│   │       ├── monitor.csv
│   │       ├── performance.txt
│   │       └── training_report.pdf
│   ├── full_param_sweep_data_20250601_105453
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_50k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_50k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_50k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_15000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_25000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_35000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_45000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_5000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   └── gamma_50.0_step_0.1_rl_40_budget_40
│   │       ├── models
│   │       ├── tensorboard
│   │       ├── config.yaml
│   │       ├── device_info.txt
│   │       ├── evaluation.txt
│   │       ├── final_model.zip
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_50k_training_metrics.json
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_50k_training_report.pdf
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_50k_training_summary.csv
│   │       ├── job_completed.yaml
│   │       ├── model_10000_steps.zip
│   │       ├── model_15000_steps.zip
│   │       ├── model_20000_steps.zip
│   │       ├── model_25000_steps.zip
│   │       ├── model_30000_steps.zip
│   │       ├── model_35000_steps.zip
│   │       ├── model_40000_steps.zip
│   │       ├── model_45000_steps.zip
│   │       ├── model_50000_steps.zip
│   │       ├── model_5000_steps.zip
│   │       ├── monitor.csv
│   │       └── performance.txt
│   ├── parameter_sweeps
│   │   └── step_domain_fraction
│   │       ├── run_2025-05-26_155744
│   │       ├── run_2025-05-26_155752
│   │       ├── run_2025-05-26_160141
│   │       ├── run_2025-05-26_184551
│   │       └── run_2025-05-27_085636
│   ├── session3_100k_uniform
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.025_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.05_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_100.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_100.0_step_0.1_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_25
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.025_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.05_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_25.0_step_0.1_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_25.0_step_0.1_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.025_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.025_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.05_rl_40_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.05_rl_40_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_10_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_10_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_25_budget_40
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_25_budget_40_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_25
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_25_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   ├── gamma_50.0_step_0.1_rl_40_budget_30
│   │   │   ├── models
│   │   │   ├── tensorboard
│   │   │   ├── config.yaml
│   │   │   ├── device_info.txt
│   │   │   ├── evaluation.txt
│   │   │   ├── final_model.zip
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_100k_training_metrics.json
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_100k_training_report.pdf
│   │   │   ├── gamma_50.0_step_0.1_rl_40_budget_30_100k_training_summary.csv
│   │   │   ├── job_completed.yaml
│   │   │   ├── model_100000_steps.zip
│   │   │   ├── model_10000_steps.zip
│   │   │   ├── model_20000_steps.zip
│   │   │   ├── model_30000_steps.zip
│   │   │   ├── model_40000_steps.zip
│   │   │   ├── model_50000_steps.zip
│   │   │   ├── model_60000_steps.zip
│   │   │   ├── model_70000_steps.zip
│   │   │   ├── model_80000_steps.zip
│   │   │   ├── model_90000_steps.zip
│   │   │   ├── monitor.csv
│   │   │   └── performance.txt
│   │   └── gamma_50.0_step_0.1_rl_40_budget_40
│   │       ├── models
│   │       ├── tensorboard
│   │       ├── config.yaml
│   │       ├── device_info.txt
│   │       ├── evaluation.txt
│   │       ├── final_model.zip
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_100k_training_metrics.json
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_100k_training_report.pdf
│   │       ├── gamma_50.0_step_0.1_rl_40_budget_40_100k_training_summary.csv
│   │       ├── job_completed.yaml
│   │       ├── model_100000_steps.zip
│   │       ├── model_10000_steps.zip
│   │       ├── model_20000_steps.zip
│   │       ├── model_30000_steps.zip
│   │       ├── model_40000_steps.zip
│   │       ├── model_50000_steps.zip
│   │       ├── model_60000_steps.zip
│   │       ├── model_70000_steps.zip
│   │       ├── model_80000_steps.zip
│   │       ├── model_90000_steps.zip
│   │       ├── monitor.csv
│   │       └── performance.txt
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
│       │   ├── evaluation.txt
│       │   ├── final_model.zip
│       │   ├── model_1000_steps.zip
│       │   ├── model_1200_steps.zip
│       │   ├── model_1400_steps.zip
│       │   ├── model_1600_steps.zip
│       │   ├── model_1800_steps.zip
│       │   ├── model_2000_steps.zip
│       │   ├── model_200_steps.zip
│       │   ├── model_400_steps.zip
│       │   ├── model_600_steps.zip
│       │   ├── model_800_steps.zip
│       │   ├── monitor.csv
│       │   ├── performance.txt
│       │   ├── test_completed.yaml
│       │   └── training_report.pdf
│       └── gamma_50.0_step_0.1_rl_25_budget_30
│           ├── models
│           ├── tensorboard
│           ├── config.yaml
│           ├── device_info.txt
│           ├── evaluation.txt
│           ├── final_model.zip
│           ├── model_1000_steps.zip
│           ├── model_1200_steps.zip
│           ├── model_1400_steps.zip
│           ├── model_1600_steps.zip
│           ├── model_1800_steps.zip
│           ├── model_2000_steps.zip
│           ├── model_200_steps.zip
│           ├── model_400_steps.zip
│           ├── model_600_steps.zip
│           ├── model_800_steps.zip
│           ├── monitor.csv
│           ├── performance.txt
│           ├── test_completed.yaml
│           └── training_report.pdf
├── scripts
│   ├── 1D_wave_amr.py
│   └── forest_example.py
├── slurm_scripts
│   ├── logs
│   │   ├── slurm-baseline-ref_3_budget_100-2044283.err
│   │   ├── slurm-baseline-ref_3_budget_100-2044283.out
│   │   ├── slurm-baseline-ref_3_budget_100-2044308.err
│   │   ├── slurm-baseline-ref_3_budget_100-2044308.out
│   │   ├── slurm-baseline-ref_3_budget_100-2044335.err
│   │   ├── slurm-baseline-ref_3_budget_100-2044335.out
│   │   ├── slurm-baseline-ref_3_budget_100-2044363.err
│   │   ├── slurm-baseline-ref_3_budget_100-2044363.out
│   │   ├── slurm-baseline-ref_3_budget_150-2044284.err
│   │   ├── slurm-baseline-ref_3_budget_150-2044284.out
│   │   ├── slurm-baseline-ref_3_budget_150-2044309.err
│   │   ├── slurm-baseline-ref_3_budget_150-2044309.out
│   │   ├── slurm-baseline-ref_3_budget_150-2044336.err
│   │   ├── slurm-baseline-ref_3_budget_150-2044336.out
│   │   ├── slurm-baseline-ref_3_budget_150-2044364.err
│   │   ├── slurm-baseline-ref_3_budget_150-2044364.out
│   │   ├── slurm-baseline-ref_3_budget_200-2044285.err
│   │   ├── slurm-baseline-ref_3_budget_200-2044285.out
│   │   ├── slurm-baseline-ref_3_budget_200-2044310.err
│   │   ├── slurm-baseline-ref_3_budget_200-2044310.out
│   │   ├── slurm-baseline-ref_3_budget_200-2044337.err
│   │   ├── slurm-baseline-ref_3_budget_200-2044337.out
│   │   ├── slurm-baseline-ref_3_budget_200-2044365.err
│   │   ├── slurm-baseline-ref_3_budget_200-2044365.out
│   │   ├── slurm-baseline-ref_3_budget_50-2044286.err
│   │   ├── slurm-baseline-ref_3_budget_50-2044286.out
│   │   ├── slurm-baseline-ref_3_budget_50-2044311.err
│   │   ├── slurm-baseline-ref_3_budget_50-2044311.out
│   │   ├── slurm-baseline-ref_3_budget_50-2044338.err
│   │   ├── slurm-baseline-ref_3_budget_50-2044338.out
│   │   ├── slurm-baseline-ref_3_budget_50-2044366.err
│   │   ├── slurm-baseline-ref_3_budget_50-2044366.out
│   │   ├── slurm-baseline-ref_3_budget_80-2044287.err
│   │   ├── slurm-baseline-ref_3_budget_80-2044287.out
│   │   ├── slurm-baseline-ref_3_budget_80-2044312.err
│   │   ├── slurm-baseline-ref_3_budget_80-2044312.out
│   │   ├── slurm-baseline-ref_3_budget_80-2044339.err
│   │   ├── slurm-baseline-ref_3_budget_80-2044339.out
│   │   ├── slurm-baseline-ref_3_budget_80-2044367.err
│   │   ├── slurm-baseline-ref_3_budget_80-2044367.out
│   │   ├── slurm-baseline-ref_4_budget_100-2044288.err
│   │   ├── slurm-baseline-ref_4_budget_100-2044288.out
│   │   ├── slurm-baseline-ref_4_budget_100-2044313.err
│   │   ├── slurm-baseline-ref_4_budget_100-2044313.out
│   │   ├── slurm-baseline-ref_4_budget_100-2044340.err
│   │   ├── slurm-baseline-ref_4_budget_100-2044340.out
│   │   ├── slurm-baseline-ref_4_budget_100-2044368.err
│   │   ├── slurm-baseline-ref_4_budget_100-2044368.out
│   │   ├── slurm-baseline-ref_4_budget_150-2044289.err
│   │   ├── slurm-baseline-ref_4_budget_150-2044289.out
│   │   ├── slurm-baseline-ref_4_budget_150-2044314.err
│   │   ├── slurm-baseline-ref_4_budget_150-2044314.out
│   │   ├── slurm-baseline-ref_4_budget_150-2044341.err
│   │   ├── slurm-baseline-ref_4_budget_150-2044341.out
│   │   ├── slurm-baseline-ref_4_budget_150-2044369.err
│   │   ├── slurm-baseline-ref_4_budget_150-2044369.out
│   │   ├── slurm-baseline-ref_4_budget_200-2044290.err
│   │   ├── slurm-baseline-ref_4_budget_200-2044290.out
│   │   ├── slurm-baseline-ref_4_budget_200-2044315.err
│   │   ├── slurm-baseline-ref_4_budget_200-2044315.out
│   │   ├── slurm-baseline-ref_4_budget_200-2044342.err
│   │   ├── slurm-baseline-ref_4_budget_200-2044342.out
│   │   ├── slurm-baseline-ref_4_budget_200-2044370.err
│   │   ├── slurm-baseline-ref_4_budget_200-2044370.out
│   │   ├── slurm-baseline-ref_4_budget_50-2044291.err
│   │   ├── slurm-baseline-ref_4_budget_50-2044291.out
│   │   ├── slurm-baseline-ref_4_budget_50-2044316.err
│   │   ├── slurm-baseline-ref_4_budget_50-2044316.out
│   │   ├── slurm-baseline-ref_4_budget_50-2044344.err
│   │   ├── slurm-baseline-ref_4_budget_50-2044344.out
│   │   ├── slurm-baseline-ref_4_budget_50-2044371.err
│   │   ├── slurm-baseline-ref_4_budget_50-2044371.out
│   │   ├── slurm-baseline-ref_4_budget_80-2044292.err
│   │   ├── slurm-baseline-ref_4_budget_80-2044292.out
│   │   ├── slurm-baseline-ref_4_budget_80-2044317.err
│   │   ├── slurm-baseline-ref_4_budget_80-2044317.out
│   │   ├── slurm-baseline-ref_4_budget_80-2044345.err
│   │   ├── slurm-baseline-ref_4_budget_80-2044345.out
│   │   ├── slurm-baseline-ref_4_budget_80-2044372.err
│   │   ├── slurm-baseline-ref_4_budget_80-2044372.out
│   │   ├── slurm-baseline-ref_5_budget_100-2044293.err
│   │   ├── slurm-baseline-ref_5_budget_100-2044293.out
│   │   ├── slurm-baseline-ref_5_budget_100-2044318.err
│   │   ├── slurm-baseline-ref_5_budget_100-2044318.out
│   │   ├── slurm-baseline-ref_5_budget_100-2044346.err
│   │   ├── slurm-baseline-ref_5_budget_100-2044346.out
│   │   ├── slurm-baseline-ref_5_budget_100-2044373.err
│   │   ├── slurm-baseline-ref_5_budget_100-2044373.out
│   │   ├── slurm-baseline-ref_5_budget_110_max_5-2062792.err
│   │   ├── slurm-baseline-ref_5_budget_110_max_5-2062792.out
│   │   ├── slurm-baseline-ref_5_budget_110_max_5-2062806.err
│   │   ├── slurm-baseline-ref_5_budget_110_max_5-2062806.out
│   │   ├── slurm-baseline-ref_5_budget_120_max_5-2062793.err
│   │   ├── slurm-baseline-ref_5_budget_120_max_5-2062793.out
│   │   ├── slurm-baseline-ref_5_budget_120_max_5-2062807.err
│   │   ├── slurm-baseline-ref_5_budget_120_max_5-2062807.out
│   │   ├── slurm-baseline-ref_5_budget_130_max_5-2062794.err
│   │   ├── slurm-baseline-ref_5_budget_130_max_5-2062794.out
│   │   ├── slurm-baseline-ref_5_budget_130_max_5-2062808.err
│   │   ├── slurm-baseline-ref_5_budget_130_max_5-2062808.out
│   │   ├── slurm-baseline-ref_5_budget_140_max_5-2062795.err
│   │   ├── slurm-baseline-ref_5_budget_140_max_5-2062795.out
│   │   ├── slurm-baseline-ref_5_budget_140_max_5-2062809.err
│   │   ├── slurm-baseline-ref_5_budget_140_max_5-2062809.out
│   │   ├── slurm-baseline-ref_5_budget_150-2044294.err
│   │   ├── slurm-baseline-ref_5_budget_150-2044294.out
│   │   ├── slurm-baseline-ref_5_budget_150-2044319.err
│   │   ├── slurm-baseline-ref_5_budget_150-2044319.out
│   │   ├── slurm-baseline-ref_5_budget_150-2044347.err
│   │   ├── slurm-baseline-ref_5_budget_150-2044347.out
│   │   ├── slurm-baseline-ref_5_budget_150-2044374.err
│   │   ├── slurm-baseline-ref_5_budget_150-2044374.out
│   │   ├── slurm-baseline-ref_5_budget_200-2044295.err
│   │   ├── slurm-baseline-ref_5_budget_200-2044295.out
│   │   ├── slurm-baseline-ref_5_budget_200-2044320.err
│   │   ├── slurm-baseline-ref_5_budget_200-2044320.out
│   │   ├── slurm-baseline-ref_5_budget_200-2044348.err
│   │   ├── slurm-baseline-ref_5_budget_200-2044348.out
│   │   ├── slurm-baseline-ref_5_budget_200-2044375.err
│   │   ├── slurm-baseline-ref_5_budget_200-2044375.out
│   │   ├── slurm-baseline-ref_5_budget_50-2044296.err
│   │   ├── slurm-baseline-ref_5_budget_50-2044296.out
│   │   ├── slurm-baseline-ref_5_budget_50-2044321.err
│   │   ├── slurm-baseline-ref_5_budget_50-2044321.out
│   │   ├── slurm-baseline-ref_5_budget_50-2044349.err
│   │   ├── slurm-baseline-ref_5_budget_50-2044349.out
│   │   ├── slurm-baseline-ref_5_budget_50-2044376.err
│   │   ├── slurm-baseline-ref_5_budget_50-2044376.out
│   │   ├── slurm-baseline-ref_5_budget_60_max_5-2062789.err
│   │   ├── slurm-baseline-ref_5_budget_60_max_5-2062789.out
│   │   ├── slurm-baseline-ref_5_budget_60_max_5-2062803.err
│   │   ├── slurm-baseline-ref_5_budget_60_max_5-2062803.out
│   │   ├── slurm-baseline-ref_5_budget_70_max_5-2062790.err
│   │   ├── slurm-baseline-ref_5_budget_70_max_5-2062790.out
│   │   ├── slurm-baseline-ref_5_budget_70_max_5-2062804.err
│   │   ├── slurm-baseline-ref_5_budget_70_max_5-2062804.out
│   │   ├── slurm-baseline-ref_5_budget_80-2044297.err
│   │   ├── slurm-baseline-ref_5_budget_80-2044297.out
│   │   ├── slurm-baseline-ref_5_budget_80-2044322.err
│   │   ├── slurm-baseline-ref_5_budget_80-2044322.out
│   │   ├── slurm-baseline-ref_5_budget_80-2044350.err
│   │   ├── slurm-baseline-ref_5_budget_80-2044350.out
│   │   ├── slurm-baseline-ref_5_budget_80-2044377.err
│   │   ├── slurm-baseline-ref_5_budget_80-2044377.out
│   │   ├── slurm-baseline-ref_5_budget_90_max_5-2062791.err
│   │   ├── slurm-baseline-ref_5_budget_90_max_5-2062791.out
│   │   ├── slurm-baseline-ref_5_budget_90_max_5-2062805.err
│   │   ├── slurm-baseline-ref_5_budget_90_max_5-2062805.out
│   │   ├── slurm-baseline-ref_6_budget_100-2044298.err
│   │   ├── slurm-baseline-ref_6_budget_100-2044298.out
│   │   ├── slurm-baseline-ref_6_budget_100-2044323.err
│   │   ├── slurm-baseline-ref_6_budget_100-2044323.out
│   │   ├── slurm-baseline-ref_6_budget_100-2044351.err
│   │   ├── slurm-baseline-ref_6_budget_100-2044351.out
│   │   ├── slurm-baseline-ref_6_budget_100-2044378.err
│   │   ├── slurm-baseline-ref_6_budget_100-2044378.out
│   │   ├── slurm-baseline-ref_6_budget_150-2044299.err
│   │   ├── slurm-baseline-ref_6_budget_150-2044299.out
│   │   ├── slurm-baseline-ref_6_budget_150-2044324.err
│   │   ├── slurm-baseline-ref_6_budget_150-2044324.out
│   │   ├── slurm-baseline-ref_6_budget_150-2044352.err
│   │   ├── slurm-baseline-ref_6_budget_150-2044352.out
│   │   ├── slurm-baseline-ref_6_budget_150-2044379.err
│   │   ├── slurm-baseline-ref_6_budget_150-2044379.out
│   │   ├── slurm-baseline-ref_6_budget_200-2044300.err
│   │   ├── slurm-baseline-ref_6_budget_200-2044300.out
│   │   ├── slurm-baseline-ref_6_budget_200-2044325.err
│   │   ├── slurm-baseline-ref_6_budget_200-2044325.out
│   │   ├── slurm-baseline-ref_6_budget_200-2044353.err
│   │   ├── slurm-baseline-ref_6_budget_200-2044353.out
│   │   ├── slurm-baseline-ref_6_budget_200-2044380.err
│   │   ├── slurm-baseline-ref_6_budget_200-2044380.out
│   │   ├── slurm-baseline-ref_6_budget_50-2044301.err
│   │   ├── slurm-baseline-ref_6_budget_50-2044301.out
│   │   ├── slurm-baseline-ref_6_budget_50-2044326.err
│   │   ├── slurm-baseline-ref_6_budget_50-2044326.out
│   │   ├── slurm-baseline-ref_6_budget_50-2044354.err
│   │   ├── slurm-baseline-ref_6_budget_50-2044354.out
│   │   ├── slurm-baseline-ref_6_budget_50-2044381.err
│   │   ├── slurm-baseline-ref_6_budget_50-2044381.out
│   │   ├── slurm-baseline-ref_6_budget_80-2044302.err
│   │   ├── slurm-baseline-ref_6_budget_80-2044302.out
│   │   ├── slurm-baseline-ref_6_budget_80-2044327.err
│   │   ├── slurm-baseline-ref_6_budget_80-2044327.out
│   │   ├── slurm-baseline-ref_6_budget_80-2044355.err
│   │   ├── slurm-baseline-ref_6_budget_80-2044355.out
│   │   ├── slurm-baseline-ref_6_budget_80-2044382.err
│   │   ├── slurm-baseline-ref_6_budget_80-2044382.out
│   │   ├── slurm-baseline-ref_7_budget_100-2044303.err
│   │   ├── slurm-baseline-ref_7_budget_100-2044303.out
│   │   ├── slurm-baseline-ref_7_budget_100-2044328.err
│   │   ├── slurm-baseline-ref_7_budget_100-2044328.out
│   │   ├── slurm-baseline-ref_7_budget_100-2044356.err
│   │   ├── slurm-baseline-ref_7_budget_100-2044356.out
│   │   ├── slurm-baseline-ref_7_budget_100-2044383.err
│   │   ├── slurm-baseline-ref_7_budget_100-2044383.out
│   │   ├── slurm-baseline-ref_7_budget_150-2044304.err
│   │   ├── slurm-baseline-ref_7_budget_150-2044304.out
│   │   ├── slurm-baseline-ref_7_budget_150-2044329.err
│   │   ├── slurm-baseline-ref_7_budget_150-2044329.out
│   │   ├── slurm-baseline-ref_7_budget_150-2044357.err
│   │   ├── slurm-baseline-ref_7_budget_150-2044357.out
│   │   ├── slurm-baseline-ref_7_budget_150-2044384.err
│   │   ├── slurm-baseline-ref_7_budget_150-2044384.out
│   │   ├── slurm-baseline-ref_7_budget_200-2044305.err
│   │   ├── slurm-baseline-ref_7_budget_200-2044305.out
│   │   ├── slurm-baseline-ref_7_budget_200-2044330.err
│   │   ├── slurm-baseline-ref_7_budget_200-2044330.out
│   │   ├── slurm-baseline-ref_7_budget_200-2044358.err
│   │   ├── slurm-baseline-ref_7_budget_200-2044358.out
│   │   ├── slurm-baseline-ref_7_budget_200-2044385.err
│   │   ├── slurm-baseline-ref_7_budget_200-2044385.out
│   │   ├── slurm-baseline-ref_7_budget_50-2044306.err
│   │   ├── slurm-baseline-ref_7_budget_50-2044306.out
│   │   ├── slurm-baseline-ref_7_budget_50-2044331.err
│   │   ├── slurm-baseline-ref_7_budget_50-2044331.out
│   │   ├── slurm-baseline-ref_7_budget_50-2044359.err
│   │   ├── slurm-baseline-ref_7_budget_50-2044359.out
│   │   ├── slurm-baseline-ref_7_budget_50-2044386.err
│   │   ├── slurm-baseline-ref_7_budget_50-2044386.out
│   │   ├── slurm-baseline-ref_7_budget_80-2044307.err
│   │   ├── slurm-baseline-ref_7_budget_80-2044307.out
│   │   ├── slurm-baseline-ref_7_budget_80-2044332.err
│   │   ├── slurm-baseline-ref_7_budget_80-2044332.out
│   │   ├── slurm-baseline-ref_7_budget_80-2044360.err
│   │   ├── slurm-baseline-ref_7_budget_80-2044360.out
│   │   ├── slurm-baseline-ref_7_budget_80-2044387.err
│   │   └── slurm-baseline-ref_7_budget_80-2044387.out
│   ├── param_sweep
│   │   ├── group_01.slurm
│   │   ├── group_02.slurm
│   │   ├── group_03.slurm
│   │   ├── group_04.slurm
│   │   ├── group_05.slurm
│   │   ├── group_06.slurm
│   │   ├── group_07.slurm
│   │   ├── group_08.slurm
│   │   └── group_09.slurm
│   ├── param_sweep_data
│   │   ├── data_group_01.slurm
│   │   ├── data_group_02.slurm
│   │   ├── data_group_03.slurm
│   │   ├── data_group_04.slurm
│   │   ├── data_group_05.slurm
│   │   ├── data_group_06.slurm
│   │   ├── data_group_07.slurm
│   │   ├── data_group_08.slurm
│   │   └── data_group_09.slurm
│   ├── batch_animation_final.slurm
│   ├── batch_animation_snapshot.slurm
│   ├── batch_baseline_evaluation_ref_3_budget_100.slurm
│   ├── batch_baseline_evaluation_ref_3_budget_150.slurm
│   ├── batch_baseline_evaluation_ref_3_budget_200.slurm
│   ├── batch_baseline_evaluation_ref_3_budget_50.slurm
│   ├── batch_baseline_evaluation_ref_3_budget_80.slurm
│   ├── batch_baseline_evaluation_ref_4_budget_100.slurm
│   ├── batch_baseline_evaluation_ref_4_budget_150.slurm
│   ├── batch_baseline_evaluation_ref_4_budget_200.slurm
│   ├── batch_baseline_evaluation_ref_4_budget_50.slurm
│   ├── batch_baseline_evaluation_ref_4_budget_80.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_100.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_110.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_120.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_130.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_140.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_150.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_200.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_50.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_60.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_70.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_80.slurm
│   ├── batch_baseline_evaluation_ref_5_budget_90.slurm
│   ├── batch_baseline_evaluation_ref_6_budget_100.slurm
│   ├── batch_baseline_evaluation_ref_6_budget_150.slurm
│   ├── batch_baseline_evaluation_ref_6_budget_200.slurm
│   ├── batch_baseline_evaluation_ref_6_budget_50.slurm
│   ├── batch_baseline_evaluation_ref_6_budget_80.slurm
│   ├── batch_baseline_evaluation_ref_7_budget_100.slurm
│   ├── batch_baseline_evaluation_ref_7_budget_150.slurm
│   ├── batch_baseline_evaluation_ref_7_budget_200.slurm
│   ├── batch_baseline_evaluation_ref_7_budget_50.slurm
│   ├── batch_baseline_evaluation_ref_7_budget_80.slurm
│   ├── batch_baseline_evaluation_template.slurm
│   ├── batch_model_evaluation_ref_0_budget_50.slurm
│   ├── batch_model_evaluation_ref_2_budget_50.slurm
│   ├── batch_model_evaluation_ref_3_budget_100.slurm
│   ├── batch_model_evaluation_ref_3_budget_150.slurm
│   ├── batch_model_evaluation_ref_3_budget_200.slurm
│   ├── batch_model_evaluation_ref_3_budget_50.slurm
│   ├── batch_model_evaluation_ref_3_budget_80.slurm
│   ├── batch_model_evaluation_ref_4_budget_100.slurm
│   ├── batch_model_evaluation_ref_4_budget_150.slurm
│   ├── batch_model_evaluation_ref_4_budget_200.slurm
│   ├── batch_model_evaluation_ref_4_budget_50.slurm
│   ├── batch_model_evaluation_ref_4_budget_80.slurm
│   ├── batch_model_evaluation_ref_5_budget_100.slurm
│   ├── batch_model_evaluation_ref_5_budget_110.slurm
│   ├── batch_model_evaluation_ref_5_budget_120.slurm
│   ├── batch_model_evaluation_ref_5_budget_130.slurm
│   ├── batch_model_evaluation_ref_5_budget_140.slurm
│   ├── batch_model_evaluation_ref_5_budget_150.slurm
│   ├── batch_model_evaluation_ref_5_budget_200.slurm
│   ├── batch_model_evaluation_ref_5_budget_50.slurm
│   ├── batch_model_evaluation_ref_5_budget_60.slurm
│   ├── batch_model_evaluation_ref_5_budget_70.slurm
│   ├── batch_model_evaluation_ref_5_budget_80.slurm
│   ├── batch_model_evaluation_ref_5_budget_90.slurm
│   ├── batch_model_evaluation_ref_6_budget_100.slurm
│   ├── batch_model_evaluation_ref_6_budget_150.slurm
│   ├── batch_model_evaluation_ref_6_budget_200.slurm
│   ├── batch_model_evaluation_ref_6_budget_300.slurm
│   ├── batch_model_evaluation_ref_6_budget_50.slurm
│   ├── batch_model_evaluation_ref_6_budget_80.slurm
│   ├── batch_model_evaluation_ref_7_budget_100.slurm
│   ├── batch_model_evaluation_ref_7_budget_150.slurm
│   ├── batch_model_evaluation_ref_7_budget_200.slurm
│   ├── batch_model_evaluation_ref_7_budget_50.slurm
│   ├── batch_model_evaluation_ref_7_budget_600.slurm
│   ├── batch_model_evaluation_ref_7_budget_80.slurm
│   ├── batch_model_evaluation_template.slurm
│   ├── full_training_job.slurm
│   ├── restart_100k.slurm
│   ├── step_domain_sweep.slurm
│   ├── step_domain_sweep_20k.slurm
│   ├── step_domain_sweep_streamlined.slurm
│   ├── test_amr_job.slurm
│   ├── test_batch_ref_0_budget_50.slurm
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
│   ├── mixed_class_test_loop.py
│   └── test_enhanced_callback.py
├── tools
│   ├── __init__.py
│   ├── analyze_rl_performance.py
│   ├── analyze_tensorboard.py
│   ├── analyze_tensorboard_pdf.py
│   ├── CODESTRUCTURE.md
│   ├── failed_transfers.txt
│   ├── generate_codestructure.py
│   ├── generate_model_transfer_commands.py
│   ├── generate_robust_model_transfer.py
│   ├── hpc_data_survey.py
│   ├── robust_transfer_commands.sh
│   └── transfer_commands.sh
├── anova_analysis_pingouin.py
├── baseline_management.sh
├── batch_analysis_runner.py
├── batch_animation_runner.py
├── CODESTRUCTURE.md
├── collect_training_reports.py
├── create_base_config.py
├── create_batch_baseline_jobs.py
├── create_batch_evaluation_jobs.py
├── create_batch_evaluation_jobs.py.backup
├── create_data_export_scripts.py
├── create_data_export_scripts_original.py
├── create_manifest_system.py
├── create_slurm_scripts.py
├── create_test_sweep.py
├── debug_paths.py
├── inspect_csv_structure.py
├── master_rename.sh
├── monitor_param_sweep.py
├── pareto_debug.log
├── project_structure.md
├── README.md
├── rename_baseline_files.sh
├── rename_model_files.sh
├── requirements.txt
├── setup.py
├── setup_local_analysis.py
├── slurm-baseline-ref_4_budget_100_max_4-2068515.err
├── slurm-baseline-ref_4_budget_100_max_4-2068515.out
├── slurm-baseline-ref_4_budget_50_max_4-2068513.err
├── slurm-baseline-ref_4_budget_50_max_4-2068513.out
├── slurm-baseline-ref_4_budget_80_max_4-2068514.err
├── slurm-baseline-ref_4_budget_80_max_4-2068514.out
├── slurm-baseline-ref_5_budget_100_max_5-2068518.err
├── slurm-baseline-ref_5_budget_100_max_5-2068518.out
├── slurm-baseline-ref_5_budget_50_max_5-2068516.err
├── slurm-baseline-ref_5_budget_50_max_5-2068516.out
├── slurm-baseline-ref_5_budget_80_max_5-2068517.err
├── slurm-baseline-ref_5_budget_80_max_5-2068517.out
├── slurm-baseline-ref_6_budget_100_max_6-2068521.err
├── slurm-baseline-ref_6_budget_100_max_6-2068521.out
├── slurm-baseline-ref_6_budget_50_max_6-2068519.err
├── slurm-baseline-ref_6_budget_50_max_6-2068519.out
├── slurm-baseline-ref_6_budget_80_max_6-2068520.err
├── slurm-baseline-ref_6_budget_80_max_6-2068520.out
├── submit_param_sweep.sh
├── submit_param_sweep_data.sh
├── submit_test_sweep.sh
├── temp_config_3.yaml
├── test_batch_animations.py
└── test_minimal_training.py
```

## Key Directories

- **experiments/**: Training configurations and results
- **numerical/**: Core AMR and RL implementation
- **slurm_scripts/**: HPC job submission scripts
- **logs/**: SLURM job output and error logs
- **tools/**: Utility scripts and analysis tools

*Generated automatically using tools/generate_codestructure.py*