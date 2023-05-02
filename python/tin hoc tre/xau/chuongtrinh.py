r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xau\\input.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xau\\output.out", "w")

xau = str(*r.readlines(1))
K = int(*r.readlines(2))

dxx = sorted(list(set(xau)))

for r in dxx:
    if xau.count(r) >= K:
        w.write(r + "\n")