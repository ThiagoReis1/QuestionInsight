h = float(input("altura do cabra: "))
s = input("sexo do cabra: ")

fm = (72.7 * h) - 58
ff = (62.1 - h) - 44.7

if((h>=1) and (h<=2.5)):
	if(s == "M"):
		print(round(fm, 2))
	elif(s == "F"):
		print(round(ff, 2))
	else:
		(print("codigo invalido de sexo"))
else:
	print("altura invalida")