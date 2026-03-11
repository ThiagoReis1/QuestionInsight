renda = float(input("qual a renda? "))
presta = float(input("qual a prestacao"))

if presta >= renda*(0.25):
	print("Emprestimo nao aprovado")
	
else: 
	print("Emprestimo aprovado")