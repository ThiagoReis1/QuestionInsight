x = float(input("digite o numero: "))
k = int(input("digite k: "))

i = 1
soma = 0
fim = k - 1
sinal = 1

while((i + 1) <= fim ):
	soma = soma + ((x**i)/i)*sinal
	i = i + 2
	sinal = - sinal
print(round(soma,6))	