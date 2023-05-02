r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\ou.out", "w")

n = int(r.readline())
S = str(r.readline()).strip()

dai = len(S)
dem = 0
chuoi = []

# if n%2 == 0:
#     kc = n-1
#     for c in range(dai-int(n/2)):
#         if c+kc > dai-1:
#             break
#         elif  S[c].lower() == S[c+kc].lower():
#             kc -= 2
#         else: kc = n-1

#         if kc <= 0:
#             dem += 1
#             dau = c + 1 - int(n/2)
#             cuoi = c + 1 + int(n/2)
#             chuoi.append(S[dau:cuoi])
#             kc = n-1
# else:
#     g = n - 1
#     for k in range(dai-int(n/2)):
#         if k+g > dai-1:
#             break
#         elif  S[k].lower() == S[k+g].lower():
#             g -= 2
#         else: g = n - 1

#         if g == 0:
#             dem += 1
#             dau = k + 1 - int(n/2)
#             cuoi = k + 2 + int(n/2)
#             chuoi.append(S[dau:cuoi])
#             g = n - 1


# w.write(str(dem) + "\n")
# for i in chuoi:
#     w.write(i + "\n")

# for i in range(dai - n + 1):
#     chuoi_phu = S[i:i + n]

#     dau = chuoi_phu[:n // 2]
#     duoi = chuoi_phu[n // 2 + n % 2:]
#     if dau == duoi[::-1]:
#         dem += 1

#         chuoi.append(chuoi_phu)

# print(dem)
# print(chuoi)