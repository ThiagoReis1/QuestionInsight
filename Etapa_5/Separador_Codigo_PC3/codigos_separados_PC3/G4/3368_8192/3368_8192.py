E = input("Escala?: ")
V = float(input("valor da temperatura?: "))

E1 = E.lower()
if ( E1 == "c" ):
	K = V + 273.15
else:
	K = V - 273.15
	
print(round(K, 2))