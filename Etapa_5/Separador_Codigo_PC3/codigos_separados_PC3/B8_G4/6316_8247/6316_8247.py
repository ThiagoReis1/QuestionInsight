st = input().upper()
d = 0
s = 0 
i = 0
total = 0
r = 0
while r < len(st):
	if st[r] == 'D':
		total = total + 2.25
		d = d + 1
	elif st[r] == 'S':
		total = total + 4
		s = s + 1
	elif st[r] == 'I':
		total = total + 6.9
		i = i + 1
	r = r + 1
print(round(total, 2), d, s, i)