x = float(input("valor de x: "))

if ( x>=-100) and (x<0):
	a = (-(1/x))
	print(round(a,4))
elif (x >0) and (x<=100):
	a = (1/x)
	print(round(a,4))
else:
	print("entrada invalida")