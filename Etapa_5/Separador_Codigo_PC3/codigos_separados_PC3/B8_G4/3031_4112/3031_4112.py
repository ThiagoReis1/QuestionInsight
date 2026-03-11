x=float(input("qual o valor de f(x)?"))
if(x<=1):
	x=1
	print(round(x,2))
elif((1<x)and(x<=2)):
	x=2
	print(round(x,2))
elif((2<x)and(x<=3)):
	x=x**2
	print(round(x,2))
elif(x>3):
	x=x**3
	print(round(x,2))