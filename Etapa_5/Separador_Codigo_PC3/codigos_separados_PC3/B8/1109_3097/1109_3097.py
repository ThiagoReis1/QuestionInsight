idade=int(input("idade "))
peso=float(input("peso "))
print("Entradas:",idade,"anos e",peso,"kg")
if(0<=idade<=130)and (0.0<=peso<=550.0):
	if(idade>=12):
		if(peso>=60):
			print("Dosagem: 1000 mg")
		else:
			print("Dosagem: 875 mg")
	else:
		if(peso<=5):
			print("Dosagem: 75 mg")
		elif(5<peso<=9):
			print("Dosagem: 125 mg")
		elif(9<peso<=16):
			print("Dosagem: 250 mg")
		elif(16<peso<=24):
			print("Dosagem: 375 mg")
		elif(24<peso<=30):
			print("Dosagem: 500 mg")
		elif(peso>30):
			print("Dosagem: 750 mg")
else:
	print("Dados invalidos")
			
		