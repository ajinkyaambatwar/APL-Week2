from scipy.integrate import quad        #quad imported to do integration opration
import numpy as np                      #numpy imported for array operations
import matplotlib.pyplot as mpt
from tabulate import tabulate as tb

def f(t):
    return 1/(1+np.multiply(t,t))       #function defined is 1/(1+x^2) (use of numpy will allow entire )

x=(np.linspace(0,5,num=101),object)    #vector x is defined
inte = np.zeros(len(x[0]))              #this array will store the values of integrals wrt to a value that will be taken from x i.e  atan(x)
error = np.zeros(len(x[0]))
for limit,i in zip(x[0],range(0,len(x[0]))):
    inte[i] = quad(f,0,limit)[0]        #integration now doing(quad returns integral and error value)

inte_def = np.arctan(x[0])
error = abs(inte_def-inte)
li = list()
#------------tabulating-----------
for ve,i_d,tan in zip(x[0],inte_def,inte):
    l_temp = [ve,i_d,tan]
    li.append(l_temp)

first_row = ["x-values","arctan function","Integral defined values"]
li.insert(0,first_row)
print(tb(li,tablefmt = 'psql',headers = "firstrow"))


#-------------First plot---------
mpt.figure(1)
mpt.plot(x[0],inte,'ro')
mpt.plot(x[0],inte_def,color = 'black', linewidth = 2)
mpt.xlabel("x")
mpt.ylabel("arctan")
mpt.title(r"Plot of $\int_{0}^{x} dt/{1+t^{2}}$")
mpt.legend(('Integral value','Arctan'))
#------------Ending plot 1--------------

#-------------Second subplot----------
mpt.figure(2)
mpt.plot(x[0],error,'ro')
mpt.yscale("log")
mpt.title("Plot of $\int_{0}^{x} dt/{1+t^{2}}$ error")
mpt.xlabel("x")
mpt.ylabel("$\int_{0}^{x} dt/{1+t^{2}}$ error")
#-----------Ending plot 2------------
mpt.show()
