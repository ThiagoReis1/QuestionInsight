consumo = float(input())
franquia = 100
if(consumo <= franquia):
	print(round(consumo * 1.20, 2))
else:
	print(round(consumo * 1.40, 2) + 25)
