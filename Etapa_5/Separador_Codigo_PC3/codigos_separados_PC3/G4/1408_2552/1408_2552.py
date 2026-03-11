arma= input("arma: ")
D=int(input("destreza: "))
dado1=int(input("dado1: "))
dado2=int(input("dado2: "))
S=(dado1+dado2)
if(arma=="katana"):
	gk=(2*S+D)
	print(gk)
else:
	gs=S+(2*D)
	print(gs)
	
	