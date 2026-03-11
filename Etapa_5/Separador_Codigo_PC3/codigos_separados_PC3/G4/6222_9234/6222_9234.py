x = int(input("digite um numero: "))
y = int(input("digite um numero: "))

c = x
soma = 0

while ( c <= y):
	if c % 2 == 0:
		soma = soma + c
	c = c + 1
print(soma)