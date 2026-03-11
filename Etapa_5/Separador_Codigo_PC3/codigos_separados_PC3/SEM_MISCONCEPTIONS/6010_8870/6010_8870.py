renda = float(input("digite a renda: "))
prestacao = float(input("valor da prestacao: "))

x = renda*(35/100) 

if prestacao >= x:
	mensagem = "Emprestimo nao aprovado"
	
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)