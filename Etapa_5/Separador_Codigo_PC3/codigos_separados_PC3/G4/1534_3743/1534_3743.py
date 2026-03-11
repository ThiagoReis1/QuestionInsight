x = float(input())
k = int(input())
a = 0
c = 0
y = 2 * c + 1
while k != c:
	c = c + 1
	a = a + 1 
	x = x + (x**y / y)
	y = 2 * c + 1
print(round(x,7))