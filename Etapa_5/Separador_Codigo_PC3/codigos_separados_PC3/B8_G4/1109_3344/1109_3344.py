a = int(input("Digite: "))
b = float(input("DIgite: "))

if(0<=a and a<=130 and 0<=b and b<=550):
	if(a>=12 and b>=60):
		print("Entradas: ",a,"anos e",b,"kg")
		print("Dosagem: 1000 mg")
	elif(a>=12 and b<60):
		print("Entradas: ",a,"anos e",b,"kg")
		print("Dosagem: 875 mg")
	else:
		if(a<12 and b<=5):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 75 mg")
		elif(a<12 and b>5 and b<=9):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 125 mg")
		elif(a<12 and b>9 and b<=16):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 250 mg")
		elif(a<12 and b>16 and b<=24):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 375 mg")
		elif(a<12 and b>24 and b<=30):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 500 mg")
		elif(a<12 and b>30):
			print("Entradas: ",a,"anos e",b,"kg")
			print("Dosagem: 750 mg")
		
else:
	print("Entradas: ",a,"anos e",b,"kg")
	print("Dados invalidos")