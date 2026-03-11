x = int(input("Qual o valor de X? "))
y = int(input("Qual o valor de Y? "))
cont = 0
soma = 0
while ( x <= y ):
	if(x % 2 == 0):
		soma = soma + x
	x = x + 1
print(soma)
