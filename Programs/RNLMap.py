"""
Created on Fri Apr 29 14:58:40 2022
RNLMap Reduced nonlinear data mapping
   Code by Fredy Vides
   For Paper, "Computing Sparse Semilinear Models for Approximately Eventually Periodic Signals"
   by F. Vides
@author: Fredy Vides
"""
def RNLMap(R,x,tp):
    from numpy import append, kron
    from qkron import q_kron   ##  rwsp

    p = x
    q = p
    for k in range(tp-1):
        q = q_kron(x,q,0.8)
        p = append(p,q)
    p = R@append(p,1)
    return p