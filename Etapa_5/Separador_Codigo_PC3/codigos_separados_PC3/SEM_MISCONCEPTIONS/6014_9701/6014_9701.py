renda = float(input("Qual sua renda? "))
prest = float(input("Quanto vc pode pagar por mes? "))
if prest > 0.35* renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")