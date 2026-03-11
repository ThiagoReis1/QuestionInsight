consumo=float(input("valor consumido:"))

if(consumo<=300):
	total=consumo+(consumo*0.1)
	print(round(total,2))
else:
	total=consumo+(consumo*0.06)
	print(round(total,2))