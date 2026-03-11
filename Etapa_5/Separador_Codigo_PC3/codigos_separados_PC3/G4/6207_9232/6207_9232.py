n = int(input("numero: "))
c = 0

while (n != -1):
	if(n >= 26) and (n <= 50):
		c = c + 1
	n = int(input('numero'))
print(c)