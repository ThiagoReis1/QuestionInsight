valor_renda = int(input())
valor_prest= int(input())
if valor_prest > 0.25 * valor_renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")