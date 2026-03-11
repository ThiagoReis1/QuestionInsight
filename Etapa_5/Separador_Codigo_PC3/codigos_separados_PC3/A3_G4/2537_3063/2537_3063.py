v = float(input("digite o valor do premio: "))
m = float(input("digite o valor de saque mensal: "))
j = float(input("digite a taxa de juros mensal: "))

x = j / 100
soma = v
i = 0

if(v<=0)and(m<=0)and(j<=0):
	print("Dados incorretos")
else:
	while(v >= v + v * 0.2):
		soma = soma - m
		y = soma+(soma*j)
		i = i + 1
		print(round(i,2))