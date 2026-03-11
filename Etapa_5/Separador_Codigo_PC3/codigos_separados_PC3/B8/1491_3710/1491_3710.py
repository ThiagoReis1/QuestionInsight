peso = float(input("Qual o peso da encomenda: "))

if(peso < 0):
	print("Entrada invalida")
elif(0 <= peso <= 5000):
	valor = (peso * 0.03) + 20
	print(round(valor,2))
elif(5001 < peso <= 6000):
	valor = (peso * 0.04) + 25
	print(round(valor,2))
elif(6001 < peso <= 7000):
	valor = (peso * 0.05) + 30
	print(round(valor,2))
elif(7001 < peso):
	valor = (peso * 0.06) + 35
	print(round(valor,2))
