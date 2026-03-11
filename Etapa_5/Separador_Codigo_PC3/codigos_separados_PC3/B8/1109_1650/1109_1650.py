idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print("Entradas: " ,idade, "anos e" ,peso, "kg")

if(idade >= 12):
	if(peso >= 60):
		dosagem = "1000 mg"
	else:
		dosagem = "875 mg"
else:
	if(peso == 5):
		dosagem = "75 mg"
	elif(peso > 5 or peso == 9):
		dosagem = "125 mg"
	elif(peso > 9 or peso == 16):
		dosagem = "250 mg"
	elif(peso > 16 or peso == 24):
		dosagem = "375 mg"
	elif(peso > 24 or peso == 30):
		dosagem = "500 mg"
	elif(peso > 30):
		dosagem = "750 mg"
		
print("Dosagem: ", dosagem)
	