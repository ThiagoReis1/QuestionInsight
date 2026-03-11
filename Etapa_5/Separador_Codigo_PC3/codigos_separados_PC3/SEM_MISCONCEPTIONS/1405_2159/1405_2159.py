# Ataque de Banshee
Ataque = input("Toque ou Grito? ").lower()
D1 = int(input("Valor do dado 1: "))
D2 = int(input("Valor do dado 2: "))

if (Ataque == "grito"):
	pontos = 6 + D1 + D2
	print(pontos)
else:
	pontos = (D1 + D2)**2
	print(pontos)
