x = int(input("X: "))
y = int(input("Y: "))
c = x

while x < y and x%5 == 0 and c <= y:
	if c%5 == 0:
		print(c)
	c = c + 1