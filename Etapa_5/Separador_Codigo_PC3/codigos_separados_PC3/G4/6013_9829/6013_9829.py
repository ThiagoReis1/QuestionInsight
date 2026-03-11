vr = float(input("Digite o valor da renda: "))
vp = float(input("Digite o valor da prestacao: "))

if (vp > (15/100)*vr):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")