vx = float(input("valor de x: "))

if vx >= -1000 and vx < -2:
	fx = -(1/(vx+2))
	print(round(fx, 4))
elif vx > 2 and vx <= 1000:
	fx = 1/(vx-2)
	print(round(fx, 4))
	
else:
	fx = "entrada invalida"
	print(fx)
	
