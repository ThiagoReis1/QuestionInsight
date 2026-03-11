nom1 = input("unidade em que a medida está: ")
val = float(input("valor da medida: "))

if( nom1.upper() == "H" ):
	Acre = 2.47105 * val
	print(round(Acre, 2))
	
else: 
	H = val / 2.47105 
	print(round(H, 2))