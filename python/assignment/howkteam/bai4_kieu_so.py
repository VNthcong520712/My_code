#demo.py
#kiểu dữ liệu số
#số nguyên 
a = 4
print(a)
print(type(a))
print ("             ")
print ("             ")
print ("             ")

#số nguyên trong python có giá trị vô hạn


#-------------------------------------------------------


#số thực 
b = 5.00
print (b)
print (type(b))
#có độ chính xác dến 15 chữ số thập phân
c = 12.12947755628304091004 # có 20 chữ số thập phân
print (c)
print ("             ")
print ("             ")
print ("             ")



#-------------------------------------------------------


# để độ chính xác cao hơn cần:

#lấy toàn bộ nội dung thư viện decimal
#dòng có nghĩa là từ thư viện decimal ---> import mọi thứ (là dấu * đó) vào
from decimal import*

#lấy tối đa 30 chữ số phần nguyên và phần thập phân
getcontext().prec = 30

d = 10/3
print (d)
print (type(d))

d = Decimal(10)/3
print (d)
print (type(d))

d = 10/Decimal(3)
print (d)
print (type(d))

d = Decimal(10)/Decimal(3)
print (d)
print (type(d))

d = Decimal(10/3)
print (d)
print (type(d))
print ("             ")
print ("             ")
print ("             ")


#---------------------------------------------------------


#phân số fraction
from fractions import*
ps1 = Fraction(6,9)# 6 phần 9
ps2 = Fraction(1,12)
ps3 = ps1 + ps2
print (ps3)
print (type(ps3))



#------------------------------------------------------------



#số phức gồm phần thực và phần ảo j là phần ảo với j^2 = -1 
e = complex(2,5)
print(e)
#lấy phần thực thì
print(e.real)
print(e.imag)


# X//Y thương nguyên của x chia y
# X%Y lấy phần dư
# X**Y lũy thừa x với cơ số y