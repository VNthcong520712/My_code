s = "9"*100+"A"*100+"1"*100+"c"*100+"a"*100

s = sorted(s)
s1 = s2 = s3 = ""
for i in s:
    if i.isnumeric(): s3+= i
    elif i.isupper(): s2+= i
    elif i.islower(): s1+= i

print(s1, len(s1))
print(s2, len(s2))
print(s3[::-1], len(s3))