x = float(input('Qual o x: '))
if x <= 0:
	fx = 0
	print(round(fx,4))
elif x > 0 and x <= 1:
	fx = 1
	print(round(fx,4))
elif x > 1 and x <= 2:
	fx = (x) ** (1/2)
	print(round(fx,4))
else:
	fx = (x) ** (1/3)
	print(round(fx,4))