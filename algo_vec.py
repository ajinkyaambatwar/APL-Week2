'''So the idea is we have the vec of which the arctan are to be found. SO now wew are taking a step = separation between consecutive elements of the
vec elements. so now we create f(vec) and then do cumsum and get the cummulative summation array. and then funrther oparations are done
as per the formulation'''

import numpy as np
import matplotlib.pyplot as mpt
import time as t

def f(t):
    return 1/(1+np.multiply(t,t))

def x(k,a,h):
    return a+k*h

t1=t.time()
step = 0.001         #step size
vec = (np.linspace(0,5,(5/step) +1),object)     #integrals have to be found for these values


arr = f(vec[0])
s = np.cumsum(arr)
#print(s)
inte = step*(s-0.5*(f(x(1,0,step))+arr))
t2=t.time()
print("The program took %.4f seconds to run with vectorization"%(t2-t1))

#-------------------plotting-------------------
mpt.figure(0)
mpt.plot(vec[0],inte,'ro')
mpt.xlabel('x')
mpt.ylabel(' $\int_{0}^{x} dx/{1+x^{2}}$')
mpt.show()
