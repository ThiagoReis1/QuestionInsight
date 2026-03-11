a = float(input("valor da renda: "))
prest = float(input("valor da prestacao: "))

if prest > (a * 30/100) :
	print('Emprestimo nao aprovado')
else:
	print("Emprestimo aprovado")