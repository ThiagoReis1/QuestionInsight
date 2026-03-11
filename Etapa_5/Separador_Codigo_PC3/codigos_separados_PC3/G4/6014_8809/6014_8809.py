vr=float(input("renda: "))
vp=float(input("prestacao: "))
vt=vr*0.35
if vt > vp:
	print("Emprestimo aprovado")
else:
	print("Emprestimo nao aprovado")