x = float(input())

if x < 5000:
	total = x*0.05
	print(round(total,2))
else:
	total = x*0.04 + 60
	print(round(total,2))