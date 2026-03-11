x = int(input("x: "))
y = int(input("y: "))
i = 0
while x<=y:
	if x%2!=0:
		i = i + x
	x = x + 1
print(i)