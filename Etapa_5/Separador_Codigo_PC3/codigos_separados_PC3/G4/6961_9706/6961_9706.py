x = int(input())
y = int(input())
soma = 0
i = x
while i <= y:
	if i % 3 == 0:
		soma += i
	i += 1
print(soma)