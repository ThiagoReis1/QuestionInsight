#Universidade Federal do Amazonas
#Avaliação 03
#Suenne Renata Lima Fernandes- 21602342

a = float(input("Quantos anos?"))
k = float(input("Quantos kg?"))

if( a >= 0 and a <= 130 and k >= 0.0 and k <= 550.0):
	print("Entradas:", a,"anos e", k,"kg")
	if(a >= 12 and k >= 60):
		print("Dosagem: 1000 mg")
	else:
		if(a >12 and k < 60):
			print("Dosagem: 875 mg")
if(a < 12 and k<=5):
	print("Dosagem: 75 mg")
if(a < 12 and k > 5 and k <= 9):
	print("Dosagem: 125 mg")
if(a < 12 and k > 9 and k<= 16):
	print("Dosagem: 250 mg")
if(a < 12 and k > 16 and k <= 24):
	print("Dosagem: 375 mg")
if(a < 12 and k > 24 and k <= 30):
	print("Dosagem: 500 mg")
if(a < 12 and k > 30):
	print("Dosagem: 750 mg")
else:
	if
	print("Dados invalidos")