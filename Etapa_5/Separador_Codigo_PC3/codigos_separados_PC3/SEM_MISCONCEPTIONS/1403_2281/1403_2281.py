n = input("nome da armadura: ")
dex = int(input("D8 = "))

malha = 15*dex -1
placas = 20*dex - 18

if (n == "malha"):
	print(malha)
else:
	print(placas)