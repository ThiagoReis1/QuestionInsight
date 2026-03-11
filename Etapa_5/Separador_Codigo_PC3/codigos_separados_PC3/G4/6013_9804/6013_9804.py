vr = float(input("valor da renda: "))
vp = float(input("Valor de prestacao: "))

if vp > (vr * 0.15):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
