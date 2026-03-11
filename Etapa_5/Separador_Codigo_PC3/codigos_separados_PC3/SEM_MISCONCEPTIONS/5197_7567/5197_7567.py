renda = float(input("Valor da renda do seu Madruga: "))
prestacao = float(input("Valor da prestacao paga por mes: "))

if(prestacao > 0.2 * renda):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")