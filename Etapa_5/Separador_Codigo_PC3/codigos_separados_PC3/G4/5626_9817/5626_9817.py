r= float(input("Digite o valor da renda:"))
p= float(input("Digite o valor da prestacao:"))

c1= 25/100 * r

if p > c1:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")