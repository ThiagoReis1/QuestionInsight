renda = float(input("Digite o valor da renda: "))
prestacao = float(input("Digite o valor da prestacao: "))

desconto = renda * 15/100

if prestacao >= desconto:
	print("Emprestimo nao aprovado")
	
else: 
	print("Emprestimo aprovado")
