c = float(input("valor do carro: "))
d = float(input("valor inicial depositado: "))
m = float(input("deposito mensal fixo: "))
j = float(input("taxa de juros: "))
pj = j / 100

soma = d
cont = 0

if((c > 0) and (d > 0) and (m > 0) and (j > 0)):
	while (soma < c):
		desconto = soma * pj
		soma = round((soma + desconto + m), 2)
		cont = cont + 1
	print(cont)
else:
	mensagem = "Dados incorretos"
	print(mensagem)

		