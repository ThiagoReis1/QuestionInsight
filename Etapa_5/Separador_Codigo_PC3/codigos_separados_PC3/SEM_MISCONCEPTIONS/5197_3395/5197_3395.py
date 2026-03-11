a=20/100
valor_renda=float(input("digite o valor da renda:"))
prestacao=float(input("digite o valor :"))
parcela_emprest=float(valor_renda*a)

if(prestacao>parcela_emprest):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")