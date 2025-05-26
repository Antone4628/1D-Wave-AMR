# Project Code Structure

Auto-generated on: Fri May 23 20:19:02 MDT 2025
Project: 1D_wave_AMR

```
1D_wave_AMR/
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
│   └── Solver_Class_1D_Wave_AMR_refdef_GIF.gif
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
├── media
│   ├── images
│   ├── Tex
│   │   ├── 5683d89f396abe50.svg
│   │   ├── 5683d89f396abe50.tex
│   │   ├── 66e1bc57a83e0f07.svg
│   │   ├── 66e1bc57a83e0f07.tex
│   │   ├── 6ecf9f51170c1a70.svg
│   │   ├── 6ecf9f51170c1a70.tex
│   │   ├── ba96de15f98acfc8.svg
│   │   ├── ba96de15f98acfc8.tex
│   │   ├── d3c1af651a272204.svg
│   │   ├── d3c1af651a272204.tex
│   │   ├── d6c3967a482a9e45.svg
│   │   ├── d6c3967a482a9e45.tex
│   │   ├── ec2b01090b1fbb55.svg
│   │   └── ec2b01090b1fbb55.tex
│   ├── texts
│   │   ├── 00f6d03009451435.svg
│   │   ├── 0169d7022fb8a9f6.svg
│   │   ├── 01b4df1ba49f37aa.svg
│   │   ├── 04069491702d941b.svg
│   │   ├── 05bb8dd8086110cd.svg
│   │   ├── 063059c2a11586f0.svg
│   │   ├── 070be0970939bdd4.svg
│   │   ├── 0cfb2d99bacfc6e4.svg
│   │   ├── 0d003d792ff41d02.svg
│   │   ├── 10d064dd5d04f830.svg
│   │   ├── 113a1f33b85c511c.svg
│   │   ├── 11bc33da59d125ba.svg
│   │   ├── 1486115a411b7fae.svg
│   │   ├── 150b7eceac0fd5ab.svg
│   │   ├── 181de1f5ea5395ff.svg
│   │   ├── 1897f1999796a601.svg
│   │   ├── 19973c10247bb2b8.svg
│   │   ├── 19c95f9b8584942f.svg
│   │   ├── 19defb6f31a1e8ed.svg
│   │   ├── 1c3d01888462f59f.svg
│   │   ├── 1ca25dbb7602548f.svg
│   │   ├── 1ce1dbf560b21186.svg
│   │   ├── 1df13ba8a0645c2c.svg
│   │   ├── 1e30a5c1b6c875e3.svg
│   │   ├── 1e9ed7b95c2ec1b7.svg
│   │   ├── 1ff645a2f6f7d496.svg
│   │   ├── 209fbd2ca70f25b4.svg
│   │   ├── 210971cff0777531.svg
│   │   ├── 2250c1a415e4abe4.svg
│   │   ├── 235883a13d7586bb.svg
│   │   ├── 242334e8187bc84d.svg
│   │   ├── 24cea75e74ea5ce0.svg
│   │   ├── 286d9ec1a95a1b8a.svg
│   │   ├── 286f1c5a0aa22a0c.svg
│   │   ├── 297a337ceabec92e.svg
│   │   ├── 29dfb57d5d4844c9.svg
│   │   ├── 2bf35c3b557c4ef5.svg
│   │   ├── 334a781f6708a08a.svg
│   │   ├── 342cf00e947c2d90.svg
│   │   ├── 34f77e007a25fde6.svg
│   │   ├── 36277e11eccb6546.svg
│   │   ├── 372e736d7c3df706.svg
│   │   ├── 37c1d4d0e2c9dc7f.svg
│   │   ├── 3906449327c2bfb3.svg
│   │   ├── 39185cbafa7c64a9.svg
│   │   ├── 3b2a2b04f61de421.svg
│   │   ├── 3d992dd1f6489e0c.svg
│   │   ├── 41b842327f6260d0.svg
│   │   ├── 466bcb191c5f51d6.svg
│   │   ├── 472d891663cd28a2.svg
│   │   ├── 48a562c7d06417c9.svg
│   │   ├── 48db7f90fdb8f11a.svg
│   │   ├── 4952bf9bc3b28dfb.svg
│   │   ├── 499e8ddbe8f5e327.svg
│   │   ├── 49d8b4066c19e27c.svg
│   │   ├── 4dfd5d3cbc999603.svg
│   │   ├── 5137834db86e47b0.svg
│   │   ├── 577aa3e2863b4c4f.svg
│   │   ├── 5b6c7bc3ad5cc0f8.svg
│   │   ├── 5c51637bd9f4b9e2.svg
│   │   ├── 5d38966c0b506207.svg
│   │   ├── 61e67cb10e02eab2.svg
│   │   ├── 64597e1b0d6602ef.svg
│   │   ├── 65b966d3a409e468.svg
│   │   ├── 663dfd3d10e118ed.svg
│   │   ├── 671e140e96cf5ec6.svg
│   │   ├── 685b1fa378e9fed5.svg
│   │   ├── 685d898da4b205aa.svg
│   │   ├── 68f8c80a86a87fd1.svg
│   │   ├── 70418b8717391803.svg
│   │   ├── 73b377d0b2d119e4.svg
│   │   ├── 7450ada85b1f09bc.svg
│   │   ├── 75103e883b9bd9f0.svg
│   │   ├── 7656d14d3fda2553.svg
│   │   ├── 76c08fc1fc3eb3aa.svg
│   │   ├── 79d857c69b814dab.svg
│   │   ├── 7c012358af515e63.svg
│   │   ├── 7c9b35e624356651.svg
│   │   ├── 7da9b6f9f8a07667.svg
│   │   ├── 8128395eb6cbc634.svg
│   │   ├── 8295daac4bc50269.svg
│   │   ├── 84331bb025acddba.svg
│   │   ├── 85309e57ba7ad1c4.svg
│   │   ├── 8b2aa512ce534c6f.svg
│   │   ├── 8bd2d642d002ba0c.svg
│   │   ├── 8dbfdbe4a23c8698.svg
│   │   ├── 90fe4588f43379c9.svg
│   │   ├── 919901ee9276ccbd.svg
│   │   ├── 92c69ce34f0e95d6.svg
│   │   ├── 944f20ede43f34b9.svg
│   │   ├── 94666c16e91a5661.svg
│   │   ├── 950de5dcc4490461.svg
│   │   ├── 95896c6d40334017.svg
│   │   ├── 95f0f4727dead115.svg
│   │   ├── 9634f4315d6cd87e.svg
│   │   ├── 986b0073f57a4272.svg
│   │   ├── 99e6b4174a019a17.svg
│   │   ├── 99ec5f697a508c8c.svg
│   │   ├── 9a55d7319f17d1f1.svg
│   │   ├── 9b3ec5b5a8f1a67c.svg
│   │   ├── 9d23ca4bae251410.svg
│   │   ├── 9e66bc6370cb366b.svg
│   │   ├── 9e91049ff2004e86.svg
│   │   ├── 9eae84d9d35b553b.svg
│   │   ├── 9f55156b433d012d.svg
│   │   ├── a345b9bf4727bfb9.svg
│   │   ├── a3e8f9713dcb131e.svg
│   │   ├── a4af630c2b2b4746.svg
│   │   ├── a4cc9890a42c12bc.svg
│   │   ├── a601ffeb33542183.svg
│   │   ├── a6305fcb6d9c9556.svg
│   │   ├── a68024cd6c06d316.svg
│   │   ├── acce4ad249dd492d.svg
│   │   ├── ae0ac83abfebbaa3.svg
│   │   ├── aec93861abddea4a.svg
│   │   ├── afdcd93515231155.svg
│   │   ├── b41ae754d02ca771.svg
│   │   ├── b44a2838777f2ae1.svg
│   │   ├── b58bbdc6793a70e3.svg
│   │   ├── b77b599da758ffcb.svg
│   │   ├── b9b8ffd4e7065586.svg
│   │   ├── bb6baf2f15d3438b.svg
│   │   ├── bd0b33f49cdf8f5e.svg
│   │   ├── bea6c4ace14098c5.svg
│   │   ├── c7e25e0f4e094b54.svg
│   │   ├── c7ee2615e12bb6d2.svg
│   │   ├── c9eef971db7492be.svg
│   │   ├── ca2ad3bf8b946667.svg
│   │   ├── ca8306589246243d.svg
│   │   ├── cb167f558edae2bf.svg
│   │   ├── cbf60fe22d39cb68.svg
│   │   ├── cbfcdd04506ccd81.svg
│   │   ├── ce48bd1517299b02.svg
│   │   ├── cef357e2ea6b3058.svg
│   │   ├── cf9fc3c9220ce86a.svg
│   │   ├── d2cd037eeb95d643.svg
│   │   ├── d318161dde26895d.svg
│   │   ├── d410b23fdeac3ce9.svg
│   │   ├── da06b3928f022614.svg
│   │   ├── db66d8e14022436f.svg
│   │   ├── db9f2e8563e2975d.svg
│   │   ├── dba4df3d7de853f2.svg
│   │   ├── dcc21f37a26ff635.svg
│   │   ├── de0fe23aeda4e2b5.svg
│   │   ├── e04a9c5429ebb14e.svg
│   │   ├── e26a526cd17669f6.svg
│   │   ├── e379b3ab6a27b11a.svg
│   │   ├── e486c0330a5379ec.svg
│   │   ├── e6fda65a75ec6738.svg
│   │   ├── e7510c193444e2bf.svg
│   │   ├── e7862533767bbed9.svg
│   │   ├── e7ec9d9bb33937e7.svg
│   │   ├── eb4ec4e8934ad31a.svg
│   │   ├── ec889ece59fa075d.svg
│   │   ├── f007ef1ee6e95136.svg
│   │   ├── f135511e00a331d9.svg
│   │   ├── f2caef91cf476264.svg
│   │   ├── f54fd4138514433e.svg
│   │   ├── f6705c2e52c172ae.svg
│   │   ├── f7e5f42619b3bdbf.svg
│   │   └── fbdea57253ea0ad0.svg
│   └── videos
│       └── 1080p60
│           ├── partial_movie_files
│           └── WaveEquationAMR.mp4
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
├── numerical.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── scripts
│   ├── media
│   │   ├── images
│   │   │   └── manim_test
│   │   ├── Tex
│   │   │   ├── 5683d89f396abe50.svg
│   │   │   ├── 5683d89f396abe50.tex
│   │   │   ├── 66e1bc57a83e0f07.svg
│   │   │   ├── 66e1bc57a83e0f07.tex
│   │   │   ├── 6ecf9f51170c1a70.svg
│   │   │   ├── 6ecf9f51170c1a70.tex
│   │   │   ├── ba96de15f98acfc8.svg
│   │   │   ├── ba96de15f98acfc8.tex
│   │   │   ├── d3c1af651a272204.svg
│   │   │   ├── d3c1af651a272204.tex
│   │   │   ├── d6c3967a482a9e45.svg
│   │   │   ├── d6c3967a482a9e45.tex
│   │   │   ├── ec2b01090b1fbb55.svg
│   │   │   └── ec2b01090b1fbb55.tex
│   │   └── texts
│   │       ├── 00f6d03009451435.svg
│   │       ├── 0169d7022fb8a9f6.svg
│   │       ├── 01b4df1ba49f37aa.svg
│   │       ├── 04069491702d941b.svg
│   │       ├── 05bb8dd8086110cd.svg
│   │       ├── 063059c2a11586f0.svg
│   │       ├── 070be0970939bdd4.svg
│   │       ├── 0cfb2d99bacfc6e4.svg
│   │       ├── 0d003d792ff41d02.svg
│   │       ├── 10d064dd5d04f830.svg
│   │       ├── 113a1f33b85c511c.svg
│   │       ├── 11bc33da59d125ba.svg
│   │       ├── 1486115a411b7fae.svg
│   │       ├── 150b7eceac0fd5ab.svg
│   │       ├── 181de1f5ea5395ff.svg
│   │       ├── 1897f1999796a601.svg
│   │       ├── 19973c10247bb2b8.svg
│   │       ├── 19c95f9b8584942f.svg
│   │       ├── 19defb6f31a1e8ed.svg
│   │       ├── 1c3d01888462f59f.svg
│   │       ├── 1ca25dbb7602548f.svg
│   │       ├── 1ce1dbf560b21186.svg
│   │       ├── 1df13ba8a0645c2c.svg
│   │       ├── 1e30a5c1b6c875e3.svg
│   │       ├── 1e9ed7b95c2ec1b7.svg
│   │       ├── 1ff645a2f6f7d496.svg
│   │       ├── 209fbd2ca70f25b4.svg
│   │       ├── 210971cff0777531.svg
│   │       ├── 2250c1a415e4abe4.svg
│   │       ├── 235883a13d7586bb.svg
│   │       ├── 242334e8187bc84d.svg
│   │       ├── 24cea75e74ea5ce0.svg
│   │       ├── 286d9ec1a95a1b8a.svg
│   │       ├── 286f1c5a0aa22a0c.svg
│   │       ├── 297a337ceabec92e.svg
│   │       ├── 29dfb57d5d4844c9.svg
│   │       ├── 2bf35c3b557c4ef5.svg
│   │       ├── 334a781f6708a08a.svg
│   │       ├── 342cf00e947c2d90.svg
│   │       ├── 34f77e007a25fde6.svg
│   │       ├── 36277e11eccb6546.svg
│   │       ├── 372e736d7c3df706.svg
│   │       ├── 37c1d4d0e2c9dc7f.svg
│   │       ├── 3906449327c2bfb3.svg
│   │       ├── 39185cbafa7c64a9.svg
│   │       ├── 3b2a2b04f61de421.svg
│   │       ├── 3d992dd1f6489e0c.svg
│   │       ├── 41b842327f6260d0.svg
│   │       ├── 466bcb191c5f51d6.svg
│   │       ├── 472d891663cd28a2.svg
│   │       ├── 48a562c7d06417c9.svg
│   │       ├── 48db7f90fdb8f11a.svg
│   │       ├── 4952bf9bc3b28dfb.svg
│   │       ├── 499e8ddbe8f5e327.svg
│   │       ├── 49d8b4066c19e27c.svg
│   │       ├── 4dfd5d3cbc999603.svg
│   │       ├── 5137834db86e47b0.svg
│   │       ├── 577aa3e2863b4c4f.svg
│   │       ├── 5b6c7bc3ad5cc0f8.svg
│   │       ├── 5c51637bd9f4b9e2.svg
│   │       ├── 5d38966c0b506207.svg
│   │       ├── 61e67cb10e02eab2.svg
│   │       ├── 64597e1b0d6602ef.svg
│   │       ├── 65b966d3a409e468.svg
│   │       ├── 663dfd3d10e118ed.svg
│   │       ├── 671e140e96cf5ec6.svg
│   │       ├── 685b1fa378e9fed5.svg
│   │       ├── 685d898da4b205aa.svg
│   │       ├── 68f8c80a86a87fd1.svg
│   │       ├── 70418b8717391803.svg
│   │       ├── 73b377d0b2d119e4.svg
│   │       ├── 7450ada85b1f09bc.svg
│   │       ├── 75103e883b9bd9f0.svg
│   │       ├── 7656d14d3fda2553.svg
│   │       ├── 76c08fc1fc3eb3aa.svg
│   │       ├── 79d857c69b814dab.svg
│   │       ├── 7c012358af515e63.svg
│   │       ├── 7c9b35e624356651.svg
│   │       ├── 7da9b6f9f8a07667.svg
│   │       ├── 8128395eb6cbc634.svg
│   │       ├── 8295daac4bc50269.svg
│   │       ├── 84331bb025acddba.svg
│   │       ├── 85309e57ba7ad1c4.svg
│   │       ├── 8b2aa512ce534c6f.svg
│   │       ├── 8bd2d642d002ba0c.svg
│   │       ├── 8dbfdbe4a23c8698.svg
│   │       ├── 90fe4588f43379c9.svg
│   │       ├── 919901ee9276ccbd.svg
│   │       ├── 92c69ce34f0e95d6.svg
│   │       ├── 944f20ede43f34b9.svg
│   │       ├── 94666c16e91a5661.svg
│   │       ├── 950de5dcc4490461.svg
│   │       ├── 95896c6d40334017.svg
│   │       ├── 95f0f4727dead115.svg
│   │       ├── 9634f4315d6cd87e.svg
│   │       ├── 986b0073f57a4272.svg
│   │       ├── 99e6b4174a019a17.svg
│   │       ├── 99ec5f697a508c8c.svg
│   │       ├── 9a55d7319f17d1f1.svg
│   │       ├── 9b3ec5b5a8f1a67c.svg
│   │       ├── 9d23ca4bae251410.svg
│   │       ├── 9e66bc6370cb366b.svg
│   │       ├── 9e91049ff2004e86.svg
│   │       ├── 9eae84d9d35b553b.svg
│   │       ├── 9f55156b433d012d.svg
│   │       ├── a345b9bf4727bfb9.svg
│   │       ├── a3e8f9713dcb131e.svg
│   │       ├── a4af630c2b2b4746.svg
│   │       ├── a4cc9890a42c12bc.svg
│   │       ├── a601ffeb33542183.svg
│   │       ├── a6305fcb6d9c9556.svg
│   │       ├── a68024cd6c06d316.svg
│   │       ├── acce4ad249dd492d.svg
│   │       ├── ae0ac83abfebbaa3.svg
│   │       ├── aec93861abddea4a.svg
│   │       ├── afdcd93515231155.svg
│   │       ├── b41ae754d02ca771.svg
│   │       ├── b44a2838777f2ae1.svg
│   │       ├── b58bbdc6793a70e3.svg
│   │       ├── b77b599da758ffcb.svg
│   │       ├── b9b8ffd4e7065586.svg
│   │       ├── bb6baf2f15d3438b.svg
│   │       ├── bd0b33f49cdf8f5e.svg
│   │       ├── bea6c4ace14098c5.svg
│   │       ├── c7e25e0f4e094b54.svg
│   │       ├── c7ee2615e12bb6d2.svg
│   │       ├── c9eef971db7492be.svg
│   │       ├── ca2ad3bf8b946667.svg
│   │       ├── ca8306589246243d.svg
│   │       ├── cb167f558edae2bf.svg
│   │       ├── cbf60fe22d39cb68.svg
│   │       ├── cbfcdd04506ccd81.svg
│   │       ├── ce48bd1517299b02.svg
│   │       ├── cef357e2ea6b3058.svg
│   │       ├── cf9fc3c9220ce86a.svg
│   │       ├── d2cd037eeb95d643.svg
│   │       ├── d318161dde26895d.svg
│   │       ├── d410b23fdeac3ce9.svg
│   │       ├── da06b3928f022614.svg
│   │       ├── db66d8e14022436f.svg
│   │       ├── db9f2e8563e2975d.svg
│   │       ├── dba4df3d7de853f2.svg
│   │       ├── dcc21f37a26ff635.svg
│   │       ├── de0fe23aeda4e2b5.svg
│   │       ├── e04a9c5429ebb14e.svg
│   │       ├── e26a526cd17669f6.svg
│   │       ├── e379b3ab6a27b11a.svg
│   │       ├── e486c0330a5379ec.svg
│   │       ├── e6fda65a75ec6738.svg
│   │       ├── e7510c193444e2bf.svg
│   │       ├── e7862533767bbed9.svg
│   │       ├── e7ec9d9bb33937e7.svg
│   │       ├── eb4ec4e8934ad31a.svg
│   │       ├── ec889ece59fa075d.svg
│   │       ├── f007ef1ee6e95136.svg
│   │       ├── f135511e00a331d9.svg
│   │       ├── f2caef91cf476264.svg
│   │       ├── f54fd4138514433e.svg
│   │       ├── f6705c2e52c172ae.svg
│   │       ├── f7e5f42619b3bdbf.svg
│   │       └── fbdea57253ea0ad0.svg
│   ├── 1D_wave_amr.py
│   └── forest_example.py
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
│   └── mixed_class_test_loop.py
├── tools
│   ├── __init__.py
│   ├── analyze_rl_performance.py
│   ├── analyze_tensorboard.py
│   ├── analyze_tensorboard_pdf.py
│   └── generate_codestructure.py
├── training
│   └── utils
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