renda = float(input("digite a renda"))
prestacao = float(input("digite a prestacao"))
if prestacao > renda*0.35:
	print("Emprestimo nao aprovado")
else:
	print ("Emprestimo aprovado")