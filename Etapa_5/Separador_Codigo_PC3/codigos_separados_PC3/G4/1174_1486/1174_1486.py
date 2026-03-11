n = int(input("Termos:"))

s = ((-1) ** (-3) / (9 + 3))
i = 1
x = 1
y = 3
e = 0

while ( n >= i):
	if (i% 2 == 0):
		s = s + e
	else:
		s = s - e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 3)/(9 + y)
print(round(s, 8))