"""
Created on Fri Sept 29 15:27:32 2022
NLMap Nonlinear data mapping
   Code by Fredy Vides
   For Paper, "Approximating equivariant evolution operators with 
   recurrent reservoir computers"
   by F. Vides
@author: Fredy Vides
""" 

def NLMap(x,tp,qalg):
    from numpy import append, kron
    from qkron import q_kron   ##  rwsp

    p = x
    q = p
    for k in range(tp-1):
        q = q_kron(x,q,qalg)
        p = append(p,q)
    p = append(p,1)
    return p