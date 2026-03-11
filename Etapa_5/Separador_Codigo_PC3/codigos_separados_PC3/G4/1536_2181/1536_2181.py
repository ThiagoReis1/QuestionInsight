x = int(input("Digite um numero: "))
k = int(input("Digite a quantidade de termos: "))

soma = 1
n = 2
i = 1

while	(i < k):
	soma = soma + ((x ** n) / n) * (-1)**(i)
	n = n + 1
	i = i + 1
print(round(soma, 10))