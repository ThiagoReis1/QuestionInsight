sl = float(input(""))
if (sl < 0):
	ns = "Dado invalido"
	print(ns)
else:
	if (sl <= 800):
		ns = sl + (50 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))
	elif (sl > 800) and (sl <= 1000):
		ns = sl + (40 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))
	elif (sl > 1000) and (sl <= 1200):
		ns = sl + (30 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))
	elif (sl > 1200) and (sl <= 1400):
		ns = sl + (20 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))
	elif (sl > 1400) and (sl <= 1600):
		ns = sl + (10 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))
	else:
		ns = sl + (5 / 100 * sl)
		print("Novo salario: R$ ", round(ns,2))