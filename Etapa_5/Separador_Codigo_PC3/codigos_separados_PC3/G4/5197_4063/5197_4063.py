re = float(input("Digite a renda: "))
p = float(input("Digite a prestacao: "))

a = (re * 20)/100

if a < p:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")