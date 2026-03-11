r = float(input("renda: "))
p = float(input("prestacao: "))

pf = r * 25/100


if(p > pf):
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")

