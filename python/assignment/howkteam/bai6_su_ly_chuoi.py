#su_ly_chuoi.py



print("nnhjsafhj\ndagf")
#chuỗi trần sẽ sửa các escape sequence
print(r"sasgdsags\nádsfg")



#cộng chuỗi
tra = "đágađga"
trb = "ấgsdgsdgfg"
trc = tra+ '\t' + trb
print(trc)



#lập chuỗi với số lần
trd = (tra + '\t')*5
print(trd)



#kiểm tra một chuỗi có trìn chuỗi khác không và sẽ trả về true hoặc false
tre = 't'
trf = tre in tra
print(trf)



#các kí tự trong chuỗi có vị trí từ 0 đến n-1 với n là số kí tự trong chuỗi
#lấy kí tự vị trí a
#vd lấy vị trí 0 trong tre
trg = tre[0]
print(trg)
#truy cập phần tử cuối cùng trong tra
print (tra[len(tra)-1])



#cắt chuỗi trái qua phải
print(" ")
tra = "nhfuvfjgkuhgbgyt"
print(tra[3:len(tra)])
print(tra[3:None])
#cắt chuỗi phải qua trái
trm = 'hoc lap trinh'
print(trm[None:7:2])#phải qua trái tính từ vị trí 7
print(trm[None:7:-2])#phải qua trái tính từ gnoaif cùng đến 7


#ép kiểu
#ép chuỗi 67 thành số
tri = int('67')+5
print(tri)

tri = float('67.776')+5
print(tri)

tri = int(67.554) 
print(tri)

#số thành chuỗi
tro = str(67) + '5'
print(tro)

#thay đổi kí tựu trong chuỗi
trw = "diduduadi"
trw = trw[0] + "0" + trw[2:None]
print(trw)