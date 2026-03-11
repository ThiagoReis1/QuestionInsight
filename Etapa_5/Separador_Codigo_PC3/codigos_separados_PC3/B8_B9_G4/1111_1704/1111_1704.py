#Universidade Federal do Amazonas - UFAM
#Introducao a Ciencia dos Computadores
#Avaliacao parcial 3
#Allan Bezerra - 21552438

E = float(input("Horas extras: "))
F = float(input("Horas de falta: "))

print("Entradas:", E, "horas extras e ", F, "horas de falta")

if (E<0) or (F<0):
		print("Dados invalidos")
else:
	H = E-(2/3)*F
	if (H <= 600):
		G = 100
	elif (H > 600) and (H <= 1200):
		G = 200
	elif (H > 1200) and (H <= 1800):
		G = 300
	elif (H > 1800) and (H <= 2400):
		G = 400
	elif (H > 2400):
		H = 400
	print("Gratificacao: R$", round(G,2))
