x = float(input("valor de x:"))

if((x >= -1000) and (x < -2)):
	y = -(1/(x+2))
	y = round(y, 4)
	print(y)
elif((x < 2) and (x <= 1000)):
	y = (1/(x-2))
	y = round(y,4)
	print(y)
else: 
	print("entrada invalida")