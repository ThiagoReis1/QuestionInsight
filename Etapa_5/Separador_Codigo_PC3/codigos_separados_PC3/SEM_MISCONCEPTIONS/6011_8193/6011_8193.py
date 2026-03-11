renda = float(input("renda:"))
prestacao = float(input("prestacao:"))

if prestacao>renda*(35/100):
	saida="Emprestimo nao aprovado"
else:
	saida="Emprestimo aprovado"
print(saida)
