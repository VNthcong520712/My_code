#tách chuỗi
a = 'how kteam free education'
b = a.split(' ')
print (a)
print(b)
print(' ')
b = a.split('e')
print(b)
print(' ')
b = a.split('a')
print(b)
print(' ')
b = a.split('e',2)
print(b)
print(' ')
b = a.rsplit('e',2)
print(b)
print(' ')

#phương thức partition
b = a.partition('e')
print(b)
print(' ')
b = a.rpartition('e')
print(b)
print(' ')

#phương thức count, đếm
b = a.count('e',0,10)#tìm số luongwjphaanf tử e trong khoảng từ 0 -> 10
print(b)
print(' ')

#phương thức satrtswith, endswith
b = a.startswith('h')
print(b)
print(' ')
b = a.startswith('k')
print(b)
print(' ')
b = a.startswith('k',4)#đến vị trí số 4
print(b)
print(' ')
b = a.startswith('h',0,9)
print(b)
print(' ')

b = a.endswith('h')
print(b)
print(' ')
b = a.endswith('n')
print(b)
print(' ')

#tìm vị trí tìm dc chuỗi
b = a.find('h')
print(b)
print(' ')
b = a.find('n')
print(b)
print(' ')
b = a.rfind('e')
print(b)
print(' ')

b = a.index('h')
print(b)
print(' ')
b = a.index('n')
print(b)
print(' ')

#khi kí tự không có trong chuỗi
b = a.find('l')
print(b)
print(' ')
'''b = a.index('l') nếu không thấy sẽ lỗi
print(b)
print(' ')'''

#kiểm tra có phải chuỗi viết thường hay viết hoa
b = a.islower()#kiểm tra vết thường
print(b)
print(' ')
a = 'How are you'
b = a.islower()
print(b)
print(' ')

b = a.isupper()#kiểm tra vết hoa
print(b)
print(' ')
a = 'HOW ARE YOU'
b = a.isupper()
print(b)
print(' ')

#kiểm tra chuỗi có phải là số hai không
a = '43123e'
c = '131414'
b = a.isdigit()
print(b)
b = c.isdigit()
print(b)
print(' ')

#kiểm tra chuỗi có phải khoảng trắng hay không
d = '          '
e = '           sfs      '
b = d.isspace()
print(b)
b = e.isspace()
print(b)
