x=float(input("Qual o valor de x?: "))
if(x<=1):
	R=1
	print(R)
elif(1<x)and(x<=2):
	R=2
	print(R)
elif(2<x)and(x<=3):
	n=(x**2)
	R=round(n,2)
	print(R)
else:
	n=x**3
	R=round(n,2)
	print(R)