#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:07:42 2023
Example 1:
    from HamiltonianSystemID import HamiltonianSystemID
    wr,w0,r,EMconst = HamiltonianSystemID(600)
@author: Fredy Vides, Department of Statistics and Research, CNBS, Honduras
"""
def StandardMapsID(K,M,NE,p0,q0,S):
    from standardmap import standardmap
    from K4SymProjector import K4SymProjector
    from SpaRCSim import SpaRCSim
    from matplotlib.pyplot import figure,show,grid,tight_layout,scatter,plot,xlabel,ylabel,title
    from numpy import array, kron, identity, zeros
    from qkron import q_kron   ##  rwsp
    from numpy.linalg import norm
    from time import time
    
#   t,X = HamiltonianSystem()
    t,X = standardmap(K,M,NE,p0,q0)

    #K4gen = array([[0,1,-1,0],[1,0,0,-1]])
    K4gen = array([[1,0,K],[1,1,K]])
    L = X.shape[0]   # Why it doesn't use L in this function? 
    s = X.shape[1]
    l = 10 
    tp = 3
    nz = int(s*l+(s*l)*(s*l+1)/2+(s*l)**3+1)
    g1 = q_kron(K4gen[:,:s],identity(l),0.8)
    g2 = q_kron(K4gen[:,s:],identity(l),0.8)
    dn = int(((s*l)**(tp+1)-s*l)/(s*l-1)+1)  # How can I define this value?
    G1 = zeros((dn,dn))
    G2 = zeros((dn,dn))
    G1[:s*l,:s*l] = g1
    G1[s*l:((s*l)**(tp-1)+s*l),s*l:((s*l)**(tp-1)+s*l)] = q_kron(g1,g1,0.8)
    G1[((s*l)**(tp-1)+s*l):-1,((s*l)**(tp-1)+s*l):-1] = q_kron(g1,q_kron(g1,g1,0.8),0.8)
    G1[-1,-1] = 1
    G2[:s*l,:s*l] = g2
    G2[s*l:((s*l)**(tp-1)+s*l),s*l:((s*l)**(tp-1)+s*l)] = q_kron(g2,g2,0.8)
    G2[((s*l)**(tp-1)+s*l):-1,((s*l)**(tp-1)+s*l):-1] = q_kron(g2,q_kron(g2,g2,0.8),0.8)
    G2[-1,-1] = 1
    t0 = time()
    w0,data,r = K4SymProjector(X.T,"svd",l,S,1,tp,nz,g1,g2,G1,G2,1e-3,1e-4)
    wr = w0@r
#    print("Elapsed time: ",time()-t0)
#    y = SpaRCSim(wr,data[:s*l,-1],tp,L-S+l-1)
#    fig0 = figure()
#    ax00 = fig0.add_subplot(1,2,1)
#    ax00.plot(X[:S,0],X[:S,1],'b')
#    grid(color='k', linestyle='--', linewidth=0.5)
#    tight_layout()
#    ax00 = fig0.add_subplot(1,2,2)
#    ax00.plot(X[(S-l):,0],X[(S-l):,1],'g')
#    ax00.plot(y[0,:].T,y[l,:].T,'r--')
#    grid(color='k', linestyle='--', linewidth=0.5)
#    tight_layout()
#    show()
    print("Elapsed time: ", time()-t0)
    y = SpaRCSim(wr, data[:s*l, -1], tp, L-S+l-1)
    fig0 = figure()

# First subplot: scatter plot for X[:S, :]
    ax00 = fig0.add_subplot(1, 2, 1)
    ax00.scatter(X[:S, 0], X[:S, 1], color='b')
    ax00.grid(color='k', linestyle='--', linewidth=0.5)
    tight_layout()

# Second subplot: scatter plots for X[(S-l):, :] and for y data
    ax01 = fig0.add_subplot(1, 2, 2)
    ax01.scatter(X[(S-l):, 0], X[(S-l):, 1], color='g')
    ax01.scatter(y[0, :].T, y[l, :].T, color='r')
    ax01.grid(color='k', linestyle='--', linewidth=0.5)
    tight_layout()

    show()

    
    # Create a scatter plot
    #scatter(t, X[:,0], color='blue', marker='o',linestyle='--', linewidth=0.5)
    plot(t, X[:,0], color='blue', marker='o',linestyle='--', linewidth=0.5)
    # Add title and labels
    title("Simple Scatter Plot")
    xlabel("X-axis")
    ylabel("Y-axis")

    # Display grid for better readability
    grid(True)

    # Show the plot
    show()



    fig0.savefig('fig_standardmap_ID_1.png',dpi=600,format='png')
    EMconst = norm(g1@wr-wr@G1)+norm(g2@wr-wr@G2)+norm(g1@g2@wr-wr@G1@G2)
    return wr,w0,r,EMconst
