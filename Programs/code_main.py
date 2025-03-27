from HamiltonianSystemID import HamiltonianSystemID
from HamiltonianSystem import HamiltonianSystem
from numpy import arange
import matplotlib.pyplot as plt
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

t, z = sm.frame(1, 250, 1)

print(z)



plt.scatter(z[0], z[1], c='blue', s=1, alpha=0.5)

plt.xlabel('Q')
plt.ylabel('P')
plt.show()


#print(t.shape)
#print(z.dtype)


# wr,w0,r,EMconst = HamiltonianSystemID(600)
#print(wr)
#print(w0)
#print(r)
#print(EMconst)