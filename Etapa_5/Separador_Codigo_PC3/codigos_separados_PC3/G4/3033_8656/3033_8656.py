x=float(input("valor de x: "))

if(x <= -100 or x < 0):
	x= -1/x
	print(round(x,4))
elif (x < 0 or x<= 100):
	x= 1/x
	print(round(x,4))
	
else:
	print("entrada invalida")
	