r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\ou.out", "w")

n = int(r.readline())
d_c = [0]

def fbnc(a):
    fb_nc = []
    u = 1
    d = 1
    for i in range(1, a+1):
        u, d = d, u + d
        fb_nc.append(u)
    nds(fb_nc)

def nds(fc):
    n_ds = [1]
    u = 1
    for y in fc:
        u += y
        n_ds.append(u)
    dc(n_ds)

def dc(ns):
    global d_c
    d_c = [0]
    u = 0
    for y in ns:
        u += y
        d_c.append(u)

t = 0
v = 0
while t < n:
    t = 0
    chuoi = []
    fbnc(v)
    v += 1
    for i in d_c:
        t += len(str(i))
        chuoi += str(i)
    
print(f"{chuoi[n-1]} {len(d_c)}", file=w)