import numpy as np      #importing nimpy as np
from matplotlib.pyplot import *     #all mthods from matplotlib.pyplot are imported

#now we are going to define the required function
def f(t):
    return 1/(1+t**2)            #'t' is the variable

start=0                 #using variables to define start
stop=5                  #and stop values for finding the stepsize for linspace
step = 0.1
x=np.linspace(start,stop,num=(stop-start)/step + 1) #samples formed
print(x)
plot(x,f(x))
xlabel('x')
ylabel('f(x)')
title("Plot of $1/(1+t^{2})$")
show()
