#Entrada

valor_renda = float(input("Digite o valor da sua renda: "))
valor_pres = float(input("Digite o valor da prestacao: "))

#Expressão e Saída

part_renda = valor_renda * 25 / 100

if part_renda < valor_pres:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")