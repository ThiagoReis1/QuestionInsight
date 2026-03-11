nf = int(input("numero fornecido"))
n1 = (nf//10000)
n2 = (nf % 10000)
print(nf)
calculo = (n1+n2)**2
if(calculo == nf):
	mensagem = "atende"
	print(mensagem)
else:
	mensagem = "nao atende"
	print(mensagem)
