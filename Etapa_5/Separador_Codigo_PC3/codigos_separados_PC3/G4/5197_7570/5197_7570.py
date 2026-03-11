x = float(input("Valor da renda: "))
y = float(input("Valor da prestacao: "))

w = x * 0.20


if(y > w):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")