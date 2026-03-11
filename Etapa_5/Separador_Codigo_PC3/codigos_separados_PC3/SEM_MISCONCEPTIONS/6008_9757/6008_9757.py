renda = float(input("Digite um valor: "))
prestacao = float(input("Digite um valor: "))
porcentagem = renda*(20/100)
if prestacao>porcentagem:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")