"""
Created on Fri Apr 29 14:58:40 2022
RNLMap Reduced nonlinear data mapping
   Code by Fredy Vides
   For Paper, "Computing Sparse Semilinear Models for Approximately Eventually Periodic Signals"
   by F. Vides
@author: Fredy Vides
"""
def RNLMap(R,x,tp,qalg):
    from numpy import append, kron,asarray
    from qkron import q_kron   ##  rwsp

    print("x.shape start",x.shape)
    p = x
    q = p
    for k in range(tp-1):
        print("parece tudo ok11!",k)
        print("x",x)
        print("q",q)
    #    x = asarray(x, dtype=float)
    #    q = asarray(q, dtype=float)
        print("x.shape",x.shape) 
        q = q_kron(x,q,qalg)
        print("q after",q)
        p = append(p,q)
    p = R@append(p,1)
    return p