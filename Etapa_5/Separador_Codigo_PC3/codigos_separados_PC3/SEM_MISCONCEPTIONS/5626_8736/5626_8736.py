renda = float(input("Renda da sr Clotilde :"))
prestacao = float(input("Prestacao ao mes :"))
						
if (prestacao >= (25/100) * renda) :
	print("Emprestimo nao aprovado")
						
else :
	print("Emprestimo aprovado")