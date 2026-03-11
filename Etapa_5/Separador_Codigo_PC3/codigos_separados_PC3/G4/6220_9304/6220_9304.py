x = int(input("X: "))
y = int(input("Y: "))

a = 0

while (x <= y):
	if (y % 3 == 0):
		
		a = a + (y % 3)
		print(a)
	else:
		intervalo = intervalo - 1
print(a)