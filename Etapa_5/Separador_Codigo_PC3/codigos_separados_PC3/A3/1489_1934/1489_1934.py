consumo = float(input(""))
if ( consumo >= 0 and consumo <= 150):
	valor = consumo * 0.6 + 5
if ( consumo > 150 and consumo <= 250):
	valor = consumo * 0.65 + 8
if ( consumo > 250 and consumo <= 350):
	valor = consumo * 0.7 + 12
if ( consumo > 350):
	valor = consumo * 0.75 + 16
print (round(valor,2))	