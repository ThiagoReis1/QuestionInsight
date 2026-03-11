preco = float(input("Informe o valor consumido: "))

if (preco <= 300):
	 mensagem = (preco + (preco * 0.1))
else:
	 mensagem = (preco + (preco * 0.06))
		
print (round(mensagem,2))		
		