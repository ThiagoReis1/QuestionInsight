x  = input()
y = float(input())

if x == 'C':
	total = y + 273.15
	print(round(total,2))
else:
	total = y - 273.15
	print(round(total,2))