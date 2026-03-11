quant_cenouras= int(input("Insira a quantidade de cenouras: "))

if quant_cenouras < 5:
	print(round(quant_cenouras * 1.2, 2))
	
else:
	print(round(quant_cenouras * 0.9, 2))