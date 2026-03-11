n = int(input("insira um numero: "))
c = 0

while n > 0:
	if(n >=100) and (n <= 199):
		c = c + 1
	n = int(input("insira um numero: "))
print(c)