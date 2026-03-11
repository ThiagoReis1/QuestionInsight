n = int(input())
c = 0

while n > -1:
	if (n >= 45) and (n <= 150):
		c += 1
	n = int(input())
	
print(c)