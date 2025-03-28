def standardmap(e, N=100, p0=1, q0=0):
    import numpy as np
    '''Generates data for N iterations of the Chirikov map with parameter e and 
    resolution r. Returns results in a format similar to odeint.'''

    def chirikov(p, q, e):
        import numpy as np
        """Applies Chirikov's standard map once with parameter e"""
    
        p_prime = (p + e*np.sin(q)) % (2*np.pi)
        q_prime = (p + q + e*np.sin(q)) % (2*np.pi)
    
        return p_prime, q_prime    
    
    t= np.arange(0, N, 1)  # Time array
#    p0 = 2.1
#    q0 = np.pi

    P, Q = p0, q0
    results = np.empty((N, 2))  # Shape: (N, 2) for [P, Q] at each step

    for i in range(N):
        import numpy as np
        P, Q = chirikov(P, Q, e=e)
        results[i] = [P, Q]

    return t, results