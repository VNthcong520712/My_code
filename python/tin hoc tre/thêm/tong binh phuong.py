r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp")
N = r.readline()
t = 0
if int(N) <= 10**200:
    if len(N) % 2 == 0:
        for i in range(int(len(N)/2)):
            t += int(N[i])**2 + int(N[len(N)-i-1])**2
    else:
        N += "0"
        for i in range(int(len(N)/2)):
            t += int(N[i])**2 + int(N[len(N)-i-1])**2
    print(t)