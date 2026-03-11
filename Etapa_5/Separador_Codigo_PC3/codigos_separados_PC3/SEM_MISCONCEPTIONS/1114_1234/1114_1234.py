X=float(input("digite o x: "))
Y=float(input("digite o y: "))
print("Entradas:",X,"Km/h e", Y,"h")

if( X>0 and Y=>0):
	if X==1 and Y=0:
		Z=Avalon
	elif X==100 and Y=1:
		Z=Bravos
	elif X==100 and Y=2:
		Z=Castamere
	elif X==200 and Y=3:
		Z=Doriath
	elif X==200 and Y=4:
		Z=Edoras
	elif X==150 and Y=5:
		Z=Fangorn
	elif X==400 and Y=6:
		Z=Gondor
	elif X==250 and Y=7:
		Z=Hogsmead
		print("Proxima parada:",Z)
else:
	print("Dados invalidos")