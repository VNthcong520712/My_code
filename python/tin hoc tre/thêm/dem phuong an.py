n = int("0000111222222222222")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\ou.out", "w")
m = sorted(list(set(str(n))))
p = [0 for i in range(len(m))]

for i in range(len(m)):
    z = str(n).count(m[i])
    p[i] = int(m[i])*z

slln = p.count(max(p))
if slln == 1:
    print(max(m), file = w)
else:
    for i in range(len(p)):
        if p[i] == max(p):
            print(m[i], end = '', file = w)