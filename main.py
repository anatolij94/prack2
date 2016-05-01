from step import *
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from time import sleep


N=101
xn=grid(x_min,x_max,N)
u_a=[u0(x) for x in xn]
u_GOD=[u0(x) for x in xn]
u_HAR=[u0(x) for x in xn]
t=0
Tau=tau(xn)
t=Tau
plt.ion()
f = plt.figure()
ax = f.gca()

while(t<t_max):
    ax.clear()
    ax.plot(xn, u_a, label='analytical', color='grey', lw=2)
    ax.plot(xn, u_GOD, label='u_GOD')
    ax.plot(xn, u_LW, label='u_HAR')
    print(t)
    u_GOD=step_GOD(u_GOD,t)
    u_HAR=step_HAR(u_LW,t)
    u_a=[ua(x,t) for x in xn]
    t+=Tau
    plt.legend()
    plt.show()
    plt.pause(0.05)
