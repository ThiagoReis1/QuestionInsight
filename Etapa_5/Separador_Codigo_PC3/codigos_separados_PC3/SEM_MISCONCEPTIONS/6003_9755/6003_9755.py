quant_cenouras = int(input("digite a quantidade de cenouras compradas: "))

if quant_cenouras <= 5:
	valor = quant_cenouras*1.20
	print(round(valor, 1))
else:
	valor = quant_cenouras*0.90
	print(round(valor, 1))

#70%