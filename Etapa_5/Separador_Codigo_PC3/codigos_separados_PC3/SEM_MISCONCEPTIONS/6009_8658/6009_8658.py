renda = float(input("valor renda: "))
prest = float(input("prestacao: "))

if prest > renda*0.3:
	mensagem = "Emprestimo nao aprovado"
	
else:
	mensagem = "Emprestimo aprovado"

print(mensagem)