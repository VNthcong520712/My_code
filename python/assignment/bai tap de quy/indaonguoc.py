n = input("nhap so nguyen n: ")
chuoi = ""
def dao(a):
    if len(a) != 1:
        return a[len(a)-1] + dao(a[:len(a)-1])
    else: return a
print(dao(n))