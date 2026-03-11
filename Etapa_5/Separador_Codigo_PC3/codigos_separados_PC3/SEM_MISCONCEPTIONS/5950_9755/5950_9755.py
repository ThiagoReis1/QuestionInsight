comida("digite se for T ou P: ")
quant = int(input("digite a quantidade: "))
cap = int(input("digite a quantidade de cappuccinos: "))

cafe = 4.50

if comida == 'T':
	conta = (6.00*quant+cafe*cap)
	print(round(conta, 1))
else:
	conta = (5.00*quant+cafe*cap)
	print(round(conta, 1))