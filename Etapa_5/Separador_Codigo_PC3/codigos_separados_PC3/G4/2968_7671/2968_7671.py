#Cantina da Neide

esc = input("Voce quer lanche(L) ou salgado(S)? ")

esc2 = int(input("Quantos lanches ou salgados? "))

esc3 = int(input("Quantos refreigerantes? "))

if(esc.upper() == "L"):
	print(5*esc2+4*esc3)
else:
	print(3.5*esc2+4*esc3)
