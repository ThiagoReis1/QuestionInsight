x = input()
y = float(input())

if x == "C":
	total = (0.393701)*y
	print(round(total,2))
else:
	total = (y)/(0.393701)
	print(round(total,2))