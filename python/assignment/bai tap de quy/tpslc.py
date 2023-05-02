n = int(input("nhap n: "))
def t(a):
    if a == 0:
        return 1
    else:
        ti = 1
        for i in range(2, 2*a+1, 2):
            ti *= i
        return 1/ti + t(a-1)
print(t(n))