x = int(input("insira um numero: "))
y = int(input("insira o numero: "))

c = x

while c <= y:
	if(c % 3 == 0):
		c = c + x
	
print(c)