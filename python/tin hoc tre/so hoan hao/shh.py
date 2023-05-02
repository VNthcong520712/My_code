r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so hoan hao\\int.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\so hoan hao\\out.out", "w")

n = int(*r.readline())
tong = 0

for i in range(1, n):
    if n%i == 0:
        tong += i

if n == tong:
    w.write("YES")