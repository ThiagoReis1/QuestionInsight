valor = int(input())

total = valor//100

resto = valor % 100

if ((total**2) + (resto)**2 == valor):
	
	print("atende")
	print(valor)
else:
	print("nao atende")
	print(valor)