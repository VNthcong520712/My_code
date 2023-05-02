r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai3.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\xxiv\\bai3.out", "w")

kl, gt = [0], [0]
x = []
n, c = map(int, r.readline().split())

for i in range(n):
    w, co = map(int, r.readline().split())
    kl.append(w)
    gt.append(co)

f = [[0 for i in range(c + 1)] for j in range(n + 1)]

for j in range(c+1):
    for i in range(n+1):
        if j == 0 or i == 0:
            f[i][j] = 0
        elif kl[i] > j:
            f[i][j] = f[i-1][j]
        elif kl[i] <= j:
            f[i][j] = max(f[i-1][j], f[i-1][j-kl[i]]+gt[i])

for j in range(c, -1, -1):
    for i in range(n, -1, -1):
        if f[i][j] != f[i-1][j]:
            print(f[i][j], i, "\n")
            br = True
            break
    if br == True:
        break

# luu = [[0 for i in range(c+1)] for j in range(n+1)]

# def f(i,j):
#     if i == 0 or j == 0:
#         return 0
#     elif luu[i][j] != 0:
#         return luu[i][j]
#     else:
#         if kl[i] <= j:
#             if f(i-1,j) > gt[i] + f(i-1, j-kl[i]):
#                 luu[i][j] = f(i-1,j)
#                 return f(i-1,j)
#             else:
#                 x.append(i)
#                 luu[i][j] = gt[i] + f(i-1, j-kl[i])
#                 return gt[i] + f(i-1, j-kl[i])
#         else:
#             luu[i][j] = f(i-1,j)
#             return f(i-1, j)

# print(f(n, c))
# print(*[i for i in sorted(set(x), reverse=True)])

