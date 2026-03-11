r = float(input(""))
k = int(input(""))

soma = 0
i = 1
sinal = 1

while (i < k):
	s = soma + sinal * (1 - r ** 2)
	i = i + 1
	sinal = - sinal
	
print(round(s, 8))