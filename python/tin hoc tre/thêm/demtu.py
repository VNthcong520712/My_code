r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
a = r.readline() + " "

d = c = 0
loai = ["." , ", " , " "]
for i in range(len(a)):
    if d == 0 and a[i] not in loai:
        d = i
    if d != 0 and a[i] in loai:
        c += 1
        d = 0
print(c)