n = int(input("nhap n: "))
def t(a):
    if a == 1:
        return a
    else:
        ti = 1
        for i in range(1,a+1):
            ti *= i
        return ti + t(a-1)
print(t(n))