consumo = int(input())

if ( consumo <= 150):
	valor = (consumo*0.6) + 5
else:
	valor = (consumo*0.75) + 16
print(round(valor,2))	