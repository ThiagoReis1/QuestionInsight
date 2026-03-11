produto = input().upper()

i = 0
h = 0
l = 0
e = 0
total = 0

while i < len(produto):
	if produto[i] == 'H':
		h += 3.85
	elif produto[i] == 'L':
		l += 2.95
	elif produto[i] == 'E':
		e += 7.90
		
	i += 1
total = h + l + e
print(round(total, 2))
		
		