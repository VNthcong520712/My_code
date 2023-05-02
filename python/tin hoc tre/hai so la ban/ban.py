r = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\hai so la ban\\vao.int", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\tin hoc tre\\hai so la ban\\ra.out", "w")


n1, n2= map(int, str(*r.readlines(1)).split())

tu1 = 0
tu2 = 0

def tonguoc(a):
    tu = 0
    for i in range(1, a):
        if a%i == 0:
            tu += i
    return tu

tu1 = tonguoc(n1)
tu2 = tonguoc(n2)

if (tu1 == n2 and tu2 == n1) and n1 != n2:
    w.write("{} {}".format(n1, n2))
r.close()