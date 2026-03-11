n = int(input("Digite um numero: "))
a = 0
s = 0
i = 3
b = 1
sinal = 1 

while(a < n):
	s = s + (b ** 3) / (5 + 1) * sinal
	i = i + 1
	b = b + 2
	sinal = sinal * -1
	a = b + 1
print(round(s, 9))	