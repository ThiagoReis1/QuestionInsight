arma = input("Arma escolhida: ")
destreza = int(input("destreza: "))
d1 = int(input("Face D1: "))
d2 = int(input("Face D2: "))
if(arma == "sabre"):
	dano=(d1+d2)+2*destreza
	print(dano)
if(arma == "katana"):
	dano=2*(d1+d2)+destreza
	print(dano)	