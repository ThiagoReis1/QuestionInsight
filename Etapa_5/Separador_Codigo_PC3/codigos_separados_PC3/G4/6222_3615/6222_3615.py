x = int(input())
y = int(input())

mim = x
soma = 0
while mim <= y:
	if mim%2 == 0:
		soma += mim
	mim +=1
print(soma)