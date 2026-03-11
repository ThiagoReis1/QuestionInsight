consumo = int(input("Valor do consumo:"))

if consumo < 10 :
	valor = consumo * 2 + 20
	print(round(valor,2))
elif consumo >= 10 and consumo < 20:
	valor = consumo * 2.5 + 20
	print(round(valor,2))
elif consumo >= 20 and consumo < 40:
	valor = consumo * 2.75 + 20
	print(round(valor,2))
else:
	valor = consumo * 3 + 20
	print(round(valor,2))