x = int(input("insira o valor:"))
y = int(input("insira o valor:"))

a = x
soma = 0

while a <= y:
	if(a % 3 == 0):
		soma += a
	a = a + 1
print(soma)