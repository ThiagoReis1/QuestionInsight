n = int(input("digite um numero: "))
p = 0

while (n != 0):
	if (n % 2 == 0):
		n = int(input("digite um numero: "))
		n = n + 1
		p = (n*100)/n
print(p)