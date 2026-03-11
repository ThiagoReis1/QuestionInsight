idade= int(input("Digite a idade: "))
peso= float(input("Digite o peso: "))
if(idade>=0 and idade<=130):
	if(peso>=0.0 and peso<=550.0):
		if (idade>=12 and peso>=60):
			print("Entradas: ",idade,"anos e ",peso,"kg")
			print("Dosagem: 1000 mg")
		elif (idade>=12 and peso<60):
			print("Entradas: ",idade,"anos e ",peso,"kg")
			print("Dosagem: 875 mg")
		elif(idade<=12):
			if(peso<=5):
				print("Entradas:",idade,"anos e ",peso,"kg")
				print("Dosagem:75 mg")
			elif (peso>5 and peso<=9):
				print("Entradas:",idade,"anos e ",peso,"kg")
				print("Dosagem: 125 mg")
			elif(peso>9 and peso<=16):
				print("Entradas:",idade,"anos e ",peso,"kg")
				print("Dosagem: 250 mg")
			elif(peso>16 and peso<=24):
				print("Entradas:",idade,"anos e ",peso,"kg")
				print("Dosagem: 375 mg")
			elif(peso>24 and peso<=30):
				print("Entradas: ",idade,"anos e ",peso,"kg")
				print("Dosagem: 500 mg")
			elif (peso>30):
				print("Entradas:",idade,"anos e ",peso,"kg")
				print("Dosagem: 750 mg")
else:
	print("Entradas:",idade,"anos e ",peso,"kg")
	print("Dados invalidos")
		
		
	