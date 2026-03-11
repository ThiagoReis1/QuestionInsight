var1=input("unidade em que a medida esta: ")
var2=float(input("valor da medida: "))

#comando
if var1.upper == "O":
	Kg= var2 * 35.274
	print(Kg)
else:
	Kg= var2 / 35.274
	print(round(Kg, 2))
	
	


