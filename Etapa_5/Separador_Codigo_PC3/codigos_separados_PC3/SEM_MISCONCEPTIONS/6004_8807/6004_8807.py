tomates = int(input("Tomates: "))

if tomates < 4:
	print(round(tomates * 0.75, 2))
else:
	print(round(tomates * 0.55, 2))