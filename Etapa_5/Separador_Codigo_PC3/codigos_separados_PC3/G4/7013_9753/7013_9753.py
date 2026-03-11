x = int(input("valor de x: "))
y = int(input("valor de y: "))
soma = 0

while x <= y :
	if x % 2 == 0:
		soma= soma + x
	x = x +1 

print(soma)