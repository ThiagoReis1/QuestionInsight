vr = float(input("Valor da Renda: "))
vp = float(input("Valor da Prestacao: "))

e = vr * (35/100)

if(vp > e):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")