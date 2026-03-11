r = float(input(":"))
m = float(input(":"))
b = float(input(":"))
o = float(input(":"))

conta = (r * 7) + (m * 6) + (b * 3) + (o * 5)

if conta <= 42 :
	total = conta - 3
	print(round(total,2)," ryous")
	
else:
	total = conta - (conta * 0.10)
	print(round(total,2)," ryous")