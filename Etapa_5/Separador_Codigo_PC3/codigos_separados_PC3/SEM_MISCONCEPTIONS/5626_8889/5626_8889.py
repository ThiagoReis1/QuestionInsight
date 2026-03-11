valor_da_renda = float(input(""))
valorpago = float(input(""))
valordaprestacao = (valor_da_renda * 25/100)

if valorpago > valordaprestacao:

	print("Emprestimo nao aprovado")

else: 
	print("Emprestimo aprovado")