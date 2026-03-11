nome = input("nome da armadura:")
fator = int(input("fator de destreza:"))
placas = (20*fator)-18
malha = (15*fator)-1
if (nome=="malha"):
	print(malha)
else:
	print(placas)
