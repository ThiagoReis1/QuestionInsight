n = int(input("numero magico: "))

c = 0

while (n >= 0):
	if (n >= 26 and n <= 50):
		c = c + 1
		
	n = int(input("numero magico: "))
	
print(c)