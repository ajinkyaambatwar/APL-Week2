import numpy as np
import matplotlib.pyplot as mpt

def f(t):
    return 1/(1+np.multiply(t,t))

def x(k,a,h):
    return a+k*h

step=[0.05]
vec = (np.linspace(0,5,(5/step[-1]) +1))     #integrals have to be found for these values
arr = f(vec)
s = np.cumsum(arr)
inte_def = np.arctan(vec)
inte_1 = step*(s-0.5*(f(x(1,0,step[-1]))+arr))
max_err = np.amax(inte_1)           #max_error initialized to some value
true_err = np.amax(abs(inte_def-inte_1))

estim=list()                         #list to store max_error
exact=[true_err]

while max_err > 1e-8:                           #condition of >10^(-8)
    stepi=(step[-1])/2                          #step size halved(last element of 'step' list)
    vec_new = (np.linspace(0,5,(5/stepi) +1))   #new vector based on the new step size formed
    arr_new = f(vec_new)
    s=np.cumsum(arr_new)
    inte_2 = stepi*(s-0.5*(f(x(1,0,stepi))+arr_new))    #integral values at new step size formed
    tan_def = np.arctan(vec_new)
    comm = np.nonzero(np.in1d(vec_new,vec))[0]      #getting indices of the common points between previous and new array
    inte_cmp = inte_2[comm]                         #new array to store the intgrals at those common points with halved h value
    max_err=np.amax(abs(inte_1-inte_cmp))           #finding max_error with difference(estimated error)
    true_err = np.amax(abs(inte_2-tan_def))
    estim.append(max_err)                           #appending the estimated error to array 'diff'
    exact.append(true_err)
    inte_1 = inte_2                                 #now for interation the inte_2 becomes inte_1
    vec = vec_new                                   #vec_new becomes vec
    arr = arr_new                                   #arr_new becomes arr
    step.append(stepi)

estim.append(0)
#this is the buffer value being appended becoz estim will end at one
#value less as it sees future error is less than threshold
#--------------------plotting-----------------------#
mpt.figure(1)
mpt.plot(step,exact,'ro')
mpt.plot(step,estim,'g+')
mpt.xlabel('h')
mpt.ylabel('Error')
mpt.xscale("log")
mpt.yscale("log")
mpt.legend(('Exact Error','Estimated Error'))
mpt.show()
