x = int(input())
total = 0

while(x != 0):
	if (x < 0):
		x = int(input())
		continue
		
	if (x > 10):
		x = int(input())
		continue
		
	if x == 1:
		total += 20
	elif x == 2:
		total += 15
	elif x == 3:
		total += 10
	elif x >= 4 and x <= 10:
		total += (11 - x)
	
	x = int(input())

print(total)