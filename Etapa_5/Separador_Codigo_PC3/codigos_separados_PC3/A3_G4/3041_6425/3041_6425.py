x= float(input("entre com o valor de x: "))
fx=0
if (x<=-1000 or x > 1000 and x>=-2 or x<2):
	print("entrada invalida")
else:
	if (x >= -1000 and x < -2):
		fx=-1/(x+2)
	else:
		fx=1/(x-2)
	print(round(fx,4))