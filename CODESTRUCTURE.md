# Project Code Structure

Auto-generated on: Fri May 23 10:03:29 MDT 2025
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
│   │   │   └── gamma_c_100.0_full_run.yaml
│   │   └── tests
│   │       └── test_quick.yaml
│   ├── results
│   │   ├── gamma_c_100.0
│   │   │   └── run_20250523_094718
│   │   └── gamma_c_25.0
│   │       └── run_20250523_093432
│   ├── run_experiments_mixed.py
│   └── test_mixed_approach.py
├── logs
│   ├── amr_100k_1879743.err
│   ├── amr_100k_1879743.out
│   ├── amr_test_1879739.err
│   └── amr_test_1879739.out
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
├── scripts
│   ├── 1D_wave_amr.py
│   └── forest_example.py
├── slurm_scripts
│   ├── full_training_job.slurm
│   └── test_amr_job.slurm
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
│   └── generate_codestructure.py
├── CODESTRUCTURE.md
├── README.md
├── requirements.txt
└── setup.py
```

## Key Directories

- **experiments/**: Training configurations and results
- **numerical/**: Core AMR and RL implementation
- **slurm_scripts/**: HPC job submission scripts
- **logs/**: SLURM job output and error logs
- **tools/**: Utility scripts and analysis tools

*Generated automatically using tools/generate_codestructure.py*