def loga(n):
    if n < 0:
        return -1
    else:
        if n >= 2:
            return 1 + loga(n/2)
        else:
            return 0
print(loga(6988))