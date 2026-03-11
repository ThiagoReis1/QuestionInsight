vr = int(input("valor da renda: "))
vp = int(input("valor da prestacao: "))

p = vr * 25 / 100

if (vp > p):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")