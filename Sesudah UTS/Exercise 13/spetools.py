# Nomor 2
from functools import reduce as r

# Define function composition
mycompose = lambda *funcs: r(lambda f,g: lambda x: f(g(x)), reversed(funcs), lambda x: x)

# Ketentuan jumlah tanggungan
def val1(jtg):
    return 1 if jtg >= 5 else 5-jtg

# Ketentuan token listrik
def val2(x):
    def rata_rata(x):
        return sum(x)/len(x)
    
    def l_cond_1(x):
        return [x, [x>100000]]
    
    def l_cond_2(x):
        return [x[0], x[1] + [x[0] >= 50000]]
    
    def to_val2(x):
        return r(lambda a,b: a + (1 if b == True else 0), x[1], 1)
    
    compose_cond = mycompose(rata_rata,l_cond_1,l_cond_2,to_val2)
    return compose_cond(x)

# Ketentuan gaji
def con_1(x):
    return [x[0], 1, x[2], [x[0] > x[2][x[1]]]]

def con_2_to_n(x):
    return [x[0], x[1] + 1, x[2], x[3] + [x[0] > x[2][x[1]]]]

def to_val(x):
    return r(lambda a,b: a + (1 if b == True else 0), x[-1], 2)

def prep(gj):
    return [gj, 0, list(map(lambda x: x*1000000, list(range(10,3,-2)) + [3]))]

def val3(gj):
    comp = mycompose(prep,con_1,*(con_2_to_n for i in range(4)), to_val)
    return comp(gj)

# Ketentuan KIP K
def val4(x=True):
    return 1 if x else 5

def gabung_val(x):
    return x + [map(lambda f,x: f(x), x[1], x[0])]

def bobot(x):
    return r(lambda a,b: a+b, map(lambda x,y: x+y, x[-1], [0.2,0.3,0.2,0.3]))

def total_ukt(x):
    return 750000 + x*500000

# Nomor 3
def split(dat):
    return dat.replace(' ', '').replace('-','+-').split('+')

def chdepan(dat):
    return dat[1:] if dat[0] == '' else dat

def eqkan(dat):
    return map( lambda x: x if '^' in x else x+ '^1' if 'x' in x else x+ 'x^0', dat)

def toarr2d(dat):
    return r( lambda a, b: a + [[float(hurf) for hurf in b.split('x^')]] , dat, [])

def sortdesc(dat):
    return sorted(dat, key=lambda x: x[1], reverse=True)

def calctur(dat):
    return map( lambda x: [0,0] if x[1] == 0 else [x[1]*x[0], x[1]-1], dat)

def tostr(dat):
    return map( lambda x: '0' if x[0] == 0 else str(x[0]) if x[1]==0 else str(x[0]) + 'x^' + str(x[1]), dat)

def prettykan(dat):
    return r( lambda a,b: a+'+' + b if b != '0' else a, dat, '')

def prettysign(dat):
    return dat.replace('+-', ' -').replace('+', '+ ')

# Nomor 4
def pajak_decorator(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print('Sub Total: ', res)
        print('Pajak: ', res * 0.01)
        print('Total: ', res + res * 0.01)
        return res
    return inner

import time

def calc_time_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('Time: ', end - start)
        return res
    return inner