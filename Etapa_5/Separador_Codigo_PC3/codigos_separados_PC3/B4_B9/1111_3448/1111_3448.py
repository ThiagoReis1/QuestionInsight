hextra = float(input("Informe o Numero de Horas extras"))
faltas = float(input("Informe as Faltas"))

h = hextra - (0.60 * faltas)
 
if (h <= 600):
	g = 100
	print("Entradas:", hextra, "horas extras e", faltas, "horas de falta")
	print("Gratificacao: R$", round(g, 2))
elif (h > 600) and (h <= 1200): 
	g = 200
	print("Entradas:", hextra, "horas extras e", faltas, "horas de falta")
	print("Gratificacao: R$", round(g, 2))
elif (h > 1200) and (h <= 1800):
	print("Entradas:", hextra, "horas extras e", faltas, "horas de falta")
	print("Gratificacao: R$", round(g, 2))
elif (h > 1800) and (h <= 2400):
	print("Entradas:", hextra, "horas extras e", faltas, "horas de falta")
	print("Gratificacao: R$", round(g, 2))
elif (h > 2400):
	print("Entradas:", hextra, "horas extras e", faltas, "horas de falta")
	print("Gratificacao: R$", round(g, 2))
else:
	print("Dados invalidos")