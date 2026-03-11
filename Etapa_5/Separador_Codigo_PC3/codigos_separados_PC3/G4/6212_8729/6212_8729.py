c = 0

while True:
	n = int(input('numero: '))
	
	if (n < 0):
		break
	if 26 <= n <= 85:
		c += 1
print(c)