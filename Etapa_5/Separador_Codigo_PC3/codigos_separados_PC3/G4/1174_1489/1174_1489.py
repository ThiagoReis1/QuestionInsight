# Leticia Filardi
# Avaliacao 4

n = int (input ("Termos:"))

soma = ((-1) ** 3)/(9 + 3)
i = 1
x = 1
y = 3
e = 0

while (n >= i):
	if (i % 2 == 0):
		soma = soma + e
	else:
		soma = soma - e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 3)/(9 + y)
print( round (soma, 8))