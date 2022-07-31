# Probability of a mutant strain invading

<h2 id="table-of-contents"> Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About the project</a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
  </ol>
</details>

<h2 id="about-the-project"> About the project</h2>
We find that a less fit strain can invade and replace a more fit one.  We conclude that it is important to rapidly assess the cross-immunity of new variants, so that we can calculate their probability of taking off, as this might happen even if they don't have a transmissibility advantage. 

Why? Effectively due to partial immunity, individuals who have previously been infected with the resident strain are susceptible to the novel strain. Thus, the pool of susceptible hosts available to the mutant strain is larger than the remaining pool of susceptibles hosts available to the resident strain. 

<h2 id="folder-structure"> Folder structure</h2>

To calculate the reproduction numbers

    mathematica_files
    └── NGM_two_strain_model.nb

To run stochastic simulations on HPC and tutorial files for using the slurm submission. First test files work, by running the bash script: `sh run_test_waning_strain_ratio.sh`. Otherwise submit the job using `sbatch ratio_waning_model.sbatch`. 

The initial conditions are hard coded. Change `initial_voc_SI = 1; initial_voc_RI = 0` to start the simulations and the corresponding string (used in saving, for identifying files) `run = "01"` in the python file `run_waning_strain_ratio.py`.

    HPC
    ├── funcs.py
    ├── ratio_waning_model.sbatch
    ├── run_waning_strain_ratio.py
    ├── test_run_waning_strain_ratio.py
    ├── run_test_waning_strain_ratio.sh
    └── intro_hpc
    │   ├── for_loop_fib_powers.sh
    │   ├── runFibonacciN.m
    │   ├── run_fib_test.sbatch
    │   ├── run_fib_test_opt2.sbatch
    │   ├── run_locally_for_loop.sh
    └── └── run_power_fib.m

To create the figures in jupyter notebooks. 

    notebooks
    ├── Bifurcation_diagram.ipynb
    ├── Cross_immunity_protection.ipynb
    ├── Distribution_susceptibles.ipynb
    ├── Example_stochastic_simulations.ipynb
    └── Prob_emergence.ipynb
    
