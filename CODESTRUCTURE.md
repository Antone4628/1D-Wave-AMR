# Project Code Structure

Auto-generated on: Thu Jun 12 20:21:22 MDT 2025
Project: 1D_wave_AMR

```
1D_wave_AMR/
├── analysis
│   ├── automated_reports
│   │   └── quick_overview.py
│   ├── data
│   │   ├── exports
│   │   │   ├── anova_results_20250605_074900.json
│   │   │   ├── anova_results_20250611_155811.json
│   │   │   └── anova_results_20250612_072903.json
│   │   ├── models
│   │   │   └── session3_100k_uniform
│   │   ├── processed
│   │   │   ├── full_param_sweep_data_20250601_105453
│   │   │   └── session3_100k_uniform
│   │   └── raw
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
│   ├── interactive_analysis
│   ├── model_performance
│   │   ├── dg_wave_solver_evaluation.py
│   │   ├── model_marker_evaluation.py
│   │   └── single_model_runner.py
│   ├── outputs
│   │   ├── figures
│   │   │   ├── anova_analysis_20250605_074855.pdf
│   │   │   ├── anova_analysis_20250611_155806.pdf
│   │   │   ├── anova_analysis_20250612_072858.pdf
│   │   │   ├── convergence_by_gamma.png
│   │   │   ├── correlation_heatmap.png
│   │   │   └── training_duration.png
│   │   ├── reports
│   │   └── thesis_assets
│   ├── statistical_analysis
│   │   ├── data
│   │   │   └── processed
│   │   ├── __init__.py
│   │   ├── anova_analysis.py
│   │   └── test_imports.py
│   ├── utilities
│   │   ├── __init__.py
│   │   └── config.py
│   └── data_sample.py
├── animations
│   ├── 1D_Wave_AMR_refdef_GIF.gif
│   ├── Gaussian_Pulse_Advection_AMR.gif
│   ├── Gaussian_Pulse_Advection_Snapshots.png
│   ├── Mixed_model_RL_AMR_1D_Wave_GIF.gif
│   ├── RL_AMR_1D_Wave_GIF 2.gif
│   ├── RL_AMR_1D_Wave_GIF.gif
│   ├── RL_Driven_AMR_Wave_Solver.gif
│   ├── RL_MODEL_AMR_1D_Wave_GIF.gif
│   ├── Sequential_RL_AMR_1D_Wave_GIF.gif
│   ├── Sequential_RL_AMR_Single_Round_1D_Wave_GIF.gif
│   ├── Sequential_RL_AMR_Single_Round_1D_Wave_step_domain_0.05_20k_GIF.gif
│   ├── Sequential_RL_AMR_Single_Round_1D_Wave_step_domain_0.15_GIF.gif
│   ├── Solver_Class_1D_Wave_AMR_refdef_GIF.gif
│   ├── step_domain_0.05_50k_Video.mp4
│   ├── step_domain_0.15_20k_GIF.gif
│   ├── step_domain_0.15_20k_Video.mp4
│   └── step_domain_0.15_50k_Video.mp4
├── data
│   └── raw
│       └── full_param_sweep_data_20250601_105453
├── debug_output
│   ├── plots
│   │   ├── accuracy_penalty_ratio_gamma_100.0.png
│   │   ├── accuracy_penalty_ratio_gamma_25.0.png
│   │   ├── accuracy_penalty_ratio_gamma_50.0.png
│   │   ├── barrier_function_gamma_100.0.png
│   │   ├── barrier_function_gamma_25.0.png
│   │   ├── barrier_function_gamma_50.0.png
│   │   ├── budget_threshold_elements_gamma_100.0.png
│   │   ├── budget_threshold_elements_gamma_25.0.png
│   │   ├── budget_threshold_elements_gamma_50.0.png
│   │   ├── elements_resources_gamma_25.0.png
│   │   ├── log_delta_u_gamma_25.0.png
│   │   ├── reward_at_budget_gamma_100.0.png
│   │   ├── reward_at_budget_gamma_25.0.png
│   │   ├── reward_at_budget_gamma_50.0.png
│   │   ├── reward_components_gamma_25.0.png
│   │   └── reward_vs_delta_u_gamma_25.0.png
│   ├── budget_test_gamma_100.0.csv
│   ├── budget_test_gamma_25.0.csv
│   ├── budget_test_gamma_50.0.csv
│   ├── reward_debug.log
│   └── reward_debug_gamma_25.0.csv
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
│   │   └── test_config.yaml
│   ├── results
│   │   ├── gamma_c_10.0
│   │   ├── gamma_c_100.0
│   │   │   ├── run_20250521_141716
│   │   │   ├── run_20250522_070538
│   │   │   ├── run_20250522_082351
│   │   │   ├── run_20250522_085537
│   │   │   └── run_20250522_092017
│   │   ├── gamma_c_25.0
│   │   └── gamma_c_50.0
│   │       ├── run_20250321_195453
│   │       ├── run_20250403_133532
│   │       └── run_20250514_090135
│   ├── analyze_model.py
│   ├── debug_mixed_approach.py
│   ├── debug_refinement.py
│   ├── generate_pdf_report.py
│   ├── run_experiments.py
│   ├── run_experiments_mixed.py
│   ├── run_experiments_mixed_gpu.py
│   ├── run_experiments_mixed_no_timestamp.py
│   ├── run_experiments_options.py
│   └── test_mixed_approach.py
├── logs
│   ├── best_model
│   ├── checkpoints
│   ├── eval_results
│   ├── tensorboard
│   │   └── A2C_1
│   │       └── events.out.tfevents.1737814772.MacBookPro.60897.0
│   ├── test_tensorboard
│   │   ├── A2C_1
│   │   │   └── events.out.tfevents.1739824577.MacBookPro.392.0
│   │   └── A2C_2
│   │       └── events.out.tfevents.1739825229.MacBookPro.1043.0
│   ├── training_20250220_072106
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_072705
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_073159
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_075239
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_075430
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_194115
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_194414
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250220_195108
│   │   └── monitor.csv
│   ├── training_20250220_195326
│   │   └── monitor.csv
│   ├── training_20250220_200552
│   │   └── monitor.csv
│   ├── training_20250220_201951
│   │   └── monitor.csv
│   ├── training_20250220_202212
│   │   └── monitor.csv
│   ├── training_20250220_202600
│   │   └── monitor.csv
│   ├── training_20250220_202721
│   │   └── monitor.csv
│   ├── training_20250220_203029
│   │   └── monitor.csv
│   ├── training_20250220_203535
│   │   └── monitor.csv
│   ├── training_20250221_063400
│   │   └── monitor.csv
│   ├── training_20250221_071239
│   │   └── monitor.csv
│   ├── training_20250221_071819
│   │   └── monitor.csv
│   ├── training_20250221_071947
│   │   └── monitor.csv
│   ├── training_20250221_074953
│   │   └── monitor.csv
│   ├── training_20250221_080301
│   │   └── monitor.csv
│   ├── training_20250221_081933
│   │   └── monitor.csv
│   ├── training_20250221_082420
│   │   └── monitor.csv
│   ├── training_20250223_090607
│   │   └── monitor.csv
│   ├── training_20250223_090919
│   │   └── monitor.csv
│   ├── training_20250223_101631
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250223_102536
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250223_102956
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250223_111408
│   │   └── monitor.csv
│   ├── training_20250223_111445
│   │   └── monitor.csv
│   ├── training_20250223_111849
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250223_112003
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_053313
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_055154
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_055651
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_055754
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_061134
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_061653
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_061958
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_062340
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_062745
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_080931
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_082307
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_082407
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_082807
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_083247
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_083351
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_083724
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_083841
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_083911
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_084213
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_155056
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_155658
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_200830
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_202113
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_202834
│   │   ├── plots
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_203925
│   │   ├── plots
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_204546
│   │   ├── plots
│   │   │   ├── final_rewards_plot.png
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_205833
│   │   ├── plots
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250224_210926
│   │   ├── plots
│   │   │   ├── final_rewards_plot.png
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_032722
│   │   └── plots
│   │       └── test_plot.png
│   ├── training_20250225_032858
│   │   ├── plots
│   │   │   ├── final_rewards_plot.png
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_033013
│   │   ├── plots
│   │   │   ├── final_rewards_plot.png
│   │   │   └── test_plot.png
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_035156
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_035430
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_035705
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_040737
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_040834
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_041238
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_041701
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_092317
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_094114
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_143231
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_143926
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_144029
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_144354
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── training_20250225_165946
│   │   ├── final_model.zip
│   │   └── monitor.csv
│   ├── final_model.zip
│   └── monitor.csv
├── mesh_evolution
│   ├── 0_initial_with_balance.png
│   ├── 0_initial_without_balance.png
│   ├── 1_with_balance.png
│   ├── 1_without_balance.png
│   ├── 2_with_balance.png
│   ├── 2_without_balance.png
│   ├── 3_with_balance.png
│   ├── 3_without_balance.png
│   ├── 4_with_balance.png
│   ├── 4_without_balance.png
│   ├── 5_with_balance.png
│   ├── 5_without_balance.png
│   ├── evolution_with_balance.png
│   └── evolution_without_balance.png
├── models
│   └── transferred
│       ├── full_sweep_data_20250601
│       │   ├── gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip
│       │   ├── gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip
│       │   ├── gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip
│       │   ├── gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip
│       │   ├── gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip
│       │   ├── gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip
│       │   ├── gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip
│       │   └── gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip
│       ├── step_domain_0
│       │   ├── _stable_baselines3_version
│       │   ├── data
│       │   ├── policy.optimizer.pth
│       │   ├── policy.pth
│       │   ├── pytorch_variables.pth
│       │   └── system_info.txt
│       ├── step_domain_0-2
│       │   ├── _stable_baselines3_version
│       │   ├── data
│       │   ├── policy.optimizer.pth
│       │   ├── policy.pth
│       │   ├── pytorch_variables.pth
│       │   └── system_info.txt
│       ├── step_domain_0.05_20ksteps_final_model.zip
│       ├── step_domain_0.05_50k_final_model.zip
│       ├── step_domain_0.05_final_model.zip
│       ├── step_domain_0.10_final_model.zip
│       ├── step_domain_0.15_20ksteps_final_model.zip
│       ├── step_domain_0.15_50k_final_model.zip
│       └── step_domain_0.15_final_model.zip
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
├── numerical.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── scripts
│   ├── 1D_wave_amr.py
│   └── forest_example.py
├── slurm_scripts
│   ├── full_training_job.slurm
│   ├── restart_100k.slurm
│   ├── step_domain_sweep.slurm
│   └── test_amr_job.slurm
├── src
│   └── dg_package
│       ├── __init__.py
│       ├── amr.py
│       ├── numerics.py
│       └── numerics_amr.py
├── tensorboard_logs
│   ├── A2C_0
│   │   ├── events.out.tfevents.1739247008.MacBookPro.45518.1
│   │   ├── events.out.tfevents.1739280563.MacBookPro.46441.1
│   │   ├── events.out.tfevents.1739280564.MacBookPro.46441.2
│   │   ├── events.out.tfevents.1739280566.MacBookPro.46441.3
│   │   ├── events.out.tfevents.1739283708.MacBookPro.46955.1
│   │   ├── events.out.tfevents.1739283938.MacBookPro.47036.1
│   │   ├── events.out.tfevents.1739283939.MacBookPro.47036.2
│   │   ├── events.out.tfevents.1739283941.MacBookPro.47036.3
│   │   └── events.out.tfevents.1739283944.MacBookPro.47036.4
│   ├── A2C_run_20250225_035156_1
│   │   └── events.out.tfevents.1740480718.Antones-MacBook-Pro.local.27472.0
│   ├── A2C_run_20250225_035430_1
│   │   └── events.out.tfevents.1740480872.Antones-MacBook-Pro.local.27565.0
│   ├── A2C_run_20250225_035705_1
│   │   └── events.out.tfevents.1740481026.Antones-MacBook-Pro.local.27631.0
│   ├── A2C_run_20250225_040737_1
│   │   └── events.out.tfevents.1740481659.Antones-MacBook-Pro.local.28067.0
│   ├── A2C_run_20250225_040834_1
│   │   └── events.out.tfevents.1740481715.Antones-MacBook-Pro.local.28130.0
│   ├── A2C_run_20250225_041238_1
│   │   └── events.out.tfevents.1740481960.Antones-MacBook-Pro.local.28257.0
│   ├── A2C_run_20250225_041701_1
│   │   └── events.out.tfevents.1740482223.Antones-MacBook-Pro.local.28376.0
│   ├── A2C_run_20250225_092317_1
│   │   └── events.out.tfevents.1740500598.Antones-MacBook-Pro.local.29924.0
│   ├── A2C_run_20250225_094114_1
│   │   └── events.out.tfevents.1740501676.Antones-MacBook-Pro.local.30295.0
│   ├── A2C_run_20250225_143231_1
│   │   └── events.out.tfevents.1740519153.antones-mbp.boisestate.edu.33487.0
│   ├── A2C_run_20250225_143926_1
│   │   └── events.out.tfevents.1740519568.antones-mbp.boisestate.edu.33667.0
│   ├── A2C_run_20250225_144029_1
│   │   └── events.out.tfevents.1740519630.antones-mbp.boisestate.edu.33725.0
│   ├── A2C_run_20250225_144354_1
│   │   └── events.out.tfevents.1740519835.antones-mbp.boisestate.edu.33854.0
│   ├── A2C_run_20250225_165946_1
│   │   └── events.out.tfevents.1740527987.Antones-MacBook-Pro.local.35693.0
│   ├── events.out.tfevents.1737826302.MacBookPro.63553.0
│   ├── events.out.tfevents.1737826555.MacBookPro.63946.0
│   ├── events.out.tfevents.1737826635.MacBookPro.64003.0
│   ├── events.out.tfevents.1737826696.MacBookPro.64036.0
│   ├── events.out.tfevents.1737826750.MacBookPro.64069.0
│   ├── events.out.tfevents.1737844407.MacBookPro.65912.0
│   ├── events.out.tfevents.1737844887.MacBookPro.66057.0
│   ├── events.out.tfevents.1737845200.MacBookPro.66154.0
│   ├── events.out.tfevents.1737846461.MacBookPro.66457.0
│   ├── events.out.tfevents.1737847580.MacBookPro.66689.0
│   ├── events.out.tfevents.1737847776.MacBookPro.66895.0
│   ├── events.out.tfevents.1737848090.MacBookPro.67002.0
│   ├── events.out.tfevents.1737849416.MacBookPro.67337.0
│   ├── events.out.tfevents.1737850072.MacBookPro.67511.0
│   ├── events.out.tfevents.1737850223.MacBookPro.67630.0
│   ├── events.out.tfevents.1737866516.MacBookPro.68566.0
│   ├── events.out.tfevents.1737866687.MacBookPro.68637.0
│   ├── events.out.tfevents.1737902747.MacBookPro.69396.0
│   ├── events.out.tfevents.1737902980.MacBookPro.69470.0
│   ├── events.out.tfevents.1737903325.MacBookPro.69566.0
│   ├── events.out.tfevents.1737909008.MacBookPro.70561.0
│   ├── events.out.tfevents.1738336587.MacBookPro.17194.0
│   ├── events.out.tfevents.1738461020.MacBookPro.35065.0
│   ├── events.out.tfevents.1738461057.MacBookPro.35102.0
│   ├── events.out.tfevents.1738461370.MacBookPro.35257.0
│   ├── events.out.tfevents.1739247005.MacBookPro.45518.0
│   ├── events.out.tfevents.1739280309.MacBookPro.46362.0
│   ├── events.out.tfevents.1739280561.MacBookPro.46441.0
│   ├── events.out.tfevents.1739283706.MacBookPro.46955.0
│   └── events.out.tfevents.1739283936.MacBookPro.47036.0
├── tests
│   ├── animations
│   ├── outputs
│   │   ├── barrier_function 2.png
│   │   ├── barrier_function.png
│   │   ├── reward_vs_resource 2.png
│   │   └── reward_vs_resource.png
│   ├── test_amr
│   │   ├── test_configs
│   │   ├── visualizations
│   │   │   ├── refinement_comparison_distribution.png
│   │   │   └── refinement_comparison_mesh.png
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
│   ├── robust_transfer_commands.sh
│   └── transfer_commands.sh
├── training
│   └── utils
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
├── setup_local_analysis.py
├── temp_config_1.yaml
├── temp_config_2.yaml
├── temp_config_3.yaml
├── test_csv_transfer.csv
├── test_manual_transfer.json
└── test_minimal_training.py
```

## Key Directories

- **experiments/**: Training configurations and results
- **numerical/**: Core AMR and RL implementation
- **slurm_scripts/**: HPC job submission scripts
- **logs/**: SLURM job output and error logs
- **tools/**: Utility scripts and analysis tools

*Generated automatically using tools/generate_codestructure.py*