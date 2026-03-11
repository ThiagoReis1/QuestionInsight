renda = int(input("qual o valor da renda?: "))
prestacao = int(input("qual o valor da prestacao?: "))

x = 0.25*renda

if prestacao>x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")