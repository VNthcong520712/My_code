a, b = map(int, input("nhap : ").split())
def lt(x, y):
    if y != 0:
        return x*lt(x, y-1) 
    else:
        return 1
print(lt(a, b))