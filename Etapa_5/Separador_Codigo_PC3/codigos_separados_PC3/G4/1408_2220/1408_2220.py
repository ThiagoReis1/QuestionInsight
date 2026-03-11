nome=input("nome da arma: ")
d=int(input("destreza do personagem: "))
d1=int(input("dado um: "))
d2=int(input("dado dois: "))

if (nome == "katana"):
	print(2*(d1+d2)+d)
	
else:
	print((d1+d2)+(2*d))