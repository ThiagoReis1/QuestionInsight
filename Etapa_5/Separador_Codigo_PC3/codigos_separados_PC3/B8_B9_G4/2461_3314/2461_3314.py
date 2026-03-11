p=float(input("Digite o valor do preco de custo: "))
if (p <= 50.00):
	l = p + p
	print(round(l,2))
elif (p > 50.00) and (p <= 100.00):
	l = p + p/2
	print(round(l,2))
elif (p > 100.00) and (p <= 500.00):
	l = p + (p*0.4)
	print(round(l,2))
elif (p > 500.00):
	l = p + (p*0.3)
	print(round(l,2))