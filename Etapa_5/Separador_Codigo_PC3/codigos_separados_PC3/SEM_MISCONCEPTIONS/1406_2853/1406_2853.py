extras = float(input("Horas extras: "))
faltas = float(input("Horas faltadas: "))

H = float(extras - (3 * faltas / 5))

if (H >= 180):
	print(str(extras) + " extras e " + str(faltas) + " de falta")
	gratificacao = float(200)
	print("R$ " + str(round(gratificacao, 2)))
else:
	print(str(extras) + " extras e " + str(faltas) + " de falta")
	gratificacao = float(100)
	print("R$ " + str(round(gratificacao, 2)))