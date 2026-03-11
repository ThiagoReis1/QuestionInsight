x = int(input("X :"))
y = int(input("Y: "))
soma = x
while x<y:
	x = x + 1
	if x%2!=0:
		soma = x + soma
		x = x + 1
print(soma)
		