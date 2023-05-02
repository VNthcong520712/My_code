#===========================CÚ PHÁP======================

#---------------biến số---------------
a =1
b = 3.7764
c ='hello word'
d = [23,'sdf',873.42]

#---------------toán tử---------------
a + b
b - a 
a*b
b/a 
a**b #a lũy thừa cơ số b
a//b #a chia b lấy phần nguyên
a%b #a chia b lấy phần dư

#---------------boolean và toán tử logic---------------
print('-----boolean và toán tử logic-----')
a > b
a < b
a == b
a != b
'''
not đảo giá trị
and và
or hoặc
'''
#EX:
print(a > b and b< a)
print(a > b or b >a)
print('  ')
c = 'the first step in the way learn python'
d = 'step'
e = d in c 
print(e)
d = 'come'
e = d in c
print(e) 
d = 'come'
e = d not in c
print(e) 

#---------------cấu trúc điều khiển---------------
print('-----cấu trúc điều khiển-----')
'''  Python hỗ trợ một số cấu trúc điều khiển thông dụng. Hầu
hết các cấu trúc điều khiển đều dựa vào thụt đầu dòng
(indention) để tạo thành một block xử lý  '''
#-----==========cấu trúc if...else...elif==========-----
print('-----if...else-----')
a = 12
b = 9
if(a == b):
    print('bằng')
elif(a>b):
 	print('a lớn')
else:
 	print('b lớn')
print('kết thúc')#nằm ngoài phạm vi if ... elif...else
print('  ')

#-----==========cấu trúc for...in===========-----
print('------for...in------')
for letter in 'python':
	print ('Current Letter:', letter)
for letter in ['cocconut', 'banana']:
	print ('Current Letter:', letter)
print('  ')

#-----==========while===========-----
print('-----while-----')
j = 0
while (j < 9):
	j += 1
	print(j)
print('    ')


#----------------hàm---------------
print('-----hàm-----')
#cú pháp khai báo: def <tên hàm>(tham số 1, tham số 2,...):
#                      lệnh 
#                      return()
#Hàm nếu không trả dữ liệu thì mặc định sẽ trả về giá trị none
def sum(c, d):
	m = c + d
	print('thay vào hàm ta được' + ' ' + str(m) + '\n')
	return(m)
	 

#gọi hàm: <tên hàm>(đối số 1, đối số 2,...)
sum (2,9)
	 

#---------------xu li chuoi---------------- 
print("-----xu ki chuoi-----")
x = "this is one of the most popular programming languages"
s = x[6]#kí tự vị trí sáu
print(s)
s = x[None:6]#chuỗi từ đầu đến kí tự sáu
print(s)
s = x[6:None]#chuỗi tự kí tự sáu đến cuối
print(s)
s = x[10:None:2]#chuỗi từ kí tự 10 đến cuối với khoảng cách 2 kí tự
print(s)
s = x[10:None:-2]#chuỗi từ kí tự 10 đến cuối với khoảng cách -2 (quay ngược lại)
print(s)
s = x[None:10:2]
print(s)
s = x[None:10-2]
print(s)
print('  ')

#chuỗi trên nhiều sòng
a = '''đây là
chuỗi được
viết trên
nhiều dòng
'''
print(a)
#bản chất là 
a = 'đây là\nchuỗi được\nviết trên\nnhiều dòng'
print(a)

#-----==========nối chuỗi==========-----
print(' ')
print('-----nối chuỗi-----')
a = 'ta có chuỗi a'
s = 'và nó sẽ được nối với chuỗi s'
#nối
f = a + ' ' + s 
print(f)

#-----==========trích chuỗi==========-----
print('-----trích-----')
o = 'vd cho trich chuoi'
print(o)
y = o[None:10]#None có thể thay băng cách không viết kí tự nào hoặc viết 0
# y = o[0:10] hoặc y = o[:10]
print(y)
y = o[10:None]# None có thể thay băng cách không viết kí tự nào y = o[10:]
print(y)
y = o[3:10]
print(y)
y = o[10:3]
print(y)
y = o[4:-3]#vị trí không là kkí tự đầu tiên, vị trí âm là đi ngược lại
#tức là vị trí kí tự cuối là -1 và giảm dần từ phải qua trái
print(y)
y = o[-3:4]
print(y)

