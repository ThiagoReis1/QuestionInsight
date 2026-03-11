x = int(input())
y = int(input())
cont = x
soma = 0 
while cont <= y:
	if cont % 2 != 0:
		soma += cont
	cont += 1
	
print(soma)