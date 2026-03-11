from math import*
amin = input("digite o aminoacido: ")

o = 15.999
c= 12.011
n= 14.00674
h= 1.00794

if (amin == "Glutamina" ):
	peso = 5*c + 8*h + n + 4*o
	print(peso)
elif(amin == "Histidina"):
	peso = 6*c + 10*h + 3*n + 2*o
	print(peso)
				elif(amin == "Prolina"):
					peso = 5*c + 10*n + n + 2*o
					print(peso)
else:
	print("Entrada:",amin, "Dado invalido")