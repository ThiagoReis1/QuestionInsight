renda = float(input("Insira o Valor da Renda de Seu Paulo: "))
prestacao = float(input("Insira o Valor da Prestacao que ele pode pagar por mes: "))

if prestacao > 25 * (renda / 100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")