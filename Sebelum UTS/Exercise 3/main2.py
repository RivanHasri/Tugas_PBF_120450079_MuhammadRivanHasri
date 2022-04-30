from solver import *
import math
from matplotlib import pyplot as plt
 
def pd(y,dy,x):
    return -y - dy + (0.5*(1 - math.cos(2*x)))

parameter = {
    't0' : 0,
    't_akhir' : 50,
    'h' : 0.05,
    'y0' : 1,
    'dy0' : -9/2
}

t2, res_euler2 = cauchy_euler(parameter, pd)

plt.plot(t2,res_euler2)
plt.show()