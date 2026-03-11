renda = float(input("renda dela: "))
prestacao = float(input("por mes: "))

if prestacao > (renda * 0.35) :
	print("Emprestimo nao aprovado")
else :
	print("Emprestimo aprovado")