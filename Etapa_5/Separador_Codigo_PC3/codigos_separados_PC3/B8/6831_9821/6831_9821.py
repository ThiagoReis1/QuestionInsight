prod = input('produtos desejados:').upper()

i = 0
total = 0

while i < len(prod):
	if  prod[i] == 'A':
		total += 16.75
	elif prod[i] == 'L':
		total += 4.6
	elif prod[i] == 'P':
		total += 2.85
	i += 1

print(round(total,2))