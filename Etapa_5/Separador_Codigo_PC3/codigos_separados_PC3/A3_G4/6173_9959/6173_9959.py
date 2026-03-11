x = input ().upper()

cont = 0
soma = 0

while x != 'S':
	if x == 'SIM':
		soma += 1
	cont += 1
	x = input().upper()
	
print(soma)