Vr = float(input("O valor da renda: "))
Vp = float(input("O valor da prestacao que ele pode pagar por mes: "))

Rp = Vr * 0.20

if Vp > Rp:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")