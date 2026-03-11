x = int(input("x?"))
y = int(input("y?"))
i = x
soma = 0
while i<=y:
	if i%2 != 0 :
		soma = soma + i
	i = i+1
print(soma)
		