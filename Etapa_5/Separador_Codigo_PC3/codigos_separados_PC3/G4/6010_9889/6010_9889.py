vr = float(input("Digite o valor da renda do seu Marcio: "))
vp = float(input("Digite o valor da prestacao: "))

i = vr * 0.35

if (vp > i):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")