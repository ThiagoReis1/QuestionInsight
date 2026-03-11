product = input()
i = 0
total = 0
while i != len(product):
	if product[i] == 'H':
		total += 5.40
	elif product[i] == 'C':
		total += 8.95
	elif product[i] == 'L':
		total += 4.50
	i += 1
print(round(total, 2))