idade = int(input('idade:'))
peso = float(input('peso:'))
print('Entradas:', idade, 'anos e', peso, 'kg')
if(idade > 0 and idade< 130 and peso > 0.0 and peso < 550.0):
	if (idade>=12 and peso>=60):
	dosagem=1000 mg
		print("Entradas:", idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade>=12 and peso<60):
	dosagem=875 mg
		print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and peso<=5):
	dosagem=75 mg
		print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and 5<peso<9):
	dosagem=125 mg
		print("Entradas:",idade "e" peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and 9<peso<16):
	dosagem=250 mg
		print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and 16<peso<24):
		dosagem=375 mg
		print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and 24<peso<30):
		dosagem=500 mg
		print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)
	elif(idade<12 and peso>30):
		dosagem=750 mg
	   print("Entradas:",idade,"e",peso)
		print("Dosagem:",dosagem)