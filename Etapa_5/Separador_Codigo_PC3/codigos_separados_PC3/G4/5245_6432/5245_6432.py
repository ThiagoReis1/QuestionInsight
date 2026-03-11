sl = float(input(""))

if ((sl <= 800) and (sl >= 0)):
	x = (sl * (50/100)) + sl
	print("Novo salario: R$", round(x,2))
elif ((sl > 800) and (sl <= 1000)):
	x = (sl * (40/100)) + sl
	print("Novo salario: R$", round(x,2))
elif ((sl > 1000) and (sl <= 1200)):
	x = (sl * (30/100)) + sl
	print("Novo salario: R$", round(x,2))
elif ((sl > 1200) and (sl <= 1400)):
	x = (sl * (20/100)) + sl
	print("Novo salario: R$", round(x,2))
elif ((sl > 1400) and (sl <= 1600)):
	x = (sl * (10/100)) + sl
	print("Novo salario: R$", round(x,2))
elif (sl > 1600):
	x = (sl * (5/100)) + sl
	print("Novo salario: R$", round(x,2))
else:
	print("Dado invalido")

