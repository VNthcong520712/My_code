print("     tính tiền điện trong 12 tháng     ")

dstd = []
tong = 0

for i in range(12):
    a = float(input(f"nhập tiền điện tháng {i+1}: "))
    tong = tong + a
    dstd.append(a)

trb = tong/12

dnh = []

for n in range(12):
    if dstd[n] > trb:
       dnh.append(n+1)
print(f"tổng tiền điện dùng cả năm là {tong}, trung bình mỗi tháng là {trb:.5f} \ncác tháng " + str(dnh)[1:-1] + " dùng nhiều hơn trung bình") 