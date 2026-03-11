var1=float(input('valor da compra:'))
var2=input('codigo da opcao de pagamento:').upper()

if (var2 == "D"):
	total=var1-(var1 * 0.11)
	print(round(total,1))
elif (var2 == "p"):
	total=var1-(var1 * 0.11)
	print(round(total,1))
elif (var2 == "C"):
	parc = int(input("parc: "))
	if (parc == 1):
		total=var1
	else:
		total= var1 + ( 0.06 * var1 )
	print(round(total,2))