#-----==========lấy độ dài chuỗi==========-----
print ('-----lấy độ dài chuỗi-----')
#sử dụng hàm len()
i = 'ví dụ cho lấy độ dài chuỗi'
u = len(i)
print(u)
print(' ')
#kết quả sẽ in ra số lượng kí tự có trong chuỗi, vị trí cuối cùng trong
#chuỗi sẽ là len() - 1

#-----==========tìm và thay thế==========-----
print('-----tìm và thay thế-----')
am = 'good morning'
pm = am.replace('morning', 'afternoon')
print(pm)
#cấu trúc tổng quát replace(search, replacell [, max])
''' nó sẽ tìm chuỗi search trong chuỗi cần tim và thay thế nó bằng chuỗi
relpace với số lượng thay thế max, nếu không ghi max thì sẽ thay thế cho 
tất cả
'''
pm = am.replace('o', 'yu', 2)
print(pm)
print('  ')

#-----===========tìm chuỗi con===========-----
print('-----tìm chỗi con-----')
#để tìm chuỗi con trong một chuỗi lớn
a = 'đây là bản thử nghiệm'
b = a.find('thử')
print('và nó sẽ hiển thị vị trí bắt đầu chuỗi con: ' + str(b))
#mặc định sẽ tìm từ trái qua phải
b = a.rfind('là')#sẽ tìm từ phải qua trái
print(b)
#cấu trúc chung find('chuỗi', <vị trí bắt đầu tìm>)
print('  ')

#-----==========tách chuỗi==========-----
print('-----tách chuỗi-------')
c = a.split(' ')
print(c)
s = 'yytdudbnndbdvdujdsnnn'
d = s.split('n', 3)
print(d)
d = s.split('n', 80)
print(d)
d = s.split('n', -1)
print(d)
print(' ')

#-----==========trim kí tự khoảng trắng===========-----
print('-----trim kí tự-----')
s = ' chuỗi kí tư thử nghiệm '
b = s.strip(' ')
g = len(s)
h = len(b)
print(g)
print(h)
print(b)
b = s.lstrip(' ')
h = len(b)
print(h)

b = s.rstrip(' ')
h = len(b)
print(h)

b = s.lstrip(' ')
h = len(b)
print(h)
print('')
''' khi không ghi phía trước strip thì sẽ 
xóa các kí tự phía trước và phía sau, khi 
không có các kí tự tìm kiếm thì sẽ không thay đổi
'''

#-----==========một số hàm xử lí chuỗi==========-----
print('-----một số hàm xử kí chuỗi-----')
a = '47772984857'
b = 'hhgg'
c = 'AABB'
d = 'JJkv'
e = 'knnkk54768839'

f = a.isnumeric()
print(f)
f = e.isnumeric()
print(f)

g = b.islower()
print(g)
g = d.islower()
print(g)

g = c.isupper()
print(g)
g = d.isupper()
print(g)
print(' ')
#chuyển toàn bộ chuỗi thành viết thường
z = c.lower()
print(z)
z = d.lower()
print(z)
#chuyển toàn bộ thành viết hoa
w = b.upper()
print(w)
w = d.upper()
print(w)
print(' ')

#---------------list--------------
print('-----list-----')
#vd ta có mảng
n = [1, 2, 3, 4, 'A', 'B', 'C']
#có thể lấy các phàn tử trong mảng theo vị trí
print(n[0])
print(n[6])
print(n[-5])
#và khi lấy vị trí không có trong mảng sẽ lỗi
#vị trí 0      1     2      3
v = ['Peter','Ana','Lara','Tomy']
print(v[3])
#ta cũng có thể dùng len để biết số lượng phần tử có trong mảng
print(len(v))
print('  ')

#-----==========kiểm tra sự tồn tại của một phần tử==========-----
print('-----kiểm tra sự tồn tại của một phần tử-----')
#-----------------------------------------------------------------
print('  1)\tKiểm tra theo index')
g = 'look before you leap (LBYL)'
a = 26
if a < len(g):
	print (g[a])
