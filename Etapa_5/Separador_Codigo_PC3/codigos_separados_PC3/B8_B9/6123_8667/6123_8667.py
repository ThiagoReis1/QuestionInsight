quant = float(input("Digite a quantidade de combustivel comum: "))

if (quant < 17.5):
	total = quant + 0.8
	print(round(total,1))
elif ((quant>= 17.5) and (quant<35.0)):
	total = quant + 1.3
	print(round(total,1))
elif ((quant>=35.0) and (quant<50.0)):
	total = quant + 2.1
	print(round(total,1))
elif (quant>=50.0):
	total = quant + 3.0
	print(round(total,1))