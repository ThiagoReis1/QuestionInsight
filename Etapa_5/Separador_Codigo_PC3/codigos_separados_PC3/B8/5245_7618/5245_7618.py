salario=float(input("digite o salario= "))


if salario >= 0:
	if salario == 800:
		total= salario + (salario * 0.50)
		print(round(total,2))
	elif salario > 800 or salario >=1000:
		total= salario + (salario * 0.40)
		print(round(total,2))
	elif salario > 1000 or salario >= 1200:
		total= salario + (salario * 0.30)
		print(round(total,2))
	elif salario > 1200 or salario  >= 1400:
		total= salario + (salario * 0.20)
		print(round(total,2))
	elif salario > 1400 or salario >= 1600:
		total=salario + (salario * 0.10)
		print(round(total,2))
	elif salario > 1600:
		total=salario + (salario * 0.05)
		print(round(total,2))
else:
	print("Novo salario: R$",total)