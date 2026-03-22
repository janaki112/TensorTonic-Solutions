import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    return_sums = np.zeros(n_states)
    return_count = np.zeros(n_states)
    V = np.zeros(n_states)
    for episode in episodes:
        states = np.array([step[0] for step in episode])
        rewards = np.array([step[1] for step in episode])
        visited = np.zeros(n_states, dtype = bool)
        T = len(states)
        for t in range(T):
           s = states[t]
           if not visited[s]:
               visited[s] = True
               discounts = gamma ** np.arange(T-t)
               G = np.sum( discounts * rewards[t:])
               return_sums[s] += G
               return_count[s] += 1

    non_zero = return_count > 0
    V [non_zero] = return_sums[non_zero] / return_count[non_zero]
    return V
    
        
    
    pass
