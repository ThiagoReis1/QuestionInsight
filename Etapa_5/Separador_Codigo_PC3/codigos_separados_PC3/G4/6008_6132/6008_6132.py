vr = float(input("digite o valor da renda: "))
vp = float(input("digite o valor da prestacao: "))

if vp > (vr*0.20):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")