numero = int(input("digite: "))
c = numero // 100
g = numero % 100
calculo = (c + g) ** 2
if (calculo == numero):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(numero)
print(mensagem)
