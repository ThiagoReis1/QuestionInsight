ufam = input("digite seu setor: ").upper()
cont = 0

while (ufam != "ICE"):
	if ufam == "ICE":
		cont = cont + 1
	ufam = input("digite seu ponto:")
		if ufam == "FT":
			cont = cont + 1
		ufam = input("digite seu setor")

print(cont)

