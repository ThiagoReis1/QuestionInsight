VRenda = float(input("Renda: "))
Prestacao = float(input("Prestacao Mensal: "))

if(Prestacao/Renda)>0.15:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")