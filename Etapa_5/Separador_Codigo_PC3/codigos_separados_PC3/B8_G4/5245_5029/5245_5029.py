s = float(input("Salario: "))

if (s < 0) :
	print("Dado invalido")
elif (s <= 800.00) :
	x = (s*50)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)
elif (s > 800.001 and s <= 1000.00) :
	x = (s*40)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)
elif (s > 1000.01 and s <= 1200.00) :
	x = (s*30)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)
elif (s > 1200.01 and s <= 1400.00) :
	x = (s*20)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)
elif (s > 1400.01 and s <= 1600.00) :
	x = (s*10)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)
elif (s > 1600.01) :
	x = (s*5)/100
	y = s+x
	y = round(y,2)
	print("Novo salario: R$", y)