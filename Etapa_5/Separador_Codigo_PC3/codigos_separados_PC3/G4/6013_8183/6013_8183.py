var1 = float(input("Informe o valor da renda: "))
var2 = float(input("Informe o valor da prestacao: "))

X = var1 * (15/100)

if (var2 > X):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")