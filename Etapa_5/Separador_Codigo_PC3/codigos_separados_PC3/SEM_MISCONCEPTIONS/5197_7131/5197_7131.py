renda=float(input("Digite o valor da renda:  "))
prestacao=float(input("Digite o valor da prestacao que pode ser paga:  "))
porcentagem=(renda*0.2)
if(prestacao>porcentagem):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")