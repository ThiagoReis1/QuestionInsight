U = input("digite A para acres e H para hectares: ").upper()
var = float(input("digite o valor da medida: "))

A = (2.47105 * var)
H = (var/2.47105)

if (U == "A"):	
	print(round(H,2))
else:	
	print(round(A,2))