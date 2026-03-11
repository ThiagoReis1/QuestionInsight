ataque = str(input("Nome do ataque: "))
d1 = int(input("Valor do Dado 1: "))
d2 = int(input("Valor do Dado 2: "))
if ataque == "grito":
	dano = (d1 + d2) + 6
if ataque == "toque":
	dano = (d1 + d2)**2
print(dano)