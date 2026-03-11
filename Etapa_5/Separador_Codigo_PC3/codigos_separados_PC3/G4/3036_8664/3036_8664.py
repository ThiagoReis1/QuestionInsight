x = float(input("Valor de x: "))

if (x<=-1)or(x>=1):
	fx = x
	print(round(fx, 2))
elif (-1 < x < 0) or (0 < x < 1):
	fx = 1
	print(round(fx, 2))
else: 
	fx = 2
	print(round(fx, 2))
	