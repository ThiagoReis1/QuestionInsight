p = input("unidade de medida").upper()
vm = float(input("valor da medida "))
if(p=="K"):
	oz=35.274*vm
	print(round(oz,2)) 
else:
	z=vm/35.274
	print(round(z,2))