nome = input("nome do aminoacido: ").upper()

Pg = 2*15.9994 + 5*1.0079 + 14.00674 + 2*12.011
Ps = 3*12.011 + 7*1.0079 + 14.00674 + 15.9994*3
if(nome == "GLICINA"):
	print(round(Pg,2))
else:
	print(round(Ps,2))
	