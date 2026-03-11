#Entrada = o valor da renda do seu Paulo e o valor da prestação que ele pode pagar
valor_renda = float(input("Digite o valor da renda:"))
valor_prest = float(input("Digite o valor da prestacao:"))
#Se o valor da prestação for maior que 25% da renda = 'Emprestimo n aprovado'
if valor_prest > valor_renda * 0.25:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")