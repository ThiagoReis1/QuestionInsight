valorrenda = float(input("digite o valor de renda: "))
valorprestacao = float(input("digite o valor da prestacao: "))

if valorprestacao > '25':
	valortotal = valorrenda * 25/100
	print("Emprestimo nao aprovado: ")
	
else:
	print("Emprestimo aprovado: ")