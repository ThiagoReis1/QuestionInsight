equi = input("nome do equipamento: ").upper()
peso = int(input("peso do equipamento: "))
comp = 12
free = 52
fura = 1.7
liqu = 1.8
micr = 15
note = 2.5
tele = 15
vent = 2.4
if (equi == "COMPUTADOR") and (peso < 1000) and (peso > 0):
	print(peso //compu)
elif (equi == "FREEZER") and (peso < 1000) and (peso > 0):
	print(peso // free)
elif (equi == "FURADEIRA") and (peso < 1000) and (peso > 0):
	print(peso // fura)
elif(equi == "LIQUIDIFICADOR")	and (peso < 1000) and (peso > 0):
	print(peso // liqu)
elif(equi == "MICROONDAS")	and (peso < 1000) and (peso > 0):
	print(peso // micr)
elif(equi == "NOTEBOOK")	and (peso < 1000) and (peso > 0):
	print(peso // note)
elif(equi == "TELEVISOR") and (peso < 1000) and (peso > 0):
	print(peso // tele)
elif(equi == "VENTILADOR") and (peso < 1000) and (peso > 0):
	print(peso // vent)
else:	
	print("Entrada invalida")	