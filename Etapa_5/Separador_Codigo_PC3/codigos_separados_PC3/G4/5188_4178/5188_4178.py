vr = float(input("Valor de renda: "))
vp = float(input("Valor da prestaao: "))

if vp > (vr*.25):
	x = "Emprestimo nao aprovado"
else:
	x = "Emprestimo aprovado"
print(x)	