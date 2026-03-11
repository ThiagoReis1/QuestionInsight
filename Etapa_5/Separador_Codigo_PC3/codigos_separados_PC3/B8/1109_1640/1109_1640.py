idade = int(input("Digite sua idade: "))
peso = float(input("Digite sua massa:"))

print("Entradas:", idade, "anos e", peso, "kg")

if(idade >= 12):
	if(peso >= 60):
		dosagem = "1000"
	else:
		dosagem = "875"

else:
	if(peso >= 0 or peso <= 5):
		dosagem = "75"
	elif(peso > 5 or peso <= 9):
		dosagem = "125"
	elif(peso > 9 or peso <= 16):
		dosagem = "250"
	elif(peso > 16 or peso <=24):
		dosagem = "375"
	elif(peso >24 or peso <= 30):
		dosagem = "500"
	elif(peso >30 or peso <= 550):
		dosagem = "750"

if(idade < 12 or idade > 130 or peso > 550):
	print("Dados invalidos")
else:
	print("Dosagem:", dosagem, "mg")