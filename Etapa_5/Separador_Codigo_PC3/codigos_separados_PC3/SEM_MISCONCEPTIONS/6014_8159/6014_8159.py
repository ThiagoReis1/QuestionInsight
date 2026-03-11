val_r=float(input("valor da renda: "))
val_p=float(input("valor da prestacao: "))
por=35/100*val_r
if(val_p>por):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")