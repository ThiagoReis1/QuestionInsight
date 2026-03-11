arma = input("informe o nome da arma: ")
D = float(input("informe a destreza do personagem: "))
S1 = int(input("informe o valor sorteado: "))
S2 = int(input("informe o valor sorteado: "))
S = S1 + S2




if(arma == "katana"):
	katana = (2*S) + D
	ataque = katana
	print(ataque)
		
else:
	sabre = S+(2*D)
	ataque2 = sabre
	print(ataque2)
	