numero = int(input("Insira um numero de 4 digitos:"))
n1 = numero // 100
n2 = numero % 100

if(n1**2+n2**2==numero):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)