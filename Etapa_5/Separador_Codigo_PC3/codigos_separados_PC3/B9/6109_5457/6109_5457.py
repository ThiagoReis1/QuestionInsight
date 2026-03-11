
combustivel = float(input("quantidade de combustivel comum: "))

if combustivel < 17.5:
	quant = combustivel + 1.5
elif combustivel >= 17.5 and combustivel < 35.0:
	quant = combustivel + 2.3
elif combustivel >= 35.0 and combustivel < 50.0:
	quant = combustivel + 3.3
else:
	quant = combustivel + 4.7
	
print(round(quant, 1))
