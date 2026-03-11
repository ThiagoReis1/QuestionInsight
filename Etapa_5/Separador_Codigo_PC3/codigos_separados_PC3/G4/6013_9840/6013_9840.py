r = float(input("valor da renda:"))
p = float(input("valor da prestacao:"))
t = r*(15/100)
if p > t:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")