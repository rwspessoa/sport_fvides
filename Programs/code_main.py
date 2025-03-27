from HamiltonianSystemID import HamiltonianSystemID
from HamiltonianSystem import HamiltonianSystem
from numpy import arange
import standardmap as sm
import numpy as np



tt, zz = HamiltonianSystem()


print(tt.shape)
print(zz.dtype)
print(zz.shape)
print(zz)
#p0 = np.arange(0, 2*np.pi, 1)
#q0 = np.arange(0, 2*np.pi, 1)

#P, Q = np.meshgrid(p0, q0)

#P = P.reshape(len(p0)*len(q0))
#Q = Q.reshape(len(p0)*len(q0))

t, z = sm.frame(3.15, 100, 1)

print(z)
#print(t.shape)
#print(z.dtype)


# wr,w0,r,EMconst = HamiltonianSystemID(600)
#print(wr)
#print(w0)
#print(r)
#print(EMconst)