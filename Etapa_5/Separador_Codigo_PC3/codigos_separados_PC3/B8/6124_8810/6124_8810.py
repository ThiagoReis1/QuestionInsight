peso = float(input("Digite seu peso, meu rei:"))

if(peso >= 0):
	if((peso >= 3000.0) and (peso < 3400)):
		x = peso * 0.8
		total = round(x,1)
		print(total)
	elif((peso >= 3400) and (peso < 3900)):
		x = peso * 1.3
		total = round(x,1)
		print(total)
	elif((peso >= 3900) and (peso < 4100,0)):
		x = peso * 2.1
		total = round(x,1)
		print(total)
	elif((peso >= 4100)):
		x = peso * 3.0
		total = round(x,1)
		print(total)
else:
	print("Entrada invalida")