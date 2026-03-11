
x = int(input("x:"))

digito1 = x // 100
resto1 = x % 100
digito2 = resto1 // 20
resto2 = resto1 % 20

soma = (digito1**2 + digito2**2)

if( x == soma ):
	print("X atende a propriedade")
else:
	print(soma)



