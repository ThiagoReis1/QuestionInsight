x = float(input("Informe o valor de x: "))

if(x<=1):
	x = 1
	print(round(x,2))
elif(1<x<=2):
	x = 2
	print(round(x,2))
elif(2<x<=3):
	x = x**2
	print(round(x,2))
elif(x>3):
	x = x**3
	print(round(x,2))
