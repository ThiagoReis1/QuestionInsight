op = input().upper()
qop = int(input())
qa = int(input())

if op == 'T':
	op = 4.50
	total = (qop*op) + (qa*12)
	print(round(total,2))
else:
	op = 5
	total = (qop*op) + (qa*12)
	print(round(total,2))