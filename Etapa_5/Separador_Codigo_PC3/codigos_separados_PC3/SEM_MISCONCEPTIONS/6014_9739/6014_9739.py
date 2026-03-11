valorR = float(input("Informe o valor da renda: "))
valorP = float(input("Informe o valor da prestacao: "))

if valorP > valorR * (35/100):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")