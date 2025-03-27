import numpy as np
# Based on https://gist.github.com/t-makaro/59a75f1694da5bd05feab2d096c174c7

def chirikov(p, q, e):
    """Applies Chirikov's standard map once with parameter e"""
    
    p_prime = (p + e*np.sin(q)) % (2*np.pi)
    q_prime = (p + q + e*np.sin(q)) % (2*np.pi)
    
    return p_prime, q_prime

def frame(e, N=100, r=1):
    '''Generates data for N iterations of the Chirikov map with parameter e and 
    resolution r. Returns results in a format similar to odeint.'''
    
    t= np.arange(0, N, 1)  # Time array
    p0 = 2.1
    q0 = np.pi

    P, Q = p0, q0
    results = np.empty((N, 2))  # Shape: (N, 2) for [P, Q] at each step

    for i in range(N):
        P, Q = chirikov(P, Q, e=e)
        results[i] = [P, Q]

    return t, results

# def plot(e, N=200, r=.5):
#    '''plots N iterations of the Chirikov map with parameter e and resolution r
#    
#    constant colour represents the same original point but after multiple iterations'''
#    P, Q, colours = frame(e, N, r)
#
#    plt.scatter(Q,P, s=.1, c=colours)
#    
#    plt.xlabel('Q')
#    plt.ylabel('P')
#    plt.show()

#plot(e=3.15,N=150,r=0.5)
