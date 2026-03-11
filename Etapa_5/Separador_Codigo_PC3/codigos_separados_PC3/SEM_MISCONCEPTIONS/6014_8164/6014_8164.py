renda = float(input("valor da renda: "))
prest = float(input("valor da prestacao que pode ser paga: "))
percent = (35/100)*renda
if prest>percent:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")