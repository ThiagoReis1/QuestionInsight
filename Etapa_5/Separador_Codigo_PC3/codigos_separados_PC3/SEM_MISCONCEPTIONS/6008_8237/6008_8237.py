v_renda = float(input("Digite um valor:"))
v_prestacao = float(input("Digite um valor:"))
d = v_renda * (20/100)
if(v_prestacao > d):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")