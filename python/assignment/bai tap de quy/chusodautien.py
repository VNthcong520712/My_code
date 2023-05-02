n = int(input("Nhap n: "))
def csdt(a):
    if a > 10:
        return csdt(a//10)
    else:
        return a
print(csdt(n))