r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
k = int(r.readline())
n = int(r.readline())

tg = 0
for i in range(n):
    t, z = [x for x in r.readline().split()]
    t = int(t)
    if z == "N" or z == "P":
        tg += t*2
    else:
        tg += t
    if tg >= 210:
        print(k + i)
        break