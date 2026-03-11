casa = input("Qual casa a bola caiu? (P)Preta (V)Vermelha ou (S): ").upper()
cont = 0
while (casa != "S"):
	if casa == "P":
		cont+= 1
		casa = input ("Qual a casa a bola caiu? (P)Preta (V)Vermelha ou (S): ").upper()
print(cont)
