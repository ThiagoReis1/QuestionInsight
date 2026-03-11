renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

parcela = renda * .20

if prestacao > parcela:
	mensagem = "Emprestimo nao aprovado"

else:
	mensagem = "Emprestimo aprovado"

print(mensagem)