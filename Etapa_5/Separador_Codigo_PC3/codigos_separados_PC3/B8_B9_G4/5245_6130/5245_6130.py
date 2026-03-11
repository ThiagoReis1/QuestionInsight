s =  float(input("salario: "))

if (s < 0):
	print("Dado invalido")
elif (s <= 800):
	t = s * 0.50 + s
	print("Novo salario: R$",round(t, 2))
elif (s > 800) and (s <= 1000):
	t = s * 0.40 + s
	print("Novo salario: R$",round(t, 2))
elif (s > 1000) and (s <= 1200):
	t = s * 0.30 + s
	print("Novo salario: R$",round(t, 2))
elif (s > 1200) and (s <= 1400):
	t = s * 0.20 + s
	print("Novo salario: R$",round(t, 2))
elif (s > 1400) and (s <= 1600):
	t = s * 0.10 + s
	print("Novo salario: R$",round(t, 2))
elif (s > 1600):
	t = s * 0.05 + s
	print("Novo salario: R$", round(t, 2))