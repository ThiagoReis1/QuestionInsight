renda_saba = float(input("renda do saba:"))
prestacao = float(input("prestacao: "))

porcentagem = (renda_saba * 15) / 100

if (prestacao > porcentagem):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
