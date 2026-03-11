x = int(input())
y = int(input())
n = 0

while x <= y:
	if x % 2 != 0:
		n += x
	x += 1
print(n)
	