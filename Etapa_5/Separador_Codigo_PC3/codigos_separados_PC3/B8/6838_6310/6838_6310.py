prods = input()
prods = prods.upper()
total = 0.0
for i in prods:
	if i == 'D':
		total += 2.25
	elif i == 'S':
		total += 4.0
	elif i == 'I':
		total += 6.9
print(round(total,2))