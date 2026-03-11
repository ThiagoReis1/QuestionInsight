roupa  = int(input('quantidade de roupas:'))
if roupa < 10:
	v = 30 + 3.25
	print(round(v, 2))
	
elif roupa == 10:
	v = 30 + 4.50
	print(round(v, 2))
	
elif roupa > 10:
	v = 30 + 6.00
	print(round(v, 2))
