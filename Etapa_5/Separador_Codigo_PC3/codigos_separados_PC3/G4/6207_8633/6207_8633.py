n = int(input("abra o numero: "))
c = 0

while(n >= 0):
	if(26 <= n <= 50):
		c = c + 1
	n = int(input("abra o numero: "))
print(c)