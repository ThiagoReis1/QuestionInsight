tomates = int(input(""))

if (tomates < 4):
	total = tomates * 0.75
else:
	total = tomates * 0.55
	
print(round(total, 2))