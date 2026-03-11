esp= float(input('inserir numero de espigas de milho compradas:'))

if esp>6:
	y= 1.5*esp
	print(round(y,2))
else:
	x= 1.85*esp
	print(round(x,2))