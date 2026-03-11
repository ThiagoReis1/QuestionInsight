x = int(input())
y = int(input())
soma = 0
while x <= y:
	if x % 3 == 0:
		soma = soma + x
	x = x + 1
print(soma)	