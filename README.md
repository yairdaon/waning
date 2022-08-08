# Probability of a mutant strain invading

<h2 id="table-of-contents"> Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About the project</a></li>
    <li><a href="#Code"> ➤ Code</a></li>
  </ol>
</details>

<h2 id="about-the-project"> About the project</h2>
We find that a less fit strain can invade and replace a more fit one.  We conclude that it is important to rapidly assess the cross-immunity of new variants, so that we can calculate their probability of taking off, as this might happen even if they don't have a transmissibility advantage. 

Why? Effectively due to partial immunity, individuals who have previously been infected with the resident strain are susceptible to the novel strain. Thus, the pool of susceptible hosts available to the mutant strain is larger than the remaining pool of susceptibles hosts available to the resident strain. 

<h2 id="Code"> Code</h2>

To run stochastic simulations on HPC cluster, modify the bash script: `runner.sh`. Submit jobs using `bash runner.sh` in your server environment. 

The initial conditions are input from the command line. E.g., run `python main.py 5 01 0.5` to start the simulations with the 5th parameter in the csv file, `Ip0=0, In0=1`, and `eps = 0.5`.

    master
    ├── funcs.py
    ├── main.py.py
    ├── runner.shsh
   
<!-- To create the figures in jupyter notebooks. 

    notebooks
    ├── Bifurcation_diagram.ipynb
    ├── Cross_immunity_protection.ipynb
    ├── Distribution_susceptibles.ipynb
    ├── Example_stochastic_simulations.ipynb
    └── Prob_emergence.ipynb
     -->
