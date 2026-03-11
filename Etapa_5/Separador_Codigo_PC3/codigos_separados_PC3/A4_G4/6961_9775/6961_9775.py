X = int(input())
Y = int(input())
sum = 0
elevator = X

while elevator <= Y:
	if elevator % 3 == 0:
		sum = sum + elevator
	elevator = elevator + 1
print(sum)