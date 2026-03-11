a=float(input("area"))

if(0<a<10000):
	n=a*5
	print(round(n,2))
else:
	n=(10000*5)+((a-10000)*4)
	print(round(n,2))