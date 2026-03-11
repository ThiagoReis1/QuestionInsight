consumo= float(input("Digite o valor do consumo de agua: "))

valor_total1= 30 + (consumo * 3.0)
valor_total2= 30 + (consumo * 3.5)

if( consumo < 10) :
	print(round(valor_total1, 2))
else:
	print(round(valor_total2, 2))