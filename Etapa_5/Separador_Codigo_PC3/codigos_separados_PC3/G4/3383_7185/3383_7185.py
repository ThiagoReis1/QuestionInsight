uni = input("unidade de medida esta: L para libras, ou K para quilogramas: ")
val = float(input("valor da medida: "))
if (uni.upper() == "K"):
	lb = 2.20462 * val
	print (round(lb, 2))
if (uni.upper() == "L"):
	kg = val/2.20462
	print (round(kg, 2))