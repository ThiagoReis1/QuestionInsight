# Entrada de variaveis

unidmedida = input("Qual unidade de medida se encontra, digite B para BTU, ou Watt-hora")
valormedida = float(input("Qual o valor de medida: "))

# Saida de variaveis

if unidmedida == 'B':
	print(round(valormedida / 3.41214, 2))
else: 
	print(round(valormedida * 3.41214, 2))