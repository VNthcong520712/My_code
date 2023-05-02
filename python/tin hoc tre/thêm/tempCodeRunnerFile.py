r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\oin.inp", "r")

# nhap vao cac gia tri
H, K = map(int, r.readline().split())
dsch = [0 for x in range(H)]
t = 0
for u in range(H):
    dsch[u] = [x for x in r.readline() if x != "\n"]
    if "." not in dsch[u]:
        t += 1
    else: t += 0

dsbt = [] 
cnlt = []
slbt = 0
# xu ly
if t == H:
    slbt = (H-1)*K + (K-1)*H + (K-1)*(H-1)
    print(slbt)
else:
    for i in range(H):
        for j in range(K):
            dem = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if (H > i + a >= 0 and K > j + b >= 0) and (i + a != i or j + b != j):
                        if dsch[i+a][j+b] == "o":
                            if dsch[i][j] == "o":
                                them = str(i) + str(j) + str(i+a) + str(j+b)
                                if them not in dsbt and (them[2:]+them[:2]) not in dsbt:
                                    dsbt.append(them)
                            elif dsch[i][j] == ".":
                                dem += 1
            cnlt.append(dem)
    dsbt
    for z in range(len(dsbt)):
        slbt += len(dsbt)
    slbt += max(cnlt)
    print(dsbt, cnlt)
