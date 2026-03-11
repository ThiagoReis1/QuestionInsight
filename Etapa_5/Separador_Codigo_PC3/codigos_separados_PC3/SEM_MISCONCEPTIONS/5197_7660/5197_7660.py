#---------------------------------------------------------------
# Aluno: Ivan Lucas de Oliveira Pacheco
# Data: 07/12/2022
# Objetivo: Definir se o personagem pode arcar com as parcelas de um emprestimo
#---------------------------------------------------------------

# Definição do percentual que pode ser comprometido a parcela
limite_renda = 0.2

# Leitura da renda e da prestação do empréstimo
renda = float(input("Qual o valor da renda de seu Madruga? "))
valor_prestacao = float(input("Defina o valor das parcelas: "))

renda_comprometida = renda * limite_renda

if renda_comprometida < valor_prestacao:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")