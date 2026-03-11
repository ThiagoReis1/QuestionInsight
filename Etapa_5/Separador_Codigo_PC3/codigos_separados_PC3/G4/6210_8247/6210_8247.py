num = int(input())
c = 0
while num >= 0:
	if num >= 35 and num <= 95:
		c = c + 1
	num = int(input())
print(c)