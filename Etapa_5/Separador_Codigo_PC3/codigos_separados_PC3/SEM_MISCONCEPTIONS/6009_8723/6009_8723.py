renda = float(input("Valor da renda: "))
presta = float(input("Valor da prestacao: "))

if(presta >= renda*(35/100)):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")