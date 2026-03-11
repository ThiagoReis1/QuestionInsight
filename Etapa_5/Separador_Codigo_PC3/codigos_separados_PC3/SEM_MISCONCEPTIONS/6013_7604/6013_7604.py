valor_r = float(input("valor: "))
valor_p = float(input("valor: "))

k = 0.15 * valor_r
if valor_p >k:

	print("Emprestimo nao aprovado")
	
else:
	
	print("Emprestimo aprovado")