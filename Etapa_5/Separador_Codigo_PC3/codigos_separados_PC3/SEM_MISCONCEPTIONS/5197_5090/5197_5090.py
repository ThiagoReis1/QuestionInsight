renda = float(input("Qual a renda do seu madruga: "))
prestacao = float(input("Qual a prestacao que ele pode pagar por mes: "))

if (prestacao > renda*0.2):
	mensagem = "Emprestimo nao aprovado"
	print(mensagem)
	
else:
	mensagem = "Emprestimo aprovado"
	print(mensagem)