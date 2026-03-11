u = input("digite a unidade de medida:")
v = float(input("digite o valor:"))

if (u.upper()) == "B" : 
	e = v / 3.41214 
	
else: 
	e = 3.41214 * v
	
print(round(e,2))