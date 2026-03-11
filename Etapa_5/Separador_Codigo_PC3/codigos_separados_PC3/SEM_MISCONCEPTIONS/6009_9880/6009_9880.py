# Inserindo valores de entrada

renda = float(input("Qual o valor da renda da Dona Fernanda?: "))
prestacao = float(input("Qual o valor da prestacao que ela pode pagar por mes?: "))

if prestacao > 0.30 * renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")