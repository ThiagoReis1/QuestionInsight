idade=int(input())
peso=float(input())
if (idade>0 and idade<130) and (peso>0.0 and peso<550.0):
	if(idade<20) and (peso>60):
		Grupo=9
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo) 
	elif (idade>20) and (peso> 60 and peso<90):
		Grupo=8
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)
	elif (idade>20 and peso>90):
		Grupo=7
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)
	elif (idade>20 and idade<50) and (peso<=60):
		Grupo=6
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo) 
	if(idade>60 and idade<50) and (peso>60 and peso<90):
		Grupo=5
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo) 
	elif (idade>20 and idade<50) and (peso>90):
		Grupo=4
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)
	elif (idade>50) and (peso<60):
		Grupo=3
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)
	elif( idade>50) and (peso>60 and peso<90):
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)
	else:
		Grupo=1
		print("Entradas:", idade,"anos e", peso,"kg")
		print("Grupo de risco:",Grupo)	
else:	
	print("Entradas:", idade,"anos e",peso,"kg")
	print("Dados invalidos")
		