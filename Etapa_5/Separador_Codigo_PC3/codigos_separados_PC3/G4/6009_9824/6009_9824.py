a = float(input("digite o valor da renda de F: "))
b = float(input("digite o valor da prestacao: "))

if b > a * (30/100):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")