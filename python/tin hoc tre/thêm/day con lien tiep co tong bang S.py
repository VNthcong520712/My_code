r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")

n, S = map(int, r.readline().split())
a = []
ad = []
vtd = []
aa = []
vta = []
z = r.readline()[:-1]
dem = 1
while z != "":
    z = int(z)
    a.append(z)
    (ad.append(z), vtd.append(dem)) if z >= 0 else (aa.append(z), vta.append(dem))
    z = str(r.readline())
    dem += 1
    
if 1 <= n <= 10**6 and abs(S) <= 10**9 and 0 < len(a) <= n and all(0 <= abs(x) <= 10**6 for x in a):
    t = 0
    t += [j for j in a]
r.realines()