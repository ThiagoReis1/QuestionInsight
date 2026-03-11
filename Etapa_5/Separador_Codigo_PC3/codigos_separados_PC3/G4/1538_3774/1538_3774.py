x = float(input("Informe o valor de x: "))
k = int(input("Informe a quantidade de termos: "))

i = 0
soma = 0
sinal = 1


while(i < k):
	soma = soma + sinal *  (x ** (2*i))
	i = i + 1
	sinal = sinal * -1
print(round(soma, 8))