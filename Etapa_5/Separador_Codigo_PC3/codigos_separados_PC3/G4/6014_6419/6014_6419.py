vr = float(input("Digite o valor: "))
vp = float(input("Digite o valor da prestacao: "))
vl = vr * 35/100

if vp > vl :
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	