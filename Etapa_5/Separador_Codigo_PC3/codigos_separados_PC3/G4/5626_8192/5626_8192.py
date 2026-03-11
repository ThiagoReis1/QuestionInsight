V = float(input("Valor da renda?: "))
V2 = float(input("Valor da prestacao?: "))

V3 = V * (25 / 100)

if (V2 > V3):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	