n = int(input("entre com um numero: "))

contadora = 0

while (n != -1):
	if (n >= 76 and n <= 100):
		contadora = contadora + 1
	n = int(input("entre com um numero: "))
	
print(contadora)