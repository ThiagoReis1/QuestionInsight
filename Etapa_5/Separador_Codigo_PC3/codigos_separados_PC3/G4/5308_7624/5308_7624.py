x = float(input("digite o numero: "))
k = int(input("digite o valor de k: "))

cont = 0
i = 1
y = 0
soma = 0

while (cont < k):
	soma = soma + i / (y * x)
	cont = cont + 1
	i = i + 1
	y = y + 2
print(round(soma, 10))