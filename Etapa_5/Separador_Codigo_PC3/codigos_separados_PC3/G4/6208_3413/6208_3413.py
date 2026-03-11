def sorte():
	value = int(input())
	count = 0
	while value != -1:
		if value >= 51 and value <= 75:
			count += 1
		value = int(input())
	print(count)
	
sorte()