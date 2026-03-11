vr= float(input("valor de renda do madruga"))
vp= float(input("valor da prestacao"))
if vp > (vr * 0.2):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")