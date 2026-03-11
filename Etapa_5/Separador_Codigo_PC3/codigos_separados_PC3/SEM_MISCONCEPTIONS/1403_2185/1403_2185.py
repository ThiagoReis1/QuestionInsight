from math import *
nome_armadura = input("malha ou placa : ")
fator = int(input("fator de destreza :"))

malha = (15 * fator) - 1
placas = (20 * fator) - 18

if (nome_armadura == "malha"):
	print(malha)
else:
	print(placas)
