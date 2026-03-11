arma = input("katana ou sabre? ")
D = int(input("destreza do bom: "))

D1 = int(input("valor do primeiro dado: "))
D2 = int(input("valor do segundo dado: "))
S = D1+D2 
if(arma == "katana"):
	katanada = ((2*S) +D)
	print(katanada)
	
else:
	voadora = (S+(2*D))
	print(voadora)