ce = float(input("ce: ")) 
if (ce <= 150):
	x = (ce * 0.60) + 5.00
	print(round(x, 2))
else: 
	x = (ce * 0.75) + 16.00
	print(round(x, 2))