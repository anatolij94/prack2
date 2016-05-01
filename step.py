from useful_features import *
def step_HAR(u_LW,t):
    pass
def step_GOD(u_GOD,t):
    u_curr=[]
    u_curr.append(uL(t))
    for i in range(1,len(u_prev)):
        u_curr.append((1-q)*u_prev[i]+q*u_prev[i-1])
    return u_curr
  
