n = int(input("digite o numero de 4 digitos: "))

a = (n //100)
resto_a = n % 100
b = resto_a

soma = (a**2) + (b**2)

if(soma == n):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)