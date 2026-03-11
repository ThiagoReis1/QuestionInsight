v_r = float(input("valor da renda: "))
v_p = float(input("valor da prestacao: "))

if  v_p > (v_r * (35/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")