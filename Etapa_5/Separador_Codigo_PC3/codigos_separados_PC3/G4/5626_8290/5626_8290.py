vr = float(input("valor renda Dona Clotilde: "))
vp = float(input("valor da prestacao que pode pagar por mes: "))

if (vp > vr * 0.25):
	s = "Emprestimo nao aprovado"
	
else:
	s = "Emprestimo aprovado"
	
print(s)