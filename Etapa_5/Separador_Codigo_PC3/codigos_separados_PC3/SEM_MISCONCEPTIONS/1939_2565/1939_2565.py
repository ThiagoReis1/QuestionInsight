
aminoacido = input("digite o nome do aminoacido: ").upper()

#pesos moleculares
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if(aminoacido == "ASPARAGINA"):
	atomo = ((c*4) +(h*8) + (n*2) +(o*3))

else:
	atomo = ((c*11) + (h*11) +(n*2) + (o*2))
	
print(round(atomo, 2))
				