n = int(input())
a = []
for i in range(1, n+1):
	a.append(int(input()))
def fibo(a):
	if a < 1:
		return 1
	return (fibo(a-1) + fibo(a-2))%(10^9+7)
for i in range(0, n):
	print(fibo(a[i]))