renda = float(input("insira o valor da renda"))
prestaçao = float(input("insira o valor da prestaçao"))

porcentagem = renda * 35/100
if (prestaçao > porcentagem):
	print("Emprestimo nao aprovado")
else:
	print ("Emprestimo aprovado")