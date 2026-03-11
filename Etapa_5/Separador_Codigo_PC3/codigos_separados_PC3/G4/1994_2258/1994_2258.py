a=input("digite o nome do aminoacido: ")

if(a=="histidina"):
	y=(6*12.011)+(10*1.0079)+(3*14.00674)+(2*15.9994)
	print(round(y,2))
elif(a=="leucina"):
	y=(6*12.011)+(13*1.0079)+(1*14.00674)+(2*15.9994)
	print(round(y,2))
elif(a=="lisina"):
	y=(6*12.011)+(15*1.0079)+(2*14.00674)+(2*15.9994)
	print(round(y,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")
