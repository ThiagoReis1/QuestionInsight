vl_renda = float(input("Renda: "))
vl_prest = float(input("Valor da Prestacao: "))

if vl_prest > vl_renda * (25/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")