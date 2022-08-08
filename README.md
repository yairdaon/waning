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
We simulate the emergence and invasion of a novel SARS-CoV-2 strain in a population previously exposed to an immunologically related pathogen.

<h2 id="Code"> Code</h2>

To run stochastic simulations on an HPC cluster, modify the bash script: `runner.sh`. Submit jobs using `bash runner.sh` in your server environment. 

The initial conditions are input from the command line. E.g., run `python main.py 5 01 0.5` to start the simulations with the 5th parameter in the csv file, `In0=0` (initial number infected individuals previously uninfected with the related strain), `Ip0=1` (initial number infected individuals previously infected with the related strain), and `eps = 0.5`. 

    waning
    ├── funcs.py
    ├── main.py.py
    ├── runner.shsh
   
   
The name of the CSV file that contains the parameters relevant to the current run is hard coded inside `main.py`.
<!-- To create the figures in jupyter notebooks. 

    notebooks
    ├── Bifurcation_diagram.ipynb
    ├── Cross_immunity_protection.ipynb
    ├── Distribution_susceptibles.ipynb
    ├── Example_stochastic_simulations.ipynb
    └── Prob_emergence.ipynb
     -->
