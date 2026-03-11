arma=input("Qual a arma? ")
D=int(input("Destreza do personagem: "))
dado1=int(input("valor sorteado no dado 1: "))
dado2=int(input("valor sorteado no dado 2: "))
	
S=(dado1+dado2)

if(arma=="sabre"):
	danos=(S+2*D)
	print(danos)
	
if(arma=="katana"):
	danok=(2*S+D)
	print(danok)