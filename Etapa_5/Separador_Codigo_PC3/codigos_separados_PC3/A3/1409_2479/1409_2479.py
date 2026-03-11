ataque = str(input("Tipo de ataque: "))
sor1 = int(input("Valor sorteado: "))
sor2 = int(input("Valor sorteado: "))
sor3 = int(input("Valor sorteado: "))
sor4 = int(input("Valor sorteado: "))
N = sor1+sor2+sor3+sor4
if (ataque.lower() == "espada"):
	sor_1 = (sor1+6)
	sor_2 = (sor2+6)
	sor_3 = (sor3+6)
	sor_4 = (sor4+6)
	N = sor_1+sor_2+sor_3+sor_4
	espada = (N)
	print(espada)
	
else:
	cauda = (sor1 + sor2 + sor3)*sor4
	print(cauda)
	