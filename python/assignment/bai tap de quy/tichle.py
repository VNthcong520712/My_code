n = int(input("nhap n: "))
def tp(a):
    if a > 0:
        return (2*a+1)*tp(a-1)
    elif a == 0: return 1
print(tp(n))