uni=input("Unidade:")
valor=float(input("medida:"))
if(uni=="L"):
	k=(valor/2.20462)
	print(round(k,2))
else:
	l=(2.20462*valor)
	print(round(l,2))

