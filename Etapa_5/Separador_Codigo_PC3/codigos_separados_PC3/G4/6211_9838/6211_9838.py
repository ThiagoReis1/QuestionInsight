n = int(input("Num val: "))

c1 = 0
c = 0

while (n != -1):
	if (100 <= n <= 199):
		c1 = c1 + 1
	c = c + 1
	n = int(input("Num val: "))

print(c1)