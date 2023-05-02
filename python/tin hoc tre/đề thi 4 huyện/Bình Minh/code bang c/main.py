inp = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Minh\\code bang c\\in.inp", "r")
out = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Bình Minh\\code bang c\\out.out", "w")

# lay toan bo dong trong file inp
ff = inp.readlines()

# lay tung dong va chay chuong trinh
for i in range(len(ff)):
    # gan bien phu bang dong dau tien
    pp = str(ff[i])
    if len(pp) == 1:
        out.write(pp + "\n")
    else:
        # gan bien phu 2 bang viet thuong cac chu cai
        pf = pp.lower() 
        # khoi tao bien dem so lan lap cua ki tu
        dem = 1
        # khoi tao danh sach luu do dai cua ki tu va vi tri cuoi cua ki tu
        dai = []
        cuoi = []
        # cho i chay tung gia tri tron bien phu 2 de dem so lan xuat hien cua ki tu
        for i in range(1, len(pf)):
            if pf[i] == pf[i - 1]: # neu ki tu hien tai bang ki tu truoc thi tang bien dem len 1
                dem += 1
                f = 1 # dung khi i di den gioi han cuoi cua chuoi va khong duoc gan trong lenh else
            else: # them dem vao dai, vi tri cuoi vao cuoi, reset lai bien dem
                f = 0
                dai.append(dem)
                cuoi.append(i-1)
                dem = 1

        if f == 1: # neu i di den gioi han cuoi cua chuoi va khong duoc gan trong lenh else thi lenh nay thay the de gan vao danh sach
            dai.append(dem)
            cuoi.append(len(pf)-1)
        max_ = max(dai) # tim max trong danh sach dai

        for i in range(len(dai)): # tim vi tri cua max trong danh sach dai
            if dai[i] == max_:
                vt = i
                break

        gtc = cuoi[vt] + 1
        gtd = gtc - max_
        out.write(pp[gtd:gtc] + "\n") # in ra kq