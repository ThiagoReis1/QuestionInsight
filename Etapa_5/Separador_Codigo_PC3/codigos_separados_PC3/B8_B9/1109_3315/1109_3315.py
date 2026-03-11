idade = int(input())
peso = float(input())

print("Entradas:", idade,"anos e ", peso,"kg")

if(idade>130 or idade<0 or peso<=0 or peso>550):
	print("Dados invalidos")
else:
	if(idade>=12):
		if(peso>=60):
			print("Dosagem: 1000 mg")
		elif(peso<60):
			print("Dosagem: 875 mg")
	elif(idade<12):
		if(peso<=5):
			print("Dosagem: 75 mg")
		elif(peso<=9):
			print("Dosagem: 125 mg")
		elif(peso<=16):
			print("Dosagem: 250 mg")
		elif(peso<=24):
			print("Dosagem: 375 mg")
		elif(peso<=30):
			print("Dosagem: 500 mg")
		elif(peso>30):
			print("Dosagem: 750 mg")