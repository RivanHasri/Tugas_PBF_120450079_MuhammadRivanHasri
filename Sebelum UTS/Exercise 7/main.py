# Nomor 1
P = 'akulupa'
P = map(lambda x: ((x[0] * 2) + 1, x[1]), enumerate(P))

print(list(P))

# Nomor 2
B = 24

fks = map(lambda b: b+1 if B % (b+1) == 0 else -1, range(B))

def filt(fks):
    x = []
    for f in fks:
        if f != -1:
            x.append(f)
    return x

print(filt(fks))

# Or use HOF filter to solve this problem
filt2 = list(filter(lambda x: x != -1, map(lambda b: b+1 if B %(b+1) == 0 else -1,range(B))))

print(filt2)

# Nomor 3
A = [[3,4], [5,6]]
B = [[1,2], [7,8]]

C = list(map(lambda x,y: list(map(lambda xx,yy: xx+yy, x, y)), A, B))

def dett(C):
    return C[0][0] * C[1][1] - C[0][1] * C[1][0]

print(dett(C))