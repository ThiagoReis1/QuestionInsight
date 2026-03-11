V = float(input("entre com o valor do premio:"))  #valor do premio
M = float(input("entre com o saque mensal:"))     #saque mensal
j = float(input("entre com a taxa de juros:"))  # taxa de juros
t = 0
saldo = V
if(V>0 and M>0 and j>0):
	while(saldo<2*V):
		saldo += saldo + (saldo*j/100)
		saldo += round(saldo,2)
		t = t + 1
		print(t)
else:
	print("Dados incorretos")