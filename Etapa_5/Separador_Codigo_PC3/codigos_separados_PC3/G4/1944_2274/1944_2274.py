#aminoacido 
aminoacido = input("digite o aminoacido: ")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if(aminoacido.lower() == "leucina"):
	x = (6 * c) + (13 * h) + (n) + (2 * o)
	
	
else:
	x = (6* c) + (15 * h) + (2 * n) + (2 * o)

	
print(round(x,2))


