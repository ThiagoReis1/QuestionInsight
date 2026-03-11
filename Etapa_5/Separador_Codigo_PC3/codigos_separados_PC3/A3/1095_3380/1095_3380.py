numero = int(input())
				 
var1 = numero // 10000
res1 = numero % 10000	
				 
var2= var1 // 10000
res2 = var1%10000

calculo = (res1+res2)**2 
print(numero)

if(calculo == numero):
	mensagem = "atende"
	print(mensagem)
else:
	mensagem = "nao atende"
	print(mensagem)
				 