idade = int(input("Qual a idade: "))
peso = float(input("Qual o peso: "))

print("Entradas:",idade,"anos e",peso,"kg")

if(idade >= 0 and idade <=130 and peso >= 0.0 and peso <=550.0):
	if(idade >= 12 and peso >= 60.0):
		dosagem = 1000
		print("Dosagem:",dosagem,"mg")
	elif(idade >= 12 and peso < 60.0):
		dosagem = 875
		print("Dosagem:",dosagem,"mg")
	elif(idade < 12 and peso <= 5.0):
		dosagem = 75
		print("Dosagem:",dosagem,"mg")
	elif(idade < 12 and peso > 5 and peso <= 9):
		dosagem = 125
		print("Dosagem:",dosagem,"mg")
	elif(idade < 12 and peso > 9 and peso <= 16):
		dosagem = 250
		print("Dosagem:",dosagem,"mg")
	elif(idade < 12 and peso > 16 and peso <= 24):
		dosagem = 375
		print("Dosagem:",dosagem,"mg")
	elif(idade < 12 and peso > 24 and peso <= 30):
		dosagem = 500
		print("Dosagem:",dosagem,"mg")
	else:
		dosagem = 750
		print("Dosagem:",dosagem,"mg")
else:
	print("Dados invalidos")