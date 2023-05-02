r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp", "r")
n = int(r.readline())
t = r.readline()
S = [x.lower() for x in t]

def all_(l):
    ou = 0
    if len(l) %2 != 0:
        l.append(l[0])
    for i in range(int(len(l)/2)):
        if l[i] == l[i+int(len(l)/2)] and l[i] == l[0]:
            ou = True
        else: 
            ou = False
            break
    return ou
    
for i in range(len(S)-n+1):
    if all_(S[i:i+n]) == True:
        print(i+1, str(t[i:i+n]))