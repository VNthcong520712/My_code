r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\be lan\\in.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\be lan\\ou.out", "w")

n, k = map(int, str(*r.readlines(1)).split())

if 0< n <= 10**7 and 0< k <= 100:    
    gtx = k*2/3

    if n%2 == 0:
        m = 8
    else:
        m = 9

    x = int((m+n)/2)
    v = int(n-x)
    if x == 0 or v == 0:
        w.write("0")
    else:
        T = round(v*k + x*k*2/3)
        w.write(f"{v} {x} {T}")