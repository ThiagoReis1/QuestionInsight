renda = float(input("Digite o valor de sua renda: "))
prestacao = float(input("Digite o valor acessivel a ser pago mensalmente: "))
if(prestacao > renda*0.3):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")