valor_renda = float(input("poe ai, seu carlos, o valor da renda: "))
valor_prest = float(input("pode pagar quanto por mes?: "))

if valor_prest > (0.20 * valor_renda):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")