renda = float(input(""))
prestacao = float(input(""))
valor = renda * (25/100)

if prestacao > valor: 
	mensagem = "Emprestimo nao aprovado"
	print(mensagem)

if prestacao <= valor:
	mensagem = "Emprestimo aprovado"
	print(mensagem)
	
