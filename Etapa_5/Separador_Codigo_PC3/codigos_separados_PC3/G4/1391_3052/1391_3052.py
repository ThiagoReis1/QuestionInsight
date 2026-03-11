e= float (input('Qual a quantidade de consumo em kWh? '))

if (e <= 150):
	print (e*0.60 + 5)
else:
	print (e*0.75 + 16)