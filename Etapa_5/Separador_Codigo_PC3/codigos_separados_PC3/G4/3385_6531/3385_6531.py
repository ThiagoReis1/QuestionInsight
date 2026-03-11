uni= (input("Digite a unidade de medida: "))
uni = uni.upper()
valorm = float(input("Digite o valor da medida: "))

hec = valorm / 2.47105
acre = 2.47105 * valorm

if( uni != "H"):
	print(round( hec , 2))
else:
	print(round( acre , 2 ))

