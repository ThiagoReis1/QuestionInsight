VR = float(input("Valor da renda: "))
VP = float(input("Valor da prestacao: "))

if VP <= VR * 0.20:
	print("Emprestimo aprovado")
else:
	print("Emprestimo nao aprovado")