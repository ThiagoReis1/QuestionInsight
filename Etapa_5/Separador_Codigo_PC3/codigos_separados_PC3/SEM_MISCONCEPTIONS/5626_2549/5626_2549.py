r = int(input("Valor da renda: "))
p = int(input("Valor da prestacao: "))

if (p > r*0.25):
	mensagem = "Emprestimo nao aprovado"
	
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)