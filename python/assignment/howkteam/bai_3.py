'''
Với số nguyên n nhất định, hãy viết chương trình để 
tạo ra một dictionary chứa (i, i*i) như là số nguyên
từ 1 đến n (bao gồm cả 1 và n) sau đó in ra 
dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra 
sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
'''
from time import sleep


#-----their code 
n=int(input("Nhập vào một số:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
    #Code by Quantrimang.com

print (d)



#-----tự nâng cấp
n = int(input("nhap n đi m: "))
d = dict()
for i in range(1, n+1):
	y = str(bytes([96+i]))
	yuu  = y[2:len(y)-1] + '-' +str(i)
	d[yuu]= i*i
print(d)

sleep(3)