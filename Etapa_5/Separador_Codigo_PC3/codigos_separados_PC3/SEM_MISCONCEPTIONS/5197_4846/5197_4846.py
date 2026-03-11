renda=float(input("Digite a renda do seu madruga:"))
prestacao=float(input("Digite o valor da prestacao:"))

if(prestacao>20*renda):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")