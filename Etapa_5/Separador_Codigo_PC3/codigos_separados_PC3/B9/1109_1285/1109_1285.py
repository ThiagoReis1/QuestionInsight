idade = int(input("Idade: "))
peso = float(input("Peso:"))
print("Entradas:",idade,"anos e",peso,"kg")
if (idade<0 or idade>130 or peso<0 or peso>550):
	print("Dados invalidos")
else:
	if(idade>=12):
		if(peso>=60):
			dos = 1000
			print("Dosagem:",dos,"mg")
		else:
			dos = 875	
			print("Dosagem:",dos,"mg")
	elif(peso<=5):
		dos = 75
		print("Dosagem:",dos,"mg")
	elif(peso>5 and peso<9):
		dos = 125
		print("Dosagem:",dos,"mg")
	elif(peso>9 and peso<16):
		dos = 250
		print("Dosagem:",dos,"mg")
	elif(peso>16 and peso<24):
		dos = 375
		print("Dosagem:",dos,"mg")
	elif(peso>24 and peso<30):
		dos = 500
		print("Dosagem:",dos,"mg")
	else:
		dos = 750
		print("Dosagem:",dos,"mg")