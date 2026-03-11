st = input().upper()

i = 0
total = 0
cl = 0
cm = 0
cs = 0

while i < len(st):
	if st[i] == 'I':
		cl = cl + 1
		total = total + 3.75
	elif st[i] == 'M':
		cm = cm + 1
		total = total + 4.5
	elif st[i] == 'S':
		cs = cs + 1
		total = total + 2.9
	i = i + 1
print(round(total, 2), cl, cm, cs)