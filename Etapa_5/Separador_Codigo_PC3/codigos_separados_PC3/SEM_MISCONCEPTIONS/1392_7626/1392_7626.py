consumo= float(input(""))

if consumo < 10:
	consumof1= consumo * 3.00 + 30
	print(round(consumof1,2))
if consumo >= 10:
	consumof2= consumo* 3.5 + 30
	print(round(consumof2, 2))