eq= input("digite o equipamento:").upper()
cap= int(input("digite a capacidade do caminhão:"))
if((0<cap<=1000) and eq=='COMPUTADOR'or eq=='FREEZER' or eq=='FURADEIRA' or eq=='LIQUIDIFICADOR'
or eq=='MICROONDAS'or eq=='NOTEBOOK'or eq=='TELEVISOR'or
	eq=='VENTILADOR' ):
	if(eq=='COMPUTADOR'):
		qtd=cap//12
		print(int(qtd))
	elif(eq=='FREEZER')	:
		qtd=cap//52
		print(int(qtd))
	elif(eq=='FURADEIRA'):
		qtd=cap//1.7
		print(int(qtd))
	elif(eq=='LIQUIDIFICADOR'):
		qtd=cap//1.8
		print(int(qtd))
	elif(eq=='MICROONDAS'):
		qtd=cap//15
		print(int(qtd))
	elif(eq=='NOTEBOOK'):
		qtd=cap//2.5
		print(int(qtd))
	elif(eq=='TELEVISOR'):
		qtd=cap//15
		print(int(qtd))
	elif(eq=='VENTILADOR'):
		qtd=cap//2.4
		print(int(qtd))
	else:
		print('Entrada invalida')
else:
	print('Entrada invalida')
