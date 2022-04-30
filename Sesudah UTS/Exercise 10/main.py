# Nomor 1
from functools import reduce

L = [2,1,9,10,3,90,15]
print(reduce(lambda x,y: x+1 if y%2 == 0 else x, L, 0))

# Nomor 2
n = 5
print(reduce(lambda x,y: x*y, range(1,n+1)))

# Nomor 3
x = [2,5,6,7,10]
y = [-2,9,2,-1,10]

euclid = lambda x,y: reduce(lambda a,b: a+b, map(lambda x,y: (x-y)**2, x,y))**0.5
print(euclid(x,y))

# Nomor 4
employee = {
    'Nagao': 35,
    'Ishii': 30,
    'Kazutomo': 20,
    'Saito': 25,
    'Hidemi': 29
}

cnt_emp = lambda lim,employee: reduce(lambda a,b: a+1 if b[1] > lim else a, employee.items(), 0)
print(cnt_emp(25,employee))

# Nomor 5
fibo_rec = lambda n: 0 if n == 0 else 1 if (n == 1 or n == 2) else fibo_rec(n-1) + fibo_rec(n-2) 
deret_fibo = lambda n: list( map( lambda x: fibo_rec(x), range(n+1) ) )
print(deret_fibo(10))