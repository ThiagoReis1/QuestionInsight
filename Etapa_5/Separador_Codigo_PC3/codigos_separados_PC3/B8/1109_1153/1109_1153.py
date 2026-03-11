idade=int(input("idade"))
peso=float(input("peso"))
if(0<idade<130) and (0.0<peso<550.0):
	if(idade>=12) and (peso>=60):
		dosagem=1000
	elif(idade>=12) and (peso<60):
		dosagem=875
	elif(idade<12) and (peso<=5):
		dosagem= 75
	elif(idade<12) and (5<peso<=9):
		dosagem= 125
	elif(idade<12) and (9<peso<=16):
		dosagem= 250
	elif(idade<12) and (16<peso<=24):
		dosagem= 375
	elif(idade<12) and (24<peso<=30):
		dosagem= 500
	elif(idade<12) and (peso>30):
		dosagem= 750
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dosagem:",dosagem,"mg")
else:
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dados invalidos")