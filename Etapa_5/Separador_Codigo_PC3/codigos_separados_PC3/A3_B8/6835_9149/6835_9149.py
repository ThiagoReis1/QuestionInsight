produtos = input().upper()

i = 0 
b = 0
c = 0
e = 0
total = 0

while i < len(produtos):
	if produtos[i] == 'B':
		b += 3.75
	elif produtos[i] == 'C':
		c += 7.90
	elif produtos[i] == 'E':
		e += 9.85
		
	i += 1
total = b + c + e

print(round(total, 2))