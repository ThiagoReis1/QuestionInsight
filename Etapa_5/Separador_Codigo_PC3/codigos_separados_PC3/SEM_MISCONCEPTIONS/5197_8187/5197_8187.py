renda= float(input("renda: "))
valor= float(input("prestacao: "))
cal=renda*(20/100)
if(valor>cal):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")