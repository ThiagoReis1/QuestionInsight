count = 0

while True:
	num = float(input(": "))
	
	if num == 6:
		count += 1
		continue
	elif  0 < num < 6:
		continue
	elif num == (-1):
		break
	else:
		continue
		
print(count)