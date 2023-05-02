n = int(input())
from math import sqrt

def tnt(a):
    ds = []
    for i in range(2, a):
        dem = 0
        for j in range(1, int(sqrt(i))+1):
            if i % j == 0:
                z = i // j
                if z != j:
                    dem += 2
                else:
                    dem += 1
        if dem == 2:
            ds.append(i)
    return ds 

k = tnt(n)
sc = 0
for i in range(len(k)):
    u = n-k[i]
    if u in k:
        k[i] = 0
        sc+= 1
print(sc)