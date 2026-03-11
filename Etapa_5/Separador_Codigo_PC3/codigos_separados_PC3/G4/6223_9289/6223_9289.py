X  = int(input("Digite o valor de X: "))
Y  = int(input("Digite o valor de Y: "))

soma = 0 
resto = X % 2

if resto == 0: 
	X += 1 
	
while X <= Y:
	soma += X
	X += 2

print(soma)
	
	