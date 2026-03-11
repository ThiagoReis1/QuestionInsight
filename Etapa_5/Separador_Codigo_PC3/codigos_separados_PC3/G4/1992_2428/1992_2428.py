ent = input("")

if(ent.lower() == "glutamina"):
	
	peso = float(12.011 * 5) + (1.00794 * 8) + (14.00674 * 1) + (15.999 * 4)
	print(round(peso,2))

	
elif(ent.lower() == "histidina"):
	peso = float(12.011 * 6) + (1.00794 * 10) + (14.00674 * 3) + (15.999 * 2)
	print(round(peso,2))
	
elif(ent.lower() == "prolina"):
	peso = float(12.011 * 5) + (1.00794 * 10) + (14.00674 + (15.999 * 2))
	print(round(peso,2))
	
else:
	
	print("Entrada:",ent)
	print("Dado Invalido")