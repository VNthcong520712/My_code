#định dạng chuỗi
a = "my team is %s"
print(a)
a = "my team is %s"%("kteam")
print(a)
#có tao nhiêu % thì cần báy nhiêu giá trị truyền vào và các giá trị truyền vào cách nhau bởi dấu phẩy
a = "my team is %s %s"%("kteam", "26")
print(a)
a = "my team is %s %s"
print(a %("kteam", "26"))
a = "my team is %s %s" 
b = a %("kteam", "26")
print(a)
"""
%s giá trị của phương thức_str_của đối tượng đó
%r giá trị của phương thức_repr_của đối tượng đó
%d giá trị của một số-nếu là số thực thì chỉ lấy phần nguyên 
%<số chữ số thập phân>f giá trị của một số-nếu là số sẽ được chuyển sang số thực
"""
#kiểu danh sách (list)
a = "%s" % ([1,3,5])
print(a)

f = '%f'%(3.776599)
print(f)
#làm tròn
f = '%.3f'%(3.776599)
print(f)
f = '%.f'%(3.776599)
print(f)
print("    ")


#định dạng chuỗi f-string
k = 'kteam'
r = '{k} - free educcation'
print(r)
r = f'{k} - free educcation'
print(r)
print("  ")


#nếu có nhiều giá trị có cấu tọa {} trong một chuỗi mà muốn thya thế một
#giá trị trong chuỗi đó thì chỉ cần bao các giá trị không thay thế bằng
#2 lớp ngoặc nhọn
d = f'{{efic}}, {{frd}}, {k}'
print(d) 
print('        ')





#định dạng phươn thức format
p = 'a: {}, b: {}, c: {}'.format(1,2,3)
print(p)
#thay thế theo thứ tự
i = 'a = {1}, b = {0} '.format('one','two')
print (i)
# trong format các giá trị sẽ có thứ tự là 0, 1, 2, 3, ... và nó sẽ thay
# thế tương ứng vào các giá trị 0, 1, 2 ở chuỗi phía trước

o = '1: {one}, 2: {two} '.format(one=111, two=222)
print(o)

#căn lề công thức {:C[</>/^]n}.format(kí tự dược căn), nếu c để tróng thì sẽ là
#dấu cách 
u = '{:*^40}'.format('cong')
print(u)