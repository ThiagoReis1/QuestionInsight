d=float(input("digite a distancia"))
t=float(input("digite o total"))

dt=(d*1000)

if t>dt:
	x= dt+10000
	print(x)
	print("vai conseguir")
	
else:
	t<dt
	print("nao vai conseguir")