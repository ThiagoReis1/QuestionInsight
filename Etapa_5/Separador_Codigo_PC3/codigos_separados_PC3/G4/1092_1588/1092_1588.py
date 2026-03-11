n = int(input("Digite um numero:  "))

a1 = n // 100
ra1 = n % 100
a2 = ra1 // 50
ra2 = a1 % 50
a3 = ra2 // 10

soma = (a1**3) + (a2**3) + (a3**3)

if(n // 2 == 0):
	mensagem = n
	mensagem1 = ("atende a propiedade")
	print(mensagem)
	print(mensagem1)
else:
	print(soma)