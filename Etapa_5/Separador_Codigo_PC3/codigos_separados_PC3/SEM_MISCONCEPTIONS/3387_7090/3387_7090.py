unidade = input("Unidade de medida: (K/M): ")
valor = float(input("Valor da medida: "))

if(unidade == "K".upper()):
	valor2 = 2.35215 * valor
else:
	valor2 = valor / 2.35215
print(round(valor2,2))