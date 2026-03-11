vr = float(input("valor da renda: "))
vp = float(input("valor da prestacao: "))
r = vr*(25/100)
if (vp>r):
	msg = "Emprestimo nao aprovado"
	
else:
	msg = "Emprestimo aprovado"
print(msg)