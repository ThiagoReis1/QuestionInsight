vrenda=float(input("valor da renda: "))
vprestacao=float(input("valor da prestacao: "))

renda=vrenda*(35/100)

if vprestacao > renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")