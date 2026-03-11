x = input()
y = float(input())

if x == 'K':
	total = y/(1.60934)
	print(round(total,2))
else:
	total = y*1.60934
	print(round(total,2))
