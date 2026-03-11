unidade = input("medida B para BTU ou W para Watt-hora: ").upper()
valor = float(input("valor da medida: "))
if(unidade == "W"):
	medida = 3.41214*valor
else:
	medida = valor/3.41214
print(round(medida,2))