while 1:
	dat = input().split()
	out = ''
	for i in dat:
		a = i.lower()
		a = a[0].upper() + a[1:]
		out += a + " "
	print(out)