x = float(input())
y = float(input())

while x <= y:
	z = x % 5
	if z == 0:
		print(int(x))
	x += 1