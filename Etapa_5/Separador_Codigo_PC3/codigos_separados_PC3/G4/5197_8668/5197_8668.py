vr = float(input("renda: "))
vp = float(input("prestacao: "))

e = vr * 0.20
if (vp > e):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")