renda = float (input("digite a renda:"))
prestacao = float (input("digite a prestacao:"))

x = renda * 0.20
if prestacao > x:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")