st = input("nhap chuoi: ")

dss = ""

for i in st:
    if i.isnumeric():
        dss += i
print(dss)

hs = 4
kq = ''
vtm = 0

dx = dss[vtm:len(dss)-hs]
mx = max(dx)
vtm = dx.find(mx)
kq += mx
hs -= 1

while hs >= 0:
    dx = dss[vtm+1:len(dss)-hs]
    mx = max(dx)
    vtm = dx.find(mx)+vtm+1
    kq += mx
    hs -= 1
print(kq)