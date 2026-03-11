nome = input("nome do amino acido:")
c = 12.011
h = 1.00794
n = 14.00674
o = 15.999


if nome.upper() == "ASPARAGINA" :
	peso = (4*c ) + (8*h) + (2*n ) + (3*o) 
	print (round (peso,2))
elif nome.upper() == "GLUTAMINA":
	peso = (5*c ) + (8*h) + (1*n ) + (4*o)
	print(round (peso,2))
elif nome.upper() == "TRIPTOFANO":
	peso = (11*c ) + (11 *h) + (2*n ) + (2*o)
	print (round (peso,2))
	
else:
	print("Entrada:", nome)
	print("Dado Invalido")