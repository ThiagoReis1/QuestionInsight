a=float(input("a area fertilizada?"))
if(a <= 10000):
	print(round(a * 5,2))
	
else:
	b=a-10000
	valor=5*10000+4*b
	print(round(valor,2))