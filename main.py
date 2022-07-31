import numpy as np
from funcs import gillespie_two_strain_waning, gillespie_daily_outputs
import multiprocessing
import sys 
import pandas as pd
import os

usr = './outputs/'

if not os.path.exists(usr):
    os.mkdir(usr)
#command line input is an integer, which corresponds to a line in the parameter file
param_index = int(sys.argv[1])
run = sys.argv[2]
eps = float(sys.argv[3]) 
print(f"run {run}, eps {eps}, param_index {param_index}")
parameters = pd.read_csv('R0_voc_values_July24.csv', header = None)

#other constant parameters
T = 365*5
N = 1e5
final_size=58281 #initial Sp, based on Rp

#simulation initial conditions
realisations = 500

Ip0= int(run[0])
In0= int(run[1])
Sp0=round(final_size)
Sn0=N-Sp0-In0-Ip0
En0=0
Ep0=0
Rp0=0
Rn0=0
initial_conds= [Sn0, En0, In0, Rn0, Sp0, Ep0, Ip0, Rp0]

R0previous=1.5 #reproduction number of seasonal strain
gamma = 1/5  
alpha = eps
epsilon = eps
mu=1/8 #mu in the new model

#select value of Rn from the file
Rn_voc = parameters.iloc[param_index][0]
beta=Rn_voc*mu #beta is set by Rn_voc

def main(repeat):
    simulations =  gillespie_two_strain_waning(
                    initial= initial_conds,
                    beta = beta,
                    gamma = gamma,
                    alpha = epsilon,
                    epsilon = epsilon,                                
                    mu = mu,
                    N = N,
                    max_time = T)
        

    save_inf = gillespie_daily_outputs(simulations)
    return save_inf

if __name__ == '__main__':
    num_threads = 12
    pool = multiprocessing.Pool(num_threads)
    repeats = range(realisations)
   
    results = np.array(pool.map(main, repeats), dtype=object)
    print(results)
    np.save((usr+
             'stochastic_Rn_diff_p_'+ run+
             str(param_index) + '_eps_'+str(epsilon)), 
             results)
