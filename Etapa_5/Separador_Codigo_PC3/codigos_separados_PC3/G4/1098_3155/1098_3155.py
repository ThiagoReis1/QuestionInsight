numero = int(input("Numero: "))
n1 = numero // 1000
n2 = numero % 1000
n3 = (n1 - n2) ** 4
if(numero == n3):
	n3 = (n1 - n2) ** 4
	print(numero)
	print("atende")
else:
	n3 = (n1 - n2) ** 4
	print(numero)
	print("nao atende")