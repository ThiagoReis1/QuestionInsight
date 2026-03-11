renda= float(input("Valor da renda: "))
prestacao= float(input("Valor da prestacao por mes: "))

x= (0.20*renda)

if(prestacao > x):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")