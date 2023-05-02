from math import sqrt

r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\nguyen to\\dulieu.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\nguyen to\\dulieu.out", "w")

N = int(*r.readlines(1))
dem = 0 

def timnguyento(a):
    if a == 1 or a ==  0:
        w.write("KSNT")
    else:
        for i in range(1, int(sqrt(a)+1)):
            if a%i == 0:
                global dem
                dem += 1 
        if dem == 1:
            w.write("SNT")
        else: w.write("KSNT")

timnguyento(N)
r.close()
w.close()