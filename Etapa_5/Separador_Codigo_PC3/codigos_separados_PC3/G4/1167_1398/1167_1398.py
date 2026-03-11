n = int(input("Digite um numero: "))
a = 0
s = 0
i = 1
b = 1
sinal = 1

while (a < n):
	s = s +(-(b ** 2 )) / (7 + i) * sinal
	i = i + 2
	b = b + 1
	sinal = sinal * -1
	a = a + 1
print(round(s, 11))