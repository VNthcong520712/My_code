a = input("\nnhập dãy a: ").split()
I = int(input("nhập vào I: "))
v = input("nhập v: ") 

if len(a) < 10**5 and 1 <= I < len(a):
    print("nhập hợp lệ ^3^\n")
    a.insert(I-1, v)
    print(a)
else:
    print("!!! dãy nhập vào không hợp lệ, vui lòng thử lại !!!")
