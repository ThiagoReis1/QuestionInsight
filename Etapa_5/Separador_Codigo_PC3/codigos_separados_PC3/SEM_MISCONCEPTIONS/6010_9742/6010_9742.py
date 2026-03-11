renda = float(input("renda; "))
prest = float(input("Prest:"))

v = renda/100
s = v*35

if prest>s:
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")
