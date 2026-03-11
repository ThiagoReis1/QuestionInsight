X = int(input('Digite o valor de x:'))
Y =  int(input('Digite o valor de y:'))

soma = 0


while X <= Y:
	if X % 7 == 0:
		soma = soma + X
	X = X + 1	
			
print(soma)
			
			
			