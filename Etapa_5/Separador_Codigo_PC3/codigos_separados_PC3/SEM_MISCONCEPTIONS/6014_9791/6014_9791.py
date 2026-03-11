valor_renda=float(input())
valor_prest=float(input())
if valor_prest>0.35*valor_renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")