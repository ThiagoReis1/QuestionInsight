l_s = input("L/S? ")
quant = float(input("quantos? "))
refris = float(input("quantos refris? "))

if (l_s == "L"):
	calc = ((quant*5)+(refris*4))
	print(round(calc,2))
else:
	calc = (quant*3.50)+(refris*4)
	print(round(calc,2))