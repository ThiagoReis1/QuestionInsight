vr=float(input("qual a renda "))
vp=float(input("valor da prestacao "))
i=vr*(35/100)
if vp>i:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")