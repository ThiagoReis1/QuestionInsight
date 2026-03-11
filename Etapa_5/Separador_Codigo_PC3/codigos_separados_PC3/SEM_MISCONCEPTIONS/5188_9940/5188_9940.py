renda= float(input("renda: "))
prestacao= float(input("prestacao: "))
x= (25/100)*renda

if prestacao>x:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")