valor_renda = float(input("insira a renda"))
valor_prestacao = float(input("insira o valor prestacao"))

if valor_prestacao > (valor_renda) * (20/100):
	 print("Emprestimo nao aprovado")
else:
	 print("Emprestimo aprovado")