x = int(input("x:"))
y = int(input("y:"))

soma = 0
i = x

while i <= y:
	if i % 2 == 0:
		soma += i
	i += 1
	
print(soma)