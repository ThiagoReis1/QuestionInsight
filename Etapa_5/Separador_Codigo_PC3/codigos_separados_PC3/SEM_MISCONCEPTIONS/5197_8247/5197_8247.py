renda = float(input("Insira a renda: "))
prest = float(input("Insria a mensalidade: "))
p = (20/100)*renda
if prest > p:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")