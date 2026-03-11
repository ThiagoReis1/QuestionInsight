nome = input("digite o nome do aminoacido:").lower()

if(nome == "glutamina"):
	cal = ((5 * 12.011)+(8*1.00794)+(1*14.00674)+(4*15.999))
	print(round(cal,2))
elif(nome == "histidina"):
	cal = ((6 * 12.011)+(10*1.00794)+(3*14.00674)+(2*15.999))
	print(round(cal,2))
elif(nome == "prolina"):
	cal = ((5 * 12.011)+(10*1.00794)+(1*14.00674)+(2*15.999))
	print(round(cal,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")
	
	