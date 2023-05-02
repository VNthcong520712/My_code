n = int(input("nhap so nguyen n: "))
def solon(b):
    if b == 0:return 0
    elif b%10 > solon(b//10): return b%10
    else: return solon(b//10)
print(solon(n))