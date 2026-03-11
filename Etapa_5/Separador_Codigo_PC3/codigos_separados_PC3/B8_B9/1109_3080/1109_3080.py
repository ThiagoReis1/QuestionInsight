idade=int(input())
peso=float(input())
print("Entradas:", idade, "anos", "e", peso, "kg")
#adultos e adolescentes
if((12<=idade<=130) and (peso>=60)):
	print("Dosagem", 1000, "mg")
else:
	if((12<=idade<=130) and (peso <60)):
		print("Dosagem", 875, "mg")
	else:
		if(0>=idade<=12):
			if(peso <= 5):
				print("Dosagem", 75, "mg")
			elif((peso>5) and (peso<=9)):
				print("Dosagem", 125, "mg")
			elif((peso>9) and (peso<=16)):
				print("Dosagem", 250, "mg")
			elif((peso>16) and (peso<=24)):
				print("Dosagem", 375, "mg")
			elif((peso>24) and (peso<=30)):
				print("Dosagem", 500, "mg")
			elif(peso>30):
				print("Dosagem", 750, "mg")
			else:
				print("Dados invalidos")


	