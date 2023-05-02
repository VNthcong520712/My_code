n = int(input("Nhap n: "))
def nhi(a):
    if a > 0:
        return a%2 + 10*nhi(a//2)
    else:
        return 0
print(nhi(n))