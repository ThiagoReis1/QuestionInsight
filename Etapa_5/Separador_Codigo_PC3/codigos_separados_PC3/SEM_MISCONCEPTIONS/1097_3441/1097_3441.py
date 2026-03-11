numero_fornecido= int(input())
#variaveis
x= (numero_fornecido//1000)
y= (numero_fornecido%1000)
#calculo
calculo= (x-y)**2
#condicoes
if (calculo == numero_fornecido):
	print("atende ")
	print(numero_fornecido)
else:
	print("nao atende ")
	print(numero_fornecido)
