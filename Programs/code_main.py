from HamiltonianSystemID import HamiltonianSystemID
from HamiltonianSystem import HamiltonianSystem
from StandardMapsID import StandardMapsID 
from numpy import arange
import matplotlib.pyplot as plt
import standardmap as sm
import numpy as np



#tt, zz = HamiltonianSystem()

#wr,w0,r,EMconst = StandardMapsID(K,NE,p0,q0,S):
wr,w0,r,EMconst = StandardMapsID(3.5,1, 10000, np.pi/2,np.pi,600)


#t, z = sm.frame(0.001, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='lightblue', s=5, alpha=0.5)
#t, z = sm.frame(0.01, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='blue', s=5, alpha=0.5)
#t, z = sm.frame(0.1, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='darkblue', s=5, alpha=0.5)
#t, z = sm.frame(0.5, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='magenta', s=5, alpha=0.5)
#t, z = sm.frame(0.75, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='darkorange', s=5, alpha=0.5)
#t, z = sm.frame(0.85, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker=4, c='darkorange', s=5, alpha=0.5)
#t, z = sm.frame(0.95, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker=4, c='black', s=5, alpha=0.5)
#t, z = sm.frame(1, 1000, 1)
#plt.scatter(z[:,0], z[:,1], marker='o', c='green', s=5, alpha=0.5)




# plt.xlabel('Q')
# plt.ylabel('P')
# plt.show()



#print(t.shape)
#print(z.dtype)


#wr,w0,r,EMconst = HamiltonianSystemID(600)
#print(wr)
#print(w0)
#print(r)
#print(EMconst)