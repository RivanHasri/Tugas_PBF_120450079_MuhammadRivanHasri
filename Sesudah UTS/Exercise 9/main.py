# Nomor 1
## Cara 1
factor = lambda n: list(filter(lambda i: n % i == 0, range(1,n+1)))
primes = lambda n: filter(lambda i: len(factor(i)) == 2, range(1,n+1))

print(*primes(100))

## Cara 2
L = lambda n: range(2,n)
factor = lambda n: list(filter(lambda i: n % i == 0, L(n)))
primes = lambda n: filter(lambda i: len(factor(i)) == 0, range(2,n+1))

print(*primes(100))

## Cara 3
L = lambda n: range(2, round(n**0.5)+1)
n_factor = lambda n: map(lambda i: i if n%i == 0 else 0, L(n))
primes = lambda n: filter(lambda i: sum(n_factor(i)) == 0, range(2,n+1))

print(*primes(100))

## Cara 4
s_factor = lambda n: map(lambda i: i if n%i == 0 else 0, range(2, round(n**0.55)+1))

gjl = lambda n: n%2 != 0
L = lambda n: filter(lambda i: 2 if i==2 else gjl(i), range(2,n+1))

primes = lambda n: filter(lambda i: sum(s_factor(i))==0, L(n))
print(*primes(100))

# Nomor 2
employee = {
    'Nagao': 35,
    'Ishii': 30,
    'Kazutomo': 20,
    'Saito': 25,
    'Hidemi': 29
}

filter_by_age = lambda age,employee: list(filter(lambda x: x[1] > 25, employee.items()))
print(*map(lambda d: d[0], filter_by_age(25,employee)))