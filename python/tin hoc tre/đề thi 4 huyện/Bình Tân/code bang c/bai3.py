r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\i.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\o.out", "w")

s = int(*r.readlines())

tu = 0
uoc = []

for i in range(1,s):
    if s%i == 0:
        tu += i
        uoc.append(i)
if tu == s:
    su = str(uoc)[1:-1]
    w.write(su.replace(", ", "+"))
else: w.write("0")