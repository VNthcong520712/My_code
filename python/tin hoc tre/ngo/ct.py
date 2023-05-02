r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\ngo\\int.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\ngo\\out.out", "w")

n,m = map(int, str(*r.readlines(1)).split())
Tpi = 0

if 0 < m <= n <= 8:
    ki = [int(x) for x in range(n, 10**n, n) if len(str(x)) == n]
    for i in ki:
        Tpi += int(str(i)[:m])
    print(Tpi)
    r.close()