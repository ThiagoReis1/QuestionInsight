renda = float(input('digite valor renda: '))
prestacao = float(input('valor da prestacao:'))
vp = prestacao > (renda * 0.15)
if vp:
	print("Emprestimo nao aprovado")

else: 
	print("Emprestimo aprovado")
	