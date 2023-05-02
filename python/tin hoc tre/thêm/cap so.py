r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")

n,m = map(int, r.readline().split())
a = list(map(int, r.readline().split()))
b = list(map(int, r.readline().split()))

min_ = [["-" for i in range(len(b)+1)] for j in range(len(a)+1)]

def f(i,j):
    if i == 0 :
        return abs(min(b[:j]))
    elif j == 0:
        return abs(min(a[:i]))
    if i == 1 and j == 1:
        return abs(a[0] + b[0])
    if min_[i][j] != "-":
        return min_[i][j]
    else:
        min_[i][j] = min(f(i-1, j), f(i, j -1), abs(a[i-1] + b[j-1]))
        return min_[i][j]

print(f(n,m))