armadura = str(input("malha ou placas: "))
fator = int(input("valor entre 1 e 8: "))


if(armadura == malha):
	resistencia = 15*fator - 1
else:
	resistencia = 20*fator - 18
	print(resistencia)