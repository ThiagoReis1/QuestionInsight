renda = float(input("Qual a renda? "))
prest = float(input("Qual a prestacao? "))
parcela = renda * 0.35
if prest > parcela:  
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")