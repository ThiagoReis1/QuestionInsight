valorcompra = float(input("valor da compra"))
formapag = input("forma de pagamento")

if formapag == "D":
	valorA = 13/100
	valorf = valorcompra - valorcompra*valorA
	print(round(valorf, 2))
elif formapag == "P":
	valorA = 13/100
	valorf = valorcompra - valorcompra * valorA
	print(round(valorf, 2))
else:
	vezes = int(input("1 ou 2"))
	if vezes == 1:
		print(round(valorcompra, 2))
	elif vezes == 2:
		valorA =  8/100
		valorf = valorcompra + valorcompra*valorA
		print(round(valorf, 2))