N = int(input("Digite o número de termos:"))
S = (-1) ** (-3) / (9 + 3)
i = 1
x = 1
y = 3
e = 0

while ( N >= i):
	if (i% 2 == 0):
		S = S + e
	else:
		S = S - e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 3)/(9 + y)
print(round(S, 8))
