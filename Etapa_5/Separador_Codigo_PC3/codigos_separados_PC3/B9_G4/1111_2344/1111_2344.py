E= float(input("Digite o numero de horas extras trabalhadas:"))
F= float(input("Digite o numero de horas de falta:"))

print("Entradas:", round(E,2), "horas extras e", round(F,1), "horas de falta")

H= ((E - 2/3 * F))

if (E < 0 or F < 0):
	print("Dados invalidos")
else:
	if (H > 2400):
		G= 500.00
	elif (H > 1800 and H <= 2400):
		G= 400.00
	elif (H > 1200 and H <= 1800):
		G= 300.00
	elif (H > 600 and H <= 1200):
		G= 200.00
	else:
		G= 100.00
	print("Gratificacao: R$", round(G,2))
