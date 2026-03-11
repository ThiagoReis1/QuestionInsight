nome= input()
quant= int(input())
if(quant<0 or quant>1000 and( nome !='COMPUTADOR' or nome != 'FREEZER' or nome != 'FURADEIRA' or nome != 'LIQUIDIFICADOR' or nome != 'MICROONDAS' or nome != 'NOTEBOOK' or nome != 'TELEVISOR' or nome != 'VENTILADOR')):
		print("Entrada invalida")
else:
	if(nome == 'COMPUTADOR'):
		peso=quant*12
	elif(nome == 'FREEZER'):
		peso= quant*52
	elif(nome == 'FURADEIRA'):
		peso= quant*1.7
	elif(nome == 'LIQUIDIFICADOR'):
		peso= quant*1.8
	elif(nome == 'MICROONDAS'):
		peso= quant*15
	elif(nome == 'NOTEBOOK'):
		peso= quant*2.5
	elif(nome == 'TELEVISOR'):
		peso= quant*15
	elif(nome == 'VENTILADOR'):
		peso= quant*2.4
	print(round(peso,2))