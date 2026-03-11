#Restaurante Bucho Cheio #

consumo = float(input("Qual o valor do Consumo? "))

if consumo <= float(300):
	total = consumo * (10/100) + consumo
	print(round(total,2))
else :
	total = consumo * (6/100) + consumo
	print (round(total,2))