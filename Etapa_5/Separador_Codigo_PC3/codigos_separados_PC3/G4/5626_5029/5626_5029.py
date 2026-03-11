vr = float(input("Valor da renda: "))
vp = float(input("Valor da prestacao: "))
x = (vr*25)/100

if (vp > x) :
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")