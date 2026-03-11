x = int(input("Valor de X: "))
y = int(input("Valor de Y: "))
cont = 0 
soma = 0

while x <= y:
	if x % 7 == 0:
		cont = x + x
		soma = soma + cont
print(soma)
	