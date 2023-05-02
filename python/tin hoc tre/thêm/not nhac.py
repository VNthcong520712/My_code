r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\thêm\\in.inp")
tone = r.readline()
tone = [i.upper() for i in tone if i in 'CDEFGBA']
sl = []

if len(tone) <= 10**6 :
    sx = sorted(list(set(tone)))
    max_ = 0
    max_i = 0
    for i in sx:
        if tone.count(i) >= max_:
            max_ = tone.count(i)
            max_i = i
    print(max_i, max_)