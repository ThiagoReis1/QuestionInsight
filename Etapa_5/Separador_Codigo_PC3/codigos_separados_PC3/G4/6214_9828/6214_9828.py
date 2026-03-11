n = int(input("N: "))
c = 0

while n != -1:
	if n >= 45 and n <= 150:
		c = c + 1
	n = int(input("N: "))

print(c)