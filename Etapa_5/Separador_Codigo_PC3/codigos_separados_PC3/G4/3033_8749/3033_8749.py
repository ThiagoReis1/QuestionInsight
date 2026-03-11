x = float(input("x: "))

if (x>=-100) and (x<0):
	y = -1/x
	print(round(y,4))
elif (x>0) and (x<=100):
	y = 1/x
	print(round(y,4))
	
else:
	print("entrada invalida")