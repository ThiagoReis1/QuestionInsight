vr = float(input("valor renda: "))
vp = float(input("valor pretacao: "))

x = 35/100*vr

if (vp > x):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")