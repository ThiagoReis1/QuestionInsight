v_renda = int(input("qual o valor da renda: "))
V_prest = int(input("valor ada prestacao que ela pode pagar: "))



if V_prest > v_renda * 0.25:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	