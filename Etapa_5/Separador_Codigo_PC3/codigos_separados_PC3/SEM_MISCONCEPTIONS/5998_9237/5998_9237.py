# maça unidade = 0.30 if < 12
# maça unidade = 0.25 if >=12

M = int(input("Macas compradas: "))

if M < 12:
	Valor = (M * 0.30)
	print(round(Valor, 2))
	
else:
	Valor = (M * 0.25)
	print(round(Valor, 2))