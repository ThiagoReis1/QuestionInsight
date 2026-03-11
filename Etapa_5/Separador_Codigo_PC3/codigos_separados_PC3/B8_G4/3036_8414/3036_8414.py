x = float(input(" qual o valor: "))

if x<= -1 or x>=1:
	print(x)
	
elif -1<x<0 or 0<x<1:
	print(round(1, 2))
	
elif x==0: 
	print(round(2, 2))