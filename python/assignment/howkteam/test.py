#open file input and output
r = open("D:\\My Documents\\Visual Studio Project\\python\\assignment\\in.txt", "r")
w = open("D:\\My Documents\\Visual Studio Project\\python\\assignment\\out.txt", "w")

#assign values to N and K
N,K = map(int, str(*r.readlines(1)).split())
#assign values to the array
A = list(map(int, str(*r.readlines(2)).split()))


result = []

while len(A) > 0:
    dem = 0
    for i in range(len(A)):
        if A[0] == A[i]:
            dem += 1
    if dem >= K:
        result.append(A[0])
        

    p = A[0]
    for u in range(dem):
        if p in A:
            A.remove(p)
print(*sorted(result), file=w)
