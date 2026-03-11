ataque = input("QUAL ATAQUE? ")
d1 = int(input("Resuldado de d1(1-6): "))
d2 = int(input("Resuldado de d2(1-6): "))
d3 = int(input("Resuldado de d3(1-6): "))
d4 = int(input("Resuldado de d4(1-6): "))

if(ataque == "espada"):
	braco1= d1+6
	braco2= d2+6
	braco3= d3+6
	braco4= d4+6
	dano = braco1 + braco2 + braco3 + braco4
if(ataque == "cauda"):
	dano = (d1 + d2 + d3) * d4
	
print(dano)