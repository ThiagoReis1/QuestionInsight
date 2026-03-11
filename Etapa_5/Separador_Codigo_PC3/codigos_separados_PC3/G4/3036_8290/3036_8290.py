x = float(input('valor de x: '))

if (x <= -1) or (x >= 1):
	fx = x
	
elif (x == 0):
	fx = 2
	
else:
	fx = 1
	
print(round(fx, 2))