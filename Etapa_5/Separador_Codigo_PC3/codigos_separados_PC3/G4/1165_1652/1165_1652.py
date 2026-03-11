n = int(input("Digite a quantidade de precisao:"))
h = 0
x = 1
j = 1
t = 0
soma = 0
while (n > t):
	valor = ((-1) ** h) * (((x) ** 3) / (5+j))
	soma = soma + valor
	t = t + 1
	x = x + 1
	j = j + 2
	h = h + 1 
print(round(soma, 9))