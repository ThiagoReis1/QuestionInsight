renda = float(input("Digite o valor da renda: "))
prestacao = float(input("Digite o valor da prestacao: "))
porcentrenda = (25/100) * renda
if prestacao > porcentrenda:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")