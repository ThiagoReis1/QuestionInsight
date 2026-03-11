vr= float(input("valor da renda"))
vp= float(input("valor da prestacao"))

if vp>(vr*0.3):
	print("Emprestimo nao aprovado")
else:
	vp<(vr*0.3)
	print("Emprestimo aprovado")