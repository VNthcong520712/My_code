'''
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện 
điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: 
QUANTRIMANG.COM
'''

from time import sleep

class InputOutString():
	def __init__(self):
		self.s = ""
	def getString(self):
		self.s = "hhiin njgh"#input("Nhập chuỗi: ")
	def printString(self):
		print(self.s.upper())
vao = InputOutString()
vao.getString()
vao.printString()
sleep(3)

'''
củng cố kiến thức class 
'''