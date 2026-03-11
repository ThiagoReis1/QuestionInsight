107097 = int(input("Qual o numero?"))

107097 = numero // 1000
resto = numero % 1000
propriedade = (107097 - resto) ** 4

if(107097 == numero):
	mensagem = ("107097 atende a propriedade")
else:
	mensagem = (propriedade)
	
print(mensagem)