else:
	print('The length of the string is:' + str(len(g)))

h = 'easier to ask forgiveness than permission'
b = 60
try:
	print(h[b])
except IndexError:
	print('không tìm thấy')
print('  ')

#-----------------------------------------------------------------
print('  2)\tKiểm tra theo giá trị')
j = ['not in', 'or', 'in']
print('a' in j)
print('a' not in j)
print('  ')

#-----===========trích xuất mảng con===========-----
#Tương tự chuỗi, có thể tạo mảng con thông qua toán tử lấy khoản
print('-----trích xuất mảng con -----')
test = ['a', '0', 'j', 'i', 'o', 'l', 'e']
print(test[:3])
print(test[1:3])
print(test[4:])
print(test[:-3])
print(test[-2:])
print(test[:19])
print(test[-20:])
print(' ')

#-----==========xóa phần tử của mảng===========-----
print('-----xóa phần tử của mảng------')
print(test)
del test[6]
print(test)
print(' ')
#có thể xóa phần tử dương và âm nằm trong chuỗi, sử dụng giá trị không có trong chuỗi sẽ lỗi
#cũng có thể xóa bằng toán tử lấy khoản

#-----==========nối mảng==========-----
a = ['-----','nối']
b = ['mảng', '-----']
print(a + b)
print('  ')

#-----==========thêm phần tử vào cuối mảng===========-----
print('-----thêm phần tử vào cuối mảng-----')
tyu = [1,4,7,2,56,'ád']
print(tyu)
tyu.append('hiy')
print(tyu)
print('  ')

#-----==========lấy phần tử cuối mảng==========-----
print('-----lấy phần tử cuối mảng-----')
o = tyu.pop()
print(o)
print(' ')

#-----==========tìm một giá trị trong mảng==========-----
print('-----tìm giá trị trong mảng-----')
example = [5,3,8,22,3.4]
print(example.index(3.4))
#khi giá trị không có trong mảng thì chương trình lỗi
#print(example.index(4))
print(' ')

#-----==========đảo ngược giá trị==========-----
print('-----đảo mảng-----')
example.reverse()
print(example)
print(' ')

#-----===========sắp xếp các giá trị==========-----
print('-----sắp xếp-----')
p = ['ghi', '123', 'abc', 'def']
p.sort()
print(p)
h = ['233166111324', 'ghg' , 'tte', 'acb']
h.sort()
print(h)
print(' ')

#---------------tuple----------------
print('-----tuple-----')
#một tuple đã được khai báo rồi thì không thay đổi
yu = ('uyy','sfd','djjdf')
#yu.pop()
#yu[:2]
print(yu)
print('Các giá trị là hằng\n')

#---------------dictionary---------------
print('-----dictionary-----')
#là một cấu trúc mảng, nhưng các phần tử bao gồm key và value
#một dictionary được khai báo bằng cặp ngoặc {...}
r = {'x':'hi', "y":6}
print(r)
print(r['x'])
#khai bào bằng dictionary sẽ gán giá trị của value vào key và muốn in ra
#value thì phải khai báo in key, nếu khai báo in value sẽ gây lỗi
print(' ')

#-----==========thêm phần tử==========-----
print('-----add-----')
k = {'name': 'Cong', 'age':'16'}
k ['country'] = 'Viet Nam'
print(k)
print(' ')

#-----==========một số hàm phương thức thông dụng==========-----
print('-----một số hàm phương thức-----')
e = {'how', 'are', 'you'}
print(e)
e.clear()
print(e)
print(' ')

f = {'c': 9, "yui": 78}
t = f.copy()
f.clear()
print(t)
print(f)
print(' ')

#tạo một đối tượng với danh sách key từ seq và nếu có truyền value thì
#lấy đó làm giá trị cho cho tất cả các phần tử
o = {'ltf','kik','oiu'}
print(o)
i = dict.fromkeys(o)
print(i)
i = dict.fromkeys(o, 9)
print(i)
i = dict.fromkeys(o, 'yy')
print(i)
#-----=====
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

#cập nhật giá trị
value.append(2)
print(vowels)

#-----=====
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)
print(' ')

nyh = {'io':98, 'as': 21}
print(nyh.__contains__('as'))
print(nyh.__contains__('re'))
print(' ')

print(nyh.keys())
#trả về danh sách chứa key
print(nyh.values())
#trả về danh sách chứa value
print(' ')


#==========================PHÂN CHIA MODULE========================
#---------------các loại module/thư viện---------------
'''' có 3 loại module thường thấy:
1// viết bằng python: có phần mở rộng là .py
2// các thư viện liên kết động: có phần mở rộng là .dll, .pyd, .so, .sl, ...
3// C-Mpdule liên kết với trình biên dịch '''

#---------------đường dẫn tìm load module--------------
''' để tải một module vào script: import modulename 
khi gặp biên dịch thì trình biên dịch sẽ tiến hành tìm kiếm file
module tương ứng theo thứ tự thư mục sau:
1.  thư mục hiện hành mà scrip đang gọi
2.  các thư mục trong PYTHONPATH (nếu có set)
3.  các thư mục cài đặt chuẩn trên linux/unix
có thể biết được đường dẫn mà một mofule đac được load bằng đoạn code dưới đây:
'''
print('-----đường dẫn tìm load module-----')
import random
print(random.__file__)
print('')
#---------------lấy danh sách thuộc tính và phương thức của một module---------------
''' để lấy được danh sách căc thuộc tính và phương thức mà module hỗ trợ
 sử dụng hàm  dir(modulename)'''
print('-----lấy danh sách thuộc tính-----')
print(dir(random))
print(' ')

''' có thể gọi hàm dir() lkhoong truyền tham sosos để lấy các thuộc tính và
 phương thức của scope hiện tại đang thực thi
 '''

 #---------------cách khai báo và sử dụng module---------------
'''giả sử bạn tạo một file mymath.py có nội dung:
def cong(a,b)
    return(a+b)
def tru(a,b)
    return(a-b)
def nhan(a,b)
    return(a*b)

#sau đó tạo một file mới vd như myexample.py có nội dung như sau và sau đó chạy chương trình:

import mymath

a = 43
c = 33

print('tong hai so là: ', str(mymath.cong(a, c)))
thì kết quả sẽ in ra 76. Như vậy ta cso thể tự tạo một module và sử dụng nó
điều kiện là nó phải cùng nằm trong một thư mục

#---------------Package module---------------
có thể gom nhiều module .py vào một thư mục và tên thư mục là tên của
package và tạo một file __init__.py trong thư mục

có thể dùng mudule trong thư mục đó bằng cách sau:
import package.module
hoặc 
import package.module as module 
hoặc
import package.module as mod

khi sử dụng một module thuộc một package thì các lệnh trong file
__init__.py sẽ được thực hiện trước. Thông thường file __init__.py sẽ rỗng

Có thể tạo các subpackage bên trong một package theo đúng cấu trúc 
thư mục, có file __init__.py . Ví dụ:

import package.subpackage.subsubpackage.module


#================================CLASS=============================
lập trình hướng đối tượng là một khái niệm thông dụng trong các ngôn ngữ 
lập trình. Python cũng hỗ trợ lập trình hướng đối tượng với các khái niệm
class, object, override, ...

#---------------khai bóa một class-----------------
'''
print('-----khai báo một class-----')
print(' ')
'''cú pháp khai báo:
class myclass([parentclass]):
	assignments
	def __init__(self):
	   statements
	def method():
		statements
	def method2():
		statements

example		
'''
class animal():
	name = ''
	age = 0
	def __init__(self, name = '', age = 0):
		self.name = name
		self.age = age
	def show(self):
		print('My name is', self.name)
		print("I'm ", self.age, ' year old')
	def run (self):
		print('Animal is running...')
	def go(self):
		print('Animal is going...')

class dog(animal):
	def run(self):
		print('Dog is running...')

myanimal = animal()		
myanimal.show()
myanimal.run()
myanimal.go()
print(' ')
mydog = dog('Lucky', 78)
mydog.show()
mydog.run()
mydog.go()
print(' ')


#======================THAO TÁC TRÊN TẬP TIN VÀ THƯ MỤC==================
#---------------tập tin---------------
print('-----tập tin-----')
#-----==========mở file==========-----
print('-----Mở file-----')
'''cú pháp fh = open(filepath, mode)
trong đó: filepath là đường danax của file sẽ mở và mode là chế độ mở:
* r: mở để đọc nội dung (mặc định)
* w: mở để ghi nội dung
* a: mở để ghi thêm nội dung vào cuối file
* r+: mở để ghi. Con trỏ nằm ở đầu file
* w+: mở để đọc và ghi. Ghi đè nếu file đã tồn tại, nếu file chưa tồn tại thì
tạo file mới để ghi
* a+: mở để đọc và thêm vào cuối file. Con trỏ nằm ở cuối file. Nếu file 
chưa tồn tại thì tạo file mới để ghi
  mặc định sẽ mở file text, nếu muốn mở file nhị phân thì thêm b vào trước
mode vd như rb, ab+, ...

Sau khi gọi hàm open()   thành công thì sẽ trả về một object có các thuộc
tính:
* closed: true nếu file đã đóng
* mode: chế độ khi mở file
* name: tên của file
* softspace: cờ đánh dấu softspace khi dùng với hàm print'''
of = open('test.txt', 'r+')
print(of)
print(' ')

#-----==========đọc nội dung từ file==========-----
print('-----đọc nội dung từ file-----')
'''sau khi file đã mở ở chế độ đọc thì gọi phương thức 
read([count]) để trả về toàn bộ nọi dung của file, vd:

f1= open('text.txt', 'r')
fata = f1.read();

hàm read() có nhận một tham số là số lượng byte muốn đọc. Nếu không truyền vào thì
sẽ đọc hết nội dung của file,VD:

f2 = open('log.txt', 'r')
bufdata = f2.read(1024)''' 
yu = of.read()
print(yu)
print(len(yu))
print(" ")

#-----==========ghi nội dung vào file==========-----
print('------ghi nội dung vào file-----')
#điều kiện là file phải mở ở chế độ có thể ghi được
of.write(' attack')
print(' ')

#-----==========tạo file==========-----
new = open('te.txt', 'a+')

#-----==========đóng file đã mở==========-----
print('-----đóng file-----')
of.close()
new.close()
print('')

#-----==========đổi tên file===========-----
print('-----đổi tên-----')
#sử dụng phương thức   os.rename(old, new) để đổi tên:
from os import rename, remove
from time import sleep
sleep(2)
rename('te.txt', 'example.txt')
print('')
 
#-----==========xóa file ==========-----
from os import remove
print('-----xóa-----')
sleep(2)
remove('example.txt')
print('')

#---------------thư mục-----------
print('-----thư mục-----')
#-----==========tạo thư mục==========-----
print('-----tạo thư mục-----')
#vẫn sử dụng phương thức os
from os import mkdir
mkdir('test')
print('')

#-----==========xóa thư mục==========-----
print('------xóa thư mục-----')
from os import rmdir
sleep(2)
rmdir('test')
print('')

#-----===========mở thư mục==========------
print('-----mở thư mục-----')
#vẫn là phương thức os
from os import listdir
gfh = listdir(r"D:\tài liệu\Files code\Code Py\Lesson\__pycache__")
print(gfh)
print('')

#---------------module os---------------
print('-----module os-----')
''' module os là một module vó nhiều phương thức hữu ích trong việc 
làm việc với cấc file và directory, như:
- os.chdir(path): đổi thie mục hiện hành
- os.getcwd(): trả về mục hiện hành
- os.chmod(path, mode): CHMOD một đường dẫn
- os.chmod(path, uid, gid):CHOWD một đường dẫn
- os.makedirs(path[, mode]): tạo đường dẫn (có recursive)
- os.removedirs(path): xóa một đường dẫn (có recursive)
xem thêm: https://docs.python.org/2/library/os.path.html '''
 
 #==========================XỬ LÍ HÌNH ẢNH============================
 #---------------cào đặt PIL---------------
 #---------------mở file---------------
print('-----mở file-----')
from PIL import Image
opp = Image.open(r"C:\Users\hp\Pictures\Bing Images\AABday_ROW7509883666_1920x1080.jpg")
print(opp)
print('')
#sau khi mở thành công thì có thể thao tác trên file im

#---------------ghi file---------------
print('-----ghi file-----')
#từ đối tượng image có thể lưu file xuống máy tính bằng phương thức save(path, type)
opp.save(r'D:\tài liệu\Files code\Code Py\Lesson\mountain.jpg', 'JPEG')
print('')

#---------------tạo thumbnail-----------------
print('------tạo thumbnail-----\n')
opp.thumbnail((1000, 1000))
opp.save(r'D:\tài liệu\Files code\Code Py\Lesson\mountaine.jpg', 'JPEG')
#***************có thể dùng os để xóa file image 
sleep(2)
remove(r'D:\tài liệu\Files code\Code Py\Lesson\mountain.jpg')
sleep(10)
remove(r'D:\tài liệu\Files code\Code Py\Lesson\mountaine.jpg')
#thumbnail không tạo file mới mà chỉ thay đổi kích thước cuẩ file hiện tại

#----------------các thao tác xử lí ảnh---------------
#http://pillow.readthedocs.org/en/latest/index.html

#=========================XỬ LÝ FILE JSON===========================
#---------------load file từ internet---------------
print('-----load file từ internet-----')
''' thồn thường dữ liệu JSON được lấy từ các nguồn khác (như file, internet,...)	
nên chương trình sẽ bắt đầu bằng cách hướng dẫ download file một file JSON từ
internet và sau đó mới parsing(phân tích) nội dung JSON download
  Sử dụng module  urllib2 để download file và module  json để encode/decode JSON data '''
from urllib.request import urlopen
import json
response = urlopen('https://api.github.com/users/voduytuan/repos')
data = json.load(response)
print(data)
print('')
#JSON chỉ dịch được một số loại trang web

#---------------Parsing JSON data---------------
print('-----parsing JOSON-----')
mystring = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
dulieu = json.loads(mystring)
print(dulieu)
print('')

#---------------Encoding JSON data---------------
print('-----encoding json-----')
#Nếu như có một biến và muốn encode thành JSON string thì có thể dùng theo cách sau:
mydata= {
	'name': "Jack",
	'age': 24
}

jsonstring = json.dumps(mydata)
print(jsonstring + str('\n'))

#============================XỬ LÍ FILE XML=============================
'''Trong phần này, chúng ta sẽ parsing nội dung XML thành
dữ liệu để xử lý. Để xử lý XML, ta sẽ sử dụng thư viện
Beautifulsoup 4. Đây là một thư viện giúp việc triển khai
việc parsing html, xml được nhanh chóng và tiện lợi.'''
#---------------cài đặt beautifulsoup--------------------
#---------------cài đặt lml parser -------------------
#---------------ví dụ về parsing XML-------------------
print('-----EX về par XML-----')
from bs4 import BeautifulSoup as Soup 
note = '''
<?xml version="1.0" encoding="UTF-8"?>
<breakfast_menu>
    <food>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>Two of our famous Belgian Waff les with plenty of real maple syrup</description>
        <calories>650</calories>
    </food>
    <food>
        <name>Strawberry Belgian Waffles</name> Belgian Waffles
        <price>$7.95</price>
        <description>Light Belgian waffles covered with strawberries and whipped cream</description>
        <calories>900</calories>
    </food>
</breakfast_menu>
'''
soup = Soup(note, 'xml')
foods = soup.findAll('food')
for x in foods :
	print(x.find('name').string, ': ', x.price.string,'\n \t', x.description.string, "\n") 
'''Trong ví dụ có một số cách truy xuất đến các phần tử như:
 *  findAll() : trả về mảng các thẻ có tên cần tìm
 *  find() : trả về phần tử đầu tiên có tên cần tìm
 *  Truy xuất trực tiếp thông qua tên thẻ như   x.price.string'''

 #---------------parsing HTML---------------
print('-----parsing HTML-----\n')
''' giống nhue xml, BTFS có thể parsing nội dung html thông qua hàm khởi tạo
và chọn html ở tham sô thứ 2 
soup = Soup(websitehtml, 'html') '''

#================================KẾT NỐI MYSQL===========================
