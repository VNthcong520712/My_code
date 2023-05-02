r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai2.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai2.out", "w")

a1 = r.readline()
a2 = r.readline()

a = str(a1[:len(a1)-1])
b = str(a2)

m, n = len(a), len(b)

c = [[0 for i in range(n+1)] for j in range(2)]
for j in range(0, n+1):
    c[0][j] = b[:j]

def lcm(s1, s2):
    while len(s1) != 0 and s1[0] == "0":
        s1 = s1[1:]
    while len(s2) != 0 and s2[0] == "0":
        s2 = s2[1:]
    if len(s1) < len(s2) or (len(s1) == len(s2) and s1 < s2):
        return s1
    else: 
        return s2

x,y = 0,1
for i in range(m):
    c[y][0] = a[:i+1]
    for j in range(n):
        if a[i] == b[j]:
            c[y][j+1] = c[x][j] + a[i]
        else:
            c[y][j+1] = lcm(c[x][j+1] + a[i], c[y][j] + b[j])
    x, y = 1-x, 1-y
    
s = c[x][n]
print(s, file=w)