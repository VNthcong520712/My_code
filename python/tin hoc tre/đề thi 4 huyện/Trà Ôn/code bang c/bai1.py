r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\in.inp", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\đề thi 4 huyện\\Trà Ôn\\code bang c\\ou.out", "w")

n = int(r.readline())

# ca a an duoc
if n == 1:
    ta = 2
elif n == 2:
    ta = 6
else:
    pna = n//3
    pda = n%3
    ta = pna*(2*9+(pna-1)*9)/2
    if pda == 1:
        ta += n+1
    elif pda == 2:
        ta += n
        ta += n+2

# ca b an duoc
if n == 1:
    tb = 3
else:
    pnb = n//2
    pdb = n%2
    tb = pnb*(2*5+(pnb-1)*4)/2
    if pdb == 1:
        tb += n+2
hs = int(ta-tb)
if hs < 0:
    print("B", abs(hs), file=w)
elif hs > 0:
    print("A", hs, file=w)
else:
    print("C", int(ta), file=w)