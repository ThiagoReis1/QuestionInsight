vr = float(input("Informe o valor da renda: "))
vp = float(input("Informe o valor da prestacao: "))

if vp > (vr * (25/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")