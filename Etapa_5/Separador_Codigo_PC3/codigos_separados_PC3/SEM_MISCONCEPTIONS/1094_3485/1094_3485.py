numero = int(input("Digite o numero:"))
n1 = numero//1000
n2 = numero%1000

if (numero == (n1+n2)**2):
	print("atende")
else:
	print("nao atende")
print(numero)