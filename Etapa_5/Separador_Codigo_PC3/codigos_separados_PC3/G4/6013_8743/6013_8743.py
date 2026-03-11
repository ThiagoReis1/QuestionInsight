a = float(input("valor da renda: "))
b = float(input("valor da prestacao: "))

x = a+b*0.15
y = x+b

if(a>y):
	print("Emprestimo nao  aprovado")
else:
	a<y
	print("Emprestimo aprovado")