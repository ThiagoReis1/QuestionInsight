renda = float(input("digite renda: "))
prest = float(input("valor prestacao: "))
cond = renda * 35/100 
if prest > cond: 
    print("Emprestimo nao aprovado")
else: 
	 print("Emprestimo aprovado")
