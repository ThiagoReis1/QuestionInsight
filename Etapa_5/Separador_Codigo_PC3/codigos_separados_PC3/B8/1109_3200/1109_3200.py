idade= int(input())
peso= float(input())

print("Entradas:",idade,"anos e",peso,"kg")

if(0<idade and idade<=130) and (0.0<peso and peso<=550.0):
	if(idade>=12) and (peso>=60):
		print("Dosagem: 1000 mg")
	elif(idade>=12 and peso<60):
		print("Dosagem: 875 mg")
	elif(idade<12):                   
		if(peso<=5):
			print("Dosagem: 75 mg")
		elif(5<peso) and (peso<=9):
			print("Dosagem: 125 mg")
		elif(9<peso) and (peso<=16):
			print("Dosagem: 250 mg")
		elif(16<peso) and (peso<=24):
			print("Dosagem: 375 mg")
		elif(24<peso) and (peso<=30):
			print("Dosagem: 500 mg")
		else:
			print("Dosagem: 750 mg")
else:
	print("Dados invalidos")
	