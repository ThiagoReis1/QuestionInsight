nome = input("Qual o ataque: ")
d1 = int(input("dado 1: "))
d2 = int(input("dado 2: "))

if (nome == "grito"):
	dano = 6 + (d1 + d2)
	print(dano)
else:
	dano1 = (d1 + d2) ** 2
	print(dano1)

