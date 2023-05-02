r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so cach tim tong\\do.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so cach tim tong\\ra.out", "w")
from math import sqrt

n = int(*r.readlines(1))
dayuoc = []
daynguyento = []


def nguyento(b):
    dem = 0
    for i in range(1, int(sqrt(b)) + 1):
        if b % i == 0:
            dem += 1
    if dem == 1:
        return "NT"


for i in range(2,n):
    if nguyento(i) == "NT":
        daynguyento.append(i)


sl = 0
for a in range(int(len(daynguyento)/2 + 1)):
    for i in range(a+1, len(daynguyento)):
        if daynguyento[a] + daynguyento[i] == n:
            print(daynguyento[a], daynguyento[i])
            sl += 1
print(daynguyento)
w.write(f"{sl}")