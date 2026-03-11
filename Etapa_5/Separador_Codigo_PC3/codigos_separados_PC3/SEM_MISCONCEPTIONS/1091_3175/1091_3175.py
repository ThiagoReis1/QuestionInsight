numero = int(input("digite um numero: "))
n1 = numero//100
n2 = numero%100

print(numero)

if (numero == (n1 + n2)**2):	
	print("atende")
else:	
	print("nao atende")

