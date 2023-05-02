r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\oin.inp", "r")
n, m, x = map(int, r.readline().split())

dsd = [] 
dpd = []
dsts = []
P = Q = 0

def sort(a):
    ma = a[0][0]
    for i in range(1,len(a)):
        if a[i][0] > ma:
            r = a[i]
            a[i] = a[i-1]
            a[i-1] = 

for i in range(n):
    p, v, d, l = map(int, r.readline().split())
    if l == 2:
        dsd.append([d, v])
        if v not in dpd: dpd.append(v)
        P += 1
    else:
        dsts.append([d, v])

sorted(dsts)#, reverse= True)
print(dsts)

for i in range(n-p):
    if dsts[i][1] not in dpd:
        dsd.append(dsts[i])
        Q += 1
    
sorted(dsd, reverse = True)
print(dsd)
k = m - P - Q -1
print(k, dsd)
r = dsd[k][0] +1
print(r)