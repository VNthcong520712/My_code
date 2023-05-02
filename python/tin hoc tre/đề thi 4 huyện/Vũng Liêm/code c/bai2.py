r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Vũng Liêm\\code c\\inp.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Vũng Liêm\\code c\\out.out", "w")

n, m = map(int, r.readline().split())
p = []
t = 0 
st = 0

def dayk(a, b):
    k = []
    for i in range (a, 10**(b-1)-1, -b):
        k.append(i)
    return k

def dayp(g, q, p):
    t = 0
    kq = []
    for i in range(len(g)):
        if p > q:
            z = g[i]*10**(p-q)
            t += z
        else:
            z = str(g[i])[:p]
            t += int(z)

        if i != len(g)-1:
            print(f"{z}+", end = "", file = w)
        else:
            print(f"{z}=\n{t}", end = "" , file = w)

if 0 < n <= 7 and 0 < m <= 13:
    for r in range(10**n-1, 10**n-n-1,-1):
        if r % n == 0: 
            st = r
            break
    dayp(dayk(st, n), n, m)