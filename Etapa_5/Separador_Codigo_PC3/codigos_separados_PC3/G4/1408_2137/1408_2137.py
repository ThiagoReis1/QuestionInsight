nda = input("nome da arma: ").lower()
D = int(input("destreza: "))
vs1 = int(input("valor sorteado 1: "))
vs2 = int(input("valor sorteado 2: "))
S = vs1 + vs2
if nda == "katana" :
	dano = (2*S + D)
	print(dano)
	
if nda == "sabre" :
	dano = S + 2*D
	print(dano)
	




