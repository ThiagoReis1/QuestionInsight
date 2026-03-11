renda = float(input("valor da renda saba"))
prestacao =float(input("valor prestacoa por mes"))
if prestacao > 0.15*renda :
	print("Emprestimo nao aprovado")
else:
	print ("Emprestimo aprovado")