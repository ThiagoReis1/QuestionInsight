r=float(input("renda por mes: "))
p=float(input("prestacao: "))
l= r * (20/100)

if (p>l):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")

