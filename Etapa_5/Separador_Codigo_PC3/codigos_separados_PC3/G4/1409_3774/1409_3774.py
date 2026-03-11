tipo_ataque = input("Tipo de ataque - espada ou cauda: ")
D1 = int(input("Valor sorteado: "))
D2 = int(input("Valor sorteado: "))
D3 = int(input("Valor sorteado: "))
D4 = int(input("Valor sorteado: "))

if (tipo_ataque == "cauda"):
	dano = (D1 + D2 + D3) * D4
	print(dano)
	
else: 
	dano = (D1 + 6) + (D2 + 6) + (D3 + 6) + (D4 + 6)
	print(dano)

