x = int(input("x: "))
y = int(input("y: "))
num_por3 = 0
num = x
while (num < y):
	if(num % 3 == 0):
		num_por3 += num

print(num_por3)