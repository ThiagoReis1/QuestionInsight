renda= float(input("Entre com sua renda: "))
prest= float(input("Entre com a prestacao: "))

cond= renda * 0.35

if prest > cond: 
	print("Emprestimo nao aprovado")
	
else: 
	print("Emprestimo aprovado")