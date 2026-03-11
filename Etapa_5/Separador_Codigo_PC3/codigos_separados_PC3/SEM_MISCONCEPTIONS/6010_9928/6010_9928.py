renda = float(input("Insira o valor da renda:"))
prestacao = float(input("Insira o valor da prestacao"))

porcentagem = renda * 35/100
if (prestacao > porcentagem):
	print ("Emprestimo nao aprovado")
else:
	print ("Emprestimo aprovado")