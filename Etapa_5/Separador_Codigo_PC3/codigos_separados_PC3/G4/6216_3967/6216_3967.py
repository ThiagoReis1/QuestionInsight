x = int(input())
y = int(input())

if x < y:
	while x <= y:
		if x % 5 == 0:
			print(x)
		x = x + 1