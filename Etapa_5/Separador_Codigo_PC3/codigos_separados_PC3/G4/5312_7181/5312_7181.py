nbac=int(input("numero de bacterias:  "))
h=int(input("horas:  "))
cont=0
while(cont<h):
	nbac=nbac+(nbac*0.02)
	nbac=int(nbac)
	cont=cont+1
print(nbac)