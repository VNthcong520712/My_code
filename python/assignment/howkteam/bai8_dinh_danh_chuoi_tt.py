#muốn sử dụng hàm hoặc thuộc tính gì đó cho giá trị thì <giá trị>.<tên hàm/thuộc tính>
#vd hàm capitalize() chỉ viết hoa chữ đầu tiên
a = "hey bro"
b = a.capitalize()
print(b)
a = "do YOU NKOW MY father"
b = a.capitalize()
print(b)

#viết hoa tất cả
b = a.upper()
print(b)

#viết thường
b = a.lower()
print(b)

#hoa thường đổi chỗ
b = a.swapcase()
print(b)

#in hoa chũ cái đầu
b = a.title()
print(b)

#căn giữa với giá trị width bằng một kí tự fillchar
#b = a.center(width,[fillchar])
b = a.center(30)
print(b)

#căn phải 
b = a.rjust(40,'-')
print(b)

#căn trái
b = a.ljust(40,'=')
print(b)

#mã hóa theo chuẩn, có thể dùng mã hóa các ngôn ngữ khác
a = 'có gì hót\n'
b = a.encode()
print(b)

#phương thức join
b = a.join(['1\t','2\t','3\t','4\t'])
print(b)

#phương thức replace
b = a.replace('\n',' không')
print(b)
b = a.replace('ó','không', 2)
print(b)
print('           ')


#phương thức strip, bỏ đi kí tự char ở hai đầu
a = 'cbcbcbhellocb'
b = a.strip('cb')
print(b)
#cắt trái thì lstrip cắt phải thì rstrip



