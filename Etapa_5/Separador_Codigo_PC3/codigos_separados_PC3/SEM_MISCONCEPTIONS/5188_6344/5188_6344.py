valrenda = float(input("Digite o valor da renda: "))
valprest = float(input("Digite o valor da prestacao: "))

t = 0.25 * valrenda

if (valprest > t):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")
