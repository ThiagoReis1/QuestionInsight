idade = int(input())
peso = float(input())
if(idade>0 and idade< 130 and peso>0.0 and peso<550.0):
	if(idade > 12 or idade == 12):
		if(peso > 60 or peso == 60):
			dosagem = 1000
		else:
			dosagem = 875
			
	else:
		if(peso < 5 or peso == 5):
			dosagem = 75
			
		elif(peso > 5 and (peso < 9 or peso == 9)):
			dosagem = 125
			
		elif(peso > 9 and (peso < 16 or peso == 16)):
			dosagem = 250
			
		elif(peso > 16 and (peso < 24 or peso == 24 )):
			dosagem = 375
			
		elif(peso > 24 and (peso < 30 or peso == 30)):
			dosagem = 500
			
		elif(peso > 30): 
			dosagem = 750
			
	print("Entradas:", idade, "anos e", peso, "kg")
	print("Dosagem:", dosagem, "mg")
else:
	print("Entradas:", idade, "anos e", peso, "kg")
	print("Dados invalidos")
