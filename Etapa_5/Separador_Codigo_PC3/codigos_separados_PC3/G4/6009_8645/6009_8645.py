vr=float(input("valor da renda: "))
vp=float(input("valor da prestacao: "))

vr1=vr*0.30

if vp>vr1:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")