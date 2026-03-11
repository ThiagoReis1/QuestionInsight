x = int(input("valor de x:"))
y = int(input("valor de y:"))
n = 0
while x<= y :
	if (x % 3 == 0):
		n = n + x
	x = x + 1
print(n)