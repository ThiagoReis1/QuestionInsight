consumo = float(input("valor consumido: "))

total1 = consumo + (consumo * (10 / 100))
total2 = consumo + (consumo * (6 / 100)) 

if (consumo<=300):
   print(round(total1, 2))
else:
	print(round(total2, 2))