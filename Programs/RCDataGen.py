"""
Created on Sun Jul 10 10:53:58 2022
RCDataGen Data generator for the recurrent reservoir computer
@author: doctor
"""

def RCDataGen(data,L,S,ss,tp,qalg):
    from numpy import zeros
    from scipy.linalg import hankel
    from RFactor import RFactor
    from RNLMap import RNLMap
    
    print("parece tudo ok4!")   

    def DataGenerator(X,R,tp,r,qalg):
        Y = zeros((r.shape[0],R))
        print("parece tudo ok9!")

        for j in range(R):
            print("parece tudo ok10!",j)
            print(X[:,j])
            print(r)
            Y[:,j] = RNLMap(r,X[:,j],tp,qalg)
        return Y
    
    
    print("parece tudo ok5!")
    data = data[:,0:S:ss]
    s = data.shape
    sL = s[0]*L
    S = s[1]
    R = S-L+1
    print("parece tudo ok6!")
    r = RFactor(s[0], L, tp, qalg=qalg)
    
    Ldata = zeros((sL,R))
    for k in range(s[0]):
        Ldata[k*L:(k+1)*L,:] = hankel(data[k,:L],data[k,(L-1):S])
    print("parece tudo ok7!")
    D = DataGenerator(Ldata,R,tp,r,qalg)
  #  print("parece tudo ok9!")
            
    return D,r
