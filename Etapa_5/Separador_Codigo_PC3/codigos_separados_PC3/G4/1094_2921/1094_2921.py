numero= int(input())
x = numero//1000
b= numero%1000
V= ((x+b)**2)
if (numero == V):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)