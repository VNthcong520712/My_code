r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
n, k = map(int, r.readline().split())

kx = 2*k

m = 8 if n%2 == 0 else 9

V = (n-m)/2
X = n - V

T = V*k + X*kx

if V != 0 or X != 0:
    print(int(V), int(X), int(T))
else: 
    print(0)