deposito = float(input("Digite o valor: "))
n = int(input("Digite o numero de meses: "))
i = 0
total = deposito
while (i < n):
	total = ((1.2 /100) * total  + total )
	i = i + 1
	print(round(total,2))
