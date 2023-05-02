r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so dac biet\\int.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so dac biet\\out.out", "w")

n = str(*r.readlines(1))
t = 1

while t != 0 and len(str(n)) == 4:
        t = int(n[0])+int(n[2])-int(n[1])-int(n[3])
        if t == 0: print(n)
        n = str(int(n)-1)
if t == 1 or len(str(n)) != 4: print(0)        