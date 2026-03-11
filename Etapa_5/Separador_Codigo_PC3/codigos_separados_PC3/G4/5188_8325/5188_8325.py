vr=float(input("valor da renda: "))
vp=float(input("valor da prestacao por mes: "))

vp1= vr*(25/100)

if (vp> vp1):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")