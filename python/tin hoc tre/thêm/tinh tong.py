r = open('D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp', 'r')
N = int(r.readline())
from math import sqrt
T = 0

def tonguoc(n):
    t = 0
    for i in range(1,int(sqrt(n)+1)):
        if n % i == 0:
            j = int(n/i)
            if i == j:
                t += i
            else:
                t += i + j
    return t

for i in range(1,N+1):
    c = tonguoc(i)
    if c >= N:
        T += i
print(T)