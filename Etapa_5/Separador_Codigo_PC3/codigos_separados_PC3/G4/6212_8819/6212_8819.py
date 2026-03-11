n = int(input())
c = 0

while n >= 0:
	if n >= 26 and n <= 85:
		c = c + 1
	n = int(input())
print(c)