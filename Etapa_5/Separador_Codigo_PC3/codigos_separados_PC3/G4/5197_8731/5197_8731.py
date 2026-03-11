x = float(input("valor da renda do seu madruga: "))
y = float(input("valor da prestacao que ele pode pagar por mes: "))

if y> x *(20/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
