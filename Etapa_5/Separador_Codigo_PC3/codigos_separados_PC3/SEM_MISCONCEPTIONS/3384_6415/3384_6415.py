uni = str(input("O para oncas, K para quilogramas:"))
medida = float(input("Digite o valor a ser convertido:"))

oz = medida / 35.274
quilo = medida * 35.274

if(uni.upper() == "O"):
	print(round(oz,2))
	
else:
	print(round(quilo,2))