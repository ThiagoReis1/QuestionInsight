r = float(input("Digite o valor da renda: "))
p = float(input("digite o valor da prestacao a pagar por mes: "))

y = r * (25/100)
y1 = r - (r * 25/100)

if(p > y):
	m = "Emprestimo nao aprovado"
	print(m)
else:
	m = "Emprestimo aprovado"
	print(m)