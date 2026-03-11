c = 0

while True:
	n = int(input("numero: "))
	
	if (n < 0):
		break
	if 0 <= n <= 25:
		c+=1
	
print(c)