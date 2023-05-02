inp = input().split()
bp = []

for i in range(len(inp)):
    if inp[i] == '+':
        bp[0] = int(inp[i-1]) + int(inp[i-2])