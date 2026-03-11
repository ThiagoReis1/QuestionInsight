vr = float(input("Digite a renda: "))
vp = float(input("Digite o valor da prestacao: "))
r = (15/100)*vr
if vp > r:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")