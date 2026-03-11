y=input("unidade: ")
x=float(input("conversao: "))


if(y=="H"):
	z=2.47105*x
else:
	z=x/2.47105
	
print(round(z,2))