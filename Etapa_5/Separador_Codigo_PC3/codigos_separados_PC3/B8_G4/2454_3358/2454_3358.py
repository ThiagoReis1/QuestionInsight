a=float(input("Altura em m: "))
b=input("Sexo em M ou F:")
if(a< 1.0 and a> 2.5 or b!="M"and b!="F"):
	print("altura invalida")
	print("codigo invalido de sexo")
else:
	if(b=="M"):
		c= 72.7* a -58
	elif(b=="F"):
		c= 62.1* a -44.7
	print(round(c,2))
	