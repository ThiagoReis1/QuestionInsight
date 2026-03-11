x = float(input("X: "))

if(x >= -100 and x < 0):
	fx = -(1/x)
	print(round(fx,4))
elif(x > 0 and x <= 100):
	fx = (1/x)
	print(round(fx,4))
else:
	print("entrada invalida")