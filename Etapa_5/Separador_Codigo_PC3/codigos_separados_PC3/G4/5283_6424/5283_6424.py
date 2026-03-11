n = int(input())
c = 0
p = 0
while n != 0:
	c = c + 1
	if n > 0:
		p = p + 1
	n = int(input())
total = (p/c)*100
print(c)
print(round(total,2))