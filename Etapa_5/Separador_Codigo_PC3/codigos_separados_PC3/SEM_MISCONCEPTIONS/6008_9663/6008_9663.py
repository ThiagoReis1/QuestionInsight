vlr_renda = float(input("Escreva o valor da renda: "))
vlr_prestacao = float(input("Escreva o valor da prestacao: "))

if vlr_prestacao > (vlr_renda * 0.20):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	