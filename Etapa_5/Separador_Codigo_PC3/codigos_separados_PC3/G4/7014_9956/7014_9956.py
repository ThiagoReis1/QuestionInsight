x = int (input("digite o numero"))
y = int (input("digite o numero"))

soma = 0
cont = x

while cont <= y:
	if cont % 2 != 0 :
		soma = soma + cont
	cont = cont + 1
	
print(soma)
	