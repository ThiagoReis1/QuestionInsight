s = float(input("Salario atual: "))

if s >= 0:
	if s <= 800:
		ns = s + ((50/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
	elif 800 < s <= 1000:
		ns = s + ((40/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
	elif 1000 < s <= 1200:
		ns = s + ((30/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
	elif 1200 < s <= 1400:
		ns = s + ((20/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
	elif 1400 < s <= 1600:
		ns = s + ((10/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
	else:
		ns = s + ((5/100)*s)
		print("Entrada: R$ ", s)
		print("Novo salario: R$", round(ns, 2))
else:
	print("Entrada: R$ ", s)
	print("Dado invalido")