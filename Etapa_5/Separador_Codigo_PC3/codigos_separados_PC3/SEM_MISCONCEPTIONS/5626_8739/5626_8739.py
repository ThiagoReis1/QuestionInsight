valorenda = float(input("valor de renda: "))
valorpres = float(input("valor da prestacao: "))

soma = valorenda * 0.25

if valorpres > soma :
	print("Emprestimo nao aprovado")
	
else :
	print("Emprestimo aprovado")