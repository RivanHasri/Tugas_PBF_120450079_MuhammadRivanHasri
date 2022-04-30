from solver import *
import matplotlib.pyplot as plt

params = {
    'g' : 9.8,
    'y0' : 1,
    't0' : 0,
    't_akhir' : 4,
    'h' : 0.001,
    'dy0' : 0.5 * 3.14
}

t, res_euler = cauchy_euler(params, Func)

plt.plot(t, res_euler)
plt.show()