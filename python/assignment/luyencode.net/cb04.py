a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(f"{a/b:.2f}") if b!= 0 else print("INF")