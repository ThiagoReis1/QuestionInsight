armadura = input("Escolha armadura - malha ou placas: ")
destreza = int(input("Digite o valor de 1 a 8: "))
malha = int((15*destreza-1))
placas = int((20*destreza-18))

if (armadura == "malha"):
	print(malha)
else:
	print(placas)