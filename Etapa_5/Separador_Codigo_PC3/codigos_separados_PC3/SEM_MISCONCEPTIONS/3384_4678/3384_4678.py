unidade = input("Unidade de medida: ")
valor = float(input("Valor a ser convertido: "))

if unidade == "O":
	VALOR = valor/35.274
	
else:
	VALOR = 35.274*valor
	
print(round(VALOR, 2))