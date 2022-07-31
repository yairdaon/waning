import numpy as np 


def gillespie_two_strain_waning(initial,
                    beta, gamma, alpha, epsilon,mu, 
                    N, max_time):
    
    '''
    Gillespie simulation of model.
    Simulation is terminated after time max_time 
    OR 
    when there are no more infected/exposed individuals
    
    This second condition for terminating speeds up the algorithm without losing info needed to approx p_10 and p_01
    
    HOWEVER, to run time-series plots replace 
    while (t <max_time) & ((pop[ind][1] + pop[ind][2]+ pop[ind][5] + pop[ind][6]) > 0):
    
    with 
    
    while (t <max_time):
    '''
    np.random.seed()
    T = []
    pop = []
    # N = sum(initial)
    pop.append(initial)
    T.append(0)
    t = 0
    ind = 0


    state = np.zeros(shape= (8,6))
    rate = np.zeros(6)
    
    #state =      [ Sn,  En, In, Rn, Sp, Ep, Ip, Rp]
    state[:,0] =  [ -1,  1,  0,  0,  0,  0,  0,  0] # Sn to En
    state[:,1] =  [  0, -1,  1,  0,  0,  0,  0,  0] # En to In
    state[:,2] =  [  0,  0, -1,  1,  0,  0,  0,  0] # In to Rn
    
    state[:,3] =  [  0,  0,  0,  0, -1,  1,  0,  0] # Sp to Ep
    state[:,4] =  [  0,  0,  0,  0,  0, -1,  1,  0] # Ep to Ip
    state[:,5] =  [  0,  0,  0,  0,  0,  0, -1,  1] # Ip to Rp
    


    
    rate[0] = beta*(pop[ind][0])/N*(pop[ind][2]+(1-epsilon)*pop[ind][6]) # Sn to En
    rate[1] = gamma*(pop[ind][1]) # En to In
    rate[2] = mu*(pop[ind][2]) # In to Rn    
    rate[3] = beta*(pop[ind][4])/N*(1-alpha)*(pop[ind][2]+(1-epsilon)*pop[ind][6])# Sp to Ep
    rate[4] = gamma*pop[ind][5] # Ep to Ip
    rate[5] = mu*pop[ind][6] # Ip to Rp


    while (t <max_time) & ((pop[ind][1] + pop[ind][2]+ pop[ind][5] + pop[ind][6]) > 0):
        Rtotal = sum(rate)
        if Rtotal >0:
            delta_t= -np.log(np.random.uniform(0,1))/Rtotal

            P = np.random.uniform(0,1)*Rtotal
            t =t+ delta_t
            event = np.min(np.where(P<=np.cumsum(rate)))
            T.append(t)
            pop.append(pop[ind]+state[:,event])
            ind=ind+1
    
            rate[0] = beta*(pop[ind][0])/N*(pop[ind][2]+(1-epsilon)*pop[ind][6]) # Sn to En
            rate[1] = gamma*(pop[ind][1]) # En to In
            rate[2] = mu*(pop[ind][2]) # In to Rn    
            rate[3] = beta*(pop[ind][4])/N*(1-alpha)*(pop[ind][2]+(1-epsilon)*pop[ind][6])# Sp to Ep
            rate[4] = gamma*pop[ind][5] # Ep to Ip
            rate[5] = mu*pop[ind][6] # Ip to Rp
        else: 
            t = max_time
            T.append(t)
            pop.append(pop[ind])
    return T, np.array(pop)

def gillespie_daily_outputs(gillespieOuput):
    '''
    Takes Gillespie output and creates the output into steps. Then interpolates results into daily timesteps
    '''
    t = gillespieOuput[0]
    i_n = gillespieOuput[1][:,2] 
    i_p = gillespieOuput[1][:,6]

    stept = []
    stepin = []
    stepip = []

    for ind, x in enumerate(t):
        if ind<len(t)-1:
            stepin.append((i_n[ind], i_n[ind]))
            stepip.append((i_p[ind], i_p[ind]))
            stept.append((t[ind], t[ind+1]))
        else:
            stepin.append((i_n[ind], i_n[ind]))
            stepip.append((i_p[ind], i_p[ind]))
            stept.append((t[ind], t[ind]))
            
    stepin = np.array(stepin).flatten()
    stepip = np.array(stepip).flatten()
    stept = np.array(stept).flatten()
   
    
    inter_t = np.arange(0, round(max(stept))+1, 1)
    inter_in = np.interp(inter_t, stept,stepin)
    inter_ip = np.interp(inter_t, stept,stepip)


    return inter_in, inter_ip