r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
n, W = map(int, r.readline().split())
w = list(map(int, r.readline().split()))
w.insert(0, 0)

def f(i,j):
    if i == 0 or j == 0:
        return 0
    else:
        if w[i] <= j:
            if f(i-1,j) > w[i] + f(i-1, j-w[i]):                
                return f(i-1,j)
            else:              
                return w[i] + f(i-1, j-w[i])
        else:
            return f(i-1, j)

print(f(n, W))