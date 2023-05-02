r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\i.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Tân\\code bang c\\o.out", "w")

st = str(*r.readlines())
chuoi = []
st = sorted(st, reverse=True)
for i in range(len(st)):
    if st[i].isnumeric():
        break
    else:
        chuoi.append(st[i])

i = len(chuoi)-1

dem = 0
for a in chuoi:
    if a.isupper():
        dem += 1

while chuoi[i].isupper():
    for y in range(i):
        if chuoi[y] > chuoi[i].lower() >= chuoi[y+1] and dem != 0:
            chuoi.insert(y+1, chuoi[i])
            chuoi.pop(i+1)
            dem -= 1
    if dem == 0: break
ht = ""
for o in chuoi:
    ht += o
print(ht, file=w)