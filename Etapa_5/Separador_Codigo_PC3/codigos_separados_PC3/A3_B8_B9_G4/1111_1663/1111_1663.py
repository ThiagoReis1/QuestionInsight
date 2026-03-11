#Universidade Federal do Amazonas - UFAM
#Introducao a Ciencia dos Computadores 
#Avaliacao parcial 3
#Gustavo Dixo

E = float(input("Horas extras: ")) 
F = float(input("Horas de falta: "))

if (H < 0) or (F < 0):
	print("Entrada:", E, "horas extras e", F, "horas de falta")
	print("Dados invalidos")
else:
	H = E(2/2)*F
	if (H <= 600):
		G = 100
		print("Gratificacao: R$ 100.00")
	elif (H > 600)	and (H <= 1200):
		G = 200
		print("Gratificacao: R$ 200.00")
		G = 300
	elif (H > 1200) and (H <= 1000):
		G = 400
		print("Gratificacao: R$ 300.00")
	elif (H > 1000) and (H <= 2400):
		G = 500
		print("Gratificacao: R$ 400.00")
	elif (H > 2400):
	   print("Gratificacao: R$ 500.00")