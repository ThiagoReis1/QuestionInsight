X = int(input(" "))
Y = int(input(" "))

soma = 0

while X <= Y:
	if X % 7 == 0:
		soma += X
	X += 1
	
print(soma)


