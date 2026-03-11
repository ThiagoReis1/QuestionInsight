renda = float(input("Renda: "))
prestacao = float(input("Prestacao: "))
valor = renda*(0.15)
if(prestacao>valor):
	mens = "Emprestimo nao aprovado"
	print(mens)

else:
	mens = "Emprestimo aprovado"
	print(mens)
	