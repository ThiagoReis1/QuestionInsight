renda = int(input("insira um numero: "))
parcela = int(input("insira este numero: "))
relacao = renda*(25/100)

if(parcela > relacao):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")