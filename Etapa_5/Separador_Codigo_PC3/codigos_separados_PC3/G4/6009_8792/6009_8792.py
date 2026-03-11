r = float(input("valor da renda: "))
pres = float(input("valor da prestacao a pagar por mes: "))

p = r*30/100

if pres > p:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")