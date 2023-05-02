r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\ou.out", "w")

n = int(r.readline())

def hex(a):
    if a == 0:
        return "0"
    elif a in range(1, 10):
        return str(a)
    elif a == 10:
        return "A"
    elif a == 11:
        return "B"
    elif a == 12:
        return "C"
    elif a == 13:
        return "D"
    elif a == 14:
        return "E"
    elif a == 15:
        return "F"
    else:
        return hex(a // 16) + hex(a % 16)
    
    
print(hex(0))
