numero = int(input("numero fornecido: "))
valor = (numero // 1000 + numero % 1000)**2
if numero == valor:
	msg = "atende"
else:
	msg = "nao atende"
	
print(msg)
print(numero)