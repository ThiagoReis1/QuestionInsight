x = input("")

a = 5.00
b = 3.50
c = 4.00
if(x == "L"):
	y = float(input(""))
	z = float(input(""))
	total = (y * a) + (z * c)
	print(round(total, 2))
if(x == "S"):
	y = float(input(""))
	z = float(input(""))
	total1 = (y * b) + (z * c)
	print(round(total1, 2))