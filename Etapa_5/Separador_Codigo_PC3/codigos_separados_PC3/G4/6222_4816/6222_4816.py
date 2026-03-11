X = int(input())
Y = int(input())

soma = 0

while X <= Y:
	if X%2 == 0:
		soma = soma+X
	X += 1
print(soma)