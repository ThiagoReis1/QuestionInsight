pa = float(input(''))
if pa > 100:
	pn = pa + (pa*0.15)
	print(round(pn,2), 'ryous')
	print('Aumento de 15 porcento')
else:
	pn = pa + (pa*0.05)
	print(round(pn,2), 'ryous')
	print('Aumento de 5 porcento')