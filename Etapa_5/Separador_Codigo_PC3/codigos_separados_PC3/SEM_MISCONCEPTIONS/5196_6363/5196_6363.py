valorantigo = float(input("valor do produto: "))

if(valorantigo<=100.00):
	valornovo = (valorantigo*5)/100 + valorantigo
	print(round(valornovo, 2) , "ryous")
	print("Aumento de 5 porcento")
else:
	valornovo = (valorantigo*15)/100 + valorantigo
	print(round(valornovo, 2) , "ryous")
	print("Aumento de 15 porcento")