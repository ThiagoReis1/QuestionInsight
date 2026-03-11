idade = int(input())
peso = float(input())
print("Entradas: ", idade,"anos e", peso, "kg")
if(0<=idade<=130 and peso<=550):
	if(idade >= 12):
		if(peso >= 60):
			msg = "1000 mg"
			print("Dosagem: ", msg)
		else:
			msg = "875 mg"
			print("Dosagem: ", msg)
	elif(idade < 12):
		if(0 < peso <= 5):
			msg = "75 mg"
			print("Dosagem: ", msg)
		elif(5 < peso <= 9):
			msg = "125 mg"
			print("Dosagem: ", msg)
		elif(9 < peso <= 16):
			msg = "250 mg"
			print("Dosagem: ", msg)
		elif(16 < peso <= 24):
			msg = "375 mg"
			print("Dosagem: ", msg)
		elif(24 < peso <= 30):
			msg = "500 mg"
			print("Dosagem: ", msg)
		else:
			msg = "750 mg"
			print("Dosagem: ", msg)
else:
	print("Dados invalidos")
