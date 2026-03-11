nf = int(input("numero fornecido: "))

a = nf // 10000
b = nf % 10000

if(nf==((a+b)**2)):
	mensagem = "atende"
	
else:
	mensagem = "nao atende"
	
print(nf)
print(mensagem)


