numero = int(input("digite um numero ineiro de 4 digitos: "))
n1 = numero // 100
n2 = numero % 100
if(numero == ((n1**2) + (n2**2))):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)