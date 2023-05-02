'''
Viết một chương trình có thể tính giai thừa của một số
cho trước. Kết quả được in thành chuỗi trên một dòng, 
phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì 
kết quả đầu ra phải là 40320.
'''

from time import sleep as sl

#-----my code
y=int(input("Nhập số cần tính giai thừa:"))
i = 1
t = y
while (i < y):
	t = t*i
	i = i+1
print(t)
print('  ')



#-----their code
x=int(input("nhập giá trị đi m: "))
def fact(x):
	if x == 1:
		return 1
	return x*fact(x-1)
print(fact(x))
sl(3)

'''     chú ý
input() có thể xuất ra giá trị và nhận vào giá trị
eturn object dùng để xuất một giá trị trong cục bộ 
trở thành gái trị toàn cục thông qua tên hàm gọi (hãy
thử thay đổi ruturn 1 thành return 3 và xem sự khác biệt)
'''