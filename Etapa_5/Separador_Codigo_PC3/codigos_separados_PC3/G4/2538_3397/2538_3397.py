S = float(input("Digite o valor do sitio: "))
D = float(input("Valor do deposito: "))
M = float(input("Deposito mensal fixo: "))
j = float(input("Taxa de juros: "))/100
t = 0
saldo = D
if(S > 0) and (D > 0) and (M > 0) and (j > 0):
	while(saldo < S):
		saldo += saldo * j
		saldo = round(saldo, 2)
		saldo = saldo + M
		t += 1
	print(t)
else:
	print("Dados incorretos")
		
	
