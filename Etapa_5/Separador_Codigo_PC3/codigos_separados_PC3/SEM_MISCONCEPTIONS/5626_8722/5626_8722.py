renda = int(input("Qual a renda de Dona Clotilde? "))
prest = int(input("Qual o valor da prestacao? "))

condicao = renda*(25/100)

if prest > condicao:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")