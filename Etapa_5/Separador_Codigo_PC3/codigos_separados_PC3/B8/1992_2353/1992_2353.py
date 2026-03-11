nome=str(input("digite o nome do aminociado:")).lower()

if(nome=="glutamina")or(nome=="histidina")or(nome=="prolina"):
	if(nome=="glutamina"):
		glutamina=(5*12.011)+(8*1.00794)+(1*14.00674)+(4*15.999)
		print(round(glutamina,2))
	elif(nome=="histidina"):
		histidina=(6*12.011)+(10*1.00794)+(3*14.00674)+(2*15.999)
		print(round(histidina,2))
	elif(nome=="prolina"):
		prolina=(5*12.011)+(10*1.00794)+(1*14.00674)+(2*15.999)
		print(round(prolina,2))

else:
	print("Entrada:",nome)
	print("Dado Invalido")