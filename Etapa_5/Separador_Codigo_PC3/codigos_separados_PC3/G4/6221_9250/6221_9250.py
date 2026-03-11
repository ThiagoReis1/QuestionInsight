x = int(input())
y = int(input())
cont = 0
soma = 0

while x <= y:
	x / 7
	if x % 7 == 0:
		soma = soma + x
	cont = cont + 1
	x = x + 1
		
print(soma)