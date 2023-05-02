n, m = map(int, input().split())
doan_khach = [int(x) for x in input().split()]  

dsp = [0 for x in range(n)]
dck = 0
for i in range(m):
    pd = doan_khach[i] % 2
    pn = doan_khach[i] // 2
    for j in range(doan_khach[i]):
        if dck < n:
            if pn > 0:
                dsp[dck] = 2
                pn -= 1
                dck += 1
            elif pd != 0:
                dsp[dck] = 1
                pd -= 1
                dck += 1
            else: break
        if dck >= n:
            t = 0
            conlai = pn*2 + pd
            for z in range(len(dsp)):
                if dsp[z] == 1 and conlai > 0:
                    dsp[z] += 1
                    conlai -= 1
                else:
                    t = 1
            if t == 1: break
print(dsp)