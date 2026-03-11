prod = input().upper()
i = 0
total = 0
while i < len(prod):
	if prod[i] == 'B':
		total += 6.8
	elif prod[i] == 'C':
		total += 11.75
	else:
		total += 5.9
	i += 1
print(round(total, 2))
