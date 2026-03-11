VR = float(input("digite o valor da sua renda: "))
VP = float(input("digite o valor da prestacao: "))

if VP > VR*(30/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")