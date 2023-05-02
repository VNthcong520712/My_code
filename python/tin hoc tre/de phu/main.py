r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\de phu\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\de phu\\ou.out", "w")

N = int(r.readline())
lst = r.readline().split()

lstp = list(set(lst))

so = []
lan = []

for i in lstp:
    ll = lst.count(i)
    lan.append(ll)

max_ = max(lan)
w.write(f"{max_}")