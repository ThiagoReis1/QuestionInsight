i = int(input("idade: "))
p = float(input("peso: "))

print("Entradas:" , i , "anos e" , p , "kg")
if(0 <= i <= 130) and (0.0 <= p <= 550.0):
	if(i >= 12):
		if(p >= 60):
			print("Dosagem: 1000 mg") 
		else:
			print("Dosagem: 875 mg")
	else:
		if(p <= 5):
			print("Dosagem: 75 mg")
		elif(5 < p <= 9):
			print("Dosagem: 125 mg")
		elif(9 < p <= 16):
			print("Dosagem: 250 mg")
		elif( 16 < p <= 24):
			print("Dosagem: 375 mg")
		elif(24 < p <= 30):
			print("Dosagem: 500 mg")
		elif(p > 30):
			print("Dosagem: 750 mg")
else:
	print("Dados invalidos")