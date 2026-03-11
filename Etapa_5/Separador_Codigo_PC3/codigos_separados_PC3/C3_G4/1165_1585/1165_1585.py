n = int(input("Digite um numero:"))
a = 1
sb = 0
b = 1
while (a <= n):
	sb = sb + (a**3/(5+b))
	a = a + 1
	b = b + 2
	sb = sb - (a**3/(5+b))
	a = a + 1
	b = b + 2
print(round(sb,9))
	
