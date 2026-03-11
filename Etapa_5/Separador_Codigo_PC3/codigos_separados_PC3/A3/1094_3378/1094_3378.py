numero= int(input())

var1=numero//1000
res1=numero%1000

var2=var1//1000
res2=var1%1000

calculo= (res1+res2)**2


if(calculo==numero):
	mensagem = "atende"
	print(mensagem)
else:
	mensagem= "nao atende"
	print(mensagem)
	
print(numero)