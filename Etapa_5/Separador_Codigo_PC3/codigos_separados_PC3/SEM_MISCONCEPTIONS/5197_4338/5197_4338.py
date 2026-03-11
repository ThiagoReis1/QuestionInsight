condicao = 0.2 #percentual de renda x mensalidade para aprovacao

renda = float(input("Renda mensal: "))
prestacao = float(input("Parcela mensal a ser paga: "))

if ((renda * condicao) < prestacao):
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"
print(mensagem)