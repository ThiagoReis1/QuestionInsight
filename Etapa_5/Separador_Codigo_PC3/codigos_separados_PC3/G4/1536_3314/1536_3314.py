x = float(input("Digite o valor de x: "))
k = int(input("Digite o numero de termos de k: "))
soma = 0
i = 0
while(i < k):
	soma = soma + ((-1)**i) * (x**i)/(i+1)
	i = i + 1
print(round(soma,10))

