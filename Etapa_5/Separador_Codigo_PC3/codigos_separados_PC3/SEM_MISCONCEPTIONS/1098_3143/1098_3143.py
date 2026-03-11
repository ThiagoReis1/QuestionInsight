numero = int(input("numero :"))
c = numero // 1000 
e  = numero % 1000
print(int(numero))
if ((c - e)**4 == numero):
	mensagem = "atende"
else:
	mensagem = "nao atende"
	
print(mensagem)

