quantidade = float(input())
com_desconto = 0.60
sem_desconto = 0.75

if quantidade < 6:
	total = quantidade * sem_desconto
	print(total)
else:
	total = com_desconto * quantidade
	print(total)