golpe = input("qual golpe foi usado?")
d1 = int(input("sorteio do primeiro dado:"))
d2 = int(input("sorteio do seundo dado:"))
d3 = int(input("sorteio do terceiro dado:"))
d4 = int(input("sorteio do quarto dado:"))

if (golpe == "espada"):
		dano = (d1+6)+(d2+6)+(d3+6)+(d4+6)
		print(dano)
else:
	dano = (d1+d2+d3)*d4
	print(dano)