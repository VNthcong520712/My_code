n = int(input("nhap n: "))
def tb(x):
    if x == 1: return 1
    else: return x**2 + tb(x-1)
print(tb(n))