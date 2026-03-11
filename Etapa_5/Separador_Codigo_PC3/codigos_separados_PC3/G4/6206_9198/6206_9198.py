x = int(input("Digite: "))
c = 0

while(x != -1):
	if (x >= 0) and (x <= 25):
		c = c + 1
	x = int(input("Digite: "))
print(c)