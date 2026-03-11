x = input("unidade (K/L)")

if(x == "L"):
	lb = float(input("valor: "))
	kg = lb/2.20462 
	print(round(kg ,2))
else:
	kg = float(input("valor: "))
	lb = 2.20462 * kg
	print(round(lb,2))