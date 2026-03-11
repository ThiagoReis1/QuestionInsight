a = input().upper()
c = 0

while a != 'X':
	if a == 'FT':
		c = c + 1
	a = input().upper()
print(c)