import numpy as np
import matplotlib.pyplot as mpt
import time as t

def f(t):
    return 1/(1+np.multiply(t,t))

def x(k,a,h):
    return a+k*h

def sumi(a,stop,h):
    val= sum(f(x(k,a,h)) for k in range(2,stop))
    return val


def I(a,h,b):
    i=(b-a)/h                   #number of partitions
    i=int(i)                    #float to int conversion(no data is lost in the process)
    if i==0:
        return 0                #0 value condition
    else:
        return h*(((f(a)+f(x(i,a,h)))/2)+ sumi(a,i,h))      #non-vectorized implementation

t1=t.time()
pi=(np.linspace(0,5,num=101),object)
num=0
integral = list()
for r in pi[0]:
    #print(type(r))
    num = I(0,0.001,r)
    integral.append(num)
    num=0

t2=t.time()
print("The program took %.4f seconds to run without vectorization"%(t2-t1))
mpt.figure(0)
mpt.plot(pi[0],integral,'ro')
mpt.xlabel('x')
mpt.ylabel('$\int_{0}^{x} dt/{1+t^{2}}$')
mpt.show()
