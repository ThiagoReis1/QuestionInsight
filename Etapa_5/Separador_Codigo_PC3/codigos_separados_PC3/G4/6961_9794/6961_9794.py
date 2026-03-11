x = int(input("Insira o numero: "))
y = int(input("Insira o numero: "))
soma = 0
i = x
while i <= y:
	if i%3==0:
		soma= soma + i
	i = i + 1
print(soma)