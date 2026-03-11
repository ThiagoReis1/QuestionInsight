A = float(input("Valor da renda: "))
B = float(input("Valor da prestacao: "))

X = A * (15/100)
if B > X:
	print("Emprestimo nao aprovado ")
else: 
	print("Emprestimo aprovado")
	