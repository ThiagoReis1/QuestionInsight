x  = float(input("valor de x?: "))

if ( (x >= -1000) and ( x < -2)):
	conta = -( 1 / ( x + 2))
	print(round(conta, 4))
elif ((x > 2) and (x <= 1000)):
	conta = (1 / (x - 2))
	print(round(conta, 4))
else:
	print("entrada invalida")