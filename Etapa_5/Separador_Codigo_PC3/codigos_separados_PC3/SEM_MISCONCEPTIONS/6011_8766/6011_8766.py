renda = float(input("Digite o valor da renda:"))
prestacao = float(input("Digite o valor da prestacao:"))
 
if prestacao >  35/100 * renda:
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")