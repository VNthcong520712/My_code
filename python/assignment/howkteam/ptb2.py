import math 

a = int(input("giải phương trình bậc 2,  nhập giá trị cho a: "))
b = int(input("giải phương trình bậc 2,  nhập giá trị cho b: "))
c = int(input("giải phương trình bậc 2,  nhập giá trị cho c: "))
 
if (a == 0) and (b == 0):
    print("phương trình này vô nghiệm")
elif (a == 0) and (b != 0):
    print("phương trinh co nghiệm là x =" + str(-c/b))
else:
    delta = b**2 -4*a*c
    if (delta < 0):
        print("phương trình nay vô nghiệm") 
    elif (delta == 0):
        print("phương trình có nghiệm kép x = " + str(-b/(2*a)))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("hai nghiệm cua phương trình là x1 = " + str(x1) + " x2 = "+ str(x2))