renda = float(input("Qual o valor da renda do seu saba?"))
prest = float(input("Qual o valor da prestacao do seu saba? "))

if prest > (renda*(15/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")