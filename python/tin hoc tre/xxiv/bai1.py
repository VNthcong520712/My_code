r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai1.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai1.out", "w")

n = int(r.readline())
t31 = [1,3,5,7,8,10,12]
t30 = [4,6,9,11]

t = 1
a = 1
b = 1
c = 2020

while t <= n:
    a += 1
    t = a**2
    if b in t31:
        if a > 31:
            a -= 30
            b += 1
    elif b in t30:
        if a > 30:
            a -= 29
            b += 1
    elif b == 2 and c%4 == 0 and c%100 != 0:
        if a >29:
            a -= 28
            b += 1
        if a >28:
            a -= 27
            b += 1
    elif b > 12:
        b -= 11
        c += 1

print(a,b,c)
print(t)