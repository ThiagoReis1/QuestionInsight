numeros = int(input("Digite os numeros: "))

num = numeros // 1000
resto = numeros % 1000

propriedade = (num - resto) ** 3

if (propriedade == numeros):
	mensagem = (numeros,"atende a propriedade")
else:
	mensagem = (numeros,"nao atende a propriedade")
	
print(mensagem)
