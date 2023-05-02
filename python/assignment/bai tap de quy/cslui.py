n = int(input("nhap n: "))
def tl(a):
    if a != 1:
        return 1/a + tl(a-1)
    else:
        return 1
print(tl(n))