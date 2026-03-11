# Isabela C Pereira - 21602331

n = int(input("Digite o valor dos termos: "))

x = 1
h = 6
f = 1
i = 0

while (n == i):
	if (x % 2 != 0):
		s = sqrt(x)/(h + f)
	else:
		s = - (sqrt(x)/(h + f))

	x = x + 1
	f = f + 2
	i = i + 1
print(round(s, 10))