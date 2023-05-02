r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\i.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\o.out", "w")

n, m = map(int, str(*r.readlines()).split())
if 0 < n <= 10**7  and 0 < m <= 10**7:
    u = 2
    dem = 0
    for i in range(1 ,n+1):
        if u%m == 0:
            dem += 1
        u += i
    w.write(dem)