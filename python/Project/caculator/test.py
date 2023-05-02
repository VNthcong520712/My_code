a = "4fa2.453"
for i in range(len(a)):
    if a[i].isnumeric():
        a[i] = int(a[i])
        print(a[i])
    else:
        print(a[i])