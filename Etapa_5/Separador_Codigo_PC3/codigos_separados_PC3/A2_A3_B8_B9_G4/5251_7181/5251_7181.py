x=input("cidade de destino:  ")
y=int(input("idade do passageiro:  "))


if(x.upper()=="PORTO VELHO"):
	z=500.0
elif(x.upper()=="SANTAREM"):
	z=370.0
elif(x.upper()=="BELEM"):
	z=600.0
elif(x.upper()=="TEFE"):
	z=360.0
elif(x.upper()=="TABATINGA"):
	z=550.0

if(y>0 and y<=150 and (x.upper()=="PORTO VELHO" or x.upper()=="SANTAREM" or x.upper()=="BELEM" or x.upper()=="TEFE" or x.upper()=="TABATINGA")):
		
	if(y<=2 and y>=0):
		z=0
		print("Entradas: ", x, ",", y)
		print("Passagem: R$", round(z, 2))
	elif(y>=3 and y<=12):
		z=z-(z*0.5)
		print("Entradas: ", x, ",", y)
		print("Passagem: R$", round(z, 2))
	elif(y>=65):
		z=z-(z*0.3)
		print("Entradas: ", x, ",", y)
		print("Passagem: R$", round(z, 2))
	elif(y>12 and y<65):
		z=z
		print("Entradas: ", x, ",", y)
		print("Passagem: R$", round(z, 2))
else:
	print("Entradas: ", x, ",", y)
	print("entradas invalidas")