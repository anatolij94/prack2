from useful_features import *
def step_HAR(u_prev,t):
    u_curr=[]
    u_curr.append(uL(t))
    u_curr.append((1-q**2)*u_prev[1]+0.5*q*(1+q)*u_prev[0]-0.5*q*(1-q)*u_prev[2])
    for i in range(2,len(u_prev)-1):
        u_curr.append((1-q)*u_prev[i]+q*u_prev[i-1]-q*0.5*(1-q)*minmod(u_prev[i+1]-u_prev[i],u_prev[i]-u_prev[i-1])+q*0.5*(1-q)*minmod(u_prev[i]-u_prev[i-1],u_prev[i-1]-u_prev[i-2]))
    u_curr.append((1-q)*u_prev[-1]+q*u_prev[-2])
        
    return u_curr
def step_GOD(u_prev,t):
    u_curr=[]
    u_curr.append(uL(t))
    for i in range(1,len(u_prev)):
        u_curr.append((1-q)*u_prev[i]+q*u_prev[i-1])
    return u_curr
  
