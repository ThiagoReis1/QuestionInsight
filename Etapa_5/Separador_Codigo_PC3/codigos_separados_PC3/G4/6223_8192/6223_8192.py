x = int(input("x?: "))
y = int(input("y?: "))

soma = 0
while ( x <= y ):
	if ( x % 2 == 1):
		soma = soma + x
	x = x + 1
print(soma)