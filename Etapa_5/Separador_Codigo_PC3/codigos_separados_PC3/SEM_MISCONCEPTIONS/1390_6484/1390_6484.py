x = float(input())


if x <= 100:
	total = x*1.20
	print(round(total,2))
else:
	total = 25 + (x*1.40)
	print(round(total,2))