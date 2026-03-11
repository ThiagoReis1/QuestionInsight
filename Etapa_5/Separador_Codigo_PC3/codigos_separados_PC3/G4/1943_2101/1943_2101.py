aminoacido = input("nome do aminoacido:")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if aminoacido .lower() == "isoleucina" :
	peso = (c * 6 ) + (h * 13 ) + n + ( o * 2)
	print (round(peso, 2))
	
else :	
	peso_2 = (c * 5) + (h * 11 ) + n + ( o * 2) + s

	print (round(peso_2, 2))