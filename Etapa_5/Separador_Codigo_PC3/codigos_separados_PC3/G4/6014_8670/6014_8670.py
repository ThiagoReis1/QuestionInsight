vr = float(input("Informe o valor de renda: "))
vp = float(input("valor de prestacao: "))

if (vp > vr * 0.35):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")