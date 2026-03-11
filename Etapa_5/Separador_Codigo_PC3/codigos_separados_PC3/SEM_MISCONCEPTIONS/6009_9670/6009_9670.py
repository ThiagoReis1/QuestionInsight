valorrenda= float(input("valor da renda da dona Fernanda: "))
valorprest= float(input("valor da prestacao: "))

x= valorrenda * 0.30

if valorprest > x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")