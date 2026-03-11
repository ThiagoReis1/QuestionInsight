num=int(input("numero fornecido:"))


b=(num//100)
c=num%100


if(num==(b**2)+(c**2)):
	mensagem="atende"
	
else:
	mensagem="nao atende"
	
print(mensagem)
print(num)