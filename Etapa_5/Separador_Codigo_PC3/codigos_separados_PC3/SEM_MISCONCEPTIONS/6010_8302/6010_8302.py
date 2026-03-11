renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

vt = renda * (35/100)

if prestacao > vt:
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"

print(mensagem)
