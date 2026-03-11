S= float(input("Digite o valor do sitio:"))
D= float(input("Digite o valor inicial do deposito:"))
M= float(input("Digite o deposito mensal fixo:"))
j= float(input("Digite o valor da taxa de juros:"))

j= j / 100
i= 0
saldo= D

if (S > 0 and D > 0 and M > 0 and j > 0):
	while (saldo < S):
			saldo= round(saldo + (saldo * j) + M,2)
			i= i + 1
	print(i)	

else:
	print("Dados incorretos")	