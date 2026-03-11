r= float(input("renda: "))
p= float(input("prestacao: "))
e= r*(35/100)
if p>=e:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")