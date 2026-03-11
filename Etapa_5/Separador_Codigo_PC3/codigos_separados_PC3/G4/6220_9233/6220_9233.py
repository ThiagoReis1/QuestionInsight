x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))

i = x
soma = 0 

while i <= y:
	if i % 3 == 0:
		soma = soma + i
	i = i + 1
print(soma)