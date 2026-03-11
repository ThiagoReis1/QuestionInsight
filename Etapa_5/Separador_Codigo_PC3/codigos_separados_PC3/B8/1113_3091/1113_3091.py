idade = int(input("digite idade: "))
peso = float(input("digite peso: "))
print("Entradas:",idade, "anos e",peso,"kg")


if((130>=idade>=0)and(0.0<=peso<=550.0)):
	if((idade<=20)and(peso<=60)):
		z = "9"
	elif((20<idade<=50)and(peso<=60)):
		z = "6"
	elif((idade>50)and(peso<=60)):
		z = "3"
	elif((idade<=20)and(60<peso<=90)):
		z = "8"
	elif((20<idade<=50)and(60<peso<=90)):
		z = "5"
	elif((idade>50)and(60<peso<=90)):
		z = "2"
	elif((idade<=20)and(peso>90)):
		z = "7"
	elif((20<idade<=50)and(peso>90)):
		z = "4"
	elif((idade>50)and(peso>90)):
		z = "1"
	print("Grupo de risco:", z)	
else:
	print("Dados invalidos")