unidade = input("K ou M: ")
medida = float(input("valor da medida: "))

if (unidade == "K"):
	medida = medida/1.60934
	print(round(medida, 2))
else:
	medida = medida*1.60934
	print(round(medida, 2))
