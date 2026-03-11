numero = int(input("Digite um numero = "))
d1 = numero // 1000
d2 = numero % 1000
subtracao = d1 - d2
calculo = subtracao**2
if numero == calculo :
	print("atende")
else :
	print("nao atende")
print(numero)

