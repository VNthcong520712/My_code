n = int(input("Nhap n: "))
def t(a):
    if a == 1:
        return a
    else:
        p = a-1
        return (-1)**(a+1) * a + t(p)
print(t(n))