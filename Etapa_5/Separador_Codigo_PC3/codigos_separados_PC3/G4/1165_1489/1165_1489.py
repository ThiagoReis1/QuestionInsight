# Leticia Filardi
# Avaliacao 4

n = int (input ("Termos:"))

soma = (1 ** 3)/(5 + 1)
i = 1
x = 1
y = 1
e = 0

while (n >= i):
	if (i % 2 == 0):
		soma = soma - e
	else:
		soma = soma + e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 3)/(5 + y)
print( round (soma, 9))