valor_renda= float(input("qual o valor da renda? "))
valor_prest= float(input("qual o valor da prestacao: "))

if valor_prest > (valor_renda *(20/100)):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado ")