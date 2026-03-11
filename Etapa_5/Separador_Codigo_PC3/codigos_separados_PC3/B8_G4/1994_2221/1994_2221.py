amino= input("digite o nome do aminoacido: ").lower()
o=15.9994
c=12.011
n=14.00674
h=1.0079
if (amino == "histidina")or (amino == "leucina") or (amino == "lisina"):
	if (amino == "histidina"):
		y= c*6 + h*10 + n*3 + o*2
	elif (amino == "leucina"):
		y= c*6 + h*13 + n*1 + o*2
	elif (amino == "lisina"):
		y= c*6 + h*15 + n*2 + o*2
	print(round(y,2))
else:
	print("Entrada:", amino)
	print("Dado Invalido")