renda= float(input("valor da renda de dona fernanda:"))
prest= float(input("valor da prestacao que pode ser paga por mes:"))

if prest > (renda * 30/100) :
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")
	
	