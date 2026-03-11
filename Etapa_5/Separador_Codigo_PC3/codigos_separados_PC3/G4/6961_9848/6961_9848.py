x = int(input('insira o numero x: '))
y = int(input('insira o numero y: '))

i = x # contadora
soma = 0 # acumuladora

while i <= y:
	if i % 3 == 0:
		soma += i
	i += 1
	
print(soma)