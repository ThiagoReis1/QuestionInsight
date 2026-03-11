q = int(input())
if q < 6:
	total = q * 1.85
	print(round(total, 2))
else:
	total = q * 1.50
	print(round(total, 2))