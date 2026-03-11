n = int(input("Numero: "))
c = 0

while (n>0):
	if (n>=100) and (n<=199):
		c = c + 1
	n = int(input("Numero: "))
print(c)