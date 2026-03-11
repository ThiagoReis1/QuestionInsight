a=float(input("altura: "))
b=input("sexo: ")

if  (a < 1.0 or a > 2.5):
	print("altura invalida")
else:	
	if	( b == "M" or b == "F"):
		if(b == "M"):
			b=(72.7*a)-58
			print(round(b,2))
		elif(b == "F"):
			a=(62.1*a)-44.7
			print(round(a,2))
	else:
		print("codigo invalido de sexo")
	
	
