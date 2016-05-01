from math import *
x_min=0
x_max=pi
a_move=2
q=0.5
t_max=0.5
def u0(x):
    if x<=0:
        return 1
    else:
        return 0
def uL(t):
    return 1
def ua(x,t):
    if x-a_move*t<=0:
        return 1
    else:
        return 0
