x = int(input("digite o valor de x"))
y = int(input("dite o valor de y"))
soma = 0
while x <= y :
	if x % 3 == 0 : 
		soma = soma + x
	x = x + 1
print(soma)