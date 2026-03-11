x = int(input("digite x: "))
y = int(input("digite y: "))
soma = 0
i = x

while i <= y:
	if i % 2 == 0:
		soma = soma + i
	i = i + 1
print(soma)