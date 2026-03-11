aminoacido = input("Aminoacido: ")

if(aminoacido == "glutamina")or(aminoacido == "histidina")or(aminoacido == "prolina"):
	if(aminoacido == "glutamina"):
		p = 12.011 * 5 + 1.00794*8 + 14.00674 + 15.999*4
		print (round (p ,2))
	elif(aminoacido == "histidina"):
		p = 12.011 * 6 + 1.00794*10 + 14.00674*3 + 15.999*2
		print (round (p ,2))
	elif(aminoacido == "prolina"):	
		p = 12.011 * 5 + 1.00794*10 + 14.00674 + 15.999*2
		print (round (p ,2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")