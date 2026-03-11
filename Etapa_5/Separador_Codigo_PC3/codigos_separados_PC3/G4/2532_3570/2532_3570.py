c = float(input("valor do carro:"))
d = float(input("valor inicial depositado:"))
m = float(input("deposito mensal fixo:"))
j = float(input("taxa de juros:"))


mes = 0
soma = d
if(c > 0) and (d > 0) and (m > 0) and (j > 0):
	while(soma < c):
		saldo = (soma)*(j/100)
		soma = soma + saldo + m
		soma = round(soma,2)
		mes = mes + 1
	
	print(mes)
else:
	print("Dados incorretos")