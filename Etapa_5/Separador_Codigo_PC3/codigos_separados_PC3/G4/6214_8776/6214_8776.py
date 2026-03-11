n = int(input())
c = 0
while n != -1:
	if n <= 150 and n >= 45:
		c = 1 + c
	n = int(input())
print(c)