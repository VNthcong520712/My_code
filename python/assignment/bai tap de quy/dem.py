n = int(input("nhap so nguyen n: "))
def dem(a):
    if a != 0:
        return 1 + dem(a//10)
    else: return 0
print(dem(n))