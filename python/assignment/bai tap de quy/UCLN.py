n, m = [int(x) for x in input("Nhap n: ").split()]
def ucln(a,b):
    if a > b :
        return ucln(a-b, b)
    elif a < b :
        return ucln(a, b-a)
    else:
        return a
print(ucln(n,m))