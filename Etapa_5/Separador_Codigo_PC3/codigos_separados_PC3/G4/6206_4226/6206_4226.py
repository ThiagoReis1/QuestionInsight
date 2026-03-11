n = int(input("> "))
c = 0

while n != -1:
	if n >= 0 and n <= 25:
		c = c+1
	n = int(input("> "))
print(c)