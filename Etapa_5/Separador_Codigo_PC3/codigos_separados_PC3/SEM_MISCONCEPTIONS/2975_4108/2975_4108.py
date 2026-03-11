suco = int (input("Informe a quantidade de suco: "))
salgado = int (input("Informe a quantidade de salgados: "))
valor_disponivel = float(input("Informe o valor dispinivel: "))
total = round(float(suco * 3 + salgado * 3.5),2)
print (total)
if valor_disponivel < total:
	print("Nao")
else:
	print("Sim")