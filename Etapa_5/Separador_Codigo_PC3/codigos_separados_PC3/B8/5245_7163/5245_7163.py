sal = float(input("Entrada: R$ "))

if (sal >= 0):
	print("Entrada: R$",sal)
	if (sal >=1) and (sal <= 800):
		n_sal = sal + (sal * 0.50)
		print("Novo salario: R$",round(n_sal,2))
	elif (sal > 800) and (sal <= 1000):
		n_sal = sal + (sal * 0.40)
		print("Novo salario: R$",round(n_sal,2))
	elif (sal > 1000) and (sal <= 1200):
		n_sal = sal + (sal * 0.30)
		print("Novo salario: R$",round(n_sal,2))
	elif (sal > 1200) and (sal <= 1400):
		n_sal = sal + (sal * 0.20)
		print("Novo salario: R$",round(n_sal,2))
	elif (sal > 1400) and (sal <= 1600):
		n_sal = sal + (sal * 0.10)
		print("Novo salario: R$",round(n_sal,2))
	elif (sal > 1600):
		n_sal = sal + (sal * 0.05)
		print("Novo salario: R$",round(n_sal,2))
else:
	print("Entrada: R$ ",sal)
	print("Dado invalido")
	