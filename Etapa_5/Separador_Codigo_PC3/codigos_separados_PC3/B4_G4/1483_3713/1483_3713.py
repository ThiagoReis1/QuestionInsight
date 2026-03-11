m = input()
q= int(input())

if(q < 0):
	print("Entrada invalida") 
elif(q > 1000):
	print("Entrada invalida")
elif( m == "COMPUTADOR"):
	c = q * 12
	print(round(c, 2))
elif (m == "FREEZER"):
	c = q * 52
	print(round(c, 2))
elif (m == "FURADEIRA"):
	c = q * 1.7
	print(round(c, 2))
elif (m == "LIQUIDIFICADOR"):
	c = q * 1.8
	print(round(c, 2))
elif (m == "MICROONDAS"):
	c = q * 15
	print(round(c, 2))
elif (m == "NOTEBOOK"):
	c = q * 2.5
	print(round(c, 2))
elif (m == "TELEVISOR"):
	c = q * 15
	print(round(c, 2))
elif (m == "VENTILADOR"):
	c = q * 2.4
	print(round(c, 2))
else:
	print("Entrada invalida")
	


	