x=int(input('insira um numero:'))
y=int(input('insira um numero:'))

i=x
soma=0

while i <= y:
	if i % 2 == 0:
		soma += i
	i += 1
	
print(soma)