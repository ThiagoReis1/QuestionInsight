r= float(input("Valor da renda: "))
p= float(input("Valor da prestacao: "))

if(p>(0.25*r)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")