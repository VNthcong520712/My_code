import string

print ("máy tính cơ bản, có thể sử lý được 3 hạng tử và các phép\n toán cơ bản như cộng trừ nhân chia nâng lỹ thừa, căn bậc 2")
print ("-"*50)
print ("lưu ý: có toán tử cho phép là + - * /; các toán hạn cho phép là các số")

def tach(a):
    for i in range(1,len(a)):
        
        if "-" in str(a[0]):
            k = str(a[0])
            k = k.lstrip("-")
            a[0] = - int(k)
        elif "+" in str(a[0]):
            k = str(a[0])
            k = k.lstrip("+")
            a[0] = int(k)
        else:
            k = str(a[0])
            a[0] = int(k)


        if a[i].isnumeric() == True:
            a[i] = int(a[i])
        elif a[i] != '+' and a[i] != '-' and a[i] != '*' and a[i] != '/':
            print ("nhập lỗi, vui lòng thử lại . . . . . ")
            continue
    return a

def tinh(b):
    S = b[0]
    for i in range(1,len(b), 2):
        if b[i] == "+":
            S += b[i+1]
        elif b[i] == "-":
            S =S - b[i+1]
        elif b[i] == "*":
            S =S * b[i+1]
        else:
            S =S / b[i+1]
    return S

while True:
    nhap = input("nhập bài toán với 3 hạng tử: ").split()
    print(tinh(tach(nhap)))
    