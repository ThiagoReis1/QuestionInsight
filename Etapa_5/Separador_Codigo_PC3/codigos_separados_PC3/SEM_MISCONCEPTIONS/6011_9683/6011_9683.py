vr = float(input("Valor da renda:"))
vp = float(input("Valor da prestacao:"))
porcento = vr * 0.35

if vp > porcento:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")