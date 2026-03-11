renda = float(input("renda dona flor? "))
p_mensal = float(input("valor da prestacao? "))

calc= renda*(25/100)

if (p_mensal > calc):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")