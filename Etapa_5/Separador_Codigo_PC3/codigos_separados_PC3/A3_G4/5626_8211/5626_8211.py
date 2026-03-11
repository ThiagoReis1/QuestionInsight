vr = float(input("valo de renda: "))
vp = float(input("valo da prestacao: "))
p1 = 25/100 * vp
x1 = vp + vp
if(x1 > vr):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
