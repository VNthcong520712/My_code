r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
N, S = map(int, r.readline().split())
a = list(map(int, r.readline().split()))
mang = []
def f(i,j):
    if i == 0 or j ==0:
        return 0
    else:
        if a[i-1] < j:
            p = f(i-1, j-a[i-1]) + a[i-1]
        else: p = 0
        q = f(i-1, j)
        
        if p > q:
            mang.append(i)
            return p
        else:
            return q 
print(f(N,S))
print(set(mang))