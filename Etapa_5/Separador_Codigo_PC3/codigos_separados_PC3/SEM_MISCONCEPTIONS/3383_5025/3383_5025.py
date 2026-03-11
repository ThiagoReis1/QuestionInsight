Unidade = input("unidade de medida: ")
valor = float(input("Valor da medida: "))

if Unidade == "K" : 
	L = 2.20462 * valor
	print (round(L,2))
else :
	K = valor / 2.20462
	print (round(K,2))