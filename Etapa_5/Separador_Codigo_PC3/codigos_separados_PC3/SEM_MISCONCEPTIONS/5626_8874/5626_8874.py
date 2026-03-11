renda = int(input("qual a renda: "))
prestacao = int(input("qual a prestacao: "))

if prestacao > renda*(25/100):
	print("Emprestimo nao aprovado")


else: 
	print("Emprestimo aprovado")