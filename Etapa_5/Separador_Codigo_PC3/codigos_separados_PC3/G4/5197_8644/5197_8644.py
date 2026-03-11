vr = float(input("valor da renda: "))
vp = float(input("valor dda prestacao: "))

t = vr * 0.20

if(vp > t):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")