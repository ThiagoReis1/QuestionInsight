duplas = int(input("Quantas duplas deliciosas: "))

val = duplas*32.9

if (duplas > 3):
	dsc = (val) * (20/100)
	tt = val - dsc
	print(round(tt, 2))
	
else:
	print(round(val, 2))