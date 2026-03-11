vx = float(input("valor de x: "))

if (vx >= -100 and vx <0):
	c = -1/vx
	print(round(c,4))
		
elif (vx >0 and vx <= 100):
	c = 1/vx
	print(round(c,4))

else:
	print("entrada invalida")