X = int(input("Insira um numero: "))
Y = int(input("Insira um numero: "))

l = X

while l <= Y:
	if l % 7 == 0:
		print(l)
	l += 1
