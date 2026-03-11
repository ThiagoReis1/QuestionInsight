n = int(input("Digite o valor de n: "))
i = 1
soma = 0
sinal = 1
while( i <= 0):
	conta = (i ** 2) / (i + 3)
	soma = conta + soma
	sinal = - sinal
	i = i + 1
print(round(soma, 7))