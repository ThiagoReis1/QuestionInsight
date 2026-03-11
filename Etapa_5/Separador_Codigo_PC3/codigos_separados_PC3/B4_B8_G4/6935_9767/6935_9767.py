vdc = float ( input ("Valor da compra: "))
mt = str ( input ("Metodo de pagamento(D/P/C): "))

if mt.upper() == "C":
	nv = int ( input ("Numero de vezes: "))
	if nv == 1:
		soma = vdc
		print (round ( soma , 2))
	elif nv == 2:
		soma = vdc + vdc * 0.07
		print (round ( soma , 2 ))
elif mt.upper() == "D":
	soma = vdc * 0.88
	print (round ( soma , 2 ))
elif mt.upper() == "P":
	soma = vdc * 0.88
	print (round ( soma , 2 ))
	