a = int(input())
x = a//100
y = a%100
if (a == (x + y)**2):
	mensagem = "atende"
	print(a)
	print(mensagem)
else:
	mensagem = "nao atende"
	print(a)
	print(mensagem)