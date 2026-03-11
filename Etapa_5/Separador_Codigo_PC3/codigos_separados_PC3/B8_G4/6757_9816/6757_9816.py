n = int(input('Digite o numero de pizzas'))
fixo=5.00

if n<3:
	c= 3.00+n*fixo
	print(round(c,2))
elif n==3:
	p = 3.25 +fixo*n
	print(round(p,2))
elif n>3:
	k = 4.50+(fixo*n)
	print(round(k,2))