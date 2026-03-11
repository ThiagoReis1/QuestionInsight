vr = float(input("Valor da renda: "))
vp = float(input("Valor da prestacao: "))
t = (vr/100)*35
if (vp > t):
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
print(msg)