y = float(input("valor da renda: "))
c = float(input("valor da prestacao: "))
b= y*(25/100)
if c > b:
	p= "Emprestimo nao aprovado"
else:
	p= "Emprestimo aprovado"
print(p)
