renda = float(input("renda do saba: "))
prestacao = float(input("prestacao para pagar: "))

if prestacao > renda * (15/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")