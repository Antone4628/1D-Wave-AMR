1D_WAVE_AMR/
├── animations/
├── experiments/
│   ├── configs/
│   │   ├── gamma_c_5.0.yaml
│   │   ├── gamma_c_10.0.yaml
│   │   ├── gamma_c_25.0.yaml
│   │   ├── gamma_c_50.0.yaml
│   │   ├── gamma_c_1000.0.yaml
│   │   └── test_config.yaml
│   ├── results/
│   │   ├── gamma_c_10.0/
│   │   └── gamma_c_25.0/
│   ├── analyze_model.py
│   ├── test_training_cycle.py
│   └── run_experiments.py
├── logs/
│   ├── best_model/
│   ├── checkpoints/
│   ├── eval_results/
│   └── tensorboard/
│       └── A2C_1/
├── numerical/
│   ├── __init__.py
│   ├── amr/
│   │   ├── __init__.py
│   │   ├── adapt.py
│   │   ├── forest.py
│   │   ├── model_marker.py
│   │   └── projection.py
│   ├── callbacks/
│   │   ├── __init__.py
│   │   └── enhanced_callback.py
│   ├── dg/
│   │   ├── __init__.py
│   │   ├── basis.py
│   │   └── matrices.py
│   ├── grid/
│   │   ├── __init__.py
│   │   └── mesh.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   ├── dg_wave_solver.py  
│   │   ├── dg_wave_solver_clean.py 
│   │   ├── wave.py           
│   │   └── utils.py
│   └── environments/
│       ├── __init__.py
│       ├── dg_amr_env_clean.py
│       └── dg_amr_env.py
├── scripts/
│    ├── 1D_wave_amr.py
│    └── forest_example.py
├── tensorboard_logs/
├── tests/
│   ├── __init__.py
│   ├── test_amr/
│   │   ├── __init__.py
│   │   ├── balance_test.py
│   │   ├── class_test.py
│   │   ├── model_class_test.py
│   │   └── projection_test.py
│   ├── test_animation/
│   │   ├── __init__.py
│   │   └── manim_test.py
│   ├── test_RL/
│       ├── __init__.py
│       ├── check_env.py
│       ├── test_env.py
│       └── train_test.py
├── tools/
│   ├── __init__.py
│   ├── analyze_rl_performance.py
│   └── analyze_tensorboard.py
├── training/
│   ├── configs/
│   │   └── config.yaml
│   ├── utils/
│   │   └── config_loader.py
│   ├── simple_train_config.py
│   └── simple_train.py
├── CODESTRUCTURE.md
├── README.md
├── requirements.txt
└── setup.py
