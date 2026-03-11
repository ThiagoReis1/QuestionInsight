v_renda = int(input("Digite o valor da renda: "))
v_prestacao = int(input("Digite o valor da prestacao: "))

v = (v_renda * (25/100))

if v_prestacao > v:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")