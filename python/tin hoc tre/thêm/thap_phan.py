from decimal import Decimal, getcontext
getcontext().prec = 100

r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\ou.out", "w") 

P, Q = map(int, r.readline().split())

frac = Decimal(P)/Decimal(Q)
pll = ""
print(frac)
ptp = str(frac)[str(frac).find(".")+1:]

dau = 0

if P < 10**5 and Q < 10**5:
    while dau < len(ptp)/4:
        for i in range(dau+1,len(ptp)):
            if ptp[i] == ptp[dau]:
                slb = 1
                for a in range(1, i-dau):
                    if ptp[dau+a] == ptp[i+a]:
                        slb += 1
                    else: break
                if slb == i-dau:
                    pll = ptp[dau:i]
                    break
        dau += 1
        if dau == len(ptp)/4:
            pll = ptp
            break

print(pll)