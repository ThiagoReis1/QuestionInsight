equip = input("")
capac = int(input(""))
if((capac<0) or capac > 1000):
	print("Entrada invalida")
else:
	if(equip == "COMPUTADOR"):
		q = capac/12
	elif(equip == "FREEZER"):
		q = capac/52
	elif(equip == "FURADEIRA"):
		q = capac/1.7
	elif(equip == "LIQUIDIFICADOR"):
		q = capac/1.8
	elif(equip == "MICROONDAS"):
		q = capac/15
	elif(equip == "NOTEBOOK"):
		q = capac/2.5
	elif(equip == "TELEVISOR"):
		q = capac/15
	else:
		q = capac/2.4
	print(int(q))