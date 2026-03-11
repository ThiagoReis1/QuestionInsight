renda = float(input("inserir renda: "))
prest = float(input("valor da prestacao: "))

renda1 = 0.2 * renda
if (prest > renda1):
	print("Emprestimo nao aprovado")
	
else: 
	print("Emprestimo aprovado")