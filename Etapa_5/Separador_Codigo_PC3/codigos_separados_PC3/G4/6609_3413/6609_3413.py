def div():
	value = int(input())
	while value != 0:
		if value % 3 == 0:
			print(value)
			value += 3
		else:
			div = value % 3
			if div == 2:
				value += 1
			else:
				value += 2
	print(value)
	print("fim")
	
div()