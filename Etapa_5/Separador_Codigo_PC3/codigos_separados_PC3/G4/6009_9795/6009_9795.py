Vr = float(input("valor de renda de Fernanda: "))
Vp = float(input("valor da prestacao por mes: "))

if Vp > 0.3*Vr:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")