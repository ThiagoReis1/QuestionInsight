antigo = float(input('valor: '))


if antigo < 100.00:
	aumento = antigo + (antigo * 5 /100)
	print(round(aumento,2),'ryous')
	print('Aumento de 5 porcento')
else:
	aumento = antigo + (antigo * 15 / 100)
	print(round(aumento,2),'ryous')
	print('Aumento de 15 porcento')