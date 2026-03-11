i = int(input())
p = float(input())

print("Entradas:",i,"anos e",p,"kg")
if (i >= 0) and (i <= 130) and (p >= 0) and (p <= 550):
	if (i>=12) and (p>=60):
		print("Dosagem: 1000 mg")
	elif(i >= 12) and (p < 60):
		print("Dosagem: 875 mg")
	elif(i < 12):
		if (p<=5):
			print("Dosagem: 75 mg")
		elif(p>5 and p<=9):
			print("Dosagem: 125 mg")
		elif(p>9 and p<=16):
			print("Dosagem: 250 mg")
		elif(p>16 and p<=24):
			print("Dosagem: 375 mg")
		elif(p>24 and p<=30):
			print("Dosagem: 500 mg")
		elif(p>30):
			print("Dosagem: 750 mg")
else:
	print("Dados invalidos")