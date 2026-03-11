from math import*
x = eval(input("Angulo: "))
k = int(input("qtd termos: "))

soma = 0
i = 0
g = 0

while(g < k):
	soma = soma + ((-1)**g) * ((x**i)/factorial(i))
	i = i + 2
	g = g + 1
print(round(soma , 10))