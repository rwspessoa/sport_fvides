from HamiltonianSystemID import HamiltonianSystemID
from HamiltonianSystem import HamiltonianSystem
from StandardMapsID import StandardMapsID 
from numpy import arange
import matplotlib.pyplot as plt
import standardmap as sm
import numpy as np


wr,w0,r,EMconst = HamiltonianSystemID(600,qalg = 1.8)
print(wr)
print(w0)
print(r)
print(EMconst)