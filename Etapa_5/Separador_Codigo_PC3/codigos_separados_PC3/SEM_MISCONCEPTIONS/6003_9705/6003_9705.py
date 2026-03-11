quant = int(input("Digite a quant: "))

if quant >= 5:
	conta = quant * 0.90
	
else:
	conta = quant * 1.20
	
print(round(conta, 2))