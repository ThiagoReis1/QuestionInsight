x = int(input("quantidade de cachos: "))

if x >= 3:
	y = x * 4.25
	print(round(y, 2))
else:
	y = x * 5.00
	print(round(y, 